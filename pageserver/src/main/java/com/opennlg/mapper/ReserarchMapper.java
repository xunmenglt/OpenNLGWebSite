package com.opennlg.mapper;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.opennlg.pojo.Reserarch;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 * <p>
 *  Mapper 接口
 * </p>
 *
 * @author Liuteng
 * @since 2023-11-02
 */
public interface ReserarchMapper extends BaseMapper<Reserarch> {

    Page<Reserarch> selectListByPage(Page<Reserarch> page,
                                    @Param("direction") String direction,
                                    @Param("author") String author,
                                    @Param("title") String title,
                                    @Param("keyword") String keyword,
                                    @Param("year") Integer year,
                                    @Param("type") String type,
                                    @Param("resource") String resource,
                                    @Param("venue") String venue);

    List<String> selectResearchDirections();

    List<Integer> selectPublicationYears();

    List<String> selectPublicationTypes();

    List<String> selectPublicationResources();

    List<String> selectPublicationVenues();
}
