package com.magichear.TCManager.dto.Course;

import com.magichear.TCManager.enums.Course.CourseType;
import com.magichear.TCManager.enums.Course.Term;

import lombok.AllArgsConstructor;
import lombok.Data;

/**
 * 课程响应 (组合了课程表和主讲课程表的详细信息)
 */
@Data
@AllArgsConstructor
public class LectureCourseResponseDTO {
    private String courseId;        // 课程号
    private String courseName;      // 课程名称
    private Integer courseHour;     // 学时数
    private CourseType courseType;  // 课程性质
    private Integer lectureYear;    // 年份
    private Term lectureTerm;       // 学期
    private Integer lectureHour;    // 承担学时
}