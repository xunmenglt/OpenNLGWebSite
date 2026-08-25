package com.opennlg.service;

import com.opennlg.pojo.User;
import com.baomidou.mybatisplus.extension.service.IService;
import com.opennlg.vo.LoginParam;
import com.opennlg.vo.RespBean;

import javax.servlet.http.HttpServletRequest;

/**
 * <p>
 *  服务类
 * </p>
 *
 * @author Liuteng
 * @since 2023-10-30
 */
public interface IUserService extends IService<User> {

    RespBean login(LoginParam loginParam, HttpServletRequest httpServletRequest);

}
