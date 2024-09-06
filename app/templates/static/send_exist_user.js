async function send_user(){

    // получаем введеные данные
    const login = document.getElementById("login").value;
    const password = document.getElementById("password").value;

    const params = new URLSearchParams();

    params.append("grant_type", "password");
    params.append("username", login);
    params.append("password", password);

    params.append("client_id", "my-client");
    params.append("client_secret", "my-client");

    // отправляем запрос
    const response = await fetch("/token", {
                        method: "POST",
                        headers: { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" },
                        body: params
                        });
    if (response.ok) {
        const data = await response.json(); 
        // Сохранение токена
        sessionStorage.setItem('authToken', data.access_token);
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