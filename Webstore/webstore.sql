-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2019 at 10:04 AM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webstore`
--

-- --------------------------------------------------------

--
-- Table structure for table `administration`
--

CREATE TABLE `administration` (
  `userID` varchar(12) NOT NULL,
  `designation` varchar(12) NOT NULL,
  `salary` float NOT NULL,
  `hireDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `salesID` varchar(35) NOT NULL,
  `categoryID` int(5) NOT NULL,
  `productID` int(5) NOT NULL,
  `quantity` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`salesID`, `categoryID`, `productID`, `quantity`) VALUES
('016769833371555833139.898479', 1001, 2, 2),
('1234', 1001, 2, 5),
('1234', 1001, 5, 2),
('1234', 1001, 7, 2),
('1234', 1002, 8, 6),
('1234', 1004, 1, 5),
('1234', 1004, 2, 6),
('2019041923242012345678901', 1001, 5, 1),
('2019041923242012345678901', 1001, 7, 1),
('2019041923242012345678901', 1002, 8, 2);

-- --------------------------------------------------------

--
-- Table structure for table `product_category`
--

CREATE TABLE `product_category` (
  `categoryID` int(5) NOT NULL,
  `categoryName` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_category`
--

INSERT INTO `product_category` (`categoryID`, `categoryName`) VALUES
(1001, 'Category 1'),
(1002, 'Category 2'),
(1003, 'Category 3'),
(1004, 'Categroy 4');

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `categoryID` int(5) NOT NULL,
  `productID` int(5) NOT NULL,
  `name` varchar(25) NOT NULL,
  `price` float NOT NULL,
  `cost` float NOT NULL,
  `quantityLeft` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`categoryID`, `productID`, `name`, `price`, `cost`, `quantityLeft`) VALUES
(1001, 2, 'Product 2', 200, 150, 94),
(1001, 3, 'Product 3', 200, 150, 0),
(1001, 4, 'Product 4', 200, 150, 0),
(1001, 5, 'Product 5', 200, 150, 99),
(1001, 6, 'Product 6', 200, 120, 80),
(1001, 7, 'Product 1', 200, 150, 97),
(1002, 2, 'Product 2', 200, 150, 0),
(1002, 8, 'Product 8', 600, 200, 90),
(1003, 1, 'Product 1', 200, 150, 0),
(1004, 1, 'Product 1', 200, 150, 0),
(1004, 2, 'Product 2', 200, 150, 0);

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `salesID` varchar(35) NOT NULL,
  `userID` varchar(12) NOT NULL,
  `orderID` varchar(35) NOT NULL,
  `totalAmount` float NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`salesID`, `userID`, `orderID`, `totalAmount`, `date`) VALUES
('016769833371555833139.898479', '01676983337', '7TB11857KM9657913', 400, '2019-04-21');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `userID` varchar(12) NOT NULL,
  `password` varchar(50) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `cellPhoneNumber` varchar(11) NOT NULL,
  `emailAddress` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`userID`, `password`, `firstName`, `lastName`, `address`, `cellPhoneNumber`, `emailAddress`, `status`) VALUES
('01676983337', '12345678', 'Tanzim', 'Ahmed', '40AHL', '01676983337', 'tan@gmail.com', 'active');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administration`
--
ALTER TABLE `administration`
  ADD PRIMARY KEY (`userID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`salesID`,`categoryID`,`productID`),
  ADD KEY `categoryID` (`categoryID`,`productID`);

--
-- Indexes for table `product_category`
--
ALTER TABLE `product_category`
  ADD PRIMARY KEY (`categoryID`);

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`categoryID`,`productID`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`salesID`),
  ADD KEY `userID` (`userID`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`userID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `administration`
--
ALTER TABLE `administration`
  ADD CONSTRAINT `administration_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user_details` (`userID`) ON UPDATE CASCADE;

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`categoryID`,`productID`) REFERENCES `product_details` (`categoryID`, `productID`) ON UPDATE CASCADE;

--
-- Constraints for table `product_details`
--
ALTER TABLE `product_details`
  ADD CONSTRAINT `product_details_ibfk_2` FOREIGN KEY (`categoryID`) REFERENCES `product_category` (`categoryID`) ON UPDATE CASCADE;

--
-- Constraints for table `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user_details` (`userID`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
