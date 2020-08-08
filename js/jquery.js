"use strict";

let map, popup, Popup;

const citymap = {
  rupavahini_tower_1: {
    center: { lat: 7.0000376, lng: 80.7714522 },
    population: 1000
  },
  rupavahini_tower_2: {
    center: { lat: 7.0000376, lng: 80.7714522 },
    population: 10000
  },
  rupavahini_tower_3: {
    center: { lat: 7.0000376, lng: 80.7714522 },
    population: 100000
  },
  receiving_tower: {
    center: { lat: 7.0000376, lng: 80.0714522 },
    population: 1837
  }
};

const styles = {
  default: [],
  silver: [
    {
      elementType: "geometry",
      stylers: [
        {
          color: "#f5f5f5"
        }
      ]
    },
    {
      elementType: "labels.icon",
      stylers: [
        {
          visibility: "off"
        }
      ]
    },
    {
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#616161"
        }
      ]
    },
    {
      elementType: "labels.text.stroke",
      stylers: [
        {
          color: "#f5f5f5"
        }
      ]
    },
    {
      featureType: "administrative.land_parcel",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#bdbdbd"
        }
      ]
    },
    {
      featureType: "poi",
      elementType: "geometry",
      stylers: [
        {
          color: "#eeeeee"
        }
      ]
    },
    {
      featureType: "poi",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#757575"
        }
      ]
    },
    {
      featureType: "poi.park",
      elementType: "geometry",
      stylers: [
        {
          color: "#e5e5e5"
        }
      ]
    },
    {
      featureType: "poi.park",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#9e9e9e"
        }
      ]
    },
    {
      featureType: "road",
      elementType: "geometry",
      stylers: [
        {
          color: "#ffffff"
        }
      ]
    },
    {
      featureType: "road.arterial",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#757575"
        }
      ]
    },
    {
      featureType: "road.highway",
      elementType: "geometry",
      stylers: [
        {
          color: "#dadada"
        }
      ]
    },
    {
      featureType: "road.highway",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#616161"
        }
      ]
    },
    {
      featureType: "road.local",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#9e9e9e"
        }
      ]
    },
    {
      featureType: "transit.line",
      elementType: "geometry",
      stylers: [
        {
          color: "#e5e5e5"
        }
      ]
    },
    {
      featureType: "transit.station",
      elementType: "geometry",
      stylers: [
        {
          color: "#eeeeee"
        }
      ]
    },
    {
      featureType: "water",
      elementType: "geometry",
      stylers: [
        {
          color: "#c9c9c9"
        }
      ]
    },
    {
      featureType: "water",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#9e9e9e"
        }
      ]
    }
  ],
  night: [
    {
      elementType: "geometry",
      stylers: [
        {
          color: "#242f3e"
        }
      ]
    },
    {
      elementType: "labels.text.stroke",
      stylers: [
        {
          color: "#242f3e"
        }
      ]
    },
    {
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#746855"
        }
      ]
    },
    {
      featureType: "administrative.locality",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#d59563"
        }
      ]
    },
    {
      featureType: "poi",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#d59563"
        }
      ]
    },
    {
      featureType: "poi.park",
      elementType: "geometry",
      stylers: [
        {
          color: "#263c3f"
        }
      ]
    },
    {
      featureType: "poi.park",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#6b9a76"
        }
      ]
    },
    {
      featureType: "road",
      elementType: "geometry",
      stylers: [
        {
          color: "#38414e"
        }
      ]
    },
    {
      featureType: "road",
      elementType: "geometry.stroke",
      stylers: [
        {
          color: "#212a37"
        }
      ]
    },
    {
      featureType: "road",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#9ca5b3"
        }
      ]
    },
    {
      featureType: "road.highway",
      elementType: "geometry",
      stylers: [
        {
          color: "#746855"
        }
      ]
    },
    {
      featureType: "road.highway",
      elementType: "geometry.stroke",
      stylers: [
        {
          color: "#1f2835"
        }
      ]
    },
    {
      featureType: "road.highway",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#f3d19c"
        }
      ]
    },
    {
      featureType: "transit",
      elementType: "geometry",
      stylers: [
        {
          color: "#2f3948"
        }
      ]
    },
    {
      featureType: "transit.station",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#d59563"
        }
      ]
    },
    {
      featureType: "water",
      elementType: "geometry",
      stylers: [
        {
          color: "#17263c"
        }
      ]
    },
    {
      featureType: "water",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#515c6d"
        }
      ]
    },
    {
      featureType: "water",
      elementType: "labels.text.stroke",
      stylers: [
        {
          color: "#17263c"
        }
      ]
    }
  ],
  retro: [
    {
      elementType: "geometry",
      stylers: [
        {
          color: "#ebe3cd"
        }
      ]
    },
    {
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#523735"
        }
      ]
    },
    {
      elementType: "labels.text.stroke",
      stylers: [
        {
          color: "#f5f1e6"
        }
      ]
    },
    {
      featureType: "administrative",
      elementType: "geometry.stroke",
      stylers: [
        {
          color: "#c9b2a6"
        }
      ]
    },
    {
      featureType: "administrative.land_parcel",
      elementType: "geometry.stroke",
      stylers: [
        {
          color: "#dcd2be"
        }
      ]
    },
    {
      featureType: "administrative.land_parcel",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#ae9e90"
        }
      ]
    },
    {
      featureType: "landscape.natural",
      elementType: "geometry",
      stylers: [
        {
          color: "#dfd2ae"
        }
      ]
    },
    {
      featureType: "poi",
      elementType: "geometry",
      stylers: [
        {
          color: "#dfd2ae"
        }
      ]
    },
    {
      featureType: "poi",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#93817c"
        }
      ]
    },
    {
      featureType: "poi.park",
      elementType: "geometry.fill",
      stylers: [
        {
          color: "#a5b076"
        }
      ]
    },
    {
      featureType: "poi.park",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#447530"
        }
      ]
    },
    {
      featureType: "road",
      elementType: "geometry",
      stylers: [
        {
          color: "#f5f1e6"
        }
      ]
    },
    {
      featureType: "road.arterial",
      elementType: "geometry",
      stylers: [
        {
          color: "#fdfcf8"
        }
      ]
    },
    {
      featureType: "road.highway",
      elementType: "geometry",
      stylers: [
        {
          color: "#f8c967"
        }
      ]
    },
    {
      featureType: "road.highway",
      elementType: "geometry.stroke",
      stylers: [
        {
          color: "#e9bc62"
        }
      ]
    },
    {
      featureType: "road.highway.controlled_access",
      elementType: "geometry",
      stylers: [
        {
          color: "#e98d58"
        }
      ]
    },
    {
      featureType: "road.highway.controlled_access",
      elementType: "geometry.stroke",
      stylers: [
        {
          color: "#db8555"
        }
      ]
    },
    {
      featureType: "road.local",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#806b63"
        }
      ]
    },
    {
      featureType: "transit.line",
      elementType: "geometry",
      stylers: [
        {
          color: "#dfd2ae"
        }
      ]
    },
    {
      featureType: "transit.line",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#8f7d77"
        }
      ]
    },
    {
      featureType: "transit.line",
      elementType: "labels.text.stroke",
      stylers: [
        {
          color: "#ebe3cd"
        }
      ]
    },
    {
      featureType: "transit.station",
      elementType: "geometry",
      stylers: [
        {
          color: "#dfd2ae"
        }
      ]
    },
    {
      featureType: "water",
      elementType: "geometry.fill",
      stylers: [
        {
          color: "#b9d3c2"
        }
      ]
    },
    {
      featureType: "water",
      elementType: "labels.text.fill",
      stylers: [
        {
          color: "#92998d"
        }
      ]
    }
  ],
  hiding: [
    {
      featureType: "poi.business",
      stylers: [
        {
          visibility: "off"
        }
      ]
    },
    {
      featureType: "transit",
      elementType: "labels.icon",
      stylers: [
        {
          visibility: "off"
        }
      ]
    }
  ]
};


