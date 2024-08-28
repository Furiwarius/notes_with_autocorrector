async function new_note() {

    const token = sessionStorage.getItem('authToken');

    // отправляем запрос
    const response = await fetch("/new_note", {
                    method: "GET",
                    headers: { 'Authorization': 'Bearer ' + token,
                        "Accept": "application/json", 
                        "Content-Type": "application/json" }});
    if (response.ok) {
        const text = await response.text(); 
        document.body.innerHTML = text;
}
}