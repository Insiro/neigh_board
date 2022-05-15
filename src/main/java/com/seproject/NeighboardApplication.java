package com.seproject;

import com.seproject.controller.WebBoardController;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

//@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
@SpringBootApplication(scanBasePackages = {"com.seproject.persistence"})
public class NeighboardApplication extends SpringBootServletInitializer {

    public static void main(String[] args) {
        SpringApplication.run(NeighboardApplication.class, args);
    }

}
