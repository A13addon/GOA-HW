
const promise = new Promise ((resolve, reject) => {
    resolve(5)
})

promise.then(num => num * 2)
promise.then(num => num * 2)
promise.then(num => num * 2)
promise.then(num => num * 2)
promise.then(console.log(num))
