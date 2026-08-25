package com.opennlg.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.conditions.update.UpdateWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.pojo.Article;
import com.opennlg.mapper.ArticleMapper;
import com.opennlg.service.IArticleService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.opennlg.utils.Uni2IdUtil;
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
public class ArticleServiceImpl extends ServiceImpl<ArticleMapper, Article> implements IArticleService {

    @Autowired
    private ArticleMapper articleMapper;

    @Override
    public RespBean createArticle(Article article) {
        if (ObjectUtils.isEmpty(article.getArticleTitle())){
            return RespBean.fail("文章标题不能为空");
        }
        article.setArticleId(Uni2IdUtil.createArticleId());
        try {
            int c = articleMapper.insert(article);
            if (c>0){
                return RespBean.success("创建成功",article.getArticleId());
            }else {
                return RespBean.fail("创建失败，请重试");
            }
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
    }

    @Override
    public RespBean deleteArticle(String id) {
        try {
            boolean flag = remove(new QueryWrapper<Article>().eq("article_id", id));
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
    public RespBean updateArticle(Article article) {
        article.setUpdateTime(LocalDateTime.now());
        try {
            boolean flag=update(article,new QueryWrapper<Article>().eq("article_id",article.getArticleId()));
            if (flag){
                return RespBean.success("更新成功");
            }else {
                return RespBean.fail("更新失败，请重试");
            }
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
    }

    @Override
    public RespBean getArticle(String articleId) {
        Article article=getOne(new QueryWrapper<Article>().eq("article_id",articleId));
        update(new UpdateWrapper<Article>().eq("article_id",articleId).set("article_read_times",article.getArticleReadTimes()+1));
        return RespBean.success("SUCCESS",article);
    }


    @Override
    public RespBean getArticleList(Integer currentPage, Integer size) {
        Page<Article> page=new Page<>(currentPage,size);
        Page<Article> newsPage=null;
        try {
            newsPage=articleMapper.selectListByPage(page);
        }catch (Exception e){
            return RespBean.fail("服务器异常，请稍后重试");
        }
        RespPageBean pageBean=RespPageBean.tranPageBeanByPageObject(newsPage);
        return RespBean.success("SUCCESS",pageBean);
    }
}
