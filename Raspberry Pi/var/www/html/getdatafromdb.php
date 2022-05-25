<?php
  $mysqli = new mysqli("localhost","pi","root","mydb");

  if ($mysqli -> connect_errno) {
    echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
    exit();
  }

  $sql = "SELECT * FROM Patient";

  if ($result = $mysqli -> query($sql)) {

  while ($row = $result -> fetch_row()) {
    printf("%s %s %s %s %s %s %s</br> \n", $row[0], $row[1], $row[2], $row[3], $row[4], $row[5], $row[6]);
    }

  $result -> free_result();
  }

?>