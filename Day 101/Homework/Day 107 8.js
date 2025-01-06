
class Appliance {
    constructor(power) {
        this._power = power
    }
}

class washingMachine extends Appliance {
    constructor (power, brand) {
    super(power)
    this.brand = brand;
    }

    dispDetails () {
        return `brand: ${this.brand}, power: ${this._power}`
    }
}

const samsungWM = new washingMachine (800, "Samsung")
console.log(samsungWM.dispDetails())
