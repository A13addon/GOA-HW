
document.getElementById("searchform").addEventListener("submit", function(e) {
    e.preventDefault()

    const username = document.getElementById("username").value.trim()
    if (!username) {
        return
    }
    fetchgithubuser (username) 
})

function fetchgithubuser(username) {
    const user = document.getElementById("userdetails")
    user.innerHTML = ''

    const errormessage = document.getElementById('div')

    fetch(`https://api.github.com/users/${username}`)
    .then(response => {
        if (!response.ok){
            errormessage.textContent = "user not found"
            return null
        }
        return response.json()

    })
    .then (data =>  {
        if (data) {
            userdetails.innerHTML = `
                    <img src="${data.avatar_url}" alt="${data.login}'s profile picture" style="width: 50px; height: 50px; border-radius: 50%;">
                    <h2>${data.name || data.login}</h2>
                    <p><strong>Bio:</strong> ${data.bio || "No bio available"}</p>
                    <p><strong>Public Repositories:</strong> ${data.public_repos}</p>
                    <p><a href="${data.html_url}" target="_blank">View GitHub Profile</a></p>
                `;
        }

    })
    .catch(error => {
        errormessage.textContent = "Fetch wasn't successful "

    })
}