package com.opennlg.service;

import com.opennlg.pojo.Members;
import com.baomidou.mybatisplus.extension.service.IService;
import com.opennlg.vo.RespBean;

/**
 * <p>
 *  服务类
 * </p>
 *
 * @author Liuteng
 * @since 2023-11-02
 */
public interface IMembersService extends IService<Members> {

    RespBean createMembers(Members members);

    RespBean deleteMembers(Integer id);

    RespBean updateMembers(Members members);

    RespBean getMembersList();

    RespBean getMembers(Integer membersId);

    RespBean getCoverMembersList();
    
}
