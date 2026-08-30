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
import org.springframework.transaction.annotation.Transactional;

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
    @Transactional(rollbackFor = Exception.class)
    public RespBean createMembers(Members members) {

        if (ObjectUtils.isEmpty(members.getCnName())){
            return RespBean.fail("中文名称不能为空");
        }
        if (ObjectUtils.isEmpty(members.getCtType())) {
            return RespBean.fail("展示类别不能为空");
        }
        try {
            int c = membersMapper.insert(members);
            if (c>0){
                synchronizeDirectoryData(members);
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
    @Transactional(rollbackFor = Exception.class)
    public RespBean updateMembers(Members members) {
        members.setUpdateTime(LocalDateTime.now());
        if (ObjectUtils.isEmpty(members.getCtType())) {
            return RespBean.fail("展示类别不能为空");
        }
        try {
            boolean flag=updateById(members);
            if (flag){
                synchronizeDirectoryData(members);
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
        Members members=membersMapper.selectMemberAdminItem(membersId);
        return RespBean.success("SUCCESS",members);
    }

    private void synchronizeDirectoryData(Members members) {
        Integer memberId = members.getMemberId();
        membersMapper.hideMemberRelations(memberId);
        membersMapper.upsertPrimaryMemberRelation(memberId, members.getCtType(), members.getSerialNum());

        if (members.getCohortYear() == null) {
            return;
        }
        String degreeType = normalizeDegreeType(members);
        String cohortLabel = members.getCohortLabel();
        if (ObjectUtils.isEmpty(cohortLabel)) {
            cohortLabel = members.getCohortYear() + "级" +
                    (ObjectUtils.isEmpty(members.getProgramType()) ? "" : members.getProgramType());
        }
        membersMapper.deleteMemberEducation(memberId, degreeType);
        membersMapper.insertMemberEducation(memberId, degreeType, members.getCohortYear(),
                cohortLabel, members.getProgramType(), members.getGraduationDestination(),
                members.getSerialNum());
    }

    private String normalizeDegreeType(Members members) {
        if (!ObjectUtils.isEmpty(members.getDegreeType())) {
            return members.getDegreeType();
        }
        if ("phd".equals(members.getCtType())) {
            return "phd";
        }
        if ("graduate_student".equals(members.getCtType())) {
            return "master";
        }
        return "master";
    }


}
