<?php
	$MyUsername = "pi";  // enter your username for mysql
	$MyPassword = "root";  // enter your password for mysql
	$MyHostname = "localhost";      // this is usually "localhost" unless your database resides on a different server
	$dbh = mysql_pconnect($MyHostname , $MyUsername, $MyPassword);
	$selected = mysql_select_db("mydb",$dbh); //Enter your database name here 
?>