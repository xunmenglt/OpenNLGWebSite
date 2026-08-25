package com.opennlg.config.swagger2;


import lombok.Data;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;

@Data
@Configuration
public class Swagger2Properties {


    @Value("${swagger.base-package}")
    private String basePackage;

    @Value("${swagger.docket.enable}")
    private Boolean enable;

    @Value("${swagger.api-info.title}")
    private String title;

    @Value("${swagger.api-info.description}")
    private String description;

    @Value("${swagger.api-info.author}")
    private String author;

    @Value("${swagger.api-info.url}")
    private String url;

    @Value("${swagger.api-info.email}")
    private String email;

    @Value("${swagger.api-info.version}")
    private String version;

}
