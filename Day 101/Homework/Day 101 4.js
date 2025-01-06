class Product {
    constructor(name, price) {
        this.name = name
        if(price > 0) {
            this._price = price

        } else {
            this._price = 0
        }
    };
    get price() {
       return(this._price)
    };
}

const Laptop = new Product("leptopi", 1999)

console.log(Laptop.price)