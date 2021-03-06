CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Patient` (
  `PatientID` int(8) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `PhoneNo` int(8) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `HealthCondition` varchar(45) NOT NULL,
  `RoomNo` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `ContactPerson` (
  `Patient_PatientID` int(8) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Relationship` varchar(45) NOT NULL,
  `PhoneNo` int(8) NOT NULL,
  `Gender` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `combine` (
  `Patient_PatientID` int(8) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `PhoneNo` int(8) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `HealthCondition` varchar(45) NOT NULL,
  `RoomNo` int(8) NOT NULL,
  `ContactPerson_FirstName` varchar(45) NOT NULL,
  `ContactPerson_LastName` varchar(45) NOT NULL,
  `ContactPerson_Relationship` varchar(45) NOT NULL,
  `ContactPerson_PhoneNo` int(8) NOT NULL,
  `ContactPerson_Gender` varchar(45) NOT NULL,
  `LoRaNo` int(8) NOT NULL,
  `State` varchar(45) NOT NULL,
  `Position` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `LoRa` (
  `Patient_PatientID` int(8) NOT NULL,
  `LoRaNo` varchar(8) NOT NULL,
  `State` varchar(45) NOT NULL,
  `Position` varchar(45) NOT NULL,
  `RSSI` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
