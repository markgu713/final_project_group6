// function that gets the data based on ID/name
function getData(location) {
  d3.json(`/manufacturing/${location}`).then((cacao_data) => {
    //console.log(cacao_data);
    company_location_data = cacao_data.filter(cacao_data => cacao_data[5] === location);
    //console.log(company_location_data.length);
    var total = 0;
    for(var i = 0; i < company_location_data.length; i++) {
        total += company_location_data[i][6];
    };
    //console.log(total);
    var avg = (total / company_location_data.length).toFixed(2);
    var demoInfo = d3.select("#sample-metadata");
    demoInfo.html("");
    demoInfo.append("h5").text("Comany Location : " + location + "\n");
    demoInfo.append("h5").text("Average Rating : " + avg + "\n");
  })
}

function buildCharts(location) {
  // @TODO: Use `d3.json` to Fetch the Sample Data for the Plots
  d3.json(`/manufacturing/${location}`).then((cacao_data) => {
    //console.log(cacao_data);
    company_location_data = cacao_data.filter(cacao_data => cacao_data[5] === location);
    //console.log(company_location_data);
    
    var formatData = [];
    var i = 0;
    company_location_data.forEach((point) => {
        i = i + 1; 
        var obj = {};
        obj["id"] = i;
        obj["company"] = point[1];
        obj["specific_bean_origin"] = point[2];
        obj["review_date"] = point[3];
        obj["cocoa_percent"] = point[4];
        obj["company_location"] = point[5];
        obj["rating"] = point[6];
        obj["bean_type"] = point[7];
        obj["bean_origin_country"] = point[8];
        formatData.push(obj);
    });
    var ratings = [];
    var cocoaId = [];
    var labels = [];
    formatData.forEach((point) => {
      cocoaId.push(point.id);
      ratings.push(point.rating);
      labels.push(`Company ${point.company}'s ${point.bean_type} (${point.cocoa_percent} % Cocoa) , year: ${point.review_date}`)
      //labels.push(point);
    });

    // create bar chart data trace
    var trace = {
      x: ratings,
      y: cocoaId,
      text: labels,
      marker: {
        color: 'blue'
      },
      type: "bar",
      orientation: "h",
    };
    var data_bar = [trace];

    // set the plotly layouts
    var layout_bar = {
      title: (`Cocoa Bean Company in ${location}`),
      yaxis: {
        tickmode: "linear",
      },
      // margin: {
      //   l: 200,
      //   r: 100,
      //   t: 100,
      //   b: 30
      // }
      automargin: true
    };
    // create the bar chart
    Plotly.newPlot("bar", data_bar, layout_bar);

    // Creat data trace for bubble chart
    var trace1 = {
      x: cocoaId,
      y: ratings,
      mode: "markers",
      marker: {
        size: 30,
        color: cocoaId
      },
      text: labels
    };
    var data_bubble = [trace1];

    // set the plotly layout
    var layout_bubble = {
      xaxis: { title: `Cocoa Bean Company in ${location}`},
      height: 600,
      width: 1000
    };

    // create the bubble plot
    Plotly.newPlot("bubble", data_bubble, layout_bubble);
  })
}

function init() {
  // Grab a Reference to the Dropdown Select Element
  var dropdown = d3.select("#selDataset");

  // Use the List of Sample Names to Populate the Select Options
  d3.json("/data").then((data) => {
    console.log(data);
    var companyLocation = [];

    data.forEach((point) => {
      if (companyLocation.indexOf(point[5]) > -1) {
        // do nothing
      } else {
        companyLocation.push(point[5]);
      };
    });
    companyLocation.forEach((location) => {
      dropdown.append("option").text(location).property("value", location);
    });
    console.log(companyLocation);
    // Use the First Sample from the List to Build Initial Plots

    buildCharts(companyLocation[0]);
    getData(companyLocation[0]);
  })
}

function optionChanged(new_location) {
  // Fetch New Data Each Time a New Sample is Selected
  buildCharts(new_location);
  getData(new_location);
}

// Initialize the Dashboard
init();