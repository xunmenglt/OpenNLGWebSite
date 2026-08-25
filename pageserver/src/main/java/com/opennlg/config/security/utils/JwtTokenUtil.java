package com.opennlg.config.security.utils;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;


@Component
public class JwtTokenUtil {
    private static final String CLAIM_KEY_USERNAME = "sub";//用户名
    private static final String CLAIM_KEY_CREATED = "created";//创建时间
    //解密加密密钥
    @Value("${jwt.secret}")
    private String secret;
    //失效时间
    @Value("${jwt.expiration}")
    private long expiration;



    /**
     * 根据用户信息生成Token：header+playload+签名
     * @param userDetails
     * @return
     */
    public String generateToken(UserDetails userDetails){
        //设置荷载
        Map<String,Object> claim=new HashMap<>();
        claim.put(CLAIM_KEY_USERNAME,userDetails.getUsername());
        claim.put(CLAIM_KEY_CREATED,new Date());
        return generateToken(claim);
    }

    /**
     * 根据荷载生成JWT Token
     * @param claim
     * @return
     */
    private  String generateToken(Map<String,Object> claim){
        //进行加密
        return Jwts.builder()
                //设置荷载
                .setClaims(claim)
                //设置超时时间
                .setExpiration(generateExpiration(expiration))
                //签名
                .signWith(SignatureAlgorithm.HS512,secret).compact();

    }


    /**
     * 生成失效时间
     * @param expiration
     * @return
     */
    private Date generateExpiration(long expiration){
        return new Date(System.currentTimeMillis()+expiration*1000);
    }




    /**
     * 从Token中获取用户名
     * @return
     */
    public String getUsernameByToken(String token){
        String username;
        try {
            Claims claims=getClaimsByToken(token);
            username=claims.getSubject();
        }catch (Exception e){
            username=null;
        }
        return username;

    }


    /**
     * 通过token获取荷载
     * @param token
     * @return
     */
    private Claims getClaimsByToken(String token){
        return Jwts.parser().setSigningKey(secret).parseClaimsJws(token).getBody();
    }


    /**
     * 判断Token是否失效
     * @param token
     * @param userDetails
     * @return
     */
    public boolean validateToken(String token,UserDetails userDetails){
        String username= getUsernameByToken(token);
        return username.equals(userDetails.getUsername())&&!isTokenExpried(token);
    }


    public boolean validateToken(String token){
        return !isTokenExpried(token);
    }
    /**
     *判断token是否可以刷新
     * @param token
     * @return
     */
    public boolean canRefresh(String token){
        return !isTokenExpried(token);
    }

    /**
     * 判断该token是否超过失效时间
     * @param token
     * @return
     */
    private boolean isTokenExpried(String token){
        Date expriedDate=getExpriedDateByToken(token);
        return expriedDate.before(new Date());
    }


    /**
     * 刷新Token
     * @param token
     * @return
     */
    public String refreshToken(String token){
        Claims claims=getClaimsByToken(token);
        claims.put(CLAIM_KEY_CREATED,new Date());
        return generateToken(claims);
    }


    /**
     * 获取失效时间
     * @return
     */
    private Date getExpriedDateByToken(String token){
        return getClaimsByToken(token).getExpiration();
    }




}
