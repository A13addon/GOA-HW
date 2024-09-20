
const form = document.getElementById('myForm')
const formElements = form.elements;
const btn = document.getElementById('btn')

function clear() {
    form.reset();

}

btn.addEventListener('click', clear)