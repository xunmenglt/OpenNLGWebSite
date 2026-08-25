package com.opennlg.service.impl;

import com.opennlg.config.cache.SecurityCache;
import com.opennlg.config.security.pojo.LoginUser;
import com.opennlg.config.security.utils.JwtTokenUtil;
import com.opennlg.pojo.User;
import com.opennlg.mapper.UserMapper;
import com.opennlg.service.IUserService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.opennlg.vo.LoginParam;
import com.opennlg.vo.RespBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import javax.servlet.http.HttpServletRequest;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author Liuteng
 * @since 2023-10-30
 */
@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements IUserService {
    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Value("${jwt.tokenHead}")
    private String tokenHeader;

    @Autowired
    private UserDetailsService userDetailsService;
    @Autowired
    private PasswordEncoder passwordEncoder;

    /**
     * 登录接口
     * @param loginParam
     * @param httpServletRequest
     * @return
     */
    @Override
    public RespBean login(LoginParam loginParam, HttpServletRequest httpServletRequest) {

        LoginUser loginUser=(LoginUser) userDetailsService.loadUserByUsername(loginParam.getUsername());

        if (null==loginUser||!passwordEncoder.matches(loginParam.getPassword(),loginUser.getPassword())){
            return RespBean.fail("密码错误");
        }

        if(!loginUser.isEnabled()){
            return RespBean.fail("账号被禁用，请联系管理员");
        }

        //更新security对象
        UsernamePasswordAuthenticationToken usernamePasswordAuthenticationToken=new UsernamePasswordAuthenticationToken(loginUser,null,loginUser.getAuthorities());
        SecurityContextHolder.getContext().setAuthentication(usernamePasswordAuthenticationToken);

        //将用户信息保存在redis中
        SecurityCache.container.put(loginUser.getUsername(),loginUser);

        //生成token
        String token=jwtTokenUtil.generateToken(loginUser);
        Map<String,String> tokenMap=new HashMap<>();
        tokenMap.put("token",token);
        tokenMap.put("tokenHead",tokenHeader);
        return RespBean.success("登录成功",tokenMap);
    }
}
