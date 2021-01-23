// Create a map object
var myMap = L.map("mapid", {
  center: [15.5994, -28.6731],
  zoom: 3
});

L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

// Country data
var countries = [
  { name: 'U.K.', location: [55.378051, -3.435973], ratings: 3.06018518518519 },
  { name: 'U.S.A.', location: [37.09024, -95.712891], ratings: 3.18993506493507 },
  { name: 'Iceland', location: [64.963051, -19.020835], ratings: 3.625 },
  { name: 'Finland', location: [61.92411, 25.748151], ratings: 3.25 },
  { name: 'Sweden', location: [60.128161, 18.643501], ratings: 3.125 },
  { name: 'Amsterdam', location: [56.26392, 9.501785], ratings: 3.5 },
  { name: 'Denmark', location: [56.26392, 9.501785], ratings: 3.1875 },
  { name: 'Canada', location: [56.130366, -106.346771], ratings: 3.4047619047619 },
  { name: 'Lithuania', location: [55.169438, 23.881275], ratings: 3.0625 },
  { name: 'Ireland', location: [53.41291, -8.24389], ratings: 2.8125 },
  { name: 'Netherlands', location: [52.132633, 5.291266], ratings: 3.5 },
  { name: 'Poland', location: [51.919438, 19.145136], ratings: 3.625 },
  { name: 'Germany', location: [51.165691, 10.451526], ratings: 3.265625 },
  { name: 'Belgium', location: [50.503887, 4.469936], ratings: 3.35 },
  { name: 'Czech Republic', location: [49.817492, 15.472962], ratings: 2.75 },
  { name: 'Austria', location: [47.516231, 14.550072], ratings: 3.17307692307692 },
  { name: 'Hungary', location: [47.162494, 19.503304], ratings: 3.25 },
  { name: 'Switzerland', location: [46.818188, 8.227512], ratings: 3.34 },
  { name: 'France', location: [46.227638, 2.213749], ratings: 3.33333333333333 },
  { name: 'Italy', location: [41.87194, 12.56738], ratings: 3.38815789473684 },
  { name: 'Spain', location: [40.463667, -3.74922], ratings: 3.30357142857143 },
  { name: 'Portugal', location: [39.399872, -8.224454], ratings: 2.75 },
  { name: 'Japan', location: [36.204824, 138.252924], ratings: 3.02272727272727 },
  { name: 'South Korea', location: [35.907757, 127.766922], ratings: 3.125 },
  { name: 'Israel', location: [31.046051, 34.851612], ratings: 3.5 },
  { name: 'Mexico', location: [23.634501, -102.552784], ratings: 2.91666666666667 },
  { name: 'Guatemala', location: [15.783471, -90.230759], ratings: 3.4 },
  { name: 'Vietnam', location: [14.058324, 108.277199], ratings: 3.40909090909091 },
  { name: 'Philippines', location: [12.879721, 121.774017], ratings: 3.5 },
  { name: 'Nicaragua', location: [12.865416, -85.207229], ratings: 3.25 },
  { name: 'Grenada', location: [12.262776, -61.604171], ratings: 2.83333333333333 },
  { name: 'Costa Rica', location: [9.748917, -83.753428], ratings: 2.875 },
  { name: 'Ghana', location: [7.946527, -1.023194], ratings: 2.75 },
  { name: 'Venezuela', location: [6.42375, -66.58973], ratings: 3.05 },
  { name: 'Colombia', location: [4.570868, -74.297333], ratings: 3.125 },
  { name: 'Suriname', location: [3.919305, -56.027783], ratings: 3.25 },
  { name: 'Singapore', location: [1.352083, 103.819836], ratings: 3.75 },
  { name: 'Ecuador', location: [-1.831239, -78.183406], ratings: 2.84848484848485 },
  { name: 'Peru', location: [-9.189967, -75.015152], ratings: 3.5 },
  { name: 'Brazil', location: [-14.235004, -51.92528], ratings: 3.5 },
  { name: 'Fiji', location: [-16.578193, 179.414413], ratings: 3.25 },
  { name: 'Madagascar', location: [-18.766947, 46.869107], ratings: 3.125 },
  { name: 'Australia', location: [-25.274398, 133.775136], ratings: 3.33333333333333 },
  { name: 'South Africa', location: [-30.559482, 22.937506], ratings: 2.5 },
  { name: 'Chile', location: [-35.675147, -71.542969], ratings: 3.75 },
  { name: 'Argentina', location: [-38.416097, -63.616672], ratings: 3.32142857142857 },
  { name: 'New Zealand', location: [-40.900557, 174.885971], ratings: 3.10714285714286 }
];

// Loop through the cities array and create one marker for each city object
for (var i = 0; i < countries.length; i++) {

  // Conditionals for countries ratings
  var color = "";
  if (countries[i].ratings > 3.25) {
    color = "green";
  }
  else if (countries[i].ratings > 3) {
    color = "blue";
  }
  else if (countries[i].ratings > 2.75) {
    color = "yellow";
  }
  else {
    color = "red";
  }

  // Add circles to map
  L.circle(countries[i].location, {
    fillOpacity: 0.75,
    color: "white",
    fillColor: color,
    // Adjust radius
    radius: countries[i].ratings * 35000
  }).bindPopup("<h1>" + countries[i].name + "</h1> <hr> <h3>Average Ratings: " + countries[i].ratings.toFixed(2) + "</h3>").addTo(myMap);
}
