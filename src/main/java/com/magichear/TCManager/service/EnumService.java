package com.magichear.TCManager.service;

import java.util.Map;

public interface EnumService {
    /**
     * 获取指定枚举类的枚举值及其对应名称
     * @param enumClassName 枚举类的全限定名
     * @return 枚举值及其对应名称的字典
     */
    Map<Integer, String> getEnumValues(String enumClassName);
}