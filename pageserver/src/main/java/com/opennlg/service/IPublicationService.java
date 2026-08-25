package com.opennlg.service;

import com.opennlg.pojo.Publication;
import com.baomidou.mybatisplus.extension.service.IService;
import com.opennlg.vo.RespBean;

/**
 * <p>
 *  服务类
 * </p>
 *
 * @author Liuteng
 * @since 2023-11-02
 */
public interface IPublicationService extends IService<Publication> {
    RespBean createPublication(Publication publication);

    RespBean deletePublication(Integer id);

    RespBean updatePublication(Publication publication);

    RespBean getPublicationList(Integer currentPage, Integer size);

    RespBean getPublication(Integer publicationId);
}
