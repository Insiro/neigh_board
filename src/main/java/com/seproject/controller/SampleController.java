package com.seproject.controller;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SampleController {

    @GetMapping("/board")
    public String sayHello() {

        return "Hello World";
    }
}
