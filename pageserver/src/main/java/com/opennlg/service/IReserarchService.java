package com.opennlg.service;

import com.opennlg.pojo.Reserarch;
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
public interface IReserarchService extends IService<Reserarch> {
    RespBean createReserarch(Reserarch reserarch);

    RespBean deleteReserarch(Integer id);

    RespBean updateReserarch(Reserarch reserarch);

    RespBean getReserarchList(Integer currentPage, Integer size, String direction,
                              String author, String title, String keyword, Integer year,
                              String type, String resource, String venue);

    RespBean getReserarchOptions();

    RespBean getReserarch(Integer reserarchId);
}
