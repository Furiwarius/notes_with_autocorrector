from app.entities.account import Account
from app.entities.note import Note
from app.database.tables.essence import AccountsTable as AccTable
from app.database.tables.essence import NotesTable
import functools 



class Converter():
    '''
    Конвертиртер

    Переводит данные из классов таблиц
    в классы с голыми данными для слоя бизнес-логики
    '''    


    compliance = {"AccountsTable": Account, 
                  "NotesTable": Note,
                  "Account": AccTable,
                  "Note": NotesTable}

    

    def conversion_to_data(self, item:AccTable|NotesTable|None) -> Note|Account|None: 
        ''' 
        Конвертация из объекта Table
        в объект бизнес логики с 
        голыми данными 
        ''' 
        if item is None:
            return None
        
        # Получаем класс бизнес логики соответствующий переданному классу из таблицы
        class_ = self.compliance.get(item.__class__.__name__)
        
        # Получаем атрибуты класса бизнес логики
        param_names = list(class_.__init__.__code__.co_varnames[:class_.__init__.__code__.co_argcount])[1:] 
        
        # Инициализируется с полями None по умолчанию
        class_instance = class_()

        # Заполнение полей
        for atr in param_names:
            setattr(class_instance, atr, getattr(item, atr))
        
        return class_instance 



    def conversion_to_table(self, item:Account|Note) -> AccTable|NotesTable:
        '''
        Конвертация из объекта 
        базнес логики с голыми
        данными в объект Table
        '''
        # Получаем атрибуты передаваемого класса
        param_names = list(item.__init__.__code__.co_varnames[:item.__init__.__code__.co_argcount])[1:] 

        # Создаем класс таблицы соответствующий классу бизнес логики
        class_instance = self.compliance.get(item.__class__.__name__)()

        # Заполняем поля
        for atr in param_names:
            setattr(class_instance, atr, getattr(item, atr))

        return class_instance
    

    def conversion_input_args(self, args:tuple) -> tuple:
        '''
        Переводит образы таблиц в entities экземпляры
        '''

        new_args = list()
        for arg in args:
            if type(arg) in (Note, Account):
                new_args.append(self.conversion_to_table(arg))
            else:
                new_args.append(arg)
        
        return new_args



    def conversion_input_kwargs(self, kwargs:dict) -> dict:
        '''
        Переводит образы таблиц в entities экземпляры  
        '''
        new_kwargs = dict()
        for key, item in kwargs.items():
            if isinstance(item, (NotesTable, AccTable)):
                new_kwargs[key] = self.conversion_to_table(item)
            else:
                new_kwargs[key] = item
        return new_kwargs
    


    def conversion_result_func(self, result:list|NotesTable|AccTable):
        
        if isinstance(result, list):
            result = [converter.conversion_to_data(item) for item in result]

        elif isinstance(result, (NotesTable, AccTable)):
            result = converter.conversion_to_data(result)
        
        return result



converter = Converter()



def convertertation(func) -> Note|Account|None:
    '''
    Конвертор декоратор

    Переводит входящие даннные в круды к табличным представлениям, 
    а результат к классам entities
    '''
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):        
        
        try:
            result = func(*converter.conversion_input_args(args), 
                          **converter.conversion_input_kwargs(kwargs))
        except Exception as er:
            raise er

        return converter.conversion_result_func(result)

    return wrapper