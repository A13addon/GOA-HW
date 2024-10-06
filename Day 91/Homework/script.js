document.getElementById('calculate').addEventListener('click', function() {
    const day = parseInt(document.getElementById('day').value);
    const month = parseInt(document.getElementById('month').value) - 1; // Months are 0-indexed
    const year = parseInt(document.getElementById('year').value);

    const today = new Date();
    const birthDate = new Date(year, month, day);
    const ageInMilliseconds = today - birthDate;

    if (isNaN(ageInMilliseconds) || ageInMilliseconds < 0) {
        alert('Please enter a valid date.');
        return;
    }

    const ageDate = new Date(ageInMilliseconds);
    const years = ageDate.getUTCFullYear() - 1970; // Subtracting 1970 to get the year difference
    const months = ageDate.getUTCMonth(); // Get the month difference
    const days = ageDate.getUTCDate() - 1; // Get the day difference

    document.getElementById('years').textContent = years;
    document.getElementById('months').textContent = months;
    document.getElementById('days').textContent = days;
});