class Car {
    constructor (name, model) {
        this.make = make;
        this.model = model;
    }
}

const newCar = new Car ("Ferrari", 'LaFerrari')

///////////////////////////////////////////////////////

class Bank {
    #balance

    constructor(nowBalance) {
        this.#balance = nowBalance
    }

    deposit (num) {
        this.#balance += num;
    }
     
    withdraw (num) {
        this.#balance -= num;
    }

    getBalance() {
        return this.#balance
    }
}

const acc = new Bank(100);

///////////////////////////////////////////////////////

class MathOperations {
    static PI = 3.14159;

    static add(a, b) {
        return a + b;
    }
}

//////////////////////////////////////////////////////////////


class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    get area() {
        return this.width * this.height;
    }

    set width(value) {
        if (value > 0) this._width = value;
    }

    get width() {
        return this._width;
    }

    set height(value) {
        if (value > 0) this._height = value;
    }

    get height() {
        return this._height;
    }
}

const rect = new Rectangle(10, 5);
console.log(rect.area);
rect.width = 20;
console.log(rect.area);


///////////////////////////////////////////////////////////////////


class User {
    #validatePassword(password) {
        return password.length >= 8;
    }

    setPassword(password) {
        if (this.#validatePassword(password)) {
            this.password = password;
        } else {
            throw new Error('Password is too weak');
        }
    }
}

const user = new User();
user.setPassword('strongPassword');

//////////////////////////////////////////////////////////////////////////


class Book {
    constructor(title, pages) {
        this.title = title;
        this.#pages = pages;
    }

    #pages;

    get pages() {
        return this.#pages;
    }

    set pages(value) {
        if (value > 0) {
            this.#pages = value;
        } else {
            throw new Error('Pages must be positive');
        }
    }
}

const book = new Book('წრიპა ბიჭის დღიური', 120);


////////////////////////////////////////////////////////////

class Player {
    static playerCount = 0;

    constructor(name) {
        this.name = name;
        Player.incrementPlayerCount();
    }

    static incrementPlayerCount() {
        this.playerCount++;
    }

    static getPlayerCount() {
        return this.playerCount;
    }
}

const player1 = new Player('გუჯა');
const player2 = new Player('ლუკა');

///////////////////////////////////////////////////////////

class Vehicle {
    #speed;

    constructor(speed) {
        this.#speed = speed;
    }

    getSpeed() {
        return this.#speed;
    }

    setSpeed(newSpeed) {
        this.#speed = newSpeed;
    }
}

class Bike extends Vehicle {
    constructor(speed) {
        super(speed);
    }
}

const bike = new Bike(15);


////////////////////////////////////////////////////////

class Student {
    constructor(name, grade) {
        this.name = name;
        this.grade = grade;
    }

    static compareGrades(student1, student2) {
        return student1.grade - student2.grade;
    }
}

const studentA = new Student('მიშო', 85);
const studentB = new Student('გრიშა', 90);