

function Human (name, age, mail, street) {
    this.name = name
    this.age = age
    this.mail = mail
    this.street = street
    
    this.greet = function() {
        console.log(this.name)
    }
}

let human1 = new Human ("gujiko", 17, "bendukiani@gmail.com", "benduqidzis 18")

human1.greet()