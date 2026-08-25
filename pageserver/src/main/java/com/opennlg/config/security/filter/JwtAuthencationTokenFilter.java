package com.opennlg.config.security.filter;

import com.opennlg.config.cache.SecurityCache;
import com.opennlg.config.security.pojo.LoginUser;
import com.opennlg.config.security.utils.JwtTokenUtil;
import com.opennlg.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.util.ObjectUtils;
import org.springframework.util.StringUtils;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

/**
 * jwt登录授权过滤器
 */
@Component
public class JwtAuthencationTokenFilter extends OncePerRequestFilter {

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Value("${jwt.tokenHeader}")
    private String tokeHeader;

    @Value("${jwt.tokenHead}")
    private String tokenHead;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {

        //获取token
        String authHeader = request.getHeader(tokeHeader);

        //判断token
        if(StringUtils.isEmpty(authHeader)){
            filterChain.doFilter(request,response);
            return;
        }

//        response.setStatus(401);

        //解析token
        if (!authHeader.startsWith(tokenHead)){
            throw new RuntimeException("token非法");
        }

        String token=authHeader.substring(tokenHead.length());


        String username;

        try {
            username = jwtTokenUtil.getUsernameByToken(token);
        }catch (Exception e){
            throw new RuntimeException("token非法");
        }
        if(StringUtils.isEmpty(username)){
            filterChain.doFilter(request,response);
            return;
        }
        //验证token是否有效
        // todo open
//        if (!jwtTokenUtil.validateToken(token)){
//            throw new RuntimeException("登录过期");
//        }

        //从redis获取用户信息
        LoginUser loginUser = null;


        Object o= SecurityCache.container.get(username);

        // todo open
        if (ObjectUtils.isEmpty(o)){
            filterChain.doFilter(request,response);
            return;
        }
        // todo delete
//        User user = new User();
//        user.setUsername(username);
//        o=new LoginUser(user);

        loginUser=(LoginUser) o;

        UsernamePasswordAuthenticationToken authenticationToken=new UsernamePasswordAuthenticationToken(loginUser,null,loginUser.getAuthorities());
        authenticationToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
        //存人SecurityContextHolder
        SecurityContextHolder.getContext().setAuthentication(authenticationToken);
        response.setStatus(200);
        filterChain.doFilter(request,response);
    }
}
