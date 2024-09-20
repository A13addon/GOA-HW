let Counter = document.getElementById('inputcounter')
let textInput = document.getElementById('textinput')

textInput.addEventListener('input', () => {
  const curLength = textInput.value.length;
  Counter.textContent = (`${curLength} / 200 Characters`)
  if(curLength > 200) {
    Counter.textContent = (`Character Limit exceeded`)
  }
})