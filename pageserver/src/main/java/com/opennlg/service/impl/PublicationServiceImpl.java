package com.opennlg.service.impl;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.pojo.Publication;
import com.opennlg.mapper.PublicationMapper;
import com.opennlg.service.IPublicationService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.opennlg.vo.RespBean;
import com.opennlg.vo.RespPageBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.ObjectUtils;

import java.time.LocalDateTime;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author Liuteng
 * @since 2023-11-02
 */
@Service
public class PublicationServiceImpl extends ServiceImpl<PublicationMapper, Publication> implements IPublicationService {
    @Autowired
    private PublicationMapper publicationMapper;

    @Override
    public RespBean createPublication(Publication publication) {
        if (ObjectUtils.isEmpty(publication.getPublicationTitle())){
            return RespBean.fail("项目标题不能为空");
        }
        if(ObjectUtils.isEmpty(publication.getPublicationDesc())){
            return RespBean.fail("项目概要不能为空");
        }
        try {
            int c = publicationMapper.insert(publication);
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
    public RespBean deletePublication(Integer id) {
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
    public RespBean updatePublication(Publication publication) {
        publication.setUpdateTime(LocalDateTime.now());
        try {
            boolean flag=updateById(publication);
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
    public RespBean getPublicationList(Integer currentPage, Integer size) {
        Page<Publication> page=new Page<>(currentPage,size);
        Page<Publication> publicationPage=null;
        try {
            publicationPage=publicationMapper.selectListByPage(page);
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
        RespPageBean pageBean=RespPageBean.tranPageBeanByPageObject(publicationPage);
        return RespBean.success("SUCCESS",pageBean);
    }

    @Override
    public RespBean getPublication(Integer publicationId) {
        Publication publication=getById(publicationId);
        return RespBean.success("SUCCESS",publication);
    }
}
