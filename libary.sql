
# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 47.93.250.86 (MySQL 5.7.18)
# Database: libary
# Generation Time: 2017-06-13 03:26:38 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table books
# ------------------------------------------------------------

DROP TABLE IF EXISTS `books`;

CREATE TABLE `books` (
  `book_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_name` varchar(255) DEFAULT NULL,
  `book_type` int(11) DEFAULT NULL,
  `book_stock` int(11) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `publish_com` varchar(255) DEFAULT NULL,
  `publish_date` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT '1',
  `remarks` varchar(255) DEFAULT NULL,
  `book_num` int(11) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `recommend` int(11) DEFAULT NULL,
  `translator` varchar(255) DEFAULT NULL,
  `page` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `in_date` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;

INSERT INTO `books` (`book_id`, `book_name`, `book_type`, `book_stock`, `author`, `publish_com`, `publish_date`, `status`, `remarks`, `book_num`, `photo`, `recommend`, `translator`, `page`, `price`, `in_date`)
VALUES
    (1,'Java核心编程',1,NULL,'张胜','电子工业出版社','2015-04-02',1,NULL,8,NULL,NULL,NULL,NULL,NULL,NULL),
    (2,'Java入门到精通',1,NULL,'李梦','机械工业出版社','2016-04-20',1,NULL,3,NULL,NULL,NULL,NULL,NULL,NULL),
    (3,'html网页设计',1,NULL,'陈广','电子工业出版社','2016-04-02',1,NULL,4,NULL,NULL,NULL,NULL,NULL,NULL),
    (4,'追风筝的人',NULL,NULL,'胡赛尼','上海人民出版社','2006-05-19',1,NULL,5,NULL,NULL,NULL,NULL,NULL,NULL),
    (5,'看见',NULL,NULL,'柴静','广西师范大学出版社','2013-01-01',0,NULL,4,NULL,NULL,NULL,NULL,NULL,NULL),
    (6,'梦的解析',NULL,NULL,'弗洛伊德','中国城市出版社','2011-01-01',0,NULL,3,NULL,NULL,NULL,NULL,NULL,NULL),
    (7,'穆斯林的葬礼',NULL,NULL,'霍达','北京十月文艺出版社','1988-12-1',0,NULL,2,NULL,NULL,NULL,NULL,NULL,NULL),
    (8,'再见，哥伦布',NULL,NULL,'菲利普·罗斯','人民文学出版社','2009-06-03',0,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL);

/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table bookshelf
# ------------------------------------------------------------

DROP TABLE IF EXISTS `bookshelf`;

CREATE TABLE `bookshelf` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table borrows
# ------------------------------------------------------------

DROP TABLE IF EXISTS `borrows`;

CREATE TABLE `borrows` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date_borrow` varchar(255) DEFAULT '',
  `date_return` varchar(255) DEFAULT '',
  `status` int(11) DEFAULT '0',
  `openid` varchar(255) DEFAULT NULL,
  `type` int(11) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `borrows` WRITE;
/*!40000 ALTER TABLE `borrows` DISABLE KEYS */;

INSERT INTO `borrows` (`id`, `book_id`, `user_id`, `date_borrow`, `date_return`, `status`, `openid`, `type`)
VALUES
    (2,2,3,'2017-04-23 11:11:00','2017-05-23 11:11:00',1,'o-pJK0tt8k66oMbQk8MMlfUV9CZU',2),
    (3,1,0,'2017-05-30 09:58:21','2017-06-29 09:58:21',1,'o-pJK0tt8k66oMbQk8MMlfUV9CZU',1),
    (4,2,0,'2017-05-30 10:03:38','2017-06-29 10:03:38',1,'o-pJK0tt8k66oMbQk8MMlfUV9CZU',1),
    (5,2,0,'2017-05-30 10:07:06','2017-06-29 10:07:06',1,'o-pJK0tt8k66oMbQk8MMlfUV9CZU',1),
    (6,2,0,'2017-05-30 10:09:10','2017-06-29 10:09:10',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (7,2,0,'2017-05-30 10:39:57','2017-06-29 10:39:57',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (8,2,0,'2017-05-30 10:44:51','2017-06-29 10:44:51',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (9,2,0,'2017-05-30 10:53:58','2017-06-29 10:53:58',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (10,1,0,'2017-05-30 10:56:48','2017-06-29 10:56:48',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (11,3,1,'2017-05-30 11:00:09','2017-06-29 11:00:09',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (12,3,0,'2017-05-30 12:06:39','2017-06-29 12:06:39',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (13,3,0,'2017-05-30 21:15:20','2017-06-29 21:15:20',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (14,1,0,'2017-05-31 11:28:42','2017-06-30 11:28:42',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (15,2,0,'2017-05-31 11:29:00','2017-06-30 11:29:00',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (16,3,0,'2017-05-31 11:31:51','2017-06-30 11:31:51',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (17,2,0,'2017-05-31 11:32:06','2017-06-30 11:32:06',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (18,6,0,'2017-05-31 11:33:13','2017-06-30 11:33:13',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (19,6,0,'2017-05-31 11:36:32','2017-06-30 11:36:32',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (20,1,0,'2017-05-31 15:47:57','2017-06-30 15:47:57',1,'o-pJK0lqtVDHPeLeloJIlEIUFcQI',1),
    (21,1,0,'2017-05-31 23:41:19','2017-06-30 23:41:19',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (22,4,0,'2017-06-01 13:25:46','2017-07-01 13:25:46',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (23,3,0,'2017-06-01 13:30:33','2017-07-01 13:30:33',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (24,6,0,'2017-06-01 13:33:24','2017-07-01 13:33:24',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (25,1,0,'2017-06-07 08:33:06','2017-07-07 08:33:06',1,'oNkhlwN4t4N5YvWJkkqikFeF4ZYM',1),
    (26,1,0,'2017-06-07 08:54:10','2017-07-07 08:54:10',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (27,2,0,'2017-06-07 10:35:30','2017-07-07 10:35:30',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (28,1,0,'2017-06-07 10:44:21','2017-07-07 10:44:21',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (29,2,0,'2017-06-07 10:45:28','2017-07-07 10:45:28',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (30,3,0,'2017-06-07 16:10:04','2017-07-07 16:10:04',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (31,1,0,'2017-06-12 23:49:32','2017-07-12 23:49:32',0,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (32,3,0,'2017-06-12 23:51:13','2017-07-12 23:51:13',0,'oNkhlwGNczb862gwhsg-_BfL42vQ',1),
    (33,4,0,'2017-06-12 23:52:00','2017-07-12 23:52:00',1,'oNkhlwGNczb862gwhsg-_BfL42vQ',1);

/*!40000 ALTER TABLE `borrows` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table library_info
# ------------------------------------------------------------

DROP TABLE IF EXISTS `library_info`;

CREATE TABLE `library_info` (
  `library_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `curator` varchar(255) DEFAULT NULL,
  `phone_num` varchar(255) DEFAULT NULL,
  `adress` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `create_date` varchar(255) DEFAULT NULL,
  `num` varchar(255) DEFAULT NULL,
  `intorduction` varchar(255) DEFAULT NULL,
  `notice` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`library_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table reader_info
# ------------------------------------------------------------

DROP TABLE IF EXISTS `reader_info`;

CREATE TABLE `reader_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `birthday` varchar(255) DEFAULT NULL,
  `papertype` varchar(255) DEFAULT NULL,
  `papernum` varchar(255) DEFAULT NULL,
  `phone_num` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `type` int(11) DEFAULT '1',
  `mark` varchar(255) DEFAULT '0',
  `openid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table renewal_info
# ------------------------------------------------------------

DROP TABLE IF EXISTS `renewal_info`;

CREATE TABLE `renewal_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date_renewal` varchar(255) DEFAULT '',
  `date_return` varchar(255) DEFAULT '',
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table users
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT '''''',
  `password` varchar(255) DEFAULT NULL,
  `openid` varchar(255) DEFAULT NULL,
  `student_id` varchar(255) DEFAULT '''''',
  `college` varchar(255) DEFAULT '''''',
  `phone` varchar(255) DEFAULT '0',
  `num` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT '''''',
  `role` int(11) DEFAULT '1',
  `isfocus` int(11) DEFAULT '0',
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `users` (`user_id`, `user_name`, `name`, `password`, `openid`, `student_id`, `college`, `phone`, `num`, `email`, `role`, `isfocus`, `status`)
VALUES
    (1,'admin',NULL,'admin',NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL),
    (2,'','冯读者','zhang','o-pJK0lqtVDHPeLeloJIlEIUFcQI','B13070667','物联网学院','18312345678','','test@qq.com',0,NULL,NULL),
    (3,'','张三','1','o-pJK0tt8k66oMbQk8MMlfUV9CZU','B13070666','计算机学院','132233100','2','test@126.com',0,NULL,NULL),
    (6,NULL,'\'\'',NULL,'oNkhlwN4t4N5YvWJkkqikFeF4ZYM','\'\'','\'\'','0',NULL,'\'\'',1,0,1),
    (7,NULL,'冯同学',NULL,'oNkhlwGNczb862gwhsg-_BfL42vQ','B13070699','物联网学院','18351928888',NULL,'test@163.com',1,0,1),
    (8,NULL,'卢同学',NULL,'oNkhlwHisvu0nSOMD8IKu6iXm5a8','B13070688','物联网学院','18351921234',NULL,'test123@qq.com',1,0,1);

/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

