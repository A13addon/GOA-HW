

const promise = new Promise ((resolve, reject) => {
    setTimeout(() => {
        resolve("Data Fetched!")
    }, 1000);
})

promise.then(message => console.log(message))