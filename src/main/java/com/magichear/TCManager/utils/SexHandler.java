package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Sex;
import org.apache.ibatis.type.MappedTypes;

/**
 * 专用于处理 Sex 枚举的 MyBatis 类型处理器。
 */
@MappedTypes(Sex.class)
public class SexHandler extends EnumTypeHandler<Sex> {

    public SexHandler() {
        super(Sex.class);
    }

    @Override
    protected Sex fromValue(int value) {
        return Sex.fromValue(value);
    }

    @Override
    protected int toValue(Sex enumValue) {
        return enumValue.getValue();
    }
}