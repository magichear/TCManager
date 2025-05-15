package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Course.CourseType;
import org.apache.ibatis.type.MappedTypes;

/**
 * 专用于处理 CourseType 枚举的 MyBatis 类型处理器。
 */
@MappedTypes(CourseType.class)
public class CourseTypeHandler extends EnumTypeHandler<CourseType> {

    public CourseTypeHandler() {
        super(CourseType.class);
    }

    @Override
    protected CourseType fromValue(int value) {
        return CourseType.fromValue(value);
    }

    @Override
    protected int toValue(CourseType enumValue) {
        return enumValue.getValue();
    }
}