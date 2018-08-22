// Graph of race/ethnicity in 2015

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawRaceChart);
function drawRaceChart() {
  var data = google.visualization.arrayToDataTable([
    ['Race/Ethnicity', 'Percent'],
    ['Asian', 0.0553],
    ['Native American', 0.0021],
    ['Unknown', 0.0027],
    ['White', 0.762],
    ['Pacific Islander', 0.0013],
    ['Black', 0.0208],
    ['Two or More', 0.0295],
    ['Non Resident Alien', 0.0787],
    ['Hispanic', 0.0475]
  ]);

  var options = {
    title: '2015 Graph of Student Race/Ethnicity',
    pieHole: 0.4,
  };

  var chart = new google.visualization.PieChart(document.getElementById('race_donutchart'));
  chart.draw(data, options);
}


// Graph of program percentages in 2015

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawProgramChart);
function drawProgramChart() {
  var data = google.visualization.arrayToDataTable([
    ['Program', 'Percentage'],
    ['English', 2.7],
    ['Education', 1.96],
    ['Family Consumer Science', 2.64],
    ['Public Administration Social Service', 1.12],
    ['Religious Philosophy', 0.74],
    ['Engineering', 11.77],
    ['Business Marketing', 11.58],
    ['Mathematics', 1.9],
    ['Resources', 1.72],
    ['Biological', 13.55],
    ['Physical Science', 2.13],
    ['Architecture', .31],
    ['Legal', 1.18],
    ['Parks Recreation Fitness', 1.43],
    ['Psychology', 3.74],
    ['Social Science', 12.36],
    ['Multidiscipline', 2.89],
    ['Health', 4.79],
    ['Language', 3.56],
    ['History', 2.16],
    ['Agriculture', 3.81],
    ['Ethnic, Cultural, and Gender', 1.43],
    ['Computer', 2.35],
    ['Performing Arts', 2.49],
    ['Communication', 5.69]
  ]);

  var options = {
    title: '2015 Program Percentages',
    pieHole: 0.4,
  };

  var chart = new google.visualization.PieChart(document.getElementById('program_donutchart'));
  chart.draw(data, options);
}


// Graph of net price by income level.

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawPriceGraph);
function drawPriceGraph() {
  var data = google.visualization.arrayToDataTable([
    ["Element", "Total Cost", { role: "style" } ],
    ["0-30000", 8443, "#008000"],
    ["30001-48000", 11061, "#008000"],
    ["48001-75000", 17032, "#008000"],
    ["75001-110000", 21726, "#008000"],
    ["110001-plus", 23451, "#008000"]
  ]);

  var view = new google.visualization.DataView(data);
  view.setColumns([0, 1,
                   { calc: "stringify",
                     sourceColumn: 1,
                     type: "string",
                     role: "annotation" },
                   2]);

  var options = {
    title: "2015 Net Price (by income level)",
    width: 500,
    height: 400,
    bar: {groupWidth: "95%"},
    legend: { position: "none" },
  };
  var chart = new google.visualization.BarChart(document.getElementById("net_price_graph"));
  chart.draw(view, options);
}


// Graph of highest educational level of student's parents.

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawParentGraph);
function drawParentGraph() {
  var data = google.visualization.arrayToDataTable([
    ["Element", "Percent", { role: "style" } ],
    ["Middle School", 0.81, "#2980B9"],
    ["High School", 16.27, "#2980B9"],
    ["Some College", 82.91, "#2980B9"],
  ]);

  var view = new google.visualization.DataView(data);
  view.setColumns([0, 1,
                   { calc: "stringify",
                     sourceColumn: 1,
                     type: "string",
                     role: "annotation" },
                   2]);

  var options = {
    title: "2015 First Generation Parent Education",
    width: 500,
    height: 400,
    bar: {groupWidth: "95%"},
    legend: { position: "none" },
  };
  var chart = new google.visualization.BarChart(document.getElementById("parent_graph"));
  chart.draw(view, options);
}
