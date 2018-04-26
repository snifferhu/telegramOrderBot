-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        10.2.12-MariaDB - mariadb.org binary distribution
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 fate 的数据库结构
CREATE DATABASE IF NOT EXISTS `fate` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `fate`;

-- 导出  表 fate.balance_info 结构
CREATE TABLE IF NOT EXISTS `balance_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tele_id` varchar(50) DEFAULT NULL,
  `nick_name` varchar(50) DEFAULT NULL,
  `amount` decimal(9,3) DEFAULT NULL,
  `driver_id` int(11) DEFAULT NULL,
  `driver_tele_id` varchar(50) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_time` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `tele_id` (`tele_id`),
  KEY `driver_tele_id` (`driver_tele_id`),
  KEY `driver_id` (`driver_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1015 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 fate.deposit_list 结构
CREATE TABLE IF NOT EXISTS `deposit_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tele_id` varchar(50) DEFAULT NULL,
  `price` decimal(10,3) DEFAULT NULL,
  `bef` decimal(10,3) DEFAULT NULL,
  `aft` decimal(10,3) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `tele_id` (`tele_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1952 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 fate.driver_list 结构
CREATE TABLE IF NOT EXISTS `driver_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tele_id` varchar(50) NOT NULL DEFAULT '0',
  `store_id` varchar(50) NOT NULL DEFAULT '0',
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `open_status` varchar(5) DEFAULT '''0''' COMMENT '0默认开启，1关闭',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 fate.follow_list 结构
CREATE TABLE IF NOT EXISTS `follow_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `driver_id` varchar(50) NOT NULL DEFAULT '0',
  `follow_id` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 fate.member 结构
CREATE TABLE IF NOT EXISTS `member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT '0',
  `nickName` varchar(50) DEFAULT '0',
  `amout` decimal(10,3) NOT NULL DEFAULT 0.000,
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `tele_id` varchar(50),
  `phone` varchar(50),
  `is_driver` int(11) DEFAULT 0,
  `driver_id` varchar(50) DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 fate.order_info 结构
CREATE TABLE IF NOT EXISTS `order_info` (
  `id` varchar(50) NOT NULL,
  `member_id` varchar(50) NOT NULL DEFAULT '0',
  `nick_name` varchar(50) NOT NULL DEFAULT '0',
  `price` decimal(10,3) NOT NULL DEFAULT 0.000,
  `item` varchar(50) NOT NULL DEFAULT '0',
  `order_status` varchar(50) NOT NULL DEFAULT '0',
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `driver_id` varchar(50) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
-- 导出  表 fate.store_info 结构
CREATE TABLE IF NOT EXISTS `store_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `store_title` varchar(50) NOT NULL DEFAULT '0',
  `store_id` varchar(50) NOT NULL DEFAULT '0',
  `menu_title` varchar(50) NOT NULL DEFAULT '0',
  `info` varchar(500) NOT NULL DEFAULT '0',
  `phone` varchar(50) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `wechat` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
