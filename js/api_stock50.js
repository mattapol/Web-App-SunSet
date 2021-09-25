// Fetch The SET50 Data
//Api1 : XZOekvNMXn8yN20nFf81x7Z6O2jz8SB03Cl81hXG 
//Api2 : insCQ6sAtm4jjbaAyw7cDafvkojNzBxhhmNrpPi4
fetch("https://yfapi.net/v6/finance/quote?region=US&lang=en&symbols=%5ESET50.BK", {
	"method": "GET",
	"headers": {
		"x-api-key": "XZOekvNMXn8yN20nFf81x7Z6O2jz8SB03Cl81hXG1", 
	}
})
.then(response => response.json().then(data => {
    console.log(data);
    let quoteResponse = data.quoteResponse;
    console.log(quoteResponse)
	let result = quoteResponse.result
		regularMarketPreviousClose.innerHTML = result[0].regularMarketPreviousClose;
		regularMarketOpen.innerHTML = result[0].regularMarketOpen;
		regularMarketDayLow.innerHTML = result[0].regularMarketDayLow;
		regularMarketDayHigh.innerHTML = result[0].regularMarketDayHigh;	
}))
.catch(err => {
	console.error(err);
});