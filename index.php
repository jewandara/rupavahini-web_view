<?php

/*
if($_SERVER["REQUEST_SCHEME"] == "http"){ header("Location: https://".$_SERVER["HTTP_HOST"].$_SERVER['REQUEST_URI'], true, 301); exit(); }
//print_r($_URL);
//print_r($_GET);
//print_r($_POST);
*/

$_URL = explode("/", $_SERVER['REQUEST_URI']);
session_start();
$MESSAGE ="";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST['username'];
  $pass = $_POST['password'];
  if( (!empty($name)) && ($name=="Admin") ) {
    if( (!empty($pass)) && ($pass=="Admin#2020") ) {
      $_SESSION["login"] = "true";
      $_SESSION["user"] = "Admin";
    } else { $MESSAGE ="Incorrect Password.<br>Please try again."; }
  } else { $MESSAGE ="Incorrect Username.<br>Please try again."; }
}

require_once('content/config.php');

if( (!empty($_SESSION["login"])) && ($_SESSION["login"]=="true") ) {
	switch ($_URL[2]) {
	    case "":
	        require_once("content/_home.php");
	        break;
	    case "index":
	        require_once("content/_home.php");
	        break;
	    case "home":
	        require_once("content/_home.php");
	        break;
	    case "dashboard":
	        require_once("content/_home.php");
	        break;
	    case "about":
	        require_once("content/_about.php");
	        break;
	    case "logout":
	    	session_destroy();
	        require_once("content/_login.php");
	        break;
	    default:
	        require_once("content/_home.php");
	        break;
	}
}
else{ require_once("content/_login.php"); }

?>