d3.csv("../static/data/cacao_clean_withbean.csv").then(function(tableData){
    console.log(tableData);

    var tbody =d3.select("tbody");

    // Loop Through `data` and console.log object
    tableData.forEach(function(chocCompany) {
        //console.log(chocCompany);

    // // Step 2:  Use d3 to append one table row `tr` for each object
        var row = tbody.append("tr");
    
    // // Step 3:  Use `Object.entries` to console.log each value
        Object.entries(chocCompany).forEach(function([key, value]) {
        //console.log(key, value);
        var cell = row.append("td");
        cell.text(value);
        });
    });

    // Getting a reference to the button on the page with the id property set to
    var button = d3.select("#filter-btn");
    var form = d3.select("#form");

    // Create event handlers 
    button.on("click", runChoc);
    form.on("submit", runChoc);

    // Complete the event handler function for the form
    function runChoc() {

    // Prevent the page from refreshing
    d3.event.preventDefault();
    
    // Select the input element and get the raw HTML node
        var inputElement = d3.select("#datetime");
        var inputCompanyElement = d3.select("#company");
        var inputCountryElement = d3.select("#country");
        var inputRatingElement = d3.select("#rating");

    // Get the value property of the input element
        var inputValue = inputElement.property("value");
        var inputCompanyValue = inputCompanyElement.property("value");
        var inputCountryValue = inputCountryElement.property("value");
        var inputRatingValue = inputRatingElement.property("value");

        //console.log(inputValue);
        //clear the old search content
        tbody.html("")
    
        var filteredData = tableData.filter(data => data.review_date === inputValue || 
            data.company===inputCompanyValue || data.company_location===inputCountryValue
            || data.rating===inputRatingValue);

        //console.log(filteredData);

    // Loop Through `filtereddata` and console.log each 
        filteredData.forEach(function(dateCompanyChoc) {
            //console.log(dateCompanyChoc);
            var row = tbody.append("tr");
            Object.entries(dateCompanyChoc).forEach(function([key, value]) {
                var cell = row.append("td");
                cell.text(value);
                });
        });
    };
});