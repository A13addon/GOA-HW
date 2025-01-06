
class User {
    constructor(name, email){
        this.name = name
        this.email = email

    };
    displayInfo() {
        console.log(this.name);
        console.log(this.email)

    };

    static compareUsers(newUser, newUser1) {
        return newUser.email === newUser1.email

    }
};

const newUser = new User ("misho", "alicestrong@gmail.com")
const newUser1 = new User ("ana", "aliicebrutal@gmail.com")
const newUser2 = new User ("lana", "lanako2007@gmail.com")

newUser.displayInfo();
newUser1.displayInfo();
newUser2.displayInfo();

console.log(User.compareUsers(newUser, newUser1));