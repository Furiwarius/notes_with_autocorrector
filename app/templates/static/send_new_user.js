async function send_new_user() {
    // получаем введеные данные
    const login = document.getElementById("login").value;
    const password = document.getElementById("password").value;

    // отправляем запрос
    const response = await fetch("/registr", {
                    method: "POST",
                    headers: { "Accept": "application/json", "Content-Type": "application/json" },
                    body: JSON.stringify({ 
                        login: login,
                        password: password
                        })
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