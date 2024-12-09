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
        else{
            alert("неверный логин или пароль")
        }
     });
    }

// Добавляем эффект при фокусе на инпуты
const inputs = document.querySelectorAll('input');
inputs.forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.style.transform = 'translateY(-2px)';
    });

    input.addEventListener('blur', function() {
        this.parentElement.style.transform = 'translateY(0)';
    });
});