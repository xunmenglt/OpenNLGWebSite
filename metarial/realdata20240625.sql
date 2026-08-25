/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 8.1.0 : Database - opennlg
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`opennlg` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `opennlg`;

/*Table structure for table `og_article` */

DROP TABLE IF EXISTS `og_article`;

CREATE TABLE `og_article` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `article_id` varchar(20) NOT NULL COMMENT '文章id',
  `article_title` varchar(250) NOT NULL COMMENT '文章标题',
  `article_summary` varchar(550) DEFAULT NULL COMMENT '文章概要',
  `article_content` mediumtext COMMENT '文章内容',
  `article_read_times` int NOT NULL DEFAULT '0' COMMENT '文章阅读次数',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_article` */

insert  into `og_article`(`id`,`article_id`,`article_title`,`article_summary`,`article_content`,`article_read_times`,`create_time`,`update_time`) values 
(26,'article_723088826287','刘腾的简历',NULL,' <center>\n     <h1>XXX</h1>\n </center>\n\n## 个人信息 \n\n* 性 别：男&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;年 龄：25  \n* 手 机：134XXXX3216 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;  邮 箱：XXXXX@XXX.com    \n* 专 业：计算机科学与计算 &emsp;&emsp;&emsp;&emsp;&emsp; 岗 位：研发工程师\n\n## 工作及教育经历\n\n* 前公司&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;2019.8~至今&emsp;&emsp;&emsp;&emsp;&emsp; 事业群名字-部门名字       \n* XXXX大学&emsp;&emsp;&emsp;&emsp;&emsp;2017.9~2019.7&emsp;&emsp;&emsp;&emsp; 计算机科学与技术专业-研究生         \n* XXXX大学&emsp;&emsp;&emsp;&emsp;&emsp;2013.9~2017.7&emsp;&emsp;&emsp;&emsp; 计算机科学与技术专业-本科  \n\n## 专业技能\n\n* 熟练使用 C++，掌握Go，了解 Java、Python、PHP 等编程语言\n* 掌握基础数据结构和算法的基本原理\n* 等等\n\n## 项目经历\n\n1. 公司/学校 - XXweb服务器 - 独立开发 - 201508- 201512 \n    * 具体功能 \n    * 运用了那些技术，技术难点是\n    * 效果如何\n    * demo演示地址，github地址 \n\n2. 公司/学校 - XX游戏 - 负责后端开发 - 201309- 201401 \n    * 具体功能 \n    * 运用了那些技术，技术难点是\n    * 效果如何\n    * demo演示地址，github地址 \n\n## 获奖经历\n* XXX 优秀新人\n* XXX 学生社团优秀干部\n* 竞赛 XXX 奖\n\n## 个人账号 \n* blog 地址 (附加自己博客特色，写了哪些技术文章)\n* github 地址 (附加自己github特色，突出的项目)\n\n## 其他信息 \n* 喜欢钻研技术 等等\n* 性格开朗，喜欢跳舞，做个主持人 等等 \n\n> 简历的word版本，可以在我的公众号[代码随想录](https://img-blog.csdnimg.cn/20200815195519696.png)中，后台回复：简历模板，别可获取\n\n# 关于作者\n\n大家好，我是程序员Carl，哈工大师兄，ACM 校赛、黑龙江省赛、东北四省赛金牌、亚洲区域赛铜牌获得者，先后在腾讯和百度从事分布式技术研发。\n\n也欢迎与我交流，备注：「个人简单介绍」 + 交流，围观朋友圈，做点赞之交（备注没有自我介绍不通过哦）\n\n![QQ图片20231102191700.jpg](https://opennlg.cn/api/files/QQ图片20231102191700.jpg)\n\n# 公众号\n\n更多精彩文章持续更新，微信搜索：「代码随想录」第一时间围观，关注后回复：「666」可以获得所有算法专题原创PDF。\n\n\n**「代码随想录」每天准时为你推送一篇经典面试题目，帮你梳理算法知识体系，轻松学习算法！**，并且公众号里有大量学习资源，也有我自己的学习心得和方法总结，更有上万录友们在这里打卡学习。\n\n**来看看就知道了，你会发现相见恨晚！**\n\n<a name=\"公众号\"></a>\n\n![](https://github.com/youngyangyang04/leetcode-master/blob/master/pics/%E5%85%AC%E4%BC%97%E5%8F%B7.png)\n\n',47,'2023-11-03 03:16:21','2023-11-03 03:27:37');

/*Table structure for table `og_members` */

DROP TABLE IF EXISTS `og_members`;

CREATE TABLE `og_members` (
  `member_id` int NOT NULL AUTO_INCREMENT COMMENT '成员id',
  `cn_name` varchar(50) NOT NULL COMMENT '中文名称',
  `en_name` varchar(50) NOT NULL COMMENT '英文名称',
  `member_desc` varchar(550) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT '描述',
  `serial_num` int NOT NULL DEFAULT '0' COMMENT '序号',
  `avatar_url` varchar(550) DEFAULT NULL COMMENT '头像链接',
  `outside_url` varchar(550) DEFAULT NULL COMMENT '外链',
  `inside_url` varchar(550) DEFAULT NULL COMMENT '内链',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_members` */

insert  into `og_members`(`member_id`,`cn_name`,`en_name`,`member_desc`,`serial_num`,`avatar_url`,`outside_url`,`inside_url`,`create_time`,`update_time`) values 
(13,'刘腾','Teng Liu','Graduate student, <br>\nExpected Graduation Date, 2027/06',14,'https://opennlg.cn/api/files/1705907847958.png','https://gitee.com/xunmenglt','','2023-11-03 03:03:05','2024-01-22 07:17:36'),
(14,'梁小波','xiaobo liang','Phd Candidate, <br>\nExpected Graduation Date, 2024/06',3,'https://opennlg.cn/api/files/1698980948653.png','','','2023-11-03 03:09:37','2023-11-06 12:35:23'),
(15,'纪一心','Yixin Ji','Phd Student, <br> \nExpected Graduation Date, 2027/06',7,'https://opennlg.cn/api/files/1698981773977.png','','','2023-11-03 03:30:49','2023-11-06 13:19:18'),
(16,'苏仪','Yi Su','Graduate student, <br>\nExpected Graduation Date, 2026/06',12,'https://opennlg.cn/api/files/1698983773476.png','https://github.com/yisunlp','','2023-11-03 03:54:19','2023-11-06 12:44:39'),
(17,'肖义胜','LittleBrother-Xiao','Phd Student, <br>\nExpected Graduation Date, 2027/01',5,'https://opennlg.cn/api/files/1698983676846.png','','','2023-11-03 03:54:42','2023-11-06 13:18:53'),
(18,'郭沛','Pei Guo','Graduate student, <br>\nExpected Graduation Date, 2025/06',10,'https://opennlg.cn/api/files/1698991865530.png','','','2023-11-03 06:16:10','2023-11-06 12:42:30'),
(19,'湯澤成','Zecheng Tang','Phd Student,<br>Expected Graduation Date, 2027/06.\nVisiting my homepage for more details. ',6,'https://opennlg.cn/api/files/1708311963716.png','https://zetangforward.github.io/','','2023-11-03 10:05:38','2024-02-19 03:06:08'),
(20,'李俊涛','Juntao Li','Associate Professor',2,'https://opennlg.cn/api/files/1699020035673.png','http://scst.suda.edu.cn/0e/49/c11250a527945/page.htm','','2023-11-03 14:02:06','2023-11-06 12:41:36'),
(21,'张民','Min Zhang','Professor',1,'https://opennlg.cn/api/files/1699020260582.png','http://scst.suda.edu.cn/12/02/c11250a528898/page.htm','','2023-11-03 14:09:12','2023-11-06 12:41:41'),
(22,'王品正','Pinzheng Wang','Phd Student, <br>\nExpected Graduation Date, 2028/06',9,'https://opennlg.cn/api/files/1699021744279.png','','','2023-11-03 14:30:30','2023-11-06 13:19:27'),
(23,'丁誉洋','Yuyang Ding','Phd Student, <br>\nExpected Graduation Date, 2028/06',8,'https://opennlg.cn/api/files/1699022324608.png','','','2023-11-03 14:39:45','2023-11-06 13:19:23'),
(24,'王纪凯','Jikai Wang','Graduate student, <br>\nExpected Graduation Date, 2026/06',13,'https://opennlg.cn/api/files/1699256799309.png','','','2023-11-06 07:46:45','2023-11-06 12:44:44'),
(25,'乔丹','Dan Qiao','Graduate student, <br>\nExpected Graduation Date, 2025/06',11,'https://opennlg.cn/api/files/1699274637690.png','','','2023-11-06 12:44:13','2023-11-06 12:44:35')