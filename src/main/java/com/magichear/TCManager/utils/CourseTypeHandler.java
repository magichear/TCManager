package com.magichear.TCManager.utils;

import com.magichear.TCManager.enums.Course.CourseType;
import org.apache.ibatis.type.BaseTypeHandler;
import org.apache.ibatis.type.JdbcType;
import org.apache.ibatis.type.MappedTypes;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * 专用于 CourseType 枚举的 TypeHandler
 */
@MappedTypes(CourseType.class)
public class CourseTypeHandler extends BaseTypeHandler<CourseType> {

    @Override
    public void setNonNullParameter(PreparedStatement ps, int i, CourseType parameter, JdbcType jdbcType) throws SQLException {
        ps.setInt(i, parameter.getValue());
    }

    @Override
    public CourseType getNullableResult(ResultSet rs, String columnName) throws SQLException {
        int value = rs.getInt(columnName);
        return CourseType.fromValue(value);
    }

    @Override
    public CourseType getNullableResult(ResultSet rs, int columnIndex) throws SQLException {
        int value = rs.getInt(columnIndex);
        return CourseType.fromValue(value);
    }

    @Override
    public CourseType getNullableResult(java.sql.CallableStatement cs, int columnIndex) throws SQLException {
        int value = cs.getInt(columnIndex);
        return CourseType.fromValue(value);
    }
}