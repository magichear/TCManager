package com.magichear.TCManager.dto;

import com.magichear.TCManager.enums.Term;
import lombok.Data;

/**
 * 主讲课程表 (LECTRUE_COURSE)
 */
@Data
public class LectureCourseDTO {
    private String teacherId;    // 教师工号
    private String courseId;     // 课程号
    private Integer lectureYear; // 年份
    private Term lectureTerm;    // 学期
    private Integer lectureHour; // 承担学时
}