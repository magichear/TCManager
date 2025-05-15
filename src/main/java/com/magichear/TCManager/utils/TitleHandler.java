package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Title;
import org.apache.ibatis.type.MappedTypes;

/**
 * 专用于处理 Title 枚举的 MyBatis 类型处理器。
 */
@MappedTypes(Title.class)
public class TitleHandler extends EnumTypeHandler<Title> {

    public TitleHandler() {
        super(Title.class);
    }

    @Override
    protected Title fromValue(int value) {
        return Title.fromValue(value);
    }

    @Override
    protected int toValue(Title enumValue) {
        return enumValue.getValue();
    }
}