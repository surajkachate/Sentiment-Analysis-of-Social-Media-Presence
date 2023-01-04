-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 10, 2022 at 09:23 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scraper`
--

-- --------------------------------------------------------

--
-- Table structure for table `monitor`
--

CREATE TABLE `monitor` (
  `id` int(11) NOT NULL,
  `type` varchar(255) NOT NULL,
  `command` text NOT NULL,
  `status` varchar(255) NOT NULL,
  `firetime` varchar(255) NOT NULL,
  `termtime` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tweets`
--

CREATE TABLE `tweets` (
  `id` int(20) NOT NULL,
  `tweet_id` varchar(20) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `renderedContent` text DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `outlinks` text DEFAULT NULL,
  `tcooutlinks` varchar(255) DEFAULT NULL,
  `replyCount` varchar(255) DEFAULT NULL,
  `retweetCount` varchar(255) DEFAULT NULL,
  `likeCount` varchar(255) DEFAULT NULL,
  `quoteCount` varchar(255) DEFAULT NULL,
  `conversationId` varchar(255) DEFAULT NULL,
  `lang` varchar(255) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `media` text DEFAULT NULL,
  `retweetedTweet` varchar(255) DEFAULT NULL,
  `quotedTweet` text DEFAULT NULL,
  `mentionedUsers` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(20) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `displayname` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `descriptionUrls` text DEFAULT NULL,
  `verified` varchar(255) DEFAULT NULL,
  `created` varchar(255) DEFAULT NULL,
  `followersCount` varchar(255) DEFAULT NULL,
  `friendsCount` varchar(255) DEFAULT NULL,
  `statusesCount` varchar(255) DEFAULT NULL,
  `favouritesCount` varchar(255) DEFAULT NULL,
  `listedCount` varchar(255) DEFAULT NULL,
  `mediaCount` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `protected` varchar(255) DEFAULT NULL,
  `linkUrl` varchar(255) DEFAULT NULL,
  `profileImageUrl` varchar(255) DEFAULT NULL,
  `profileBannerUrl` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `monitor`
--
ALTER TABLE `monitor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tweets`
--
ALTER TABLE `tweets`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `monitor`
--
ALTER TABLE `monitor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tweets`
--
ALTER TABLE `tweets`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
