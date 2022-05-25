<?php
  // Initialize the session
  session_start();
 
  // Check if the user is logged in, if not then redirect him to login page
  if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
      header("location: login.php");
      exit;
  }
?>

<!DOCTYPE html>
<html>
<head>
  <style>
	  h2{
	    text-align: center;		
	  }

	  h3{
	    text-align: left;		
	  }

	  table, th, td 
	  {
	  border: 1px solid black;
	  }

	  body {
	    margin: 0;
	    background-color: powderblue;
	  }

	  button 
	  {
	    background-color: rgb(255,0,0);
	    color: white;
	    padding: 14px 20px;
	    margin: 8px 0;
	    border: none;
	    cursor: pointer;
	    width: 100%;
	  }

	  h1 {
	  background-color: black;
	  color: white;
	  text-align: center;
	  }

	  ul {
	    list-style-type: none;
	    margin: 0;
	    padding: 0;
	    width: 25%;
	    background-color: #f1f1f1;
	    position: fixed;
	    height: 100%;
	    overflow: auto;
	  }

	  li a {
	    display: block;
	    color: #000;
	    padding: 8px 16px;
	    text-decoration: none;
	  }

	  li a.active {
	    background-color: #04AA6D;
	    color: white;
	  }

	  li a:hover:not(.active) {
	    background-color: #555;
	    color: white;
	  }

	* {
	  box-sizing: border-box;
	}

	.box {
	  float: left;
	  width: 50%;
	  padding: 30px;
	  height: 550px;
	}

	.clearfix::after {
	  content: "";
	  clear: both;
	  display: table;
	}

  </style>
</head>
<body>

<h1>LoRa Location Tracker</h1>

<ul>
  <li><a class="active" href="home.php">Home</a></li>
  <li><a href="patientlist.php">Patient List</a></li>
  <li><a href="LoRaList.php">LoRa List</a></li>
  <li><a href="insert.php">Insert Patient</a></li>
  <li><a href="logout.php">Sign Out</a></li>
</ul>

<div style="margin-left:25%;padding:1px 16px;height:1000px;">

	<title>Insert</title>

	<h2>Insert Patient Information</h2>

	<div class="clearfix">
	  <div class="box" style="background-color:#bbb">
		<h2>Patient</h2>
		<form method="post" action="process.php">
			Patient ID:<br>
			<input type="text" name="PatientID">
			<br>
			First Name:<br>
			<input type="text" name="FirstName">
			<br>
			Last Name:<br>
			<input type="text" name="LastName">
			<br>
			Phone Number:<br>
			<input type="text" name="PhoneNo">
			<br>
			Gender:<br>
			<input type="text" name="Gender">
			<br>
			Health Condition:<br>
			<input type="text" name="HealthCondition">
			<br>
			Room Number:<br>
			<input type="text" name="RoomNo">
			<br>
		
	  </div>

	  <div class="box" style="background-color:#ccc">
	  <h2>Contact Person</h2>
			First Name:<br>
			<input type="text" name="CFirstName">
			<br>
			Last Name:<br>
			<input type="text" name="CLastName">
			<br>
			Relationship:<br>
			<input type="text" name="CRelationship">
			<br>
			Phone Number:<br>
			<input type="text" name="CPhoneNo">
			<br>
			Gender:<br>
			<input type="text" name="CGender">
			<br>
	  <h2>LoRa</h2>		
			LoRa Number<br>
			<input type="text" name="LLoRaNo">
			<br>	
	  </div>
	</div>

<br>
		<input type="submit" name="save" value="submit">
</form>
</body>
</html>
