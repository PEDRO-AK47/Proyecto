const username = document.getElementById("username");
const email = document.getElementById("email");
const password = document.getElementById("password");
const password2 = document.getElementById("password2");
const form = document.getElementById("form");
const parrafo = document.getElementById("warnings");

form.addEventListener("submit", (e) => {
    e.preventDefault();
    let warnings = "";
    let entrar = false;  
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    parrafo.innerHTML = "";
    
    if (username.value.length < 6) {
        warnings += "El nombre es muy corto <br>";
        entrar = true;
    }
    if (!regexEmail.test(email.value)) {
        warnings += "El email no es valido <br>";
        entrar = true;
    }
    if (password.value.length < 8) {
        warnings += "La contraseña no es valida <br>";
        entrar = true;
    }
    if (password.value !== password2.value) {
        warnings += "Las contraseñas no son iguales <br>";
        entrar = true;  // Añade esto aquí
    }
    
    if (entrar) {
        parrafo.innerHTML = warnings;
    }

    console.log(entrar + " - " + warnings);
});
