async function loginUser() {
    const url = "/auth/login";
    const data = {
    email: document.getElementById("email").value,
    password: document.getElementById("password").value,
    };
    await fetch(url, {
        method: 'POST',
        headers: {'Accept': 'application/json','Content-Type': 'application/json'},
        body: JSON.stringify(data),
    }).then(response => {
        if (response.status === 200) {
            window.location.href = "/pages/chat/main"
        }
        else {
            alert("Неверный логин или пароль")
        }
     });
    }
