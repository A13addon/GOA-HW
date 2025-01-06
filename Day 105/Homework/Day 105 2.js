
const promise = new Promise ((resolve, reject ) => {
    reject("Something went wrong!")

})

promise.catch(error => console.log(error))
