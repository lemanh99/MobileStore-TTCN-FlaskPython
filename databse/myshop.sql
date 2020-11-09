-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: myshop4
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addproduct`
--

LOCK TABLES `addproduct` WRITE;
/*!40000 ALTER TABLE `addproduct` DISABLE KEYS */;
INSERT INTO `addproduct` VALUES (2,'Samsung Galaxy Note 20 Ultra',945.00,10,3,'Đỏ, Trắng, Đen','Samsung Note 20 Ultra: Thiết kế sang trọng và nhiều công nghệ cực tốt\r\nSamsung là gã khổng lồ công nghệ cực kỳ nổi tiếng đến từ đất nước Hàn Quốc, mỗi chiếc điện thoại của hãng đều mang thiết kế hiện đại, sang trọng đi kèm với đa dạng công nghệ cực kỳ nổi bật. Note 20 Ultra là một trong những chiếc smartphone nổi tiếng và đang được nhiều người quan tâm, đón nhận. Samsung hứa hẹn sẽ chiều lòng khách hàng với thiết kế lộng lẫy, cùng với vô vàng công nghệ, chip xử lý mới mẻ, thật hiện đại. Ngoài ra, bạn cũng có thể tham khảo thêm Note 20 Ultra 5G.','2020-11-09 05:13:09',4,6,'984669c3387528916718.jpg','52fad50c0db8f54402ff.jpg','a83d0464b0a6575faab2.jpg'),(3,'Samsung Galaxy A71',355.00,10,22,'Đỏ, Trắng, Đen','Samsung A71 – Smartphone tầm trung của Samsung\r\nSamsung Galaxy A71 sẽ là điện thoại giá cả phải chăng của Samsung với mục đích tiếp cận đối tượng rộng hơn. Samsung A71 là sản phẩm thuộc series Samsung Galaxy A với màn hình đục lỗ, cấu hình mạnh mẽ, cụm bốn camera sau chất lượng cao và cùng nhiều công nghệ thời thượng.\r\nSau Galaxy A51 và A71, rất có thể Galaxy A01 sẽ là sản phẩm tiếp theo thuộc dòng Galaxy A 2020 được Samsung trình làng trong thời gian sắp tới.','2020-11-09 05:14:53',4,6,'636bb3e1614d1c8d19bb.jpg','05f32f573b7ada244553.jpg','c839d80c476db2fce9c2.jpg'),(4,'Samsung Galaxy Note 20',778.00,25,22,'Đỏ, Trắng, Đen','Samsung Note 20 – Màn hình 2K tuyệt hảo và bút S-Pen cho trải nghiệm tiện ích\r\nSau hàng loạt thành công từ những thế hệ Galaxy Note trước, Samsung lại tiếp tục khiến cộng đồng công nghệ phải phát cuồng với siêu phẩm tiếp theo của mình – Samsung Galaxy Note 20, ra mắt cùng với Note 20 Ultra và phiên bản 5G. Siêu phẩm này hứa hẹn sẽ mang đến cho người dùng những trải nghiệm vượt trội hơn, mạnh mẽ hơn với một thiết kế tinh tế, hoàn hảo.','2020-11-09 05:16:09',4,6,'665920a44777ee75452a.jpg','f9ff942d115c5d4f872c.jpg','d0ef8b225c1ac80920ff.jpg'),(5,'Samsung Galaxy Note 10 Lite',425.00,0,22,'Red, Black, Blue','Samsung Note 10 Lite - Phiên bản nhỏ gọn, đa năng của siêu phẩm Note 10\r\nGalaxy Note 10 Lite (ra mắt cùng với Galaxy S10 Lite) là phiên bản nhỏ gọn hơn, giá rẻ hơn bộ đôi siêu phẩm Note 10 / Note 10+ nhưng vẫn giữ nguyên những tinh hoa của người tiền nhiệm nhưng với mức giá hấp dẫn hơn. Mặc dù điện thoại Samsung Note 20 sắp ra mắt nhưng đây vẫn là sự lựa chọn hợp lý ở thời điểm hiện tại. \r\n\r\nSamsung Note 10 Lite có cấu hình như thế nào\r\nTrong thuật ngữ công nghệ, chữ \"lite\" đại diện cho \"light\", nghĩa là phiên bản nhẹ hơn, được thu nhỏ để vận hành ổn định mà không bị giật. Về cơ bản, bất kỳ thiết bị nào có chữ \"Lite\" trong tên sản phẩm đều là phiên bản nhỏ hơn, vận hành nhẹ hơn so với thiết bị gốc được ra mắt trước đó','2020-11-09 05:17:45',4,6,'925185710782e88e0760.jpg','895d025ab3aa230efe6b.jpg','8e8f850ae4b7bdf6c4c4.jpg'),(6,'iPhone 11',769.00,10,22,'Red, Black, Blue','iPhone 11 chính hãng VN/A – Chiếc điện thoại nhiều màu sắc, camera nâng cấp\r\niPhone 11 là model có nhiều màu sắc nhất và có giá rẻ nhất trong bộ 3 iPhone 11 series được Apple ra mắt trong năm 2019. Bên cạnh đó, cấu hình iPhone 11 cũng được nâng cấp đặc biệt về cụm camera sau và Face ID, viên pin dung lượng lớn hơn.\r\n\r\nĐa dạng sự lựa chọn với 6 phiên bản màu sắc\r\nĐiểm nổi bật của iPhone 11 2019 đó là bên cạnh hai phiên bản đen và trắng quen thuộc thì máy còn có thêm bốn phiên bản khác đó là tím, vàng, xanh lá, đỏ. Với tất cả các phiên bản, bao gồm cả điện thoại iPhone 12 sắp ra mắt thì Apple đều thiết kế cạnh bên trùng màu với thân máy, tạo nên một thể thống nhất.','2020-11-09 05:20:34',4,7,'4862d261f6e1a730e160.jpg','2cb871fab028a73627df.jpg','2570259d2e49289bac6a.jpg'),(7,'iPhone 11 Pro Max',1169.00,15,22,'Đỏ, Vàng, Đen','iPhone 11 Pro Max – Bộ ba camera sau chụp ảnh đỉnh cao\r\nRa mắt cùng với iPhone 11 và 11 Pro là iPhone 11 Pro Max, đây mẫu smartphone cao cấp nhất của iPhone 11 Series được ra mắt năm 2019 và sắp tới là điện thoại iPhone 12 trong năm 2020. Với thiết kế cao cấp, hệ thống camera 3 camera cùng cấu hình siêu mạnh mẽ thì đây chính là một chiếc smartphone đáp ứng mọi trải nghiệm của người dùng.','2020-11-09 05:22:19',4,7,'0f77b538a69f5c1345fc.jpg','9c9059d1e37e17dc40fc.jpg','f1defada99fb679940ba.jpg'),(8,'Apple iPhone 8 Plus 128GB',599.00,12,5,'Red, Black, Blue','Điện thoại iPhone 8 Plus 128GB chính hãng – Bộ nhớ lưu trữ lớn, camera kép nâng cấp trải nghiệm\r\nKế thừa sự thành công của iPhone 7/7 Plus, Apple lại tiếp tục làm cộng đồng yêu công nghệ phải chú ý khi cho ra mắt mẫu điện thoại iPhone 12 và kế tiếp của họ - iPhone 8 Plus 128GB. iPhone 8 Plus 128GB sở hữu thiết kế đẳng cấp với mặt lưng làm từ kính hoàn toàn mới lạ, độc đáo và sang trọng hơn người anh em tiền nhiệm. Bên cạnh đó, iPhone 8 Plus cũng có nhiều nâng cấp từ camera, hiệu năng,… để mang đến cho người dùng những trải nghiệm đỉnh cao hơn.','2020-11-09 05:24:30',4,7,'4bb1c39e920f194b57bb.jpg','fdfab6fc9587237ada1e.jpg','2f95ad97e6fdcaf7cb81.jpg'),(9,'iPhone 11 Pro',1069.00,15,22,'Red, Black, Blue','iPhone 11 Pro - Siêu phẩm 3 camera chụp ảnh chuyên nghiệp\r\niPhone 11 Pro là 1 trong 3 mẫu smartphone mới nhất của iPhone 11 series được Apple ra mắt vào năm 2019, bên cạnh iPhone 11 và iPhone 11 Pro Max. Bộ ba siêu phẩm này đều tập trung về nâng cấp phần cứng và hiệu năng. Đặc biệt, chiếc iPhone 11 Pro có đến 3 camera có các chứng năng chụp hình và quay phim chuyên nghiệp đỉnh cao.\r\n\r\nThiết kế thép nguyên khối với mặt lưng kính mờ và màn hình 5.8 inches sắc nét','2020-11-09 05:26:01',4,7,'2933e899cb972532e530.jpg','72a5231731385ad73a66.jpg','1a1452f9d9ac740ff355.jpg'),(10,'Xiaomi Mi 10T Pro 5G',569.00,0,22,'Red, Black, Blue','Điện thoại Xiaomi Mi 10T Pro – Bộ ba camera chụp ảnh siêu đỉnh\r\nNếu bạn là một Mifan hay là một người dùng yêu công nghệ thì chắc chắn bạn sẽ không thể bỏ qua Xiaomi Mi 10T Pro. Với nhiều tính năng đặc biệt và công nghệ chụp ảnh cao cấp, Xiaomi đang dần đánh bóng tên tuổi mình hơn với chiếc smartphone này.\r\n\r\nThiết kế cao cấp cùng mặt lưng kính mềm mại, mượt mà\r\nMáy sở hữu cho mình một khung viền nhựa chắc chắn, giúp tạo cho bản thân một độ chắc chắn và bền bỉ nhất định. Cùng với đó là độ hoàn thiện cao cấp đến từ các phím bấm cũng như độ bo cong các góc cạnh của máy.','2020-11-09 05:28:14',4,8,'66776398241dcb2ba520.jpg','fa5f2f3c3f0a2afbfc7e.png','65c459b6e4ab8b53a4d7.jpg'),(11,'Oppo Reno4 Pro',529.00,5,22,'Red, Black, Blue','Điện thoại OPPO Reno 4 Pro - Smartphone thời thượng với cấu hình ấn tượng\r\nHãng smartphone nổi tiếng OPPO vừa qua đã trình làng sản phẩm mới thuộc dòng Reno, đó chính là OPPO Reno 4 Pro cùng với Reno 4. Đây là chiếc smartphone có thiết kế thời thượng, hiệu năng mạnh mẽ cùng bộ ba camera chụp ảnh ấn tượng, hứa hẹn sẽ là \"siêu phẩm\" đáng chú ý của hãng OPPO trong năm nay.\r\n\r\nThân máy nguyên khối cứng cáp, màn hình 6.55 inch viền siêu mỏng','2020-11-09 05:29:49',4,9,'f7e978ccd851863a975f.jpg','a4e656e8a023cfa2d34a.jpg','ee2634c941689fdf0172.jpg'),(12,'Tai nghe Bluetooth Apple AirPods 2',169.00,0,22,'Black, White','Tai nghe Apple AirPods 2 – Thiết kế tối giản, chất lượng âm thanh tuyệt vời\r\nVừa qua, Apple đã chính thức cho ra mắt chiếc tai nghe Airpods 2. Thế hệ thứ 2 lần này không có nhiều sự khác biệt so với thế hệ đầu về ngoại hình, trừ một số chi tiết về đèn báo hiệu cũng như ra mắt thêm phiên bản sạc không dây và sạc thường (sạc có dây). Ngoài ra, bạn có thể tham khảo thêm Apple Airpods 3, sắp được ra mắt trong thời gian tới.','2020-11-09 05:36:33',5,10,'6ebdc2d5255b2f8f1c62.jpg','875fed6f9afa958960b5.jpg','210ba12993ebd0158bc6.jpg'),(13,'Bút cảm ứng Apple Pencil 2 MU8F2',159.00,0,22,'Black, White','Bút cảm ứng Apple Pencil 2 – Cải tiến sâu, nâng cao trải nghiệm người dùng\r\nSau sự ủng hộ của người dùng về bút cảm ứng Apple Pencil, phụ kiện Apple đã tiếp tục cho ra mắt Apple Pencil thế hệ thứ hai với tên gọi bút cảm ứng Apple Pencil 2. Nhận được sự kế thừa của người tiền nhiệm cùng những nâng cấp quý giá, bút cảm ứng Apple Pencil 2 xứng đáng là phụ kiện đồ chơi công nghệ không thể thiếu khi người dùng đang sở hữu một chiếc iPad.','2020-11-09 05:37:51',5,12,'3dc7ab42a6a5250ce3d2.jpg','49f562fb4a06d509a4e4.jpg','fa5a346e4956073d1677.jpg'),(14,'Xiaomi Mi Band 5',39.00,5,22,'Black, White','Xiaomi Mi Band 5 – Nâng cấp về màn hình, tính năng thú vị\r\nKhi nói đến đồng hồ thông minh thì Xiaomi là cái tên không thể không nghĩ đến. Các thiết bị của hãng không chỉ đẹp, mang tính năng động mà còn rất bền bỉ và luôn mang đến những trải nghiệm tuyệt vời nhất cho người dùng. Để nối tiếp thành công của dòng Xiaomi Mi Band, hãng đã tiếp tục cho ra mắt sản phẩm vòng đeo tay thông minh Mi Band 5 hứa hẹn mang tới những trải nghiệm thật hoàn hảo cho người dùng.\r\n\r\nThiết kế nhỏ gọn, sang trọng kế thừa nét đặc trưng của đàn anh\r\nNhìn qua về tổng thể có thấy thiết kế Xiaomi Mi Band 5 không quá khác biệt so với Mi Band 4 trước đó. Sáng tạo, bền bỉ và năng động là những tính từ được sử dụng để đánh giá những chiếc đồng hồ thông minh của Xiaomi. Phần thân của Mi Band 5 được làm hoàn thiện từ nhựa cao cấp, tạo nên một thiết kế cứng cáp cho vòng và đồng thời cũng làm cho vòng có trọng lượng nhẹ hơn, cho cảm giác bạn đang đeo một thiết bị đắt tiền.','2020-11-09 05:47:15',6,16,'085663b48a0a30edd49b.jpg','24386a9174be1143d02b.jpg','a76744f2a0a5d2044d96.jpg'),(15,'Apple Watch SE 44mm (GPS)',386.00,0,22,'Black, White','Apple Watch SE 44MM (GPS) tiện nghi, thân thiện, trang bị nhiều tính năng cao cấp\r\nApple Watch SE 44MM (GPS) là phiên bản giá rẻ của Apple Watch Series 6. Mặc dù mới được ra mắt nhưng sản phẩm đã nhanh chóng thu hút được đông đảo người hâm mộ. Đặc biệt là phiên bản giá rẻ nhưng sản phẩm được thiết kế vô cùng sang trọng bên cạnh đó là nhiều tính năng cao cấp mang đến trải nghiệm hoàn hảo cho người sử dụng.\r\n\r\nThiết kế sang trọng, màn hình Retina có độ sáng cao\r\nApple Watch SE 44MM (GPS) có thiết kế sang trọng với hình vuông vức quen thuộc. Các góc cạnh của sản phẩm được bo cong nhẹ và thiết kế nút Digital Crown ở bên phải mang đến sự tiện ích trong quá trình sử dụng.','2020-11-09 05:48:56',6,13,'e80704fe6d0a59126e63.jpg','931a81daca150b9c1c9f.jpg','23526c3ddb7151931fed.jpg');
/*!40000 ALTER TABLE `addproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(180) NOT NULL,
  `profile` varchar(180) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'lemanh','lemanh','lemanh@gmail.com','$2b$12$NoTx4w4h6YS23CX5y29kBeS3YAFh5bsr2trp/trLnt8Znw9cCqQmO','profile.jpg');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category_id` int NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `brand_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (6,4,'Samsung'),(7,4,'Apple'),(8,4,'Xiaomi '),(9,4,'Oppo '),(10,5,'Accessories apple'),(11,5,'Rechargeable battery backup'),(12,5,'Charging cable'),(13,6,'Apple Watch'),(16,6,'Xiaomi Watch ');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (5,'Accessories'),(6,'Clock'),(4,'SmartPhone');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_order`
--

DROP TABLE IF EXISTS `customer_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `invoice` varchar(20) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `customer_id` int NOT NULL,
  `orders` text,
  `date_created` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `invoice` (`invoice`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_order`
--

LOCK TABLES `customer_order` WRITE;
/*!40000 ALTER TABLE `customer_order` DISABLE KEYS */;
INSERT INTO `customer_order` VALUES (1,'f8f92fb1f1','Pending','Da Nang',1,'{\"1\": {\"brand\": \"Apple\", \"color\": \"\\u0110\\u1ecf\", \"colors\": \"\\u0110\\u1ecf, Tr\\u1eafng, \\u0110en\", \"discount\": 0, \"image\": \"dc7080d65f1cc13f56fa.png\", \"name\": \"SamSung\", \"price\": 222.0, \"quantity\": 1}}','2020-11-09 03:35:17'),(2,'a6908d78ea','Pending','Da Nang',1,'{\"14\": {\"brand\": \"Xiaomi Watch \", \"color\": \"Black\", \"colors\": \"Black, White\", \"discount\": 5, \"image\": \"085663b48a0a30edd49b.jpg\", \"name\": \"Xiaomi Mi Band 5\", \"price\": 39.0, \"quantity\": 2}}','2020-11-09 05:50:32');
/*!40000 ALTER TABLE `customer_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rate`
--

DROP TABLE IF EXISTS `rate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `register_id` int NOT NULL,
  `time` datetime NOT NULL,
  `desc` text NOT NULL,
  `rate_number` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `register_id` (`register_id`),
  CONSTRAINT `rate_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `addproduct` (`id`),
  CONSTRAINT `rate_ibfk_2` FOREIGN KEY (`register_id`) REFERENCES `register` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rate`
--

LOCK TABLES `rate` WRITE;
/*!40000 ALTER TABLE `rate` DISABLE KEYS */;
/*!40000 ALTER TABLE `rate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `gender` varchar(5) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `date_created` datetime NOT NULL,
  `lock` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`),
  CONSTRAINT `register_chk_1` CHECK ((`lock` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES (1,'Manh','Lê','Mạnh','xuanmanhitweb1011@gmail.com','0339134073','M','$2b$12$KzjjXsRaDOKAsuQu3X2jUe5unm3wN3.j6QdH07J//zxzc0dt55RaC','2020-11-09 03:35:01',0);
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-09 13:33:11
