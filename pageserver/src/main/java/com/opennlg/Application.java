package com.opennlg;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.opennlg.mapper")
public class Application {

    public static void main(String[] args) {
        // 设置系统启动时间
//        System.setProperty("applicationRunTime",String.valueOf(new Date().getTime()));
        SpringApplication.run(Application.class,args);
    }

}
