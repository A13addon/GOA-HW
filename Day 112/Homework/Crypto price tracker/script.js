document.getElementById("searchform").addEventListener("submit", function(e) {
    e.preventDefault();

    const cryptotitle = document.getElementById("cryptotitle").value.trim().toLowerCase();
    if (!cryptotitle) return
    fetchcryptodata (cryptotitle);

})

async function fetchcryptodata (cryptotitle) {
    const cryptodetails = document.getElementById("cryptodetails");
    cryptodetails.innerHTML = 'Fetching'


    try {
        const response = await fetch(`https://api.coingecko.com/api/v3/coins/${cryptotitle}`)
        const data = await response.json();

        if(data.error) {
            cryptodetails.innerHTML = "Incorrect name"
            return
        }

        displaycryptodetails (data)
    } catch (error) { 
        cryptodetails.innerHTML = "Error fetching data"

    }
    
}


function displaycryptodetails(data) {
    const cryptodetails = document.getElementById("cryptodetails")
    cryptodetails.innerHTML = `
        <h2>${data.name} (${data.symbol.toUpperCase()})</h2>
        <p><strong>Price:</strong> $${data.market_data.current_price.usd}</p>
        <p><strong>24h Change:</strong> ${data.market_data.price_change_percentage_24h.toFixed(2)}%</p>
        <p><strong>Market Cap:</strong> $${data.market_data.market_cap.usd.toLocaleString()}</p>
        <img src="${data.image.small}" alt="${data.name} Logo">
    `;
}