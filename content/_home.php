<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Xtra Blog</title>

  <link rel="stylesheet" href="./css/css2.css" >
  <link rel="stylesheet" href="./css/bootstrap.min.css" >
  <link rel="stylesheet" href="./css/web-style.css" >
  <link rel="stylesheet" href="./css/map.css" >
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

  <script type="text/javascript" src="./js/jquery-1.11.1.min.js"></script>
  <script type="text/javascript" src="./js/canvasjs.stock.min.js"></script>
  <script type="text/javascript" src="https://polyfill.io/v3/polyfill.min.js?features=default"></script>
  <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDbndF8WMYh7wKQiNZ1EvtelEZkHD1XfwA&callback=initMap&libraries=&v=weekly" defer></script>
  <script type="text/javascript" src="./js/jquery.js"></script>
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
                <li class="tm-nav-item active"><a href="home" class="tm-nav-link"><i class="fas fa-home"></i> Dashboard</a></li>
                <li class="tm-nav-item"><a href="about" class="tm-nav-link"><i class="fas fa-home"></i> About</a></li>
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
                  <div id="map" style="width: 100%; height: 450px;"></div>
                </div>                
            </div>     

            <hr class="tm-hr-primary tm-mb-55">
            <div id="towerDetailsPanal"></div>

            <hr class="tm-hr-primary tm-mb-55">
            <!--<div class="row tm-row tm-mb-45">
                <div class="col-12">
                  <img id="loader" src="https://canvasjs.com/wp-content/uploads/images/gallery/javascript-stockcharts/overview/loading.gif" style="position: absolute; top: 150px; left: 48%; display: none"/>
                    <div id="chartContainer" style="height:700px; width: 100%; margin: 0px auto;"></div>
                </div>
            </div>
            -->

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