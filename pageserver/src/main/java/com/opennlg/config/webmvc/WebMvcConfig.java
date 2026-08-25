package com.opennlg.config.webmvc;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.convert.converter.Converter;
import org.springframework.format.FormatterRegistry;
import org.springframework.util.ObjectUtils;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurationSupport;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Configuration
public class WebMvcConfig extends WebMvcConfigurationSupport {
    @Value(value = "${file.path}")
    private String filePath ;

    @Value(value = "${file.resource-path}")
    private String resourcePath;

    @Override
    protected void addFormatters(FormatterRegistry registry) {
        super.addFormatters(registry);
        registry.addConverter(new Converter<String, LocalDateTime>() {
            @Override
            public LocalDateTime convert(String source) {
                DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

                if (ObjectUtils.isEmpty(source)){
                    return null;
                }

                return LocalDateTime.parse(source, fmt);
            }
        });
        registry.addConverter(new Converter<String, LocalDateTime>() {
            @Override
            public LocalDateTime convert(String source) {
                DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd");

                if (ObjectUtils.isEmpty(source)){
                    return null;
                }

                return LocalDateTime.parse(source, fmt);
            }
        });
        registry.addConverter(new Converter<String, LocalDate>(){
            @Override
            public LocalDate convert(String source) {
                DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd");

                if (ObjectUtils.isEmpty(source)){
                    return null;
                }
                return LocalDate.parse(source, fmt);
            }
        } );
    }
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("doc.html")
                .addResourceLocations("classpath:/META-INF/resources/");
        registry.addResourceHandler("/webjars/**")
                .addResourceLocations("classpath:/META-INF/resources/webjars/");
        registry.addResourceHandler(resourcePath)
                .addResourceLocations("file:".concat(filePath));
    }
}
