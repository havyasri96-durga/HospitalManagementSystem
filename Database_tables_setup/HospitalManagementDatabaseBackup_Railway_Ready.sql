-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: hospitaldb
-- ------------------------------------------------------
-- Server version	9.7.0

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;


--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `patient_name` varchar(100) DEFAULT NULL,
  `doctor_name` varchar(100) DEFAULT NULL,
  `appointment_date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

INSERT INTO `appointments` VALUES (1,'Ravi','karthik','2026-06-26','Approved'),(2,'Lily','David','2026-06-29','Approved'),(3,'Ravi','David','2026-06-27','Approved'),(4,'merry david','karthik','2026-06-25','completed'),(5,'Siva','kiran','2026-06-25','Pending');

--
-- Table structure for table `bills`
--

DROP TABLE IF EXISTS `bills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bills` (
  `bill_id` int NOT NULL AUTO_INCREMENT,
  `patient_name` varchar(100) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`bill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills`
--

INSERT INTO `bills` VALUES (1,'Ravi',5000.00,'paid'),(2,'Lily',1500.00,'paid'),(3,'Ravi',4500.00,'paid'),(4,'merry david',2000.00,'paid'),(5,'Siva',1500.00,'paid');

--
-- Table structure for table `disease_medicines`
--

DROP TABLE IF EXISTS `disease_medicines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disease_medicines` (
  `id` int NOT NULL AUTO_INCREMENT,
  `disease` varchar(100) DEFAULT NULL,
  `medicine_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disease_medicines`
--

INSERT INTO `disease_medicines` VALUES (1,'Fever','Paracetamol'),(2,'Fever','Dolo 650'),(3,'Fever','Crocin'),(4,'Cold','Cetirizine'),(5,'Cold','Sinarest'),(6,'Cold','Levocetirizine'),(7,'Diabetes','Metformin'),(8,'Diabetes','Insulin'),(9,'Headache','Saridon'),(10,'Headache','Paracetamol'),(11,'Cough','Benadryl'),(12,'Cough','Ascoril'),(13,'fever','Paracetamol'),(14,'cold','Cetirizine'),(15,'cough','Benadryl Syrup'),(16,'headache','Ibuprofen'),(17,'acidity','Pantoprazole'),(18,'diabetes','Metformin'),(19,'hypertension','Amlodipine'),(20,'asthma','Salbutamol Inhaler'),(21,'allergy','Levocetirizine'),(22,'migraine','Sumatriptan'),(23,'gastritis','Omeprazole'),(24,'vomiting','Ondansetron'),(25,'diarrhea','ORS + Loperamide'),(26,'constipation','Lactulose Syrup'),(27,'anemia','Ferrous Sulphate'),(28,'arthritis','Diclofenac'),(29,'back pain','Aceclofenac'),(30,'toothache','Ibuprofen'),(31,'ear infection','Amoxicillin'),(32,'skin infection','Mupirocin Ointment'),(33,'fungal infection','Clotrimazole'),(34,'urinary infection','Nitrofurantoin'),(35,'bronchitis','Azithromycin'),(36,'pneumonia','Amoxicillin-Clavulanate'),(37,'thyroid','Levothyroxine'),(38,'vitamin d deficiency','Vitamin D3'),(39,'b12 deficiency','Methylcobalamin'),(40,'insomnia','Melatonin'),(41,'dehydration','ORS'),(42,'heartburn','Pantoprazole');

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `doctor_id` int NOT NULL AUTO_INCREMENT,
  `doctor_name` varchar(100) DEFAULT NULL,
  `specialization` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `experience` int DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` VALUES (2,'David','MBBS ','1234567890',15),(3,'kiran','MD','5346574652',20),(4,'Bharath ','surgeon','5462465748',12);

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `feedback_id` int NOT NULL AUTO_INCREMENT,
  `patient_name` varchar(100) DEFAULT NULL,
  `comments` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` VALUES (1,'Ravi','good treatment'),(2,'Lily','good treatment');

--
-- Table structure for table `medicines`
--

DROP TABLE IF EXISTS `medicines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicines` (
  `medicine_id` int NOT NULL AUTO_INCREMENT,
  `medicine_name` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`medicine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicines`
--

INSERT INTO `medicines` VALUES (2,'Sinarest',25.00,6),(3,'Solvin Cold',30.00,6),(4,'Insulin',150.00,10),(5,'Saridon',45.00,20);

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `patient_name` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `disease` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` VALUES (3,'Lily',20,'Female','6749034567','Cough and Cold'),(4,'keerthi',24,'Female','6576546345','headace'),(5,'Ravi',24,'Male','6867385764','Cough and Cold'),(6,'merry david',16,'Female','3456328453','cough'),(7,'Siva',12,'Male','5426542847','Fever');

--
-- Table structure for table `prescriptions`
--

DROP TABLE IF EXISTS `prescriptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prescriptions` (
  `prescription_id` int NOT NULL AUTO_INCREMENT,
  `patient_name` varchar(100) DEFAULT NULL,
  `doctor_name` varchar(100) DEFAULT NULL,
  `diagnosis` varchar(200) DEFAULT NULL,
  `medicines` varchar(500) DEFAULT NULL,
  `prescription_date` date DEFAULT NULL,
  `disease` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`prescription_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prescriptions`
--

INSERT INTO `prescriptions` VALUES (1,'Lily','David','Viral Fever','Paracetamol','2026-06-26',NULL),(2,'Lily','David','Viral Fever','Paracetamol','2026-06-26',NULL),(3,'Ravi','David','cough','Benadryl Syrup','2026-06-25',NULL),(4,'Ravi','David','Headache','Saridon','2026-06-25',NULL),(5,'Ravi','David',NULL,'Metformin','2026-06-25','Diabetes'),(6,'Lily','karthik',NULL,'Amoxicillin','2026-06-25','Ear Infection'),(7,'Ravi','David',NULL,'Ondansetron','2026-06-25','Vomiting'),(8,'Ravi','David',NULL,'Ondansetron','2026-06-25','Vomiting'),(9,'Siva','karthik',NULL,'Ondansetron','2026-06-25','Vomiting');

--
-- Table structure for table `reports`
--

DROP TABLE IF EXISTS `reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `patient_name` varchar(100) DEFAULT NULL,
  `diagnosis` varchar(200) DEFAULT NULL,
  `prescription` varchar(200) DEFAULT NULL,
  `report_date` date DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports`
--

INSERT INTO `reports` VALUES (1,'Ravi','Viral Fever','Paracetamol','2026-07-01'),(2,'Lily','Cough and Cold','Solvin Cold and Sinarest','2026-06-29');

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

INSERT INTO `users` VALUES (2,'admin','admin123','Admin'),(3,'doctor1','doctor123','Doctor'),(4,'reception','recep123','Receptionist'),(5,'admin','admin123','Admin'),(6,'vernon','vernon13','Doctor'),(7,'reception','recep123','Receptionist');
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-26 12:17:19
