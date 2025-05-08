package com.magichear.TCManager.dto;

import com.magichear.TCManager.enums.Sex;
import com.magichear.TCManager.enums.Title;

import lombok.Data;


/**
 * 教师表 (TEACHER)
 */
@Data
public class TeacherDTO {
    private String teacherId;       // 工号
    private String teacherName;     // 姓名
    private Sex teacherSex;         // 性别
    private Title teacherTitle;     // 职称
}