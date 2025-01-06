
class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    dispDetails() {

        return `name: ${this.name}, age: ${this.age}`

    }
}

class Student extends Person {
    constructor (name, age, studentID) {
        super(name, age)
        this.studentID = studentID;

    }
    dispDetails() {
        const dispDetails2 = super.dispDetails();
        return `${dispDetails2}, Student ID: ${this.studentID}`
    }
}


const newPerson = new Person ("misho", 17)
const newStudent = new Student("luka", 19, 123321)

console.log(newPerson.dispDetails());
console.log(newStudent.dispDetails());