async function send_user(){

    // получаем введеные данные
    const login = document.getElementById("login").value;
    const password = document.getElementById("password").value;

    // отправляем запрос
    const response = await fetch("/login", {
                        method: "POST",
                        headers: { "Accept": "application/json", "Content-Type": "application/json" },
                        body: JSON.stringify({ 
                            login: login,
                            password: password
                            })
                        });
    if (response.ok) {
        const data = await response.json(); 
        // Сохранение токена
        sessionStorage.setItem('authToken', data.token);
        await notes()
    }
    else {
        await invalid_input()
    }
}


async function invalid_input() {
    alert("Неверный логин или пароль!");
}



async function notes() {

    const token = sessionStorage.getItem('authToken');

    // отправляем запрос
    const response = await fetch("/notes", {
                    method: "GET",
                    headers: { 'Authorization': 'Bearer ' + token,
                        "Accept": "application/json", 
                        "Content-Type": "application/json" }});
    if (response.ok) {
        const text = await response.text(); 
        document.body.innerHTML = text;
}
}