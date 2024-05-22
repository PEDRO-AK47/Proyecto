const nombre=document.getElementById("name")
const email = document.getElementById("email")
const pass = document.getElementById("password")
const pass2 = document.getElementById("password2")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")
let entrar = false;

form.addEventListener("submit", e=>{
    e.preventDefault();
    let warnings = " ";
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    parrafo.innerHTML = ""
    if(nombre.value.length <6){
      warnings += "El nombre es muy corto <br>"
      entrar = true
    }
    if(!regexEmail.test(email.value)){
      warnings += "El email no es valido <br>"
      entrar = true
    }
    if(pass.value.length < 8){
      warnings += "la contraseña no es valida <br>"
      entrar = true


    }
    if(pass.value != pass2.value){
      warnings += "las contraseñas no son iguales <br>"
      

    }
    if(entrar){
      parrafo.innerHTML = warnings
    }


    console.log(entrar+" - "+warnings);
})



