$(function () {

    // create the chart
    $('#container').highcharts('StockChart', {
        data: {
            csv: document.getElementById('data.csv').innerHTML
        }
    });
});