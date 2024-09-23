

function sumNumbers(start, end) {
    let final = []
    for(let i = start; i <= end; i++) {
        final.push(i)
    }
    console.log(final)
    
}

sumNumbers(1, 20)

function calcAverage(final) {
    let sum = 0
    for(let i = 0; i < final.length; i++){
        sum += final[i]
    }
    let average = sum / final.length
    console.log(average)
}

calcAverage([
   1,  2,  3,  4,  5,  6,  7,
   8,  9, 10, 11, 12, 13, 14,
  15, 16, 17, 18, 19, 20
])



