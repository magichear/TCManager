package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Course.Term;
import org.apache.ibatis.type.MappedTypes;

/**
 * 专用于处理 Term 枚举的 MyBatis 类型处理器。
 */
@MappedTypes(Term.class)
public class TermHandler extends EnumTypeHandler<Term> {

    public TermHandler() {
        super(Term.class);
    }

    @Override
    protected Term fromValue(int value) {
        return Term.fromValue(value);
    }

    @Override
    protected int toValue(Term enumValue) {
        return enumValue.getValue();
    }
}