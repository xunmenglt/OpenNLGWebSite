-- Run this migration once after backing up the production database.
-- Existing publication rows remain valid; every new field is nullable.
ALTER TABLE `og_reserarch`
    ADD COLUMN `publication_year` INT NULL COMMENT '正式发表年份' AFTER `reserarch_author`,
    ADD COLUMN `publication_type` VARCHAR(32) NULL COMMENT 'conference/journal/preprint/book' AFTER `publication_year`,
    ADD COLUMN `research_direction` VARCHAR(128) NULL COMMENT '研究方向' AFTER `publication_type`,
    ADD COLUMN `venue_short_name` VARCHAR(64) NULL COMMENT '会议或期刊简称' AFTER `research_direction`,
    ADD COLUMN `pdf_url` VARCHAR(512) NULL COMMENT 'PDF链接' AFTER `venue_short_name`,
    ADD COLUMN `doi_url` VARCHAR(512) NULL COMMENT 'DOI链接' AFTER `pdf_url`,
    ADD COLUMN `code_url` VARCHAR(512) NULL COMMENT '代码链接' AFTER `doi_url`,
    ADD COLUMN `project_url` VARCHAR(512) NULL COMMENT '项目链接' AFTER `code_url`,
    ADD INDEX `idx_reserarch_year_type` (`publication_year`, `publication_type`),
    ADD INDEX `idx_reserarch_direction` (`research_direction`);
