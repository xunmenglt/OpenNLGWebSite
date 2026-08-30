-- Apply after V3_1__extend_publication_library.sql.
-- Supports the public publication catalogue's year/type/venue filtering.
ALTER TABLE `og_reserarch`
    ADD INDEX `idx_reserarch_year_type_venue` (`publication_year`, `publication_type`, `venue_short_name`);
