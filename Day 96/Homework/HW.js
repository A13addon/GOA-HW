

const person = {
    name: 'მიხეილი',
    age: 17,
    city: 'თბილისი'
};

console.log(person);
console.log(person.name);
console.log(person.city);

const { name, age } = person;
console.log(name)
console.log(age)

/////////////////////////////////

const student = {
    name :'misho',
    age: 17,
    city: 'Tbilisi',
    address: {
        country: "Georgia",
        street: "Rustaveli"
    }
}

const { country, street } = student.address;

console.log(country)
console.log(street)

/////////////////////////////////

?????