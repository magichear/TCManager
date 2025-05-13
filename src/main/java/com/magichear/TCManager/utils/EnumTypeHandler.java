package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Paper.PaperRank;
import com.magichear.TCManager.enums.Paper.PaperType;
import com.magichear.TCManager.enums.Project.ProjType;

import org.apache.ibatis.type.BaseTypeHandler;
import org.apache.ibatis.type.JdbcType;
import org.apache.ibatis.type.MappedTypes;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * 通用枚举类型处理器，用于将数据库中的整数值映射到枚举类型。
 * 适用于所有实现了 fromValue 方法的枚举。
 *
 * @param <E> 枚举类型
 */
@MappedTypes({PaperType.class, PaperRank.class, ProjType.class})
public class EnumTypeHandler<E extends Enum<E>> extends BaseTypeHandler<E> {

    private final Class<E> type;

    /**
     * 带参构造函数，传入枚举类型的 Class 对象。
     *
     * @param type 枚举类型
     */
    public EnumTypeHandler(Class<E> type) {
        if (type == null) {
            throw new IllegalArgumentException("Type argument cannot be null");
        }
        this.type = type;
    }

    @Override
    public void setNonNullParameter(PreparedStatement ps, int i, E parameter, JdbcType jdbcType) throws SQLException {
        try {
            int value = (int) type.getMethod("getValue").invoke(parameter);
            ps.setInt(i, value);
        } catch (Exception e) {
            throw new SQLException("Failed to get value from enum: " + parameter, e);
        }
    }

    @Override
    public E getNullableResult(ResultSet rs, String columnName) throws SQLException {
        int value = rs.getInt(columnName);
        return fromValue(value);
    }

    @Override
    public E getNullableResult(ResultSet rs, int columnIndex) throws SQLException {
        int value = rs.getInt(columnIndex);
        return fromValue(value);
    }

    @Override
    public E getNullableResult(java.sql.CallableStatement cs, int columnIndex) throws SQLException {
        int value = cs.getInt(columnIndex);
        return fromValue(value);
    }

    private E fromValue(int value) throws SQLException {
        try {
            return EnumUtils.fromValue(type, value);
        } catch (IllegalArgumentException e) {
            throw new SQLException("Failed to convert value " + value + " to enum " + type.getName(), e);
        }
    }
}