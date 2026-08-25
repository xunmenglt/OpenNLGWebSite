package com.opennlg.mapper;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.pojo.Article;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;

/**
 * <p>
 *  Mapper 接口
 * </p>
 *
 * @author Liuteng
 * @since 2023-10-31
 */
public interface ArticleMapper extends BaseMapper<Article> {

    Page<Article> selectListByPage(Page<Article> page);
}
