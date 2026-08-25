package com.opennlg.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.pojo.Members;
import com.opennlg.mapper.MembersMapper;
import com.opennlg.pojo.MembersCategory;
import com.opennlg.service.IMembersService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.opennlg.vo.RespBean;
import com.opennlg.vo.RespPageBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.ObjectUtils;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author Liuteng
 * @since 2023-11-02
 */
@Service
public class MembersServiceImpl extends ServiceImpl<MembersMapper, Members> implements IMembersService {
    @Autowired
    private MembersMapper membersMapper;

    @Override
    public RespBean createMembers(Members members) {

        if (ObjectUtils.isEmpty(members.getCnName())){
            return RespBean.fail("中文名称不能为空");
        }
        if(ObjectUtils.isEmpty(members.getEnName())){
            return RespBean.fail("英文名称不能为空");
        }
        if(ObjectUtils.isEmpty(members.getAvatarUrl())){
            return RespBean.fail("头像不能为空");
        }
        if(ObjectUtils.isEmpty(members.getMemberDesc())){
            return RespBean.fail("描述不能为空");
        }

        try {
            int c = membersMapper.insert(members);
            if (c>0){
                return RespBean.success("创建成功");
            }else {
                return RespBean.fail("创建失败，请重试");
            }
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
    }

    @Override
    public RespBean deleteMembers(Integer id) {
        try {
            boolean flag=removeById(id);
            if (flag){
                return RespBean.success("删除成功");
            }else {
                return RespBean.fail("删除失败，请重试");
            }
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
    }


    @Override
    public RespBean updateMembers(Members members) {
        members.setUpdateTime(LocalDateTime.now());
        try {
            boolean flag=updateById(members);
            if (flag){
                return RespBean.success("修改成功");
            }else {
                return RespBean.fail("修改失败，请重试");
            }
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
    }

    @Override
    public RespBean getMembersList() {
        List<Members> membersList=null;
        try {
            membersList=membersMapper.selectList(new QueryWrapper<Members>().orderByAsc("serial_num"));
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
        return RespBean.success("SUCCESS",membersList);
    }

    @Override
    public RespBean getCoverMembersList() {
        List<MembersCategory> membersCategoryList=new ArrayList<>();
        try {
            membersCategoryList=membersMapper.selectMembersList();
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
        return RespBean.success("SUCCESS",membersCategoryList);
    }
    
    @Override
    public RespBean getMembers(Integer membersId) {
        Members members=getById(membersId);
        return RespBean.success("SUCCESS",members);
    }


}
