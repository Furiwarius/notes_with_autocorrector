async function send_new_user() {
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
    const response = await fetch("/registr", {
                    method: "POST",
                    headers: { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" },
                    body: params
                    });
    if (response.ok) {
        window.location.href = "/"
    }
    else {
        await server_error()
    }
}


async function server_error() {
    alert("Этот логин уже занят");
}