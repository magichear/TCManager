package com.magichear.TCManager.controller;

import com.magichear.TCManager.service.EnumService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class EnumController {

    @Autowired
    private EnumService enumService;

    /**
     * 获取指定枚举类的枚举值及其对应名称
     * @param enumClassName 枚举类的全限定名
     * @return 枚举值及其对应名称的字典
     */
    @GetMapping("/api/enums")
    public Map<Integer, String> getEnumValues(@RequestParam String enumClassName) {
        return enumService.getEnumValues(enumClassName);
    }
}