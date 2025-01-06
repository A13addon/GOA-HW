
class Counter {
    static count = 0
    
    static increment() {
        Counter.count += 1
    }
}

Counter.increment()
console.log(Counter.count)