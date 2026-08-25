package com.opennlg.service.impl;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.pojo.News;
import com.opennlg.mapper.NewsMapper;
import com.opennlg.service.INewsService;
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
 * @since 2023-10-31
 */
@Service
public class NewsServiceImpl extends ServiceImpl<NewsMapper, News> implements INewsService {

    @Autowired
    private NewsMapper newsMapper;

    @Override
    public RespBean createNews(News news) {
        if (ObjectUtils.isEmpty(news.getNewsTitle())){
            return RespBean.fail("新闻标题不能为空");
        }
        if(ObjectUtils.isEmpty(news.getNewsSummary())){
            return RespBean.fail("新闻概要不能为空");
        }
        try {
            int c = newsMapper.insert(news);
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
    public RespBean deleteNews(Integer id) {
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
    public RespBean updateNews(News news) {
        news.setUpdateTime(LocalDateTime.now());
        try {
            boolean flag=updateById(news);
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
    public RespBean getNewsList(Integer currentPage, Integer size) {
        Page<News> page=new Page<>(currentPage,size);
        Page<News> newsPage=null;
        try {
            newsPage=newsMapper.selectListByPage(page);
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
        RespPageBean pageBean=RespPageBean.tranPageBeanByPageObject(newsPage);
        return RespBean.success("SUCCESS",pageBean);
    }

    @Override
    public RespBean getNews(Integer newsId) {
        News news=getById(newsId);
        return RespBean.success("SUCCESS",news);
    }

}
