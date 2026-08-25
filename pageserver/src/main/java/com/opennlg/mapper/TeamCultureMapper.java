package com.opennlg.mapper;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.pojo.TeamCulture;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;

/**
 * <p>
 * 团队文化 Mapper 接口
 * </p>
 *
 * @author Liuteng
 * @since 2024-06-29
 */
public interface TeamCultureMapper extends BaseMapper<TeamCulture> {

    Page<TeamCulture> selectListByPage(Page<TeamCulture> page);
}
