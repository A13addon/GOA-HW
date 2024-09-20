let dropDown = document.getElementById('myDropdown')
let colorDisplay = document.getElementById('colorDisplay')

dropDown.addEventListener('change', () => {
  let colorSelected = dropDown.value
  colorDisplay.textContent = `${colorSelected} was Picked`
  if (dropDown.value === '') {
    colorDisplay.textContent = `Please Select a Color`
  }
})