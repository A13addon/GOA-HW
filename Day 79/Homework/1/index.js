const form = document.getElementById('myForm');
const pass = document.getElementById('pass');
const btn = document.getElementById('btn');
const par = document.getElementById('myPar');

function checkPassLength() {
    console.log("Button clicked"); // Debugging statement
    let passLength = pass.value.length;
    console.log("Password length:", passLength); // Debugging statement

    if (passLength < 8) {
        par.textContent = "Password is Invalid";
    } else {
        par.textContent = "Password is Valid";
    } 

}

btn.onclick = checkPassLength;