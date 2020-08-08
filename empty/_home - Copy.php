<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Xtra Blog</title>

  <link rel="stylesheet" href="./css/css2.css" >
  <link rel="stylesheet" href="./css/bootstrap.min.css" >
  <link rel="stylesheet" href="./css/web-style.css" >

  <script type="text/javascript" src="./js/jquery-1.11.1.min.js"></script>
  <script type="text/javascript" src="./js/canvasjs.stock.min.js"></script>
  <script type="text/javascript">

/* Project270$*2020 
//AIzaSyDbndF8WMYh7wKQiNZ1EvtelEZkHD1XfwA
window.onload = function () {
  var stockChart = new CanvasJS.StockChart("chartContainer",{
    title:{ text:"VC Means Vision Carrier"},
    animationEnabled: true,
    exportEnabled: true,
    charts: [{
      axisX: { crosshair: { enabled: true, snapToDataPoint: true, valueFormatString: "MMM DD, YYYY HH:mm:ss" } },
      axisY: { 
        title: "Pageviews Per Second", 
        crosshair: { enabled: true, snapToDataPoint: true }, 
        stripLines: [{ showOnTop: true, lineDashType: "dash", color: "#ff4949", labelFontColor: "#ff4949", labelFontSize: 7 }] 
      },
      toolTip: { shared: true },
      data: [{ type: "splineArea", color: "#800040", yValueFormatString: "€1 = $#,###.##", dataPoints : dataPoints }]
    }],
    rangeSelector: {
      inputFields: { startValue: 4000, endValue: 6000, valueFormatString: "###0" },
      buttons: [
      { label: "10", range: 10, rangeType: "number" },
      { label: "2000", range: 2000, rangeType: "number" },
      { label: "5000", range: 5000, rangeType: "number" },
      { label: "All", rangeType: "all" }
      ]
    }
  });

  stockChart.render();

  var dataCount = 700, ystart = 50, interval = 1000, xstart = (currentDate.getTime() - (700 * 1000));
  updateChart(xstart, ystart, dataCount, interval);
  function updateChart(xstart, ystart, length, interval) {
    var xVal = xstart, yVal = ystart;
    for(var i = 0; i < length; i++) {
      yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
      yVal = Math.min(Math.max(yVal, 5), 90);
      dataPoints.push({x: xVal,y: yVal});
      xVal += interval;
    }
    stockChart.options.navigator.slider.minimum = new Date(xVal - (90 * 1000));
    stockChart.options.charts[0].axisY.stripLines[0].value =  dataPoints[dataPoints.length - 1].y;
    stockChart.options.charts[0].axisY.stripLines[0].label = stockChart.options.charts[0].axisY.stripLines[0]["value"];
    xstart = xVal;
    dataCount = 1;
    ystart = yVal;
    stockChart.render();
    setTimeout(function() { updateChart(xstart, ystart, dataCount, interval); }, 1000);
  }
}

var limit = 10000;    //increase number of dataPoints by increasing this
var y = 1000;
var data = []; var dataSeries = { type: "spline" };
var dataPoints = [];
for (var i = 0; i < limit; i += 1) {
  y += Math.round((Math.random() * 10 - 5));
  dataPoints.push({ x: i, y: y });
}
dataSeries.dataPoints = dataPoints;
data.push(dataSeries);
*/

/*
window.onload = function () {
  var dataPoints = [], currentDate = new Date();
  var stockChart = new CanvasJS.StockChart("chartContainer",{
    theme: "light2",
    title:{
      text:"Dynamic StockChart with Stripline"
    },
    charts: [{
      axisX: {
         crosshair: {
          enabled: true,
          valueFormatString: "MMM DD, YYYY HH:mm:ss"
        }
      },
      axisY: {
        title: "Pageviews Per Second",
        stripLines: [{
          showOnTop: true,
          lineDashType: "dash",
          color: "#ff4949",
          labelFontColor: "#ff4949",
          labelFontSize: 14
        }]
      },
      toolTip: {
        shared: true
      },
      data: [{
        type: "line",
        name: "Pageviews",
        xValueFormatString: "MMM DD, YYYY HH:mm:ss",
        xValueType: "dateTime",
        dataPoints : dataPoints
      }]
    }],
    navigator: {
      slider: {
        minimum: new Date(currentDate.getTime() - (90 * 1000))
      }
    },
    rangeSelector: {
      enabled: false
    }
  });



  var dataCount = 100, ystart = 50, interval = 300000, xstart = (currentDate.getTime() - (700 * 1000));
  updateChart(xstart, ystart, dataCount, interval);



  function updateChart(xstart, ystart, length, interval) {
    var xVal = xstart, yVal = ystart;
    for(var i = 0; i < length; i++) {
      yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
      console.log(yVal);
      yVal = Math.min(Math.max(yVal, 5), 90);
      dataPoints.push({x: xVal,y: yVal});
      xVal += interval;
    }
    stockChart.options.navigator.slider.minimum = new Date(xVal - (90 * 1000));
    stockChart.options.charts[0].axisY.stripLines[0].value =  dataPoints[dataPoints.length - 1].y;
    stockChart.options.charts[0].axisY.stripLines[0].label = stockChart.options.charts[0].axisY.stripLines[0]["value"];
    xstart = xVal;
    dataCount = 1;
    ystart = yVal;
    stockChart.render();
    setTimeout(function() { updateChart(xstart, ystart, dataCount, interval); }, 1000);
  }
}
*/


