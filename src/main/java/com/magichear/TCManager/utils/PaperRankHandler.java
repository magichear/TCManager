package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Paper.PaperRank;
import org.apache.ibatis.type.MappedTypes;

/**
 * 专用于处理 PaperRank 枚举的 MyBatis 类型处理器。
 */
@MappedTypes(PaperRank.class)
public class PaperRankHandler extends EnumTypeHandler<PaperRank> {

    public PaperRankHandler() {
        super(PaperRank.class);
    }

    @Override
    protected PaperRank fromValue(int value) {
        return PaperRank.fromValue(value);
    }

    @Override
    protected int toValue(PaperRank enumValue) {
        return enumValue.getValue();
    }
}