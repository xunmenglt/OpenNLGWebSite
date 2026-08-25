package com.opennlg.service;

import com.opennlg.pojo.Article;
import com.baomidou.mybatisplus.extension.service.IService;
import com.opennlg.vo.RespBean;

/**
 * <p>
 *  服务类
 * </p>
 *
 * @author Liuteng
 * @since 2023-10-31
 */
public interface IArticleService extends IService<Article> {

    RespBean createArticle(Article article);

    RespBean deleteArticle(String id);

    RespBean updateArticle(Article article);

    RespBean getArticle(String articleId);

    RespBean getArticleList(Integer currentPage, Integer size);
}
