
const promise = new Promise ((resolve, reject) => {
    setTimeout(() => {
        resolve("2 seconds have passed")
    }, 2000);
})
