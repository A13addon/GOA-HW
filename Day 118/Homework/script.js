

class libraryItem {
    constructor(title, year) {
        this.title = title
        this.year = year
        this.isAvailable = true
    }

    borrowitem() {
        if(this.isAvailable) {
            this.isAvailable = false
            console.log(`book was borrowed`)
        } else {
            console.log(`book is unavailable`)

        }

    }

    returnItem() {
        this.isAvailable = true
        console.log(`This book had been returned`)
    }


}

class book extends libraryItem {
    constructor(title, year, author, genre) {
        super(title, year)
        this.author = author
        this.genre = genre
    }

    getsummary() {
        return `Book title: ${this.title}, release date: ${this.year}, Author: ${this.author} and genre:${this.genre}`

    }
}

class magazine extends libraryItem {
    constructor(title, year, issueNumber){
        super(title, year)
        this.issueNumber = issueNumber
    }

    getsummary() {
        return `magazine title: ${this.title}, release date: ${this.year} and issueNumber:${this.issueNumber}`
    }
}


const booktest = new book("The Great Gatsby", 1925, "F. Scott Fitzgerald", "Classic Fiction");
const magtest = new magazine("New York Times", 1921, 2292929991111111111)

console.log(booktest.getsummary())
console.log(magtest.getsummary())
console.log(magtest.borrowitem())
console.log(magtest.isAvailable)