package com.magichear.TCManager.enums.Course;
import org.apache.ibatis.type.MappedTypes;

import com.magichear.TCManager.utils.EnumUtils;
import lombok.Getter;

/**
 * 表示课程的类型：1-本科生课程，2-研究生课程
 */
@Getter
@MappedTypes(CourseType.class)
public enum CourseType {
    UNDERGRADUATE(1), // 本科生课程
    POSTGRADUATE(2);  // 研究生课程

    private final int value;

    CourseType(int value) {
        this.value = value;
    }

    public static CourseType fromValue(int value) {
        return EnumUtils.fromValue(CourseType.class, value);
    }
}