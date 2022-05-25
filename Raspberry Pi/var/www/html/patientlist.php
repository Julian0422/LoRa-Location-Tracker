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

	  <title>PatientList</title>
	  
<h2>Target Position</h2>

<?php
echo "The time is " . date("h:i:sa");
?>

<?php
$mysqli = new mysqli("localhost","pi","root","mydb");

if ($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}

$sql = "SELECT Patient.PatientID, Patient.FirstName, Patient.LastName, LoRa.Position FROM Patient INNER JOIN LoRa ON LoRa.Patient_PatientID =Patient.PatientID ORDER BY Patient.PatientID;";

// Execute multi query
if ($mysqli -> multi_query($sql)) {
	echo "<table>";
	echo "<tr>
	        <th>Patient No</th>
	        <th>First Name</th>
	        <th>Last Name</th>
	        <th>Positon</th>
	      </tr>";
  do {

    // Store first result set
    if ($result = $mysqli -> store_result()) {
      while ($row = $result -> fetch_row()) {
	echo "<tr>
		<th>$row[0]</th>
		<th>$row[1]</th>
		<th>$row[2]</th>
		<th>$row[3]</th>
	      </tr>";
      }
     $result -> free_result();
    }
    // if there are more result-sets, the print a divider
    if ($mysqli -> more_results()) {

    }
     //Prepare next result set
  } while ($mysqli -> next_result());
}

$mysqli -> close();
?>


<?php
$mysqli = new mysqli("localhost","pi","root","mydb");

if ($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}

$sql = "SELECT  * FROM Patient ORDER BY Patient.PatientID;";

// Execute multi query
if ($mysqli -> multi_query($sql)) {
	echo "<table>";
	echo "<tr>
		<th colspan='7'>Patient Information</th>
	      </tr>";
	echo "<tr>
	        <th>Patient No</th>
	        <th>First Name</th>
	        <th>Last Name</th>
	        <th>Phone NO.</th>
	        <th>Gender</th>
	        <th>Health Condition</th>
	        <th>Room No.</th>
	      </tr>";
  do {

    // Store first result set
    if ($result = $mysqli -> store_result()) {
      while ($row = $result -> fetch_row()) {
	echo "<tr>
		<th>$row[0]</th>
		<th>$row[1]</th>
		<th>$row[2]</th>
		<th>$row[3]</th>
		<th>$row[4]</th>
		<th>$row[5]</th>
		<th>$row[6]</th>
	      </tr>";
      }
     $result -> free_result();
    }
    // if there are more result-sets, the print a divider
    if ($mysqli -> more_results()) {

    }
     //Prepare next result set
  } while ($mysqli -> next_result());
}

$mysqli -> close();
?>

<br>

<?php
$mysqli = new mysqli("localhost","pi","root","mydb");

if ($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}

$sql = "SELECT * FROM ContactPerson ORDER BY Patient_PatientID;";

// Execute multi query
if ($mysqli -> multi_query($sql)) {
	echo "<table>";
	echo "<tr>
		<th colspan='6'>Contact Person Information</th>
	      </tr>";
	echo "<tr>
	        <th>Patient No</th>
	        <th>First Name</th>
	        <th>Last Name</th>
		<th>Relationship</th>
	        <th>Phone NO.</th>
	        <th>Gender</th>
	      </tr>";
  do {

    // Store first result set
    if ($result = $mysqli -> store_result()) {
      while ($row = $result -> fetch_row()) {
	echo "<tr>
		<th>$row[0]</th>
		<th>$row[1]</th>
		<th>$row[2]</th>
		<th>$row[3]</th>
		<th>$row[4]</th>
		<th>$row[5]</th>
	      </tr>";
      }
     $result -> free_result();
    }
    // if there are more result-sets, the print a divider
    if ($mysqli -> more_results()) {

    }
     //Prepare next result set
  } while ($mysqli -> next_result());
}

$mysqli -> close();
?>
<br>

<meta http-equiv = "refresh" content = "100">

<?php
http_response_code(404);
?>

</body>
</html>