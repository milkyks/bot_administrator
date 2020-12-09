package com.polytech.dormbot.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

import static springfox.documentation.builders.PathSelectors.regex;

@Configuration
@EnableSwagger2
public class SwaggerConfig {

    @Bean
    public Docket documentation() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.polytech.dormbot.api.v1.controller"))
                .paths(regex("/api/v1/.*"))
                .build();
    }

    private ApiInfo metadata() {
        return new ApiInfoBuilder()
                .title("Documentation of Shared Notes")
                .description("")
                .version("1.0.0")
                .build();
    }
}
