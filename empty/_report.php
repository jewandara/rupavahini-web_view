<!DOCTYPE html>
<html>
  <head>
    <title>Circles</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=default"></script>
    <script
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDbndF8WMYh7wKQiNZ1EvtelEZkHD1XfwA&callback=initMap&libraries=&v=weekly"
      defer
    ></script>
    <style type="text/css">
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }

      /* Optional: Makes the sample page fill the window. */
      html,
      body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
    <script>
      "use strict";

      const citymap = {
        chicago: {
          center: { lat: 41.878, lng: -87.629 },
          population: 2714856
        },


        newyork: {
          center: { lat: 40.714, lng: -74.005 },
          population: 8405837
        }

      };

      function initMap() {
        // Create the map.
        const map = new google.maps.Map(document.getElementById("map"), {
          zoom: 4,
          center: {
            lat: 37.09,
            lng: -95.712
          },
          mapTypeId: "terrain"
        }); // Construct the circle for each value in citymap.
        // Note: We scale the area of the circle based on the population.

        for (const city in citymap) {
          // Add the circle for this city to the map.
          const cityCircle = new google.maps.Circle({
            strokeColor: "#FF0000",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#FF0000",
            fillOpacity: 0.35,
            map,
            center: citymap[city].center,
            radius: Math.sqrt(citymap[city].population) * 100
          });
        }


        


      }
    </script>
  </head>
  <body>
    <div id="map"></div>
  </body>
</html>