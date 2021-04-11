-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 11, 2021 at 12:58 PM
-- Server version: 8.0.23-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `205CDE`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `discription` varchar(500) DEFAULT NULL,
  `creater_id` text NOT NULL,
  `time_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `name`, `discription`, `creater_id`, `time_create`) VALUES
(203, 'df', '', '3', '2021-04-09 08:21:29'),
(204, 'ipods', '100% new', '4', '2021-04-09 08:21:29'),
(205, 'banana', 'banana from uk', '3', '2021-04-09 08:21:29'),
(206, 'iphone', 'apple iphone, second hand', '2', '2021-04-09 08:21:29'),
(207, 'apple', 'apple from UK', '1', '2021-04-09 08:21:29'),
(208, 'C890 Computer', 'white', '1', '2021-04-09 09:35:30'),
(209, 'Sell:Second Hand Scarf', '$20', '6', '2021-04-10 18:36:26');

-- --------------------------------------------------------

--
-- Table structure for table `service`
--

CREATE TABLE `service` (
  `service_id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `discription` varchar(500) DEFAULT NULL,
  `creater_id` int DEFAULT NULL,
  `time_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `service`
--

INSERT INTO `service` (`service_id`, `name`, `discription`, `creater_id`, `time_create`) VALUES
(700, 'cleaning ', '$600 for 2hr ', 3, '2021-04-09 14:12:58'),
(701, 'programming', 'required a part time $70/hr', 6, '2021-04-09 14:12:58'),
(703, '3 Pilaties Teachers', 'Required teaching pilaties ', 1, '2021-04-09 15:44:30'),
(704, 'Piano Teacher for beginners', 'Teaching a 3 yrs old boy', 1, '2021-04-09 16:24:14'),
(711, 'need a music teacher', '$120 per hour, Female', 21, '2021-04-11 04:17:49'),
(712, 'required a dancing teacher', 'teach beginners for ballets ', 22, '2021-04-11 04:37:01');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `Age` int NOT NULL,
  `phone` int NOT NULL,
  `time_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `email`, `name`, `Age`, `phone`, `time_create`) VALUES
(1, 'kkh', 'kkh', 'kkh@gmail.com', 'kkh', 10, 12345678, '2021-04-09 08:22:35'),
(2, 'jo', 'jo', 'jo@gmail.com', 'jo', 10, 36776666, '2021-04-09 08:22:35'),
(3, 'ho', 'ho', 'ho@himail.com', 'ho', 20, 28888888, '2021-04-09 08:22:35'),
(4, 'v', 'vv', 'vv@mail.com', 'Small V', 28, 13880000, '2021-04-09 08:22:35'),
(5, 'five', 'five', 'five@umail.com', 'high five', 26, 68885943, '2021-04-09 08:22:35'),
(6, 'user', 'user', 'user@hotmail.com', 'user', 0, 67234233, '2021-04-09 08:22:35'),
(7, 'kate', 'kate', 'kate@apple.mail.com', 'kate', 9, 56323434, '2021-04-09 08:22:35'),
(8, 'fiona', 'fiona', 'fiona@hotmail.com', 'fiona', 56, 34234234, '2021-04-09 08:22:35'),
(9, 'mi', 'mi', 'mi@gmail.com', 'mi', 56, 23423443, '2021-04-09 08:22:35'),
(10, 'mimi', 'mimi', 'mim@iii.com', 'mimi', 56, 23423443, '2021-04-09 08:22:35'),
(11, 'asd', 'asd', 'asd@gamil.com', 'jg', 56, 12345678, '2021-04-09 08:56:50'),
(12, 'dzf', 'sdf', 'sdf@gmail.com', 'we', 23, 12345678, '2021-04-10 09:27:39'),
(14, 'ken', 'ken', 'ken@gmail.com', 'ken', 12, 12345678, '2021-04-10 09:55:01'),
(15, 'many', '123', 'mandy25@gmail.com', 'mandy', 23, 12345678, '2021-04-10 09:56:19'),
(16, 'ghfe', 'kjdwfk', 'djkshf@dsb.com', 'pc', 34, 12376789, '2021-04-10 10:04:10'),
(17, 'try', 'ret', 'try@gmail.com', 'try', 12, 12345678, '2021-04-10 10:05:52'),
(18, 'try1', '12345', 'try@gmail.com', 'try', 34, 123456789, '2021-04-10 10:06:37'),
(19, 'new', 'new', 'new@gmail.com', 'new', 23, 15556666, '2021-04-10 10:07:59'),
(22, 'test', 'test', 'test@gmail.com', 'test', 45, 12345678, '2021-04-11 04:34:27');

-- --------------------------------------------------------

--
-- Table structure for table `venue`
--

CREATE TABLE `venue` (
  `venue_id` int NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `address` varchar(500) DEFAULT NULL,
  `discription` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `creater_id` int DEFAULT NULL,
  `time_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `venue`
--

INSERT INTO `venue` (`venue_id`, `name`, `address`, `discription`, `creater_id`, `time_create`) VALUES
(1001, 'Party room Provide', 'Rm 706, Floor 7, Happy Building, Happy Street', 'Good view', 3, '2021-04-10 06:50:50'),
(1002, 'House Rent--Northern distract', 'Flat 21, Beautiful St., Northern distract', 'Near the Beautiful bus station\r\n$10000 per month', 2, '2021-04-10 06:50:50'),
(1003, 'Rent Office in Central', 'Flat 59, Floor 59, Rich Building, Central', 'Having three rooms, one hall $30000 per month', 1, '2021-04-10 08:55:30'),
(1007, 'Rent Office in TST', 'Flat 56, TT, Happy St., TST', '$8000 per month\r\nNo window', 6, '2021-04-10 18:38:10'),
(1008, 'Renting  Flat', 'Happy St. 2180', '2 rooms, 2 toilets, a garden', 21, '2021-04-11 04:19:02'),
(1009, 'Rent House', 'Flat 567, Paficfic Court, NT', 'good view, $50000 per month', 22, '2021-04-11 04:38:29');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `service`
--
ALTER TABLE `service`
  ADD PRIMARY KEY (`service_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `venue`
--
ALTER TABLE `venue`
  ADD PRIMARY KEY (`venue_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=212;

--
-- AUTO_INCREMENT for table `service`
--
ALTER TABLE `service`
  MODIFY `service_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=713;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `venue`
--
ALTER TABLE `venue`
  MODIFY `venue_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1010;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
