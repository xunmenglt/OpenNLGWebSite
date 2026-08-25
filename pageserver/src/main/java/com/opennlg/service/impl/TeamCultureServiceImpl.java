package com.opennlg.service.impl;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.mapper.TeamCultureMapper;
import com.opennlg.pojo.TeamCulture;
import com.opennlg.service.ITeamCultureService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.opennlg.vo.RespBean;
import com.opennlg.vo.RespPageBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.ObjectUtils;

import java.time.LocalDateTime;

/**
 * <p>
 * 团队文化 服务实现类
 * </p>
 *
 * @author Liuteng
 * @since 2024-06-29
 */
@Service
public class TeamCultureServiceImpl extends ServiceImpl<TeamCultureMapper, TeamCulture> implements ITeamCultureService {
    @Autowired
    private TeamCultureMapper teamCultureMapper;

    @Override
    public RespBean createTeamCulture(TeamCulture teamCulture) {
        if (ObjectUtils.isEmpty(teamCulture.getTitle())){
            return RespBean.fail("标题不能为空");
        }
        if(ObjectUtils.isEmpty(teamCulture.getImage())){
            return RespBean.fail("图片不能为空");
        }
        try {
            int c = teamCultureMapper.insert(teamCulture);
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
    public RespBean deleteTeamCulture(Integer id) {
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
    public RespBean updateTeamCulture(TeamCulture teamCulture) {
        try {
            boolean flag=updateById(teamCulture);
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
    public RespBean getTeamCultureList(Integer currentPage, Integer size) {
        Page<TeamCulture> page=new Page<>(currentPage,size);
        Page<TeamCulture> teamCulturePage=null;
        try {
            teamCulturePage=teamCultureMapper.selectListByPage(page);
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
        RespPageBean pageBean=RespPageBean.tranPageBeanByPageObject(teamCulturePage);
        return RespBean.success("SUCCESS",pageBean);
    }

    @Override
    public RespBean getTeamCulture(Integer teamCultureId) {
        TeamCulture teamCulture=getById(teamCultureId);
        return RespBean.success("SUCCESS",teamCulture);
    }
}
