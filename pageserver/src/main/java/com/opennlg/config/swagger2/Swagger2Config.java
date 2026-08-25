package com.opennlg.config.swagger2;

import com.github.xiaoymin.swaggerbootstrapui.annotations.EnableSwaggerBootstrapUI;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.*;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spi.service.contexts.SecurityContext;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

import java.util.ArrayList;
import java.util.List;

/**
 * swagger配置类
 */
@Configuration
@EnableSwagger2
@EnableSwaggerBootstrapUI
public class Swagger2Config {


    @Bean
    public Docket createRestApi(Swagger2Properties properties){
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo(properties))
                .enable(properties.getEnable())
                .select()
                .apis(RequestHandlerSelectors.basePackage(properties.getBasePackage()))
                .paths(PathSelectors.any())
                .build()
                .securityContexts(securityContexts())
                .securitySchemes(securitySchemes());
    }



    private ApiInfo apiInfo(Swagger2Properties properties){
        return new ApiInfoBuilder()
                .title(properties.getTitle())
                .description(properties.getDescription())
                .contact(new Contact(properties.getAuthor(),properties.getUrl(),properties.getUrl()))
                .version(properties.getVersion())
                .build();
    }

    private List<ApiKey> securitySchemes(){
        //设置请求头
        List<ApiKey> apiKeys=new ArrayList<>();
        ApiKey apiKey=new ApiKey("Authorization","Authorization","Header");
        apiKeys.add(apiKey);
        return apiKeys;
    }

    private List<SecurityContext> securityContexts(){
        //设置需要登录认证的路径
        List<SecurityContext> result=new ArrayList<>();
        result.add(getContextPath("/hello/.*"));
        return result;
    }

    private SecurityContext getContextPath(String path){
        return SecurityContext.builder()
                .securityReferences(defaultAuth())
                .forPaths(PathSelectors.regex(path))
                .build();
    }


    private List<SecurityReference> defaultAuth(){
        List<SecurityReference> result=new ArrayList<>();
        AuthorizationScope authorizationScope=new AuthorizationScope("global","accessEverything");
        AuthorizationScope[] authorizationScopes=new AuthorizationScope[1];
        authorizationScopes[0]=authorizationScope;
        result.add(new SecurityReference("Authorization",authorizationScopes));
        return result;
    }



}
