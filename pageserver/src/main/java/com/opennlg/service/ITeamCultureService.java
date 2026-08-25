package com.opennlg.service;

import com.opennlg.pojo.TeamCulture;
import com.baomidou.mybatisplus.extension.service.IService;
import com.opennlg.vo.RespBean;

/**
 * <p>
 * 团队文化 服务类
 * </p>
 *
 * @author Liuteng
 * @since 2024-06-29
 */
public interface ITeamCultureService extends IService<TeamCulture> {
    RespBean createTeamCulture(TeamCulture teamCulture);

    RespBean deleteTeamCulture(Integer id);

    RespBean updateTeamCulture(TeamCulture teamCulture);

    RespBean getTeamCultureList(Integer currentPage, Integer size);

    RespBean getTeamCulture(Integer teamCultureId);
}
