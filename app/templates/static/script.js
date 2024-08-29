$(document).ready(function(){
  fix_spell = function(data) {
    data.forEach(function(elem) {
      $('#text_field').val(
        $('#text_field').val().replace(
          elem['word'],
          elem['s'][0] || elem['word']
        )
      );
    });
  }});


async function correction() {
    var lines = $('#text_field').val().replace(/\r\n|\n\r|\n|\r/g, "\n").split("\n");

    lines.forEach(function(line) {
      if (line.length) {
        $.getScript('http://speller.yandex.net/services/spellservice.json/checkText?text=' + line + '&callback=fix_spell');
      }
    });
  }


async function save() {
    // получаем введеные данные
    const name = document.getElementById("note_name").value;
    const text = document.getElementById("text_field").value;
    const token = sessionStorage.getItem('authToken');

    // отправляем запрос
    const response = await fetch("/new_note", {
                    method: "POST",
                    headers: { 'Authorization': 'Bearer ' + token, 
                      "Accept": "application/json", 
                      "Content-Type": "application/json" },
                    body: JSON.stringify({ 
                        name: name,
                        text: text
                        })
                    });
    if (response.ok) {
        await notes()
    }
    else {
        await server_error()
    }
}


async function server_error() {
  alert("При сохранении заметки произошла ошибка!");
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