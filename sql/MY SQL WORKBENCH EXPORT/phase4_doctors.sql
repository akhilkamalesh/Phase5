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
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `Doctor_ID` int NOT NULL,
  `First_Name` varchar(100) DEFAULT NULL,
  `Last_Name` varchar(100) DEFAULT NULL,
  `Hospital_ID` int DEFAULT NULL,
  `Phone_Number` bigint DEFAULT NULL,
  `Email_ID` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Doctor_ID`),
  KEY `Hospital_ID` (`Hospital_ID`),
  CONSTRAINT `doctors_ibfk_1` FOREIGN KEY (`Hospital_ID`) REFERENCES `hospitals` (`Hospital_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (1001,'Rick','Sanchez',708,7146901159,'rsanchez708@gmail.com'),(1002,'Mort','Smith',183,5484781654,'m.smith@hotmail.com'),(1003,'Beth','Smith',265,3344473224,'beth.s@gmail.com'),(1004,'Susan','Wong',456,9116567920,'susan.wong@gmail.com'),(1005,'Xenon','Bloom',874,5583211154,'b.xenon@yahoo.com'),(1006,'Alice','Rousseau',184,7926801524,'Alice.Rousseau@yahoo.com'),(1007,'Vincent','Gomez',184,2077170430,'V.Gomez22@gmail.com'),(1008,'Cécile','Chevalier',184,4170167484,'Cécile.Chevalier@yahoo.com'),(1009,'Tiffany','Lewis',185,4912837589,'TLewis@gmail.com'),(1010,'Judith','Collins',185,3173766880,'Judith1.Collins@yahoo.com'),(1011,'Sarah','Wright',185,9667351158,'Sarah.Wright22@yahoo.com'),(1012,'Carole','Vincent',186,3018577919,'C.Vincent@gmail.com'),(1013,'Marion','Perez',186,8536018062,'Marion.Perez@yahoo.com'),(1014,'Sylvain','Hubert',186,5281641727,'S.Hubert353@gmail.com'),(1015,'Ashley','Green',187,9451214257,'A.Green@hotmail.com'),(1016,'Vincent','Davis',187,6210584253,'V.Davis@gmail.com'),(1017,'Nathan','Williams',187,6025397419,'Nathan.Williams@yahoo.com'),(1018,'Carole','Vincent',188,3018577919,'C.Vincent@gmail.com'),(1019,'Marion','Perez',188,8536018062,'Marion.Perez11@yahoo.com'),(1020,'Sylvain','Hubert',188,5281641727,'S.Hubert353@gmail.com');
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
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
