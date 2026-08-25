package com.opennlg.mapper;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.pojo.Reserarch;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;

/**
 * <p>
 *  Mapper 接口
 * </p>
 *
 * @author Liuteng
 * @since 2023-11-02
 */
public interface ReserarchMapper extends BaseMapper<Reserarch> {

    Page<Reserarch> selectListByPage(Page<Reserarch> page);
}
