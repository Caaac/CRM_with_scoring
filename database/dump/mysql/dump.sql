-- MySQL dump 10.13  Distrib 8.4.0, for macos14 (arm64)
--
-- Host: localhost    Database: crm-sistem
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add company',7,'add_company'),(26,'Can change company',7,'change_company'),(27,'Can delete company',7,'delete_company'),(28,'Can view company',7,'view_company'),(29,'Can add contact',8,'add_contact'),(30,'Can change contact',8,'change_contact'),(31,'Can delete contact',8,'delete_contact'),(32,'Can view contact',8,'view_contact'),(33,'Can add crm deal',9,'add_crmdeal'),(34,'Can change crm deal',9,'change_crmdeal'),(35,'Can delete crm deal',9,'delete_crmdeal'),(36,'Can view crm deal',9,'view_crmdeal'),(37,'Can add landing rate',10,'add_landingrate'),(38,'Can change landing rate',10,'change_landingrate'),(39,'Can delete landing rate',10,'delete_landingrate'),(40,'Can view landing rate',10,'view_landingrate'),(41,'Can add statement',11,'add_statement'),(42,'Can change statement',11,'change_statement'),(43,'Can delete statement',11,'delete_statement'),(44,'Can view statement',11,'view_statement'),(45,'Can add users',12,'add_users'),(46,'Can change users',12,'change_users'),(47,'Can delete users',12,'delete_users'),(48,'Can view users',12,'view_users'),(49,'Can add p user field',13,'add_puserfield'),(50,'Can change p user field',13,'change_puserfield'),(51,'Can delete p user field',13,'delete_puserfield'),(52,'Can view p user field',13,'view_puserfield'),(53,'Can add p user field enum',14,'add_puserfieldenum'),(54,'Can change p user field enum',14,'change_puserfieldenum'),(55,'Can delete p user field enum',14,'delete_puserfieldenum'),(56,'Can view p user field enum',14,'view_puserfieldenum'),(57,'Can add p user',15,'add_puser'),(58,'Can change p user',15,'change_puser'),(59,'Can delete p user',15,'delete_puser'),(60,'Can view p user',15,'view_puser'),(61,'Can add p option',16,'add_poption'),(62,'Can change p option',16,'change_poption'),(63,'Can delete p option',16,'delete_poption'),(64,'Can view p option',16,'view_poption'),(65,'Can add Token',17,'add_token'),(66,'Can change Token',17,'change_token'),(67,'Can delete Token',17,'delete_token'),(68,'Can view Token',17,'view_token'),(69,'Can add Token',18,'add_tokenproxy'),(70,'Can change Token',18,'change_tokenproxy'),(71,'Can delete Token',18,'delete_tokenproxy'),(72,'Can view Token',18,'view_tokenproxy');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$4niPF6dJx7a4XG9k3XrSpH$ur1y1G/qAMWuSm+HcBhueJAp03kro/6mVHMBFgwoqlg=','2025-02-22 11:50:04.338638',1,'admin','','','vedyaev03@mail.ru',1,1,'2025-02-22 11:49:53.216926');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('3dbfc90e98da5e0775fbf01fdf1321d778223e98','2025-02-22 12:07:17.516157',1);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'api','company'),(8,'api','contact'),(9,'api','crmdeal'),(10,'api','landingrate'),(11,'api','statement'),(12,'api','users'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(17,'authtoken','token'),(18,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(16,'main','poption'),(15,'main','puser'),(13,'main','puserfield'),(14,'main','puserfieldenum'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-21 18:16:38.781079'),(2,'auth','0001_initial','2025-02-21 18:16:38.874988'),(3,'admin','0001_initial','2025-02-21 18:16:38.904876'),(4,'admin','0002_logentry_remove_auto_add','2025-02-21 18:16:38.909641'),(5,'admin','0003_logentry_add_action_flag_choices','2025-02-21 18:16:38.913690'),(6,'api','0001_initial','2025-02-21 18:16:38.917363'),(7,'contenttypes','0002_remove_content_type_name','2025-02-21 18:16:38.941395'),(8,'auth','0002_alter_permission_name_max_length','2025-02-21 18:16:38.955256'),(9,'auth','0003_alter_user_email_max_length','2025-02-21 18:16:38.965129'),(10,'auth','0004_alter_user_username_opts','2025-02-21 18:16:38.969224'),(11,'auth','0005_alter_user_last_login_null','2025-02-21 18:16:38.983677'),(12,'auth','0006_require_contenttypes_0002','2025-02-21 18:16:38.984953'),(13,'auth','0007_alter_validators_add_error_messages','2025-02-21 18:16:38.988658'),(14,'auth','0008_alter_user_username_max_length','2025-02-21 18:16:39.005144'),(15,'auth','0009_alter_user_last_name_max_length','2025-02-21 18:16:39.020851'),(16,'auth','0010_alter_group_name_max_length','2025-02-21 18:16:39.031793'),(17,'auth','0011_update_proxy_permissions','2025-02-21 18:16:39.037451'),(18,'auth','0012_alter_user_first_name_max_length','2025-02-21 18:16:39.052804'),(19,'sessions','0001_initial','2025-02-21 18:16:39.060077'),(20,'authtoken','0001_initial','2025-02-22 12:07:00.403331'),(21,'authtoken','0002_auto_20160226_1747','2025-02-22 12:07:00.415349'),(22,'authtoken','0003_tokenproxy','2025-02-22 12:07:00.417225'),(23,'authtoken','0004_alter_tokenproxy_options','2025-02-22 12:07:00.420457');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ejrgj8pq495ow6nq5xo7emmv7xhuc974','.eJxVjEEOwiAQRe_C2hBKIQwu3XsGMswMUjU0Ke3KeHdt0oVu_3vvv1TCba1p67KkidVZDer0u2Wkh7Qd8B3bbdY0t3WZst4VfdCurzPL83K4fwcVe_3WaIQRXXBhiJ6koAfxowVgD8URI3Bg4-NohIgt2ALMhiJkMQWsVe8PAMM4og:1tlo1E:bpVIhA3UGaR4sHbNmPhHl__Cl1iV3yJD9miKBj5MKy4','2025-03-08 11:50:04.340162');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_crm_contact`
--

DROP TABLE IF EXISTS `p_crm_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_crm_contact` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `NAME` varchar(255) NOT NULL,
  `LAST_NAME` varchar(255) NOT NULL,
  `SECOND_NAME` varchar(255) NOT NULL,
  `CREATED_BY_ID` bigint NOT NULL,
  `BIRTHDATE` date DEFAULT (curdate()),
  `PHOTO` bigint DEFAULT NULL,
  `MODIFY_BY_ID` bigint DEFAULT NULL,
  `ASSIGNED_BY_ID` bigint DEFAULT NULL,
  `COMPANY_ID` bigint DEFAULT NULL,
  `SOURCE_ID` bigint DEFAULT NULL,
  `LEAD_ID` bigint DEFAULT NULL,
  `DATE_CREATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `DATE_MODIFY` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_crm_contact`
--

LOCK TABLES `p_crm_contact` WRITE;
/*!40000 ALTER TABLE `p_crm_contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `p_crm_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_crm_deal`
--

DROP TABLE IF EXISTS `p_crm_deal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_crm_deal` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `TITLE` varchar(255) NOT NULL,
  `CREATED_BY_ID` bigint NOT NULL,
  `MODIFY_BY_ID` bigint DEFAULT NULL,
  `ASSIGNED_BY_ID` bigint NOT NULL,
  `LEAD_ID` bigint DEFAULT NULL,
  `COMPANY_ID` bigint DEFAULT NULL,
  `CONTACT_ID` bigint DEFAULT NULL,
  `STAGE_ID` varchar(255) NOT NULL,
  `IS_NEW` tinyint(1) NOT NULL DEFAULT '1',
  `CLOSED` tinyint(1) NOT NULL DEFAULT '0',
  `TYPE_ID` varchar(255) NOT NULL,
  `OPPORTUNITY` varchar(255) DEFAULT NULL,
  `DATE_CREATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `DATE_MODIFY` datetime NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_crm_deal`
--

LOCK TABLES `p_crm_deal` WRITE;
/*!40000 ALTER TABLE `p_crm_deal` DISABLE KEYS */;
INSERT INTO `p_crm_deal` VALUES (1,'Сделка 1',1,NULL,2,NULL,NULL,NULL,'NEW',1,0,'Тип 1','10000','2025-02-26 06:47:09','2025-02-26 06:47:09'),(2,'Сделка 2',1,NULL,2,NULL,NULL,NULL,'С_2736',1,0,'Тип 1','15000','2025-02-26 06:47:09','2025-02-26 06:47:09'),(3,'Сделка 3',2,NULL,3,NULL,NULL,NULL,'С_2736',0,1,'Тип 2','20000','2025-02-26 06:47:09','2025-02-26 06:47:09'),(4,'Сделка 4',2,NULL,3,NULL,NULL,NULL,'LOSE',1,0,'Тип 2','25000','2025-02-26 06:47:09','2025-02-26 06:47:09'),(5,'Сделка 5',3,NULL,1,NULL,NULL,NULL,'С_8945',1,0,'Тип 1','30000','2025-02-26 06:47:09','2025-02-26 06:47:09'),(6,'Сделка 6',3,NULL,1,NULL,NULL,NULL,'APOLOGY',0,1,'Тип 1','35000','2025-02-26 06:47:09','2025-02-26 06:47:09'),(7,'Сделка 7',1,NULL,2,NULL,NULL,NULL,'NEW',1,0,'Тип 3','40000','2025-02-26 06:47:09','2025-02-26 06:47:09'),(8,'Сделка 8',2,NULL,3,NULL,NULL,NULL,'С_2736',1,0,'Тип 2','45000','2025-02-26 06:47:09','2025-02-26 06:47:09'),(9,'Сделка 9',2,NULL,3,NULL,NULL,NULL,'WON',0,1,'Тип 3','50000','2025-02-26 06:47:09','2025-02-26 06:47:09'),(10,'Сделка 10',3,NULL,1,NULL,NULL,NULL,'WON',1,0,'Тип 1','55000','2025-02-26 06:47:09','2025-02-26 06:47:09');
/*!40000 ALTER TABLE `p_crm_deal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_crm_field_multi`
--

DROP TABLE IF EXISTS `p_crm_field_multi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_crm_field_multi` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `ENTITY` varchar(25) NOT NULL,
  `ELEMENT_ID` bigint NOT NULL,
  `TYPE_ID` varchar(20) NOT NULL,
  `VALUE_TYPE` varchar(30) NOT NULL,
  `VALUE` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_crm_field_multi`
--

LOCK TABLES `p_crm_field_multi` WRITE;
/*!40000 ALTER TABLE `p_crm_field_multi` DISABLE KEYS */;
/*!40000 ALTER TABLE `p_crm_field_multi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_crm_status`
--

DROP TABLE IF EXISTS `p_crm_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_crm_status` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `ENTITY_ID` varchar(255) NOT NULL,
  `STATUS_ID` varchar(255) NOT NULL,
  `TITLE` varchar(255) NOT NULL,
  `COLOR` varchar(255) NOT NULL,
  `SYSTEM_STATUS` tinyint(1) NOT NULL,
  `SEMANTICS` char(1) DEFAULT NULL,
  `SORT` bigint NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_crm_status`
--

LOCK TABLES `p_crm_status` WRITE;
/*!40000 ALTER TABLE `p_crm_status` DISABLE KEYS */;
INSERT INTO `p_crm_status` VALUES (1,'DEAL_STAGE','NEW','Новая сделка','#FF5752',1,NULL,100),(2,'DEAL_STAGE','С_2736','Определение требований','#FF5752',0,'P',200),(3,'DEAL_STAGE','С_8945','Подготовка документов','#FF5752',0,'P',300),(4,'DEAL_STAGE','APOLOGY','Анализ причины провала','#FF5752',1,'F',0),(5,'DEAL_STAGE','LOSE','Сделка провальна','#FF5752',1,'F',0),(6,'DEAL_STAGE','WON','Сделка успешна','#7BD500',1,'S',0);
/*!40000 ALTER TABLE `p_crm_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_option`
--

DROP TABLE IF EXISTS `p_option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_option` (
  `MODULE` varchar(50) NOT NULL,
  `NAME` varchar(100) NOT NULL,
  `VALUE` mediumtext,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`MODULE`),
  UNIQUE KEY `NAME` (`NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_option`
--

LOCK TABLES `p_option` WRITE;
/*!40000 ALTER TABLE `p_option` DISABLE KEYS */;
/*!40000 ALTER TABLE `p_option` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_user`
--

DROP TABLE IF EXISTS `p_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_user` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `LOGIN` bigint NOT NULL,
  `EMAIL` bigint NOT NULL,
  `PASSWORD` bigint NOT NULL,
  `DATE_REGISTER` bigint NOT NULL,
  `LAST_LOGIN` bigint NOT NULL,
  `NAME` bigint NOT NULL,
  `LAST_NAME` bigint NOT NULL,
  `PERSONAL_GENDER` char(1) NOT NULL,
  `PERSONAL_PHOTO` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_user`
--

LOCK TABLES `p_user` WRITE;
/*!40000 ALTER TABLE `p_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `p_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_user_field`
--

DROP TABLE IF EXISTS `p_user_field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_user_field` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `TITLE` varchar(255) NOT NULL,
  `FIELD_NAME` varchar(70) NOT NULL,
  `USER_TYPE_ID` varchar(70) NOT NULL,
  `XML_ID` varchar(255) DEFAULT NULL,
  `SORT` int DEFAULT NULL,
  `MULTIPLE` tinyint(1) NOT NULL DEFAULT '0',
  `MANDATORY` tinyint(1) NOT NULL DEFAULT '0',
  `SHOW_FILTER` tinyint(1) NOT NULL DEFAULT '0',
  `SHOW_IN_LIST` tinyint(1) NOT NULL DEFAULT '1',
  `EDIT_IN_LIST` tinyint(1) NOT NULL DEFAULT '1',
  `IS_SEARCHABLE` tinyint(1) NOT NULL DEFAULT '0',
  `ENTITY_ID` varchar(70) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_user_field`
--

LOCK TABLES `p_user_field` WRITE;
/*!40000 ALTER TABLE `p_user_field` DISABLE KEYS */;
INSERT INTO `p_user_field` VALUES (1,'Годовой доход','UF_CRM_3478539932943','string',NULL,200,0,1,0,1,1,0,'DEAL'),(16,'Тест строка','UF_CRM_9295170076','string',NULL,100,0,0,0,0,0,0,'DEAL'),(18,'мэйби','UF_CRM_322946257195','boolean',NULL,100,0,0,0,0,0,0,'DEAL');
/*!40000 ALTER TABLE `p_user_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_user_field_enum`
--

DROP TABLE IF EXISTS `p_user_field_enum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_user_field_enum` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `USER_FIELD_ID` bigint NOT NULL,
  `VALUE` varchar(255) DEFAULT NULL,
  `SORT` int DEFAULT NULL,
  `XML_ID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `USER_FIELD_ID` (`USER_FIELD_ID`),
  CONSTRAINT `p_user_field_enum_ibfk_1` FOREIGN KEY (`USER_FIELD_ID`) REFERENCES `p_user_field` (`ID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_user_field_enum`
--

LOCK TABLES `p_user_field_enum` WRITE;
/*!40000 ALTER TABLE `p_user_field_enum` DISABLE KEYS */;
/*!40000 ALTER TABLE `p_user_field_enum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_utm_crm_contact`
--

DROP TABLE IF EXISTS `p_utm_crm_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_utm_crm_contact` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `CONTACT_ID` bigint NOT NULL,
  `FIELD_ID` bigint NOT NULL,
  `VALUE` varchar(255) DEFAULT NULL,
  `VALUE_INT` bigint DEFAULT NULL,
  `VALUE_DOUBLE` double DEFAULT NULL,
  `VALUE_DATETIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `CONTACT_ID` (`CONTACT_ID`),
  KEY `FIELD_ID` (`FIELD_ID`),
  CONSTRAINT `p_utm_crm_contact_ibfk_1` FOREIGN KEY (`CONTACT_ID`) REFERENCES `p_crm_contact` (`ID`) ON DELETE CASCADE,
  CONSTRAINT `p_utm_crm_contact_ibfk_2` FOREIGN KEY (`FIELD_ID`) REFERENCES `p_user_field` (`ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_utm_crm_contact`
--

LOCK TABLES `p_utm_crm_contact` WRITE;
/*!40000 ALTER TABLE `p_utm_crm_contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `p_utm_crm_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_utm_crm_deal`
--

DROP TABLE IF EXISTS `p_utm_crm_deal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_utm_crm_deal` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `DEAL_ID` bigint NOT NULL,
  `FIELD_ID` bigint NOT NULL,
  `VALUE` varchar(255) DEFAULT NULL,
  `VALUE_INT` bigint DEFAULT NULL,
  `VALUE_DOUBLE` double DEFAULT NULL,
  `VALUE_DATETIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `DEAL_ID` (`DEAL_ID`),
  KEY `FIELD_ID` (`FIELD_ID`),
  CONSTRAINT `p_utm_crm_deal_ibfk_1` FOREIGN KEY (`DEAL_ID`) REFERENCES `p_crm_deal` (`ID`) ON DELETE CASCADE,
  CONSTRAINT `p_utm_crm_deal_ibfk_2` FOREIGN KEY (`FIELD_ID`) REFERENCES `p_user_field` (`ID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_utm_crm_deal`
--

LOCK TABLES `p_utm_crm_deal` WRITE;
/*!40000 ALTER TABLE `p_utm_crm_deal` DISABLE KEYS */;
INSERT INTO `p_utm_crm_deal` VALUES (1,2,1,'ASHAB BRATKA',NULL,NULL,NULL),(2,3,1,'23',NULL,NULL,NULL),(3,5,1,'23',NULL,NULL,NULL),(6,1,1,'342423',NULL,NULL,NULL),(7,1,16,'уцау',NULL,NULL,NULL),(8,1,18,'1',NULL,NULL,NULL),(9,3,16,NULL,NULL,NULL,NULL),(10,3,18,NULL,NULL,NULL,NULL),(11,2,16,NULL,NULL,NULL,NULL),(12,2,18,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `p_utm_crm_deal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-15 22:40:34
