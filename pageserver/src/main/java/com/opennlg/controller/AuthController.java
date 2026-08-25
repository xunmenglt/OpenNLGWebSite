package com.opennlg.controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.opennlg.pojo.User;
import com.opennlg.service.IUserService;
import com.opennlg.vo.LoginParam;
import com.opennlg.vo.RespBean;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.security.Principal;


@RestController
@RequestMapping("/auth")
@Api(tags = "授权操作接口")
public class AuthController {
    @Autowired
    private IUserService userService;


    @ApiOperation(value = "用户登录接口")
    @PostMapping("/login")
    public RespBean login(@RequestBody LoginParam loginParam, HttpServletRequest httpServletRequest){
        return userService.login(loginParam,httpServletRequest);
    }


    @ApiOperation(value = "获取当前用户信息")
    @GetMapping("/user/info")
    public RespBean getAdminInfo(Principal principal){
        if (principal==null){
            return new RespBean(401,"未登录",null);
        }
        String username = principal.getName();
        User user=userService.getOne(new QueryWrapper<User>().eq("username",username));
        return RespBean.success("SUCCESS",user);
    }


}
