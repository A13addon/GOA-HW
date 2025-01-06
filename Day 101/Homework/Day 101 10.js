

class Book {
    constructor(name, author) {
        this.name = name
        this.author = author
    }
}

const books = [
    new Book("მთვარის მოტაცება", "კონსტანტინე გამსახურდია"),
    new Book("ვეფხისტყაოსანი", "შოთა რუსთაველი")
]

books.forEach(book => console.log(`სახელი: ${book.name}, ავტორი: ${book.author}`))