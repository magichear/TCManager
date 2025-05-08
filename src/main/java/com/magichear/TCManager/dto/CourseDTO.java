package com.magichear.TCManager.dto;

import com.magichear.TCManager.enums.CourseType;
import lombok.Data;

/**
 * 课程表 (COURCE)
 */
@Data
public class CourseDTO {
    private String courseId;       // 课程号
    private String courseName;     // 课程名称
    private Integer courseHour;    // 学时数
    private CourseType courseType; // 课程性质
}