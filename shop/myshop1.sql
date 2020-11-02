-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: myshop
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `addproduct`
--

DROP TABLE IF EXISTS `addproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addproduct` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `discount` int DEFAULT NULL,
  `stock` int NOT NULL,
  `colors` text NOT NULL,
  `desc` text NOT NULL,
  `pub_date` datetime NOT NULL,
  `category_id` int NOT NULL,
  `brand_id` int NOT NULL,
  `image_1` varchar(150) NOT NULL,
  `image_2` varchar(150) NOT NULL,
  `image_3` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `brand_id` (`brand_id`),
  CONSTRAINT `addproduct_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `addproduct_ibfk_2` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addproduct`
--

LOCK TABLES `addproduct` WRITE;
/*!40000 ALTER TABLE `addproduct` DISABLE KEYS */;
INSERT INTO `addproduct` VALUES (1,'iPhone 12 | 12 mini',699.00,0,2,'Xanh, Trắng','iPhone 12 mini 64GB chính hãng (VN/A) là phiên bản nhỏ nhất với thiết kế nhỏ gọn, sang trọng. Máy sở hữu màn hình 5,4 inch, công nghệ màn hình đem đến hình ảnh chi tiết, sắc nét. Máy cũng được trang bị cấu hình cao cấp với chip A14 Bionic, bộ đôi camera 12MP với nhiều chế độ chụp ảnh đẹp.','2020-10-22 10:37:57',3,1,'5d2ebf191ac43412b63b.jpg','2364285b06beeb1dca1d.jpg','bd5e2b7b0d5866669477.jpg'),(2,'IPhone 12',799.00,0,2,'Đỏ, Trắng, Đen','iPhone 12 64GB chính hãng (VN/A) với thiết kế vuông vắn, cá tính phù hợp với sự lựa chọn của nhiều người dùng. Máy được trang bị hiệu năng mạnh mẽ với chip A14 Bionic. iPhone 12 phù hợp với người dùng thích dùng smartphone thương hiệu lớn, hiệu năng mạnh và đa nhiệm tốt.','2020-10-22 10:40:39',3,1,'e89d64c8cf646601f7b3.jpg','ecc2e689df9f3dfa6a60.jpg','b952bf405b04fd5a1f9d.jpg'),(3,'IPhone 12 Pro Max',1099.00,0,2,'Đỏ, Trắng, Đen','Cấu hình mạnh nhất thế giới smartphone\r\nBộ vi xử lý Apple A13 Bionic trước đó trên iPhone 11 Series vốn đã vô cùng mạnh mẽ, hiệu năng lẫn khả năng chụp ảnh vẫn thuộc hàng “bá đạo” nhất hiện nay. Tuy nhiên, vi xử lý mới Apple A14 Bionic sẽ đưa iPhone 12 Pro Max – 128GB Chính hãng lên một tầm cao mới.\r\n\r\nTrong năm 2020, Apple sẽ giới thiệu một dòng chip hoàn toàn mới dựa trên tiến trình 5nm. Những thông tin rò rỉ gần đây cho thấy con chip mới sẽ nâng sức mạnh của iPhone 12 Pro Max – 128GB Chính hãng lên ngang tầm Macbook Air. Với thế hệ flagship mới, Apple sẽ phải cải tiến tốt hơn để phát huy tối đa hiệu năng của máy.','2020-10-22 10:43:25',3,1,'2ddc17309472a8a649cd.jpg','8785c37de069faaa80db.jpg','01e53cfb8fd107be67f9.jpg'),(4,'IPhone 12 Pro',999.00,0,2,'Đỏ, Trắng, Đen','iPhone 12 Pro 128GB chính hãng (VN/A) là smartphone sở hữu thiết kế sang trọng cá tính. Máy được trang bị màn hình OLED cao cấp. iPhone 12 pro đem đến trải nghiệm mạnh mẽ với con chip A14 Bionic, phiên bản bộ nhớ 128GB giúp máy chạy đa nhiệm tốt. Dung lượng pin trên máy cũng được nâng cấp hơn nhiều.','2020-10-22 10:45:02',3,1,'2fd21da0e2e886f16f58.jpg','7e72c75c6cd322a24152.jpg','c4953dead5cfc6fd0560.jpg'),(5,'Samsung Galaxy Note 20 Ultra',1000.00,20,2,'Trắng, Đen','Samsung Note 20 Ultra: Thiết kế sang trọng và nhiều công nghệ cực tốt\r\nSamsung là gã khổng lồ công nghệ cực kỳ nổi tiếng đến từ đất nước Hàn Quốc, mỗi chiếc điện thoại của hãng đều mang thiết kế hiện đại, sang trọng đi kèm với đa dạng công nghệ cực kỳ nổi bật. Note 20 Ultra là một trong những chiếc smartphone nổi tiếng và đang được nhiều người quan tâm, đón nhận. Samsung hứa hẹn sẽ chiều lòng khách hàng với thiết kế lộng lẫy, cùng với vô vàng công nghệ, chip xử lý mới mẻ, thật hiện đại. Ngoài ra, bạn cũng có thể tham khảo thêm Note 20 Ultra 5G.','2020-10-22 10:49:01',3,2,'11631fbe13eec987a33c.png','c49c757271fedb62b710.jpg','7b2a8293f5714cad5834.jpg'),(6,'Samsung Galaxy Note 10+ (Plus)',699.00,0,2,'Trắng, Đen','Samsung Note 10 Plus – Màn hình lớn cho trải nghiệm tuyệt đỉnh, S-Pen tiện dụng\r\nLà phiên bản nâng cấp đáng giá ra đời cùng thời điểm với Samsung Galaxy Note 10, Samsung Galaxy Note 10 Plus là sự lựa chọn tuyệt vời cho người dùng đam mê công nghệ có nhu cầu sở hữu một chiếc điện thoại hoàn hảo về mọi mặt. Với Note 10 Plus, Samsung đã thật sự mang đến một chiếc điện thoại có sức mạnh vượt trội, đáp ứng toàn diện các nhu cầu về làm việc và giải trí của người dùng. Ngoài ra, bạn có thể tham khảo thêm Galaxy Note 20 sắp được ra mắt.','2020-10-22 10:50:43',3,2,'3147109bc3d76150d0d5.jpg','80cbf109ef258b960fb6.jpg','01627dafb8c4dcf47563.jpg'),(7,'Xiaomi Mi 10T Pro',499.00,0,22,'Trắng, Đen','Nếu bạn là một Mifan hay là một người dùng yêu công nghệ thì chắc chắn bạn sẽ không thể bỏ qua Xiaomi Mi 10T Pro. Với nhiều tính năng đặc biệt và công nghệ chụp ảnh cao cấp, Xiaomi đang dần đánh bóng tên tuổi mình hơn với chiếc smartphone này.','2020-10-22 10:53:00',3,3,'2797af38bfed9f0a17a8.jpg','75c2d92ae2eb4a2f954f.jpg','f48b7d8d0167475880d4.jpg'),(8,'Xiaomi Redmi Note 9 Pro',299.00,10,22,'Đỏ, Trắng, Đen','Điện thoại Xiaomi Redmi Note 9 Pro – Smartphone màn hình rộng, viên pin lớn\r\nCùng với Xiaomi Redmi Note 9s, Xiaomi Redmi Note 9 Pro là phiên bản nâng cấp của điện thoại Xiaomi Redmi Note 9 với sự lựa chọn hoàn hảo dành cho những ai đang mong muốn sở hữu một chiếc điện thoại tầm trung có dung lượng pin cao cùng thiết kế sang trọng và khả năng chụp ảnh tốt. Ngày nay, việc sở hữu một chiếc smartphone là điều thiết yếu với mỗi người, giúp người dùng có thể giải quyết cả những công việc mà trước đây chỉ có thể thực hiện trên laptop, mở ra một trai nghiệm thú vị, hiện đại và tiện lợi hơn rất nhiều. ','2020-10-23 02:36:41',3,3,'10fa244542f3352f0db5.jpg','0ee99c5fd12985aaac0b.jpg','889e90d0c9cb21be8374.jpg'),(9,'Vsmart Active 3 6GB Ram',139.00,5,22,'Đỏ, Vàng, Đen','Vsmart Active 3 - Điện thoại giá rẻ thương hiệu Việt\r\nVsmart thuộc tập đoàn Vingroup là dòng điện thoại thương hiệu Việt đang ngày càng được đông đảo người dân quan tâm. Mới đây, hãng tiếp tục giới thiệu thêm nhiều mẫu smartphone mới như Vsmart  Live 3, Vsmart  Star 3... và Vsmart Active 3. Trong đó, Active 3 mang trong mình nhiều tính năng và cấu hình cao với mức giá vô cùng tốt.','2020-10-23 02:41:10',3,6,'f90e5f2b6dfbb39219da.png','4fe3b496d005b7e0b6a7.png','e7d1327d0c9b98d3389b.png'),(10,'Vivo V19',299.00,0,22,'Trắng, Đen','Điện thoại Vivo V19 – Thiết kế nổi bật, 4 camera chụp đêm cực đỉnh\r\nVivo V19 là smartphone thuộc phân khúc tầm trung được ra mắt vào năm 2020 của thương hiệu Vivo và nhận được sự yêu thích của nhiều người dùng. Điện thoại Vivo này với thiết kế nổi bật và phù hợp với xu hướng hiện đại với màu sắc thời thượng, cấu hình vượt trội cùng với hệ thống camera với chế độ chụp ảnh ban đêm siêu ấn tượng chắc chắn sẽ mang đến cho người dùng nhiều trải nghiệm thú vị.','2020-10-23 02:44:00',3,7,'d608e18bd634ba46c45b.png','3f2b1795a10a027444ed.png','f0a9e0a548cb7aafa919.png');
/*!40000 ALTER TABLE `addproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (1,'IPhone'),(5,'Sạc dự phòng'),(2,'Samsung'),(7,'Vivo'),(6,'Vsmart'),(3,'Xiaomi');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (2,'Laptop'),(4,'Phụ kiện'),(3,'SmartPhone');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(180) NOT NULL,
  `profile` varchar(180) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'lemanh1011','lemanh1011','lexuanmanh101199@gmail.com','$2b$12$GQwX6Yolk2iuhczDbuDn3.upgdDtfO7LKH2qlPw2nuWw1ZeXI.See','profile.jpg'),(2,'Le Manh','Manh','lexuanmanh10111199@gmail.com','$2b$12$Su2HINmJMjyDlMb6QLYtwuF3C0F/SjBy5gttR6i1g6ilb9LhjMgK6','profile.jpg'),(3,'lemanh1011','lemanh1111','lexuanmanhs101199@gmail.com','$2b$12$az/Smi4dE9LHmFl0y6RRr.q9h59eHRa/Nk6qa/uNn7e.Ml4URmERO','profile.jpg');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-23 22:21:38
