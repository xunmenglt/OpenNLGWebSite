-- Local member directory extension.
-- The legacy og_members.ct_type remains the primary category for compatibility.
-- Multi-category display memberships and grade data live in the two tables below.

ALTER TABLE `og_members`
    MODIFY COLUMN `en_name` VARCHAR(50) NULL COMMENT '英文名称';

CREATE TABLE IF NOT EXISTS `og_member_category_rel` (
    `member_category_id` INT NOT NULL AUTO_INCREMENT COMMENT '关系id',
    `member_id` INT NOT NULL COMMENT '成员id',
    `ct_type` VARCHAR(20) NOT NULL COMMENT '展示类别',
    `is_primary` TINYINT(1) NOT NULL DEFAULT 0 COMMENT '是否主类别',
    `is_visible` TINYINT(1) NOT NULL DEFAULT 1 COMMENT '是否公开展示',
    `serial_num` INT NOT NULL DEFAULT 0 COMMENT '类别内序号',
    `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `update_time` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`member_category_id`),
    UNIQUE KEY `uk_member_category` (`member_id`, `ct_type`),
    KEY `idx_member_category_display` (`ct_type`, `is_visible`, `serial_num`),
    CONSTRAINT `fk_member_category_member`
        FOREIGN KEY (`member_id`) REFERENCES `og_members` (`member_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='成员多类别展示关系';

CREATE TABLE IF NOT EXISTS `og_member_education` (
    `education_id` INT NOT NULL AUTO_INCREMENT COMMENT '教育信息id',
    `member_id` INT NOT NULL COMMENT '成员id',
    `degree_type` VARCHAR(20) NOT NULL COMMENT 'bachelor/master/phd',
    `cohort_year` SMALLINT NOT NULL COMMENT 'Excel登记年级，例如2025',
    `cohort_label` VARCHAR(32) NOT NULL COMMENT '原始年级文本，例如2025级直博',
    `program_type` VARCHAR(32) DEFAULT NULL COMMENT '直博/硕博连读/博士等',
    `graduation_destination` VARCHAR(550) DEFAULT NULL COMMENT '毕业去向，仅毕业生公开展示',
    `education_note` VARCHAR(550) DEFAULT NULL COMMENT '原始备注，不在公开页面展示',
    `source_name` VARCHAR(80) DEFAULT NULL COMMENT '数据来源文件',
    `source_row` INT DEFAULT NULL COMMENT '数据来源行号',
    `display_order` INT NOT NULL DEFAULT 0 COMMENT '同年级排序',
    `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `update_time` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`education_id`),
    UNIQUE KEY `uk_member_degree_cohort` (`member_id`, `degree_type`, `cohort_year`),
    KEY `idx_member_education_grade` (`degree_type`, `cohort_year`, `display_order`),
    CONSTRAINT `fk_member_education_member`
        FOREIGN KEY (`member_id`) REFERENCES `og_members` (`member_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='成员学历、年级与毕业去向';

-- Seed the relation table from the historical single-category column.
INSERT IGNORE INTO `og_member_category_rel` (`member_id`, `ct_type`, `is_primary`, `is_visible`, `serial_num`)
SELECT `member_id`, `ct_type`, 1, 1, `serial_num`
FROM `og_members`
WHERE `ct_type` IS NOT NULL AND `ct_type` <> '';