window.onload = function () {
  var dataPoints1 = [], dataPoints2 = [];
  var stockChart = new CanvasJS.StockChart("chartContainer",{
    title:{
      text:"Loading Graph ..."
    },
    rangeChanged: rangeChanged,
    charts: [{
      axisY2: {
        prefix: "$"
      },
      data: [{
        type: "candlestick",
        yValueFormatString: "$#,###.##",
        axisYType: "secondary",
        dataPoints : dataPoints1
      }]
    }],
    navigator: {
      dynamicUpdate: false,
      data: [{
        dataPoints: dataPoints2
      }],
      slider: {
        minimum: new Date(2015, 05, 01),
        maximum: new Date(2025, 05, 01)
      }
    }
  });
  function addData(data) {
    stockChart.options.charts[0].data[0].dataPoints = [];
    for(var i = 0; i < data.length; i++){
      stockChart.options.charts[0].data[0].dataPoints.push({x: new Date(data[i].dateTime*1000), y: [ Number(data[i].open), Number(data[i].high), Number(data[i].low), Number(data[i].close) ]});
    }
    stockChart.render();
  }
  function rangeChanged(e) {
    var minimum = parseInt(e.minimum / 1000);
    var maximum = parseInt(e.maximum / 1000);
    var url = "https://canvasjs.com/services/data/datapoints-bitcoinusd.php?minimum="+minimum+"&maximum="+maximum;
    $("#loader").css("display", "block");
    $.getJSON(url, function(data) {
      addData(data);
      $("#loader").css("display", "none");
    });
  }
  $("#loader").css("display", "block");
  $.getJSON("https://canvasjs.com/services/data/datapoints-bitcoinusd.php", function(data) {
    for(var i = 0; i < data.length; i++){
      dataPoints1.push({x: new Date(data[i].dateTime*1000), y: [Number(data[i].open), Number(data[i].high), Number(data[i].low), Number(data[i].close)]});
      dataPoints2.push({x: new Date(data[i].dateTime*1000), y: Number(data[i].close)});
    }
    $("#loader").css("display", "none");
    stockChart.render();
  });
}
</script>
</head>
<body>

  <header class="tm-header" id="tm-header">
    <div class="tm-header-wrapper">
      <div class="tm-site-header">
        <table>
          <tr>
            <td> <img src="./images/ru_logo.png" alt="Girl in a jacket" width="100"></td>
            <td> <h3> Rupavahini</h3></td>
          </tr>
          <tr>
        </table>
        <nav class="tm-nav" id="tm-nav">            
            <ul>
                <li class="tm-nav-item active"><a href="map" class="tm-nav-link"><i class="fas fa-home"></i> Map View</a></li>
                <li class="tm-nav-item"><a href="report" class="tm-nav-link"><i class="fas fa-home"></i> Report View</a></li>
                <li class="tm-nav-item"><a href="contact" class="tm-nav-link"><i class="fas fa-home"></i> Contact</a></li>
                <li class="tm-nav-item"><a href="logout" class="tm-nav-link"><i class="fas fa-home"></i> Logout</a></li>
            </ul>
        </nav>
      </div>
    </div>
  </header>


<div class="container-fluid">
        <main class="tm-main">
            <div class="row tm-row">
                <div class="col-12">


                </div>                
            </div>            

            <div class="row tm-row tm-mb-45">
                <div class="col-12">
                  <img id="loader" src="https://canvasjs.com/wp-content/uploads/images/gallery/javascript-stockcharts/overview/loading.gif" style="position: absolute; top: 150px; left: 48%; display: none"/>
                    <div id="chartContainer" style="height:700px; width: 100%; margin: 0px auto;"></div>
                </div>
            </div>
            <footer class="row tm-row">
                <hr class="col-12">
                <div class="col-md-6 col-12 tm-color-gray"> Design: <a rel="nofollow" target="_parent" href="https://jewandara.com" class="tm-external-link">Jewandara.Com</a></div>
                <div class="col-md-6 col-12 tm-color-gray tm-copyright"> Copyright 2020 Jeewandara Industries </div>
            </footer>
        </main>
    </div>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/templatemo-script.js"></script>
</body>
</html>