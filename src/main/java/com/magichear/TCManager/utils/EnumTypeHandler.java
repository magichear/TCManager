package com.magichear.TCManager.utils;

import org.apache.ibatis.type.BaseTypeHandler;
import org.apache.ibatis.type.JdbcType;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * 通用抽象枚举类型处理器，用于减少重复代码。
 *
 * @param <E> 枚举类型
 */
public abstract class EnumTypeHandler<E extends Enum<E>> extends BaseTypeHandler<E> {

    @SuppressWarnings("unused")
    private final Class<E> type;

    /**
     * 构造函数，传入枚举类型的 Class 对象。
     *
     * @param type 枚举类型
     */
    protected EnumTypeHandler(Class<E> type) {
        if (type == null) {
            throw new IllegalArgumentException("Type argument cannot be null");
        }
        this.type = type;
    }

    /**
     * @param value 数据库中的整数值
     * @return 对应的枚举值
     */
    protected abstract E fromValue(int value);

    /**
     * @param enumValue 枚举值
     * @return 对应的整数值
     */
    protected abstract int toValue(E enumValue);

    @Override
    public void setNonNullParameter(PreparedStatement ps, int i, E parameter, JdbcType jdbcType) throws SQLException {
        ps.setInt(i, toValue(parameter));
    }

    @Override
    public E getNullableResult(ResultSet rs, String columnName) throws SQLException {
        int value = rs.getInt(columnName);
        if (rs.wasNull()) {
            return null;
        }
        return fromValue(value);
    }

    @Override
    public E getNullableResult(ResultSet rs, int columnIndex) throws SQLException {
        int value = rs.getInt(columnIndex);
        if (rs.wasNull()) {
            return null;
        }
        return fromValue(value);
    }

    @Override
    public E getNullableResult(java.sql.CallableStatement cs, int columnIndex) throws SQLException {
        int value = cs.getInt(columnIndex);
        if (cs.wasNull()) {
            return null;
        }
        return fromValue(value);
    }
}