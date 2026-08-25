/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 8.0.27 : Database - opennlg
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`opennlg` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;

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
  `member_desc` text CHARACTER SET utf8 COLLATE utf8_general_ci COMMENT '描述',
  `profession` varchar(550) DEFAULT NULL COMMENT '职业',
  `direction` varchar(550) DEFAULT NULL COMMENT '研究方向',
  `email` varchar(100) DEFAULT NULL COMMENT '邮箱',
  `serial_num` int NOT NULL DEFAULT '0' COMMENT '序号',
  `avatar_url` varchar(550) DEFAULT NULL COMMENT '头像链接',
  `outside_url` varchar(550) DEFAULT NULL COMMENT '外链',
  `inside_url` varchar(550) DEFAULT NULL COMMENT '内链',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `ct_type` varchar(20) DEFAULT NULL COMMENT '类别',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_members` */

insert  into `og_members`(`member_id`,`cn_name`,`en_name`,`member_desc`,`profession`,`direction`,`email`,`serial_num`,`avatar_url`,`outside_url`,`inside_url`,`create_time`,`update_time`,`ct_type`) values 
(13,'刘腾','Teng Liu','Graduate student, <br>\nExpected Graduation Date, 2027/06','学生','自然语言处理','xmliuteng@163.com',14,'https://opennlg.cn/api/files/1705907847958.png','https://gitee.com/xunmenglt','','2023-11-03 03:03:05','2024-06-30 12:08:06','graduate_student'),
(14,'梁小波','xiaobo liang','Phd Candidate, <br>\nExpected Graduation Date, 2024/06',NULL,NULL,NULL,3,'https://opennlg.cn/api/files/1698980948653.png','','','2023-11-03 03:09:37','2023-11-06 12:35:23','phd'),
(15,'纪一心','Yixin Ji','Phd Student, <br> \nExpected Graduation Date, 2027/06',NULL,NULL,NULL,7,'https://opennlg.cn/api/files/1698981773977.png','','','2023-11-03 03:30:49','2023-11-06 13:19:18','phd'),
(16,'苏仪','Yi Su','Graduate student, <br>\nExpected Graduation Date, 2026/06',NULL,NULL,NULL,12,'https://opennlg.cn/api/files/1698983773476.png','https://github.com/yisunlp','','2023-11-03 03:54:19','2023-11-06 12:44:39','graduate_student'),
(17,'肖义胜','LittleBrother-Xiao','Phd Student, <br>\nExpected Graduation Date, 2027/01',NULL,NULL,NULL,5,'https://opennlg.cn/api/files/1698983676846.png','','','2023-11-03 03:54:42','2023-11-06 13:18:53','phd'),
(18,'郭沛','Pei Guo','Graduate student, <br>\nExpected Graduation Date, 2025/06',NULL,NULL,NULL,10,'https://opennlg.cn/api/files/1698991865530.png','','','2023-11-03 06:16:10','2023-11-06 12:42:30','graduate_student'),
(19,'湯澤成','Zecheng Tang','Phd Student,<br>Expected Graduation Date, 2027/06.\nVisiting my homepage for more details. ',NULL,NULL,NULL,6,'https://opennlg.cn/api/files/1708311963716.png','https://zetangforward.github.io/','','2023-11-03 10:05:38','2024-02-19 03:06:08','phd'),
(20,'李俊涛','Juntao Li','苏州大学计算机科学与技术学院副教授，2020年于北京大学获得博士学位，近5年在TPAMI、Artificial Intelligence、ACM TOIS、NeurIPS、ACL、KDD、EMNLP、NAACL和AAAI等CCF A/B会议和期刊发表论文近40篇，出版Fundations and Trends系列专著（期刊）1部，入选微软亚洲研究院2022年“铸星计划”访问学者，曾在CCF A类会议（AAAI-20和IJCAI-19）上做讲习报告（Tutorial），主要研究方向为文本生成。主持包括国自然青年项目在内的3项纵向项目，主持/共同主持阿里/华为横向项目4项，主导完成了苏州大学140亿参数自研预训练大模型的训练。多次担任高水平会议和期刊审稿人，如ARR Action Editor、 ACL-22/EMNLP-22/ACL-21领域主席、IJCAI-23/21 Senior PC、TAPMI、TKDE、TNNLS等审稿人，中文信息处理协会自然语言生成专委会委员。曾在佐治亚理工学院（Georgia Institute of Technology）、新加坡国立大学交流学习。指导本科生完成华为“昇腾众智”计划20余人次、华为奖学金4人次、获中国软件杯国家一等奖、14人次在CCF A/B类会议上发表论文。','苏州大学计算机科学与技术学院副教授','文本生成、预训练语言模型','ljt@suda.edu.cn',2,'https://opennlg.cn/api/files/1699020035673.png','http://scst.suda.edu.cn/0e/49/c11250a527945/page.htm','','2023-11-03 14:02:06','2024-06-30 00:39:53','teacher'),
(21,'张民','Min Zhang','张民，男，苏州大学教授，计算机学院院长，人类语言技术研究所长。国家杰青，国家“百千万人才”，国家有突出贡献中青年专家，享受国务院政府特殊津贴专家，江苏省“双创人才”和“双创团队”首席科学家。长期从事自然语言处理和机器翻译研究，聚焦语言认知智能中的自然语言分析、理解、翻译、交互和知识发掘的核心技术研究和产业应用。近年来作为负责人主持国家自然科学基金杰青和重点项目、科技部重点研发计划课题、工信部重大软件专项课题、大型产业界项目多项。已发表CCF A/B类论文150余篇，申请发明专利34项（已授权9项），出版Springer英文专著2部，主编论文集16本，获部级科技进步奖4项，担任包括IEEE/ACM T-ASLP、CL、NLE、JCST、Science China: Information Science、《中国科学：信息科学》、《软件学报》和《自动化学报》编委。',' 张民 苏州大学教授，计算机学院院长','自然语言处理、机器翻译、人工智能','minzhang@suda.edu.cn',1,'https://opennlg.cn/api/files/1699020260582.png','http://scst.suda.edu.cn/12/02/c11250a528898/page.htm','','2023-11-03 14:09:12','2024-06-30 00:38:55','teacher'),
(22,'王品正','Pinzheng Wang','Phd Student, <br>\nExpected Graduation Date, 2028/06',NULL,NULL,NULL,9,'https://opennlg.cn/api/files/1699021744279.png','','','2023-11-03 14:30:30','2023-11-06 13:19:27','phd'),
(23,'丁誉洋','Yuyang Ding','Phd Student, <br>\nExpected Graduation Date, 2028/06',NULL,NULL,NULL,8,'https://opennlg.cn/api/files/1699022324608.png','','','2023-11-03 14:39:45','2023-11-06 13:19:23','phd'),
(24,'王纪凯','Jikai Wang','Graduate student, <br>\nExpected Graduation Date, 2026/06',NULL,NULL,NULL,13,'https://opennlg.cn/api/files/1699256799309.png','','','2023-11-06 07:46:45','2023-11-06 12:44:44','graduate_student'),
(25,'乔丹','Dan Qiao','Graduate student, <br>\nExpected Graduation Date, 2025/06',NULL,NULL,NULL,11,'https://opennlg.cn/api/files/1699274637690.png','','','2023-11-06 12:44:13','2023-11-06 12:44:35','graduate_student'),
(27,'王越','Yue Wang','Phd Student, <br>\nExpected Graduation Date, 2026/06',NULL,NULL,NULL,4,'https://opennlg.cn/api/files/1699277495715.png','','','2023-11-06 13:18:13','2023-11-06 13:31:38','phd');

/*Table structure for table `og_members_category` */

DROP TABLE IF EXISTS `og_members_category`;

CREATE TABLE `og_members_category` (
  `ct_type` varchar(20) NOT NULL COMMENT '类别',
  `ct_zh_name` varchar(50) DEFAULT NULL COMMENT '类别中文名称',
  `sort` int DEFAULT '0' COMMENT '排序',
  PRIMARY KEY (`ct_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='成员类别';

/*Data for the table `og_members_category` */

insert  into `og_members_category`(`ct_type`,`ct_zh_name`,`sort`) values 
('graduate','毕业生',3),
('graduate_student','研究生（含访问学生）',2),
('phd','博士生（含访问学生）',1),
('teacher','指导老师',0);

/*Table structure for table `og_news` */

DROP TABLE IF EXISTS `og_news`;

CREATE TABLE `og_news` (
  `news_id` int NOT NULL AUTO_INCREMENT COMMENT '新闻id',
  `news_title` varchar(250) NOT NULL COMMENT '新闻标题',
  `news_summary` varchar(550) NOT NULL COMMENT '新闻概要',
  `news_read_times` int NOT NULL DEFAULT '0' COMMENT '阅读次数',
  `outside_url` varchar(550) DEFAULT NULL COMMENT '外链路径',
  `inside_url` varchar(550) DEFAULT NULL COMMENT '内链路径',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_new` int DEFAULT '0' COMMENT '是否是新的',
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_news` */

insert  into `og_news`(`news_id`,`news_title`,`news_summary`,`news_read_times`,`outside_url`,`inside_url`,`create_time`,`update_time`,`is_new`) values 
(26,'6 papers are accepted by the ACL 2023 main conference and its findings!','',0,'','','2023-05-02 00:00:00','2024-06-30 11:55:24',1),
(27,'7 long papers are accepted by EMNLP 2023 and its Findings!','',0,'','','2023-10-08 00:00:00','2023-11-20 03:30:41',0),
(28,'1 paper is accepted by Artificial Intelligence!','Are the BERT Family Zero-Shot Learners? A Study on Their Potential and Limitations',0,'','','2023-05-01 00:00:00','2023-11-08 03:13:58',0),
(29,'1 paper is accepted by TPAMI!','A survey on non-autoregressive generation for neural machine translation and beyond',0,'','','2023-05-04 00:00:00','2023-11-08 03:15:19',0),
(30,'2 papers are accepted by ICLR-24!','Are Bert Family Good Instruction Followers? A Study on Their Potential And Limitations',0,'','','2024-01-16 00:00:00','2024-02-19 03:05:32',0),
(31,'1 paper is accepted TPAMI!','Randomness Regularization with Simple Consistency Training for Neural Networks',0,'https://www.baidu.com/s?wd=mysql%20insert%E8%AF%AD%E5%8F%A5&tn=15007414_10_pg','','2024-02-12 00:00:00','2024-06-30 11:53:54',1);

/*Table structure for table `og_publication` */

DROP TABLE IF EXISTS `og_publication`;

CREATE TABLE `og_publication` (
  `publication_id` int NOT NULL AUTO_INCREMENT COMMENT '项目id',
  `publication_title` varchar(200) NOT NULL COMMENT '项目标题',
  `publication_desc` varchar(550) NOT NULL COMMENT '项目名称',
  `publication_cover` varchar(550) DEFAULT NULL COMMENT '项目封面',
  `outside_url` varchar(550) DEFAULT NULL COMMENT '外链',
  `inside_url` varchar(550) DEFAULT NULL COMMENT '内链',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`publication_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_publication` */

/*Table structure for table `og_reserarch` */

DROP TABLE IF EXISTS `og_reserarch`;

CREATE TABLE `og_reserarch` (
  `reserarch_id` int NOT NULL AUTO_INCREMENT COMMENT '研究文章id',
  `reserarch_title` varchar(550) NOT NULL COMMENT '研究文章标题',
  `reserarch_source` varchar(550) DEFAULT NULL COMMENT '研究文章来源',
  `reserarch_author` varchar(550) NOT NULL COMMENT '研究文章作者',
  `reserarch_cover` varchar(550) DEFAULT NULL COMMENT '研究文章封面',
  `is_new` int DEFAULT '1' COMMENT '是否是最新发布',
  `outside_url` varchar(550) DEFAULT NULL COMMENT '外链',
  `inside_url` varchar(550) DEFAULT NULL COMMENT '内链',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`reserarch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_reserarch` */

insert  into `og_reserarch`(`reserarch_id`,`reserarch_title`,`reserarch_source`,`reserarch_author`,`reserarch_cover`,`is_new`,`outside_url`,`inside_url`,`create_time`,`update_time`) values 
(32,'Are Bert Family Good Instruction Followers? A Study on Their Potential And Limitations','ICLR2024','肖义胜','http://localhost:3000/files/1719717128855.png',1,'https://www.yuque.com/dashboard','','2024-06-30 11:13:13','2024-06-30 11:13:13');

/*Table structure for table `og_team_culture` */

DROP TABLE IF EXISTS `og_team_culture`;

CREATE TABLE `og_team_culture` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '唯一id',
  `image` varchar(550) DEFAULT NULL COMMENT '图像',
  `title` varchar(550) DEFAULT NULL COMMENT '标题',
  `outside_url` varchar(550) DEFAULT NULL COMMENT '外链',
  `inside_url` varchar(550) DEFAULT NULL COMMENT '内链',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COMMENT='团队文化';

/*Data for the table `og_team_culture` */

insert  into `og_team_culture`(`id`,`image`,`title`,`outside_url`,`inside_url`,`create_time`) values 
(1,'http://localhost:3000/files/1719722930575.png','【2023】下山啦','','','2024-06-30 12:49:07'),
(2,'http://localhost:3000/files/1719722967136.png','【2023】登顶合照','','','2024-06-30 12:49:36'),
(3,'http://localhost:3000/files/1719723001239.png','【2023】展望未来','','','2024-06-30 12:50:15'),
(4,'http://localhost:3000/files/1719723034234.png','【2023】嘿嘿','','','2024-06-30 12:50:42'),
(5,'http://localhost:3000/files/1719723057974.png','【2024】欢声笑语','','','2024-06-30 12:51:07'),
(6,'http://localhost:3000/files/1719723084907.png','【2023】兄弟你好','','','2024-06-30 12:51:33'),
(7,'http://localhost:3000/files/1719723151657.png','【2023】笑一个','','','2024-06-30 12:52:42');

/*Table structure for table `og_user` */

DROP TABLE IF EXISTS `og_user`;

CREATE TABLE `og_user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `username` varchar(50) NOT NULL COMMENT '用户名',
  `password` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户密码',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_user` */

insert  into `og_user`(`id`,`username`,`password`,`create_time`,`update_time`) values 
(1,'OpenNLG','$2a$10$dfkkYv7owhc6jMF.4zbPAuv7ZgEqRBro7W8wOWaVGXaKXiHuQDr06','2023-10-30 14:51:50','2023-10-30 14:51:50');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
