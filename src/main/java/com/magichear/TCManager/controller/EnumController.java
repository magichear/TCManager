package com.magichear.TCManager.controller;

import com.magichear.TCManager.service.EnumService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class EnumController {

    private static final Logger logger = LoggerFactory.getLogger(EnumController.class);

    @Autowired
    private EnumService enumService;

    /**
     * 获取指定枚举类的枚举值及其对应名称
     * @param enumClassName 枚举类的全限定名
     * @return 枚举值及其对应名称的字典
     */
    @GetMapping("/api/enums")
    public Map<Integer, String> getEnumValues(@RequestParam String enumClassName) {
        logger.info("Received request to fetch enum values for class: {}", enumClassName);
        Map<Integer, String> enumValues = enumService.getEnumValues(enumClassName);
        logger.info("Fetched {} enum values for class: {}", enumValues.size(), enumClassName);
        return enumValues;
    }
}