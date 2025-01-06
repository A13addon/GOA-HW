
class bankAccount {
    _balance
  
    constructor (Balance) {
      this._balance = Balance
    }
    
    deposit(amount) {
      if (amount > 0) {
          this._balance += amount
          return this._balance
      } else {
          console.log("amount must be positive")
      }
    }
    withdraw(amount) {
      if (amount > 0 && this._balance >= amount){
          this._balance -= amount
          
      } else {
          console.log("withdrawal amount exceeds the balance")
      }
    }
    balanceDisplay () {
      return this._balance
    }
  }
  
  const Account = new bankAccount(1000)
  
  Account.deposit(500)
  Account.withdraw(200)
  
  console.log(Account.balanceDisplay())