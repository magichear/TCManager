package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Project.ProjType;
import org.apache.ibatis.type.MappedTypes;

/**
 * 专用于处理 ProjType 枚举的 MyBatis 类型处理器。
 */
@MappedTypes(ProjType.class)
public class ProjTypeHandler extends EnumTypeHandler<ProjType> {

    public ProjTypeHandler() {
        super(ProjType.class);
    }

    @Override
    protected ProjType fromValue(int value) {
        return ProjType.fromValue(value);
    }

    @Override
    protected int toValue(ProjType enumValue) {
        return enumValue.getValue();
    }
}