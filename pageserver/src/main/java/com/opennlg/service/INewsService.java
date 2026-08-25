package com.opennlg.service;

import com.opennlg.pojo.News;
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
public interface INewsService extends IService<News> {

    RespBean createNews(News news);

    RespBean deleteNews(Integer id);

    RespBean updateNews(News news);

    RespBean getNewsList(Integer currentPage, Integer size);

    RespBean getNews(Integer newsId);
}
