package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.service.EnumService;
import org.springframework.stereotype.Service;

import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Map;

@Service
public class EnumServiceImpl implements EnumService {

    @Override
    public Map<Integer, String> getEnumValues(String enumClassName) {
        Map<Integer, String> result = new HashMap<>();
        try {
            // 加载枚举类
            Class<?> enumClass = Class.forName(enumClassName);
            if (!enumClass.isEnum()) {
                throw new IllegalArgumentException("Provided class is not an enum: " + enumClassName);
            }

            // 获取枚举常量
            Object[] enumConstants = enumClass.getEnumConstants();
            Method getValueMethod = enumClass.getMethod("getValue");
            Method nameMethod = enumClass.getMethod("name");

            for (Object enumConstant : enumConstants) {
                // 调用 getValue 和 name 方法
                Integer value = (Integer) getValueMethod.invoke(enumConstant);
                String name = (String) nameMethod.invoke(enumConstant);
                result.put(value, name);
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to retrieve enum values for: " + enumClassName, e);
        }
        return result;
    }
}