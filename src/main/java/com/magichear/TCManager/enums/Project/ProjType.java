package com.magichear.TCManager.enums.Project;

import lombok.Getter;

import org.apache.ibatis.type.MappedTypes;

import com.magichear.TCManager.utils.EnumUtils;
/**
 * 表示项目的类型：1-国家级项目，2-省部级项目，3-市厅级项目，4-企业合作项目，5-其它类型项目
 */
@Getter
@MappedTypes(ProjType.class)
public enum ProjType {
    NATIONAL(1),    // 国家级项目
    PROVINCIAL(2),  // 省部级项目
    MUNICIPAL(3),   // 市厅级项目
    ENTERPRISE(4),  // 企业合作项目
    OTHER(5);       // 其它类型项目

    private final int value;

    ProjType(int value) {
        this.value = value;
    }
    
    public static ProjType fromValue(int value) {
        return EnumUtils.fromValue(ProjType.class, value);
    }
}