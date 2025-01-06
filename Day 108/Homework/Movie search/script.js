document.getElementById("searchform").addEventListener("submit", function(e) { 
    e.preventDefault();

    const movieTitle = document.getElementById("movietitle").value.trim();
    if (!movieTitle) return;

    fetchMovieData(movieTitle);
});

function fetchMovieData(title) {
    const movieDetails = document.getElementById('moviedetails');
    movieDetails.innerHTML = '';

    fetch(`https://www.omdbapi.com/?apikey=f8bfa78&t=${title}`)
        .then(response => response.json())
        .then(data => {
            if (data.Response === "False") {
                movieDetails.innerHTML = 'Movie not found';
            } else {
                movieDetails.innerHTML = `
                    <h2>${data.Title} (${data.Year})</h2>
                    <p><strong>Plot:</strong> ${data.Plot}</p>
                    <img src="${data.Poster}" alt="${data.Title} Poster">
                    <p><strong>IMDb Rating:</strong> ${data.imdbRating}</p>
                `;
            }
        })
        .catch(error => {
            movieDetails.innerHTML = 'Error fetching movie data';
        });
}
