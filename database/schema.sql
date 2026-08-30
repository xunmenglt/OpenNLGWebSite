-- OpenNLG public application schema (MySQL 8).
-- This file intentionally contains no personal directory data or login account.
SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS og_members (
  member_id INT NOT NULL AUTO_INCREMENT COMMENT '成员id',
  cn_name VARCHAR(50) NOT NULL COMMENT '中文名称',
  en_name VARCHAR(50) DEFAULT NULL COMMENT '英文名称',
  member_desc TEXT COMMENT '描述',
  profession VARCHAR(550) DEFAULT NULL COMMENT '职业',
  direction VARCHAR(550) DEFAULT NULL COMMENT '研究方向',
  email VARCHAR(100) DEFAULT NULL COMMENT '邮箱',
  serial_num INT NOT NULL DEFAULT 0 COMMENT '序号',
  avatar_url VARCHAR(550) DEFAULT NULL COMMENT '头像链接',
  outside_url VARCHAR(550) DEFAULT NULL COMMENT '外链',
  inside_url VARCHAR(550) DEFAULT NULL COMMENT '内链',
  create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  update_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  ct_type VARCHAR(20) DEFAULT NULL COMMENT '兼容旧版的主类别',
  PRIMARY KEY (member_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS og_members_category (
  ct_type VARCHAR(20) NOT NULL COMMENT '类别',
  ct_zh_name VARCHAR(50) DEFAULT NULL COMMENT '类别中文名称',
  sort INT DEFAULT 0 COMMENT '排序',
  PRIMARY KEY (ct_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='成员类别';

INSERT IGNORE INTO og_members_category (ct_type, ct_zh_name, sort) VALUES
  ('teacher', '教师', 1),
  ('phd', '博士生', 2),
  ('graduate_student', '硕士生', 3),
  ('graduate', '毕业生', 4);

CREATE TABLE IF NOT EXISTS og_member_category_rel (
  member_category_id INT NOT NULL AUTO_INCREMENT COMMENT '关系id',
  member_id INT NOT NULL COMMENT '成员id',
  ct_type VARCHAR(20) NOT NULL COMMENT '展示类别',
  is_primary TINYINT(1) NOT NULL DEFAULT 0 COMMENT '是否主类别',
  is_visible TINYINT(1) NOT NULL DEFAULT 1 COMMENT '是否公开展示',
  serial_num INT NOT NULL DEFAULT 0 COMMENT '类别内序号',
  create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (member_category_id),
  UNIQUE KEY uk_member_category (member_id, ct_type),
  KEY idx_member_category_display (ct_type, is_visible, serial_num),
  CONSTRAINT fk_member_category_member FOREIGN KEY (member_id)
    REFERENCES og_members (member_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='成员多类别展示关系';

CREATE TABLE IF NOT EXISTS og_member_education (
  education_id INT NOT NULL AUTO_INCREMENT COMMENT '教育信息id',
  member_id INT NOT NULL COMMENT '成员id',
  degree_type VARCHAR(20) NOT NULL COMMENT 'bachelor/master/phd',
  cohort_year SMALLINT NOT NULL COMMENT '登记年级',
  cohort_label VARCHAR(32) NOT NULL COMMENT '原始年级标签',
  program_type VARCHAR(32) DEFAULT NULL COMMENT '培养类型',
  graduation_destination VARCHAR(550) DEFAULT NULL COMMENT '毕业去向',
  education_note VARCHAR(550) DEFAULT NULL COMMENT '内部备注',
  source_name VARCHAR(80) DEFAULT NULL COMMENT '来源文件',
  source_row INT DEFAULT NULL COMMENT '来源行号',
  display_order INT NOT NULL DEFAULT 0 COMMENT '同年级排序',
  create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (education_id),
  UNIQUE KEY uk_member_degree_cohort (member_id, degree_type, cohort_year),
  KEY idx_member_education_grade (degree_type, cohort_year, display_order),
  CONSTRAINT fk_member_education_member FOREIGN KEY (member_id)
    REFERENCES og_members (member_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='成员学历、年级与毕业去向';

CREATE TABLE IF NOT EXISTS og_reserarch (
  reserarch_id INT NOT NULL AUTO_INCREMENT COMMENT '论文id',
  reserarch_title VARCHAR(550) NOT NULL,
  reserarch_source VARCHAR(550) DEFAULT NULL,
  reserarch_author VARCHAR(550) NOT NULL,
  publication_year INT DEFAULT NULL,
  publication_type VARCHAR(32) DEFAULT NULL,
  research_direction VARCHAR(128) DEFAULT NULL,
  venue_short_name VARCHAR(64) DEFAULT NULL,
  pdf_url VARCHAR(512) DEFAULT NULL,
  doi_url VARCHAR(512) DEFAULT NULL,
  code_url VARCHAR(512) DEFAULT NULL,
  project_url VARCHAR(512) DEFAULT NULL,
  reserarch_cover VARCHAR(550) DEFAULT NULL,
  is_new INT DEFAULT 1,
  outside_url VARCHAR(550) DEFAULT NULL,
  inside_url VARCHAR(550) DEFAULT NULL,
  create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (reserarch_id),
  KEY idx_reserarch_year_type (publication_year, publication_type),
  KEY idx_reserarch_direction (research_direction),
  KEY idx_reserarch_year_type_venue (publication_year, publication_type, venue_short_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS og_news (
  news_id INT NOT NULL AUTO_INCREMENT,
  news_title VARCHAR(250) NOT NULL,
  news_summary VARCHAR(550) NOT NULL,
  news_read_times INT NOT NULL DEFAULT 0,
  outside_url VARCHAR(550) DEFAULT NULL,
  inside_url VARCHAR(550) DEFAULT NULL,
  create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  is_new INT DEFAULT 0,
  PRIMARY KEY (news_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS og_team_culture (
  id INT NOT NULL AUTO_INCREMENT,
  image VARCHAR(550) DEFAULT NULL,
  title VARCHAR(550) DEFAULT NULL,
  outside_url VARCHAR(550) DEFAULT NULL,
  inside_url VARCHAR(550) DEFAULT NULL,
  create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS og_article (
  id INT NOT NULL AUTO_INCREMENT,
  article_id VARCHAR(20) NOT NULL,
  article_title VARCHAR(250) NOT NULL,
  article_summary VARCHAR(550) DEFAULT NULL,
  article_content MEDIUMTEXT,
  article_read_times INT NOT NULL DEFAULT 0,
  create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS og_publication (
  publication_id INT NOT NULL AUTO_INCREMENT,
  publication_title VARCHAR(200) NOT NULL,
  publication_desc VARCHAR(550) NOT NULL,
  publication_cover VARCHAR(550) DEFAULT NULL,
  outside_url VARCHAR(550) DEFAULT NULL,
  inside_url VARCHAR(550) DEFAULT NULL,
  create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (publication_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS og_user (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(100) NOT NULL,
  create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uk_user_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
