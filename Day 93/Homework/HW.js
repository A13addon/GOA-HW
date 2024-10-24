//1

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];


const isPrime = num => {
    for(let i = 2, s = Math.sqrt(num); i <= s; i++) {
        if(num % i === 0) return false;
    }
    return num > 1;
}

const primeNumbers = numbers.filter(isPrime)

console.log(primeNumbers)

//2

const users = [
    { id: 1, name: 'Misho' },
    { id: 2, name: 'Luka' },
    { id: 3, name: 'Zuka' }
];


const names = users.map(user => user.name)
console.log(names)

//3
const products = [
    { name: 'კომპიუტერი', price: 1000 },
    { name: 'კლავიატურა', price: 20 },
    { name: 'ყურსასმენი', price: 50 },
    { name: 'მაუსი', price: 200 }
];

const filterCheap = products.filter(name => name.price < 100)

console.log(filterCheap)

//4

const books = [
    { title: 'წრიპა ბიჭის დღიური', author: 'ჯეფ კინი' },
];

const bookBy = books.map(book => `${books.author}-(ი)ს ${books.title}`);
console.log(bookBy);

//5

const numbersArray = [5, 12, 15, 24, 30, 7, 18];

const filterNum = numbersArray.filter(number => number > 10 && number % 3 == 0);

console.log(filterNum)

//6
const usersWithAge = [
    { name: 'ლუკა', age: 20 },
    { name: 'მიშო', age: 17 },
    { name: 'ლაშა', age: 22 }
];

const filterAge = usersWithAge.filter(user => user.age > 18)
console.log(filterAge)

//7 
const numbersArr = [10, 55, 70, 45, 80, 30];

const filterNum = numbersArr
    .filter(num => num > 50)
    .map(num => num / 2)

console.log(filterNum);

//8

const words = ['მალხაზი', 'მალხაზი', 'მალხაზი', 'გუჯა', 'გუჯიკო', 'მიშიკო', 'ანზორი'];

const wordFrequencies = {};

words.forEach(word => {

    if (wordFrequencies[word]) {
        wordFrequencies[word]++;
    } else {

        wordFrequencies[word] = 1;
    }
});

console.log(wordFrequencies)

//9

const cars = [
    { brand: { name: 'Toyota' }, model: 'Camry' },
    { brand: { name: 'Honda' }, model: 'Accord' },
    { brand: { name: 'Toyota' }, model: 'Corolla' }
];

const toyotaCars = cars.filter(car => car.brand.name === 'Toyota');
console.log(toyotaCars); 
