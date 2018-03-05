/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : jzsc

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2018-03-05 22:16:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jz_credentials
-- ----------------------------
DROP TABLE IF EXISTS `jz_credentials`;
CREATE TABLE `jz_credentials` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `social_code` varchar(128) NOT NULL,
  `c_type` varchar(16) DEFAULT NULL,
  `c_code` varchar(64) DEFAULT NULL,
  `c_name` varchar(64) DEFAULT NULL,
  `c_creatdate` varchar(32) DEFAULT NULL,
  `c_expiredate` varchar(32) DEFAULT NULL,
  `c_issuer` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jz_info
-- ----------------------------
DROP TABLE IF EXISTS `jz_info`;
CREATE TABLE `jz_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `social_code` varchar(128) NOT NULL,
  `name` varchar(64) NOT NULL,
  `legal_re` varchar(16) DEFAULT NULL,
  `com_type` varchar(16) DEFAULT NULL,
  `province` varchar(16) DEFAULT NULL,
  `addr` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `社会代码` (`social_code`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jz_person
-- ----------------------------
DROP TABLE IF EXISTS `jz_person`;
CREATE TABLE `jz_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `social_code` varchar(128) NOT NULL,
  `p_name` varchar(64) NOT NULL,
  `p_code` varchar(32) DEFAULT NULL,
  `p_ctype` varchar(16) DEFAULT NULL,
  `p_ccode` varchar(64) DEFAULT NULL,
  `p_profession` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for jz_progress
-- ----------------------------
DROP TABLE IF EXISTS `jz_progress`;
CREATE TABLE `jz_progress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `social_code` varchar(128) NOT NULL,
  `p_code` varchar(255) NOT NULL,
  `p_name` varchar(255) NOT NULL,
  `p_addr` varchar(32) DEFAULT NULL,
  `p_type` varchar(32) DEFAULT NULL,
  `p_company` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
