// THAILAND
let cases = document.getElementById('cases');
let new_cases = document.getElementById('new_cases');
let new_death = document.getElementById('new_deaths');
let death = document.getElementById('deaths');
let total_recovered = document.getElementById('total_recovered');
let serious_critical = document.getElementById('serious_critical');
let active_cases = document.getElementById('active_cases');
let countries_stat = document.getElementById('countries_stat');
// Fetch The Data
fetch("https://corona-virus-world-and-india-data.p.rapidapi.com/api", {
	"method": "GET",
	"headers": {
		"x-rapidapi-key": "557172587cmsh5a7bca76c78c78dp1f5459jsnc0ca094042d7",
		"x-rapidapi-host": "corona-virus-world-and-india-data.p.rapidapi.com"
	}
})
.then(response => response.json().then(data => {
    console.log(data);
    let countries_stat = data.countries_stat;
    console.log(countries_stat)
        cases.innerHTML = countries_stat[32].cases;
        new_cases.innerHTML = countries_stat[32].new_cases;
        new_death.innerHTML = countries_stat[32].new_deaths;
        death.innerHTML = countries_stat[32].deaths;
        total_recovered.innerHTML = countries_stat[32].total_recovered;
        serious_critical.innerHTML = countries_stat[32].serious_critical;
        active_cases.innerHTML = countries_stat[32].active_cases;
}))
.catch(err => {
	console.error(err);
});