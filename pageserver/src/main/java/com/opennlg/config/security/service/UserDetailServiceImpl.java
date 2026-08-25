package com.opennlg.config.security.service;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.opennlg.config.security.pojo.LoginUser;
import com.opennlg.mapper.UserMapper;
import com.opennlg.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.util.ObjectUtils;

import java.util.List;


@Service
public class UserDetailServiceImpl implements UserDetailsService {
    @Autowired
    private UserMapper userMapper;

    @Override
    public UserDetails loadUserByUsername(String s) throws UsernameNotFoundException {
        //根据用户名查取用户
        User user = userMapper.selectOne(new QueryWrapper<User>().eq("username", s));
        if (ObjectUtils.isEmpty(user)){
            throw new UsernameNotFoundException("用户名不存在!");
        }
        //封装成UserDetails
        LoginUser loginUser = new LoginUser(user);
        return loginUser;
    }
}