function initMap() {
  map = new google.maps.Map(document.getElementById("map"), { 
    center: { lat: 7.0000376, lng: 80.4714522 }, 
    zoom: 10,  
    mapTypeControl: false,
    mapTypeId: "terrain"
  });

  

  /*
   for (const city in citymap) {
    cityCircle = new google.maps.Circle({
      strokeColor: "#d61900",
      strokeOpacity: 0.8,
      strokeWeight: 0,
      fillColor: "#d61900",
      fillOpacity: 0.35,
      map,
      center: citymap[city].center,
      radius: Math.sqrt(citymap[city].population) * 100
    });
  }
  */


  const contentStringRupavahini =
    '<div id="content"><div id="siteNotice"></div>' +
    '<h1 id="firstHeading" class="firstHeading">Sri Lanka Rupavahini Corporation</h1>' +
    '<div id="bodyContent">' +
    '<p>Sri Lanka Rupavahini (TV) Corporation, the State Television stands for the benefit of all Sri Lankans. We do recognise the peoples diversity of expectations, values , interests and needs. We reach our target groups in Sinhala, Tamil and English languages.</p>' +
    '<p>Rupavahini Web: <a href="http://www.rupavahini.lk/">Visit Site</a></p>' +
    "</div></div>";
  const infowindowRupavahini = new google.maps.InfoWindow({ content: contentStringRupavahini, maxWidth: 400 });
  var iconRupavahini = { url: "images/rupavahini_tower.png", scaledSize: new google.maps.Size(22, 67) };
  const markerRupavahini = new google.maps.Marker({ position: { lat: 7.0000376, lng: 80.7714522 }, map, icon: iconRupavahini, title: "Sri Lanka Rupavahini (TV) Corporation" });
  markerRupavahini.addListener("click", () => { infowindowRupavahini.open(map, markerRupavahini); });


  var contentStringTower =
    '<div id="content">' +
    ' <h3 class="tm-color-primary tm-post-title mb-2">Testing Location One</h3>' +
    ' <div id="bodyContent">' +
    '   <h4 class="tm-h3 mb-3">Considering recent time : 2020-08-04 12:24:05</h4>'+
    '   <div class="w3-container">'+
    '     <p>Strength of (175.25 Mz):</p>'+
    '     <div class="w3-light-grey" style="border: 1px groove">'+
    '       <div class="w3-green" style="height:16px;width:100%"><p style="color:#fff; padding-left: 5px;">Strength : -34.48 dBm</p></div>'+
    '     </div>'+
    '     <br><input type="button" onclick="viewMoreBellowPage()" value="VIEW MORE" /><input type="button" style="margin-left: 10px;" onclick="viewMoreBellowPage()" value="REFRESH" />'+
    '   </div>'+
    " </div>"+
    "</div>";
  var infowindowTower = new google.maps.InfoWindow({ content: contentStringTower, maxWidth: 250 });
  var iconTower = { url: "images/receiving_tower.png", scaledSize: new google.maps.Size(25, 34) };
  var markerTower = new google.maps.Marker({ position: { lat: 7.0000376, lng: 80.0714522 }, map, icon: iconTower, title: "Testing Location One" });
  markerTower.addListener("click", () => { infowindowTower.open(map, markerTower); });

  function markerTowerUpdate(data){
    contentStringTower =
      '<div id="content">' +
      ' <h3 class="tm-color-primary tm-post-title mb-2">Testing Location One</h3>' +
      ' <div id="bodyContent">' +
      '   <h4 class="tm-h3 mb-3">Considering recent time : '+data.time+'</h4>'+
      '   <div class="w3-container">'+
      '     <p>Strength of (175.25 Mz):</p>'+
      '     <div class="w3-light-grey" style="border: 1px groove">'+
      '       <div style="height:16px;width:100%;background-color:'+data.color+';"><p style="color:#fff; padding-left: 5px;">Strength : '+data.value+' dBm</p></div>'+
      '     </div>'+
      '     <br><input type="button" onclick="viewMoreBellowPage()" value="VIEW MORE" /><input type="button" style="margin-left: 10px;" onclick="viewMoreBellowPage()" value="REFRESH" />'+
      '   </div>'+
      " </div>"+
      "</div>";
    infowindowTower = new google.maps.InfoWindow({ content: contentStringTower, maxWidth: 250 });
    markerTower.addListener("click", () => { infowindowTower.open(map, markerTower); });
  }




  const styleControl = document.getElementById("style-selector-control");
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(styleControl);
  const styleSelector = document.getElementById("style-selector");
  map.setOptions({ styles: styles["retro"] });
  //styleSelector.addEventListener("change", () => { map.setOptions({ styles: styles["retro"] }); });
  


  var towerCircle_one = new google.maps.Circle({
    strokeColor: "#000000",
    strokeOpacity: 0.8,
    strokeWeight: 0,
    fillColor: "#000000",
    fillOpacity: 0.35,
    map,
    center: { lat: 7.0000376, lng: 80.0714522 },
    radius: Math.sqrt(1000) * 100
  });
  var towerCircle_two = new google.maps.Circle({
    strokeColor: "#000000",
    strokeOpacity: 0.8,
    strokeWeight: 0,
    fillColor: "#000000",
    fillOpacity: 0.35,
    map,
    center: { lat: 7.0000376, lng: 80.0714522 },
    radius: Math.sqrt(10000) * 100
  });
  var rupavahiniCircle_one = new google.maps.Circle({
    strokeColor: "#000000",
    strokeOpacity: 0.8,
    strokeWeight: 0,
    fillColor: "#000000",
    fillOpacity: 0.35,
    map,
    center: { lat: 7.0000376, lng: 80.7714522 },
    radius: Math.sqrt(1000) * 100
  });
  var rupavahiniCircle_two = new google.maps.Circle({
    strokeColor: "#000000",
    strokeOpacity: 0.8,
    strokeWeight: 0,
    fillColor: "#000000",
    fillOpacity: 0.35,
    map,
    center: { lat: 7.0000376, lng: 80.7714522 },
    radius: Math.sqrt(10000) * 100
  });
  var rupavahiniCircle_three = new google.maps.Circle({
    strokeColor: "#000000",
    strokeOpacity: 0.8,
    strokeWeight: 0,
    fillColor: "#000000",
    fillOpacity: 0.35,
    map,
    center: { lat: 7.0000376, lng: 80.7714522 },
    radius: Math.sqrt(100000) * 100
  });

  function updateCircle(colour) {
    towerCircle_one.setMap(null);
    towerCircle_two.setMap(null);
    rupavahiniCircle_one.setMap(null);
    rupavahiniCircle_two.setMap(null);
    rupavahiniCircle_three.setMap(null);
    towerCircle_one = new google.maps.Circle({
      strokeColor: colour,
      strokeOpacity: 0.8,
      strokeWeight: 0,
      fillColor: colour,
      fillOpacity: 0.35,
      map,
      center: { lat: 7.0000376, lng: 80.0714522 },
      radius: Math.sqrt(1000) * 100
    });
    towerCircle_two = new google.maps.Circle({
      strokeColor: colour,
      strokeOpacity: 0.8,
      strokeWeight: 0,
      fillColor: colour,
      fillOpacity: 0.35,
      map,
      center: { lat: 7.0000376, lng: 80.0714522 },
      radius: Math.sqrt(10000) * 100
    });
    rupavahiniCircle_one = new google.maps.Circle({
      strokeColor: colour,
      strokeOpacity: 0.8,
      strokeWeight: 0,
      fillColor: colour,
      fillOpacity: 0.35,
      map,
      center: { lat: 7.0000376, lng: 80.7714522 },
      radius: Math.sqrt(5000) * 100
    });
    rupavahiniCircle_two = new google.maps.Circle({
      strokeColor: colour,
      strokeOpacity: 0.8,
      strokeWeight: 0,
      fillColor: colour,
      fillOpacity: 0.35,
      map,
      center: { lat: 7.0000376, lng: 80.7714522 },
      radius: Math.sqrt(50000) * 100
    });
    rupavahiniCircle_three = new google.maps.Circle({
      strokeColor: colour,
      strokeOpacity: 0.8,
      strokeWeight: 0,
      fillColor: colour,
      fillOpacity: 0.35,
      map,
      center: { lat: 7.0000376, lng: 80.7714522 },
      radius: Math.sqrt(100000) * 100
    });
  }

  function updateMap() {
    towerCircle_one.setMap(null);
    towerCircle_two.setMap(null);
    rupavahiniCircle_one.setMap(null);
    rupavahiniCircle_two.setMap(null);
    rupavahiniCircle_three.setMap(null);

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var mapObj = JSON.parse(this.responseText);
        updateCircle(mapObj.color);
        markerTowerUpdate(mapObj);
      }
    };
    xmlhttp.open("GET", "http://localhost/vc_means_vision_carrier/php_vc_means_vision_carrier_server/ajax-map.php", true);
    xmlhttp.send();
    setTimeout(function() { updateMap(); }, 1000);
  }


  updateMap();
}



/**********************************************************/
/**********************************************************/
/**********************************************************/

function viewMoreBellowPage() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("towerDetailsPanal").innerHTML = this.responseText;
      }
    }
    xmlhttp.open("GET", "http://localhost/vc_means_vision_carrier/php_vc_means_vision_carrier_server/ajax-data.php", true);
    xmlhttp.send();
}




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