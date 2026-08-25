package com.opennlg.vo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * 公共返回对象
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class RespBean {
    private long code;
    private String message;
    private Object data;

    /**
     * 成功返回结果
     * @param message
     * @return
     */
    public static RespBean success(String message){
        return new RespBean(200,message,null);
    }

    /**
     * 成功返回结果
     * @param message
     * @return
     */
    public static RespBean success(String message,Object data){
        return new RespBean(200,message,data);
    }


    /**
     * 失败返回结果
     * @param message
     * @return
     */
    public static RespBean fail(String message){
        return new RespBean(500,message,null);
    }

    /**
     * 失败返回结果
     * @param message
     * @return
     */
    public static RespBean fail(String message,Object data){
        return new RespBean(500,message,data);
    }
}
