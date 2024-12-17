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
        if (response.status === 409) {
            alert("Такой пользователь уже существует. Попробуйте ещё раз");
        }
        if (response.status === 422) {
            alert("Неверный формат email или пароля. Попробуйте ещё раз");
        }
        if (response.status === 201) {
            window.location.href = "/pages/auth/login"
        }
    });
}
