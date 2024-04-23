-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: phase4
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `medical_records`
--

DROP TABLE IF EXISTS `medical_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_records` (
  `MedRecID` int NOT NULL,
  `Patient_ID` int DEFAULT NULL,
  `COVID_Positive` tinyint(1) DEFAULT NULL,
  `Vaccine` varchar(100) DEFAULT NULL,
  `Positive_Date` date DEFAULT NULL,
  `vaccination_Date` date DEFAULT NULL,
  PRIMARY KEY (`MedRecID`),
  KEY `Patient_ID` (`Patient_ID`),
  CONSTRAINT `medical_records_ibfk_1` FOREIGN KEY (`Patient_ID`) REFERENCES `patients` (`Patient_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_records`
--

LOCK TABLES `medical_records` WRITE;
/*!40000 ALTER TABLE `medical_records` DISABLE KEYS */;
INSERT INTO `medical_records` VALUES (1234,2331,1,'1',NULL,NULL),(1235,2336,1,'0','2021-08-12','2021-07-06'),(1236,2337,1,'0','2021-09-24','2022-09-18'),(1237,2338,1,'0','2021-08-18','2021-05-25'),(1238,2339,1,'0','2022-08-01','2021-04-15'),(1239,2340,1,'0',NULL,'2021-09-15'),(1240,2341,1,'0','2021-09-23','2022-05-11'),(1241,2342,0,'0',NULL,NULL),(1242,2343,1,'0','2022-06-29',NULL),(1243,2344,1,'0',NULL,'2021-03-27'),(1244,2345,1,'0',NULL,'2021-05-23'),(1245,2346,1,'0',NULL,'2021-09-12'),(1246,2347,0,'0',NULL,NULL),(1247,2348,1,'0','2020-09-13','2021-07-04'),(1248,2349,1,'0','2022-05-05',NULL),(1249,2350,1,'0','2021-10-07','2021-09-08'),(1250,2351,1,'0','2020-10-20','2021-04-09'),(1534,2333,0,'1',NULL,NULL),(1777,2334,1,'0',NULL,NULL),(2345,2335,0,'0',NULL,NULL),(9022,2332,0,'1',NULL,NULL);
/*!40000 ALTER TABLE `medical_records` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-22 23:07:04
