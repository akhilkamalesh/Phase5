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
-- Table structure for table `hospitals`
--

DROP TABLE IF EXISTS `hospitals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospitals` (
  `Hospital_ID` int NOT NULL,
  `Country_ID` int DEFAULT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `GeoLocation` varchar(255) DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  PRIMARY KEY (`Hospital_ID`),
  KEY `Country_ID` (`Country_ID`),
  CONSTRAINT `hospitals_ibfk_1` FOREIGN KEY (`Country_ID`) REFERENCES `country` (`Country_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospitals`
--

LOCK TABLES `hospitals` WRITE;
/*!40000 ALTER TABLE `hospitals` DISABLE KEYS */;
INSERT INTO `hospitals` VALUES (100,2001,'Indraprastha Apollo Hospital','1233',1150),(101,2002,'Lahore General Hospital','7643',805),(102,2003,'JR Tokyo General Hospital','1299',1205),(103,2004,'Hospital Costa del Sol','4888',745),(104,2005,'Toronto General Hospital','2342',890),(105,2006,'Santa Maria Nuova Hospital','3894',1920),(106,2007,'Zuid-Afrikaans Hospital','7644',825),(107,2008,'Clinique Assalam','2938',365),(108,2009,'Kolan International Hospital','1974',445),(109,2010,'Beijing Jishuitan Hospital','1297',800),(110,2011,'Hôtel Dieu Hospital','1288',1050),(111,2012,'University of Chile Clinical Hospital','2364',885),(112,2013,'Colombia National University Hospital','2341',765),(113,2014,'Austin Hospital','1293',845),(114,2015,'Waitakere Hospital','8462',650),(183,3425,'Alexander Hospital','8882',865),(184,2011,'Hôpital Lariboisière','1233',1000),(185,1039,'Mercy Hospital','6900',950),(186,2011,'Centre Hospitalier Universitaire de Nantes','2746',700),(187,1039,'Massachusetts General Hospital','5380',1600),(188,2011,'Centre Hospitalier Universitaire de Lyon','2746',700),(265,4324,'Hospital Santa Lúcia Sul','1561',1265),(456,8493,'Amanuel Mental Hospital','7315',945),(708,1039,'Massachusetts General Hospital','1010',1350),(874,3425,'Centro Médico Nacional Siglo XXI','3117',850);
/*!40000 ALTER TABLE `hospitals` ENABLE KEYS */;
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
