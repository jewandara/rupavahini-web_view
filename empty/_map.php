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

  <script type="text/javascript" src="./js/jquery-1.11.1.min.js"></script>
  <script type="text/javascript" src="./js/canvasjs.stock.min.js"></script>
  <script type="text/javascript" src="https://polyfill.io/v3/polyfill.min.js?features=default"></script>
  <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDbndF8WMYh7wKQiNZ1EvtelEZkHD1XfwA&callback=initMap&libraries=&v=weekly" defer></script>
  <script type="text/javascript" src="./js/map.js"></script>
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
                  <!--
                  <div id="style-selector-control" class="map-control">
                    <select id="style-selector" class="selector-control">
                      <option value="default">Default</option>
                      <option value="silver" selected="selected">Silver</option>
                      <option value="night">Night mode</option>
                      <option value="retro">Retro</option>
                      <option value="hiding">Hide features</option>
                    </select>
                  </div>-->
                  <div id="map" style="width: 100%; height: 450px;"></div>

                </div>                
            </div>     




            <hr class="tm-hr-primary tm-mb-55">
            <div class="row tm-row tm-mb-60">               
                <div class="col-lg-6 tm-mb-60 tm-person-col">
                    <div class="media tm-person">
                      <hr class="tm-hr-primary tm-mb-55">
                        <div class="media-body">
                            <h2 class="tm-color-primary tm-post-title mb-2">Receiver Signal Levels</h2>
                            <h3 class="tm-h3 mb-3">Considering recent time : 2020-08-04 12:24:05</h3>

                              <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
                              <div class="w3-container">

                                <h4>Signal Level Colors</h4>
                                <p>Strength of Cutoff Frequency (175.25 Mz):</p>

                                <div class="w3-light-grey" style="border: 1px groove">
                                  <div class="w3-green" style="height:24px;width:55%"><p style="color:#fff; padding-left: 10px;">-34.48 dBm</p></div>
                                </div>
                                <p style="margin-bottom:-5px;">Lower Cutoff Frequency (175.00 Mz) : -34.48 dBm</p>
                                <p style="margin-bottom:-5px;">Upper Cutoff Frequency (175.00 Mz) : -34.48 dBm</p>
                                <p style="margin-bottom:-5px;">Sampling Interval : 0.25 Mz</p>
                                <p style="margin-bottom:-5px;">Gain : 234</p><br>
                                <h4>Signal Strength Colors Explained</h4>

                                <div class="w3-light-grey">
                                  <div style="height:24px;width:100%;border: 1px groove #000; border-bottom: none; background-color: #b8fc17"><p style="color:#fff; padding-left: 10px;">TOO STRONG : 10 dBm UPTO -05 dBm</p></div>
                                  <div style="height:24px;width:100%;border: 1px groove #000; border-bottom: none; background-color: #3bde26"><p style="color:#fff; padding-left: 10px;">STRONG : -05 dBm UPTO -35 dBm</p></div>
                                  <div style="height:24px;width:100%;border: 1px groove #000; border-bottom: none; background-color: #1f8a1d"><p style="color:#fff; padding-left: 10px;">GOOD : -35 dBm UPTO -50 dBm</p></div>
                                  <div style="height:24px;width:100%;border: 1px groove #000; border-bottom: none; background-color: #0952e3"><p style="color:#fff; padding-left: 10px;">MODERATE : -50 dBm UPTO -60 dBm</p></div>
                                  <div style="height:24px;width:100%;border: 1px groove #000; border-bottom: none; background-color: #8f0000"><p style="color:#fff; padding-left: 10px;">MARGINAL : -60 dBm UPTO -65 dBm</p></div>
                                  <div style="height:24px;width:100%;border: 1px groove #000; border-bottom: none; background-color: #7a7a7a"><p style="color:#fff; padding-left: 10px;">LOW : -65 dBm UPTO -95 dBm</p></div>
                                  <div style="height:24px;width:100%;border: 1px groove #000; background-color: #292929"><p style="color:#fff; padding-left: 10px;">NOISE : -95 dBm UPTO</p></div>
                                </div>
                              </div>
                        </div>
                    </div>                  
                </div>
                <div class="col-lg-6 tm-mb-60 tm-person-col">
                    <div class="media tm-person">
                      <hr class="tm-hr-primary tm-mb-55">
                        <div class="media-body">
                            <h2 class="tm-color-primary tm-post-title mb-2">Tv Screen Test Image</h2>
                            <h3 class="tm-h3 mb-3">Considering recent time : 2020-08-04 12:24:05</h3>
                            <img src="https://api.maxford.lk/rupavahini/vc_means_vision_carrier/image.php?id=32" alt="Girl in a jacket" width="100%">
                        </div>
                    </div> 
                </div>
            </div>

            <hr class="tm-hr-primary tm-mb-55">





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