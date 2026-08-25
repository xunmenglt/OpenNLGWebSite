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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_article` */

insert  into `og_article`(`id`,`article_id`,`article_title`,`article_summary`,`article_content`,`article_read_times`,`create_time`,`update_time`) values 
(4,'article_680860228679','文章1',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:05:05','2023-11-01 19:05:05'),
(5,'article_313078533470','文章2',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:05:09','2023-11-01 19:05:09'),
(6,'article_389330582109','文章3',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:05:13','2023-11-01 19:05:13'),
(7,'article_435176689297','文章4',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:05:17','2023-11-01 19:05:17'),
(14,'article_380661555592','文章5',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:09:27','2023-11-01 19:09:27'),
(15,'article_092919708452','文章6',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:09:30','2023-11-01 19:09:30'),
(16,'article_528842334260','文章7',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:09:33','2023-11-01 19:09:33'),
(17,'article_004658183711','文章8',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:09:36','2023-11-01 19:09:36'),
(18,'article_428913555714','文章9',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:09:39','2023-11-01 19:09:39'),
(19,'article_634399596631','文章10',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:09:42','2023-11-01 19:09:42'),
(21,'article_504597038004','文章12',NULL,'# 一、登录OpenBA控制台',15,'2023-11-01 19:09:49','2023-11-01 19:09:49'),
(23,'article_356330502714','文章12',NULL,'# 一、登录OpenBA控制台',0,'2023-11-01 19:39:09','2023-11-01 19:39:09'),
(24,'article_279029958332','重大消息，BUSINC正式上线',NULL,'::: hljs-center\n\n<div align=\"center\"><img src=\"http://localhost:3000/files/clip_image002.png\"></div>\n\n:::\n\n<h1 align=\"center\" style=\"margin: 30px 0 30px; font-weight: bold;\">Buinc v3.8.3</h1>\n<h4 align=\"center\">基于SpringMVC/SpringBoot的后台管理系统开发模板</h4>\n\n\n## 前言\n\n​         近年来，随着计算机技术的发展和互联网时代的到来，我们已经进入了信息时代，也有人称为数字化时代，在这数字化的时代里，大学生创业孵化基地的办公管理都受到了极大的挑战。Internet 技术持续迅猛的发展，也给传统的商业办公提出了新的模式。通过设计和建设网络拓扑架构、网络安全系统、数据库基础结构、信息共享与管理、信息的发布与管理，从而方便管理者、企业、老师和学生间信息发布、信息交流和信息共享。以现代计算技术、网络技术为基础的数字化教学主要是朝着信息化、网络化、现代化的目标迈进。作为新型的办公模式，它们具有对于工作、办公方式来说极为宝贵的特性，可以为新型办公模式的建构提供理想的环境。在此开发的创业孵化基地信息系统，旨在探索一种以互联网为基础的办公模式。通过这种新的模式，为大学生创业孵化基地的营造一种新的办公环境，使管理突破时空限制，提高工作效率，使管理者、企业、教师和学生可以在任何时候、任何地点通过网络进行办公交流。\n\n \n\n##  一、  技术介绍\n\n**服务端**：\n\n​     SpringMVC/SpringBoot、SpringSecurity、Websocket、MyBatis、Redis、RabbitMq等\n\n**客户端**：\n\n​     Vue、Vuex、Element-ui、Axios、Router、Sass等\n\n**数据库**：MySQL8.0\n\n## 二、  项目部署\n\n* **本教程只介绍本地允许部署**\n\n* **git地址**：https://gitee.com/xunmenglt/businc\n\n* **在线访问地址**：https://businc.xunmeng.icu\n\n* **测试账号：xunmeng 密码：123456**\n\n* **个人博客地址**：https://blog.csdn.net/m0_54349490\n\n### （一）   数据库部署\n\n​         本系统采用mysql8.0数据进行数据存储，向数据库中导入提供的数据：db.sql文件\n\n### （二）   服务端部署\n\n​         本项目采用SpringMvc、SpringBoot两种框架，下面介绍SpringMVC运行方式，为了方便部署和运行，本项目将tomcat内嵌至项目中，只需要允许 **BusincApplication.java** 中的主类即可允许本项目，无需考虑tomcat版本和部署配置问题，像SpringBoot一样一键启动。\n\n​         当然本项目采用SpringBoot框架设计思想，将**applocation.yml**文件设为本项目的配置文件，用户需要在该配置文件中修改相应的配置，如：MySql数据库配置、rabbitMq配置、Redis配置、WebScoket配置等。\n\n### （三）   客户端部署\n\n​          前端采用Vue2框架进行开发，只需要到客户端程序目录下用cmd命令行工具运行以下命令：\n\n```sh\nnpm install\nnpm run serve\n```\n\n​         最后访问：http://localhost/ 网址即可。\n\n\n\n## 三、  结语\n\n​         以上系统介绍中只是介绍了大概的系统功能，然而还有许多交互功能并未体现，因此当运行本项目后可以仔细体验。\n\n​         希望能帮助您，也希望您能为本系统提供宝贵的意见发送至邮箱: 3339372755@qq.com。\n\n​         同时感谢 **RuoYi框架** 提供的架构思路构想，致敬！',161,'2023-11-01 19:39:15','2023-11-01 21:28:28'),
(25,'article_220447159881','OpenBA：打开人工智能语言处理的新篇章',NULL,'随着人工智能技术的不断发展，自然语言处理领域也越来越受到关注。在众多的自然语言处理工具中，OpenBA（Open Source BA）模型脱颖而出，以其强大的处理能力和高效的应用场景，成为了人工智能领域的一匹黑马。\n\nOpenBA模型是由苏州大学的一个研发团队推出的开源seq2seq模型。它拥有150亿参数，是当前中国开源模型社区中最大的语言模型变体。与其他seq2seq模型相比，OpenBA模型具有更强的泛化能力和更高的性能表现。\n\n在自然语言处理任务中，OpenBA模型表现出了极高的性能。无论是文本分类、情感分析、机器翻译等任务，OpenBA都能够取得优异的成绩。同时，OpenBA模型还支持多种语言，可以为跨语言应用提供强大的支持。\n\nOpenBA模型的出现，不仅推动了人工智能领域的发展，也为人们的生活带来了更多的便利。它可以应用于智能客服、智能推荐、智能问答等场景中，帮助人们更快速地获取所需信息，提高工作效率和生活品质。\n\n总的来说，OpenBA模型是一款强大的人工智能语言处理工具，具有广泛的应用前景和重要的价值。它的出现，为人工智能领域注入了新的活力，也为人们的生活带来了更多的可能性。相信在不久的将来，OpenBA模型将会在更多的领域得到应用和发展。',9,'2023-11-01 19:51:57','2023-11-01 19:51:57');

/*Table structure for table `og_members` */

DROP TABLE IF EXISTS `og_members`;

CREATE TABLE `og_members` (
  `member_id` int NOT NULL AUTO_INCREMENT COMMENT '成员id',
  `cn_name` varchar(50) NOT NULL COMMENT '中文名称',
  `en_name` varchar(50) NOT NULL COMMENT '英文名称',
  `member_desc` varchar(550) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '描述',
  `serial_num` int NOT NULL DEFAULT '0' COMMENT '序号',
  `avatar_url` varchar(550) DEFAULT NULL COMMENT '头像链接',
  `outside_url` varchar(550) DEFAULT NULL COMMENT '外链',
  `inside_url` varchar(550) DEFAULT NULL COMMENT '内链',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_members` */

insert  into `og_members`(`member_id`,`cn_name`,`en_name`,`member_desc`,`serial_num`,`avatar_url`,`outside_url`,`inside_url`,`create_time`,`update_time`) values 
(1,'张三','Zhang San','张三是一个优秀的软件工程师，他在编程方面有着丰富的经验。',17,'http://localhost:3000/files/1698917995260.png',NULL,'/article/view?id=article_279029958332','2023-11-02 10:22:20','2023-11-02 18:58:45'),
(2,'李四','Li Si','李四是一个热心的志愿者，他经常参与各种公益活动。',2,'http://localhost:3000/files/1698918058239.png',NULL,NULL,'2023-11-02 10:22:28','2023-11-02 17:41:07'),
(3,'王五','Wang Wu','王五是一个有着广泛兴趣爱好的人，他喜欢旅行和摄影。',3,'http://eb118-file.cdn.bcebos.com/upload/a1d3caa52a574ea990c4d324203521bc_1500036511?x-bce-process=style/wm_ai',NULL,NULL,'2023-11-02 10:22:33','2023-11-02 10:22:33'),
(4,'赵六','Zhao Liu','赵六是一个勤奋的学生，他总是努力学习和提高自己的成绩。',5,'http://eb118-file.cdn.bcebos.com/upload/a1d3caa52a574ea990c4d324203521bc_1500036511?x-bce-process=style/wm_ai',NULL,NULL,'2023-11-02 10:22:40','2023-11-02 10:22:40'),
(5,'孙七','Sun Qi','孙七是一个有创意的设计师，他擅长设计各种独特的图案和造型。',4,'http://eb118-file.cdn.bcebos.com/upload/949a50c7dead43ae84d8b6aae1e0abd0_1012818125?x-bce-process=style/wm_ai',NULL,NULL,'2023-11-02 10:22:45','2023-11-02 10:22:45'),
(6,'周八','Zhou Ba','周八是一个热爱运动的年轻人，他经常参加各种体育活动。',13,'http://eb118-file.cdn.bcebos.com/upload/949a50c7dead43ae84d8b6aae1e0abd0_1012818125?x-bce-process=style/wm_ai','https://example.com/avatar8.jpg',NULL,'2023-11-02 10:22:51','2023-11-02 15:36:22'),
(7,'吴九','Wu Jiu','吴九是一个有才华的音乐家，他擅长演奏各种乐器。',6,'http://eb118-file.cdn.bcebos.com/upload/949a50c7dead43ae84d8b6aae1e0abd0_1012818125?x-bce-process=style/wm_ai',NULL,NULL,'2023-11-02 10:22:56','2023-11-02 10:22:56'),
(12,'陈十','Chen Shi','陈十是一个热情洋溢的导游，他总是尽力让游客感到满意。',16,'http://eb118-file.cdn.bcebos.com/upload/a1d3caa52a574ea990c4d324203521bc_1500036511?x-bce-process=style/wm_ai','','https://example.com/avatar8.jpg','2023-11-02 15:17:18','2023-11-02 15:36:46');

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
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_news` */

insert  into `og_news`(`news_id`,`news_title`,`news_summary`,`news_read_times`,`outside_url`,`inside_url`,`create_time`,`update_time`) values 
(2,'标题3','内容3',0,NULL,NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(3,'标题4','内容4',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(4,'标题5','内容5',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(5,'标题6','内容6',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(6,'标题7','内容7',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(7,'标题8','内容8',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(8,'标题9','内容9',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(9,'标题10','内容10',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(10,'标题11','内容11',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(11,'标题12','内容12',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(12,'标题13','内容13',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(13,'标题14','内容14',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(14,'标题15','内容15',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(15,'标题16','内容16',0,'https://blog.csdn.net/it_xushixiong/article/details/131183140',NULL,'2023-10-31 19:13:58','2023-10-31 19:13:58'),
(16,'OpenBA数据开源：助力数据科学家、研究者和创新者的新机遇','OpenBA是一家专注于大数据分析和商业智能的公司，积累了大量的经济、社会、环境等领域的数据。通过开源这些数据，OpenBA旨在鼓励更多的人参与数据科学和研究，以共同解决当今社会和商业领域的重大挑战。',0,'https://www.csdn.net/','https://www.baidu.net/','2023-10-31 19:14:05','2023-11-01 10:25:09'),
(18,'苏州大学研发团队推出OpenBA：150亿参数双非seq2seq模型','苏州大学的一个研发团队近日推出了一款名为OpenBA的开源seq2seq模型，该模型具有150亿参数，是首个加入中国开源模型社区的大语言模型变体。',0,'http://localhost:8080','/artical/1','2023-11-01 10:28:03','2023-11-01 10:28:03'),
(19,'OpenBA：打破语言障碍的强大工具','OpenBA的独特之处在于其采用了高效的技术和三阶段的训练策略，从头开始训练了这款模型。实验显示，OpenBA在多种语言任务中表现出色，为跨语言应用提供了强大的支持。',0,'','','2023-11-01 10:28:28','2023-11-01 10:28:28'),
(20,'OpenBA：推动人工智能领域的发展','OpenBA的推出，不仅提升了中国在全球人工智能领域的影响力，也为推动人工智能领域的发展提供了强大的支持。这款模型的出现，让人们看到了人工智能技术在未来的更多可能性。',0,'','','2023-11-01 10:28:53','2023-11-01 10:28:53'),
(21,'苏州大学团队研发的OpenBA模型：带来全新的AI体验','OpenBA模型的推出，为人工智能领域带来了全新的体验。该模型在处理复杂语言任务方面表现出色，让人们对人工智能技术的未来充满了期待。',0,'','','2023-11-01 10:29:12','2023-11-01 10:29:12'),
(22,'OpenBA：引领AI技术新潮流','OpenBA的出现，引领了AI技术的新潮流。这款模型在处理自然语言处理任务方面表现出了极高的性能，让人们对人工智能技术的未来充满了信心。',0,'','','2023-11-01 10:29:23','2023-11-01 10:29:23'),
(23,'苏州大学团队：OpenBA模型实现AI技术的新突破','苏州大学的一个研发团队通过OpenBA模型实现了AI技术的新突破。这款模型具有150亿参数，能够在多种语言任务中表现出色，为人工智能技术的发展带来了新的希望。',0,'','','2023-11-01 10:29:33','2023-11-01 10:29:33'),
(24,'OpenBA：开启AI新时代','OpenBA的推出，标志着AI新时代的开启。这款模型具有强大的处理能力，能够在自然语言处理、机器翻译等多个领域表现出色，为人工智能技术的发展带来了新的动力。',0,'','','2023-11-01 10:29:44','2023-11-01 10:29:44'),
(25,'苏州大学团队：OpenBA模型提升AI技术的国际竞争力','苏州大学的一个研发团队通过OpenBA模型的研发，提升了AI技术的国际竞争力。这款模型具有150亿参数，能够在多种语言任务中表现出色，为人工智能技术的发展注入了新的活力。',0,'','','2023-11-01 10:29:54','2023-11-01 10:29:54'),
(26,'OpenBA：推动AI技术的普及和应用','OpenBA的出现，为AI技术的普及和应用提供了强大的支持。这款模型具有150亿参数，能够在自然语言处理、机器翻译等多个领域表现出色，为人工智能技术的普及和应用提供了强有力的工具。',0,'','','2023-11-01 10:30:04','2023-11-01 10:30:04'),
(27,'OpenBA：引领AI技术未来发展方向','OpenBA的出现，引领了AI技术未来发展的方向。这款模型具有强大的处理能力，能够在多种语言任务中表现出色，为人工智能技术的发展指明了新的方向。',0,'aaaa','','2023-11-01 10:30:13','2023-11-01 10:40:52');

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

insert  into `og_publication`(`publication_id`,`publication_title`,`publication_desc`,`publication_cover`,`outside_url`,`inside_url`,`create_time`,`update_time`) values 
(1,'java代码','这是一份很好的代码','http://localhost:3000/files/1698937659795.png','url','todo','2023-11-02 23:08:02','2023-11-02 23:08:02'),
(2,'物理实验','这是一份很好的物理实验','http://localhost:3000/files/1698937870775.png','abbd','cbds','2023-11-02 23:10:34','2023-11-02 23:11:13');

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
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;

/*Data for the table `og_reserarch` */

insert  into `og_reserarch`(`reserarch_id`,`reserarch_title`,`reserarch_source`,`reserarch_author`,`reserarch_cover`,`is_new`,`outside_url`,`inside_url`,`create_time`,`update_time`) values 
(1,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:35','2023-11-02 21:36:35'),
(2,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:36','2023-11-02 21:36:36'),
(3,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:37','2023-11-02 21:36:37'),
(4,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:37','2023-11-02 21:36:37'),
(5,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:37','2023-11-02 21:36:37'),
(6,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:37','2023-11-02 21:36:37'),
(7,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:37','2023-11-02 21:36:37'),
(8,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:38','2023-11-02 21:36:38'),
(9,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:38','2023-11-02 21:36:38'),
(10,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:38','2023-11-02 21:36:38'),
(11,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:38','2023-11-02 21:36:38'),
(12,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:39','2023-11-02 21:36:39'),
(13,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:39','2023-11-02 21:36:39'),
(14,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:39','2023-11-02 21:36:39'),
(15,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:39','2023-11-02 21:36:39'),
(16,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:39','2023-11-02 21:36:39'),
(17,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:40','2023-11-02 21:36:40'),
(18,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:40','2023-11-02 21:36:40'),
(19,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:40','2023-11-02 21:36:40'),
(20,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:40','2023-11-02 21:36:40'),
(21,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:40','2023-11-02 21:36:40'),
(22,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:41','2023-11-02 21:36:41'),
(23,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:41','2023-11-02 21:36:41'),
(24,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:41','2023-11-02 21:36:41'),
(25,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:41','2023-11-02 21:36:41'),
(26,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:41','2023-11-02 21:36:41'),
(27,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','https://vcc-szu.s3.ap-southeast-1.amazonaws.com/1695111436587.jpg',1,NULL,NULL,'2023-11-02 21:36:42','2023-11-02 21:36:42'),
(29,'TwinTex: Geometry-aware Texture Generation for Abstracted 3D Architectural Models','ACM Transactions on Graphics (Proceedings of SIGGRAPH ASIA 2023)','Weidan Xiong, Hongqian Zhang, Botao Peng, Ziyu Hu, Yongli Wu, Jianwei Guo, Hui Huang*','http://localhost:3000/files/1698936843248.png',0,NULL,NULL,'2023-11-02 21:36:42','2023-11-02 22:54:10'),
(31,'标题1','来源1','作者1','http://localhost:3000/files/1698936193858.png',0,'a','b','2023-11-02 22:43:49','2023-11-02 22:43:49');

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
