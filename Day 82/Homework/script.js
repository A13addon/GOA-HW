let dataBase = []

const form = document.getElementById("myForm")
const user = document.getElementById("name")
const mail = document.getElementsById("mail")
const pass = document.getElementsById("pass")

form.addEventListener('submit', function(event){
    event.preventDefault();

    const nameVal = user.value
    const mailVal = mail.value
    const passVal = pass.value

    let emailExists = false

    for(let i = 0; i < dataBase.length; i++){
        if(dataBase[i].email === emailValue) {
            emailExists = true
            break;
        }
    }
    
    if(emailExists) {
        alert(`Account with same email already exists!`)

    } else {

        let newUser = {
            user: nameVal,
            mail: mailVal,
            pass: passVal
        }
        dataBase.push(newUser);
        alert(`Account created successfully`)
        form.clear
    }
})

