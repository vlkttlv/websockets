async function registerUser() {
   const url = "/auth/register";
   const data = {
   email: document.getElementById("email").value,
   password: document.getElementById("password").value,
   firstname: document.getElementById("firstname").value,
   lastname: document.getElementById("lastname").value, 
   };
    await fetch(url, {
        method: 'POST',
        headers: {'Accept': 'application/json','Content-Type': 'application/json'},
        body: JSON.stringify(data),
    }).then(response => {
        console.log(response);
        if (response.status === 200) {
            window.location.href = "/pages/auth/login"
        }
        if (response.status === 409) {
            wrongCredentialsSpan.textContent = "Такой пользователь уже существует. Попробуйте ещё раз";
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