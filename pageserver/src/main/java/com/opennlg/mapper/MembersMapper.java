package com.opennlg.mapper;

import com.opennlg.pojo.Members;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.opennlg.pojo.MembersCategory;

import java.util.List;

/**
 * <p>
 *  Mapper 接口
 * </p>
 *
 * @author Liuteng
 * @since 2023-11-02
 */
public interface MembersMapper extends BaseMapper<Members> {

    List<MembersCategory> selectMembersList();
    
}
