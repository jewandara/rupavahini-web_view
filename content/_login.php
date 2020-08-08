<!DOCTYPE html>
<head>
	<meta charset="utf-8">
	<title>Rupavahini - vc means vision carrier</title>
	<link rel="apple-touch-icon" href="./images/ru_logo.png">
    <link rel="shortcut icon" type="image/x-icon" href="./images/ru_logo.png">
	<link rel="stylesheet" type="text/css" href="./css/style.css" />
</head>
<body>

	<div class="login">
    <table>
    	<tr>
    		<td> <img src="./images/ru_logo.png" alt="Girl in a jacket" width="100"></td>
    		<td> <h3>VC Means Vision Carrier</h3></td>
    	</tr>
    </table>

    <form method="post">
        <input type="text" name="username" placeholder="Username" required="required" />
        <input type="password" name="password" placeholder="Password" required="required" />
        <button type="submit" class="btn btn-primary btn-block btn-large">LOGIN</button>
    </form>
    <h5><?=$MESSAGE?></h5>
</div>
</body>
</html>