// THE WORLD
let new_cases = document.getElementById('new_cases');
let new_death = document.getElementById('new_deaths');
let total_death = document.getElementById('total_deaths');
let total_recovered = document.getElementById('total_recovered');
let total_cases = document.getElementById('total_cases');
let statistic_taken_at = document.getElementById('statistic_taken_at');

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
    let world_total = data.world_total;
    console.log(world_total)
    total_cases.innerHTML = world_total.total_cases;
    new_cases.innerHTML = world_total.new_cases;
    new_death.innerHTML = world_total.new_deaths;
    total_death.innerHTML = world_total.total_deaths;
    total_recovered.innerHTML = world_total.total_recovered;
    statistic_taken_at.innerHTML = world_total.statistic_taken_at;
}))
.catch(err => {
	console.error(err);
});

/*/ Fetch the Country of Covid 19 Data
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
    for (let i = 0; i < countries_stat.length; i++) {
        console.log(countries_stat[i]);
        let row = table.insertRow(i + 1);
        let country_name = row.insertCell(0);
        let cases = row.insertCell(1);
        let deaths = row.insertCell(2);
        let serious_critical = row.insertCell(3);
        let recovered_per_country = row.insertCell(4);
        country_name.innerHTML = countries_stat[i].country_name;
        cases.innerHTML = countries_stat[i].cases;
        deaths.innerHTML = countries_stat[i].deaths;
        serious_critical.innerHTML = countries_stat[i].serious_critical;
        recovered_per_country.innerHTML = countries_stat[i].total_recovered;
    }
}))
.catch(err => {
	console.error(err);
});*/
