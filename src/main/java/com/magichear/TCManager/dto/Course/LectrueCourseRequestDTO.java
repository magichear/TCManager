package com.magichear.TCManager.dto.Course;

import java.util.List;

import lombok.Data;

/**
 * 课程请求 (组合了课程表和主讲课程表)
 * 一门课可能在多个学年、学期由多个老师主讲
 */
@Data
public class LectrueCourseRequestDTO {
    private List<LectureCourseDTO> lectures;    // 主讲课程表信息

    /**
     * 带参数的构造函数
     * @param lectures 主讲课程表信息
     */
    public LectrueCourseRequestDTO(CourseDTO course, List<LectureCourseDTO> lectures) {
        this.lectures = lectures;
    }
}