async function loguot() {
    sessionStorage.removeItem('authToken');
    window.location.href = "/"
}