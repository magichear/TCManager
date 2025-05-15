package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Paper.PaperType;
import org.apache.ibatis.type.MappedTypes;

/**
 * 专用于处理 PaperType 枚举的 MyBatis 类型处理器。
 */
@MappedTypes(PaperType.class)
public class PaperTypeHandler extends EnumTypeHandler<PaperType> {

    public PaperTypeHandler() {
        super(PaperType.class);
    }

    @Override
    protected PaperType fromValue(int value) {
        return PaperType.fromValue(value);
    }

    @Override
    protected int toValue(PaperType enumValue) {
        return enumValue.getValue();
    }
}