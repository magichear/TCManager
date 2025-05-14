package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Course.Term;
import org.apache.ibatis.type.BaseTypeHandler;
import org.apache.ibatis.type.JdbcType;
import org.apache.ibatis.type.MappedTypes;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * 专用于处理 Term 枚举的 MyBatis 类型处理器。
 */
@MappedTypes(Term.class)
public class TermHandler extends BaseTypeHandler<Term> {

    @Override
    public void setNonNullParameter(PreparedStatement ps, int i, Term parameter, JdbcType jdbcType) throws SQLException {
        ps.setInt(i, parameter.getValue());
    }

    @Override
    public Term getNullableResult(ResultSet rs, String columnName) throws SQLException {
        int value = rs.getInt(columnName);
        if (rs.wasNull()) {
            return null;
        }
        return Term.fromValue(value);
    }

    @Override
    public Term getNullableResult(ResultSet rs, int columnIndex) throws SQLException {
        int value = rs.getInt(columnIndex);
        if (rs.wasNull()) {
            return null;
        }
        return Term.fromValue(value);
    }

    @Override
    public Term getNullableResult(java.sql.CallableStatement cs, int columnIndex) throws SQLException {
        int value = cs.getInt(columnIndex);
        if (cs.wasNull()) {
            return null;
        }
        return Term.fromValue(value);
    }
}