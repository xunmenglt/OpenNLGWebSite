package com.opennlg.service.impl;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.pojo.Reserarch;
import com.opennlg.mapper.ReserarchMapper;
import com.opennlg.service.IReserarchService;
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
public class ReserarchServiceImpl extends ServiceImpl<ReserarchMapper, Reserarch> implements IReserarchService {
    @Autowired
    private ReserarchMapper reserarchMapper;

    @Override
    public RespBean createReserarch(Reserarch reserarch) {
        if (ObjectUtils.isEmpty(reserarch.getReserarchTitle())){
            return RespBean.fail("标题不能为空");
        }
        if(ObjectUtils.isEmpty(reserarch.getReserarchSource())){
            return RespBean.fail("来源不能为空");
        }
        if(ObjectUtils.isEmpty(reserarch.getReserarchAuthor())){
            return RespBean.fail("作者不能为空");
        }
        try {
            int c = reserarchMapper.insert(reserarch);
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
    public RespBean deleteReserarch(Integer id) {
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
    public RespBean updateReserarch(Reserarch reserarch) {
        reserarch.setUpdateTime(LocalDateTime.now());
        try {
            boolean flag=updateById(reserarch);
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
    public RespBean getReserarchList(Integer currentPage, Integer size) {
        Page<Reserarch> page=new Page<>(currentPage,size);
        Page<Reserarch> reserarchPage=null;
        try {
            reserarchPage=reserarchMapper.selectListByPage(page);
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
        RespPageBean pageBean=RespPageBean.tranPageBeanByPageObject(reserarchPage);
        return RespBean.success("SUCCESS",pageBean);
    }

    @Override
    public RespBean getReserarch(Integer reserarchId) {
        Reserarch reserarch=getById(reserarchId);
        return RespBean.success("SUCCESS",reserarch);
    }
}
