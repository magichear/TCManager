package com.magichear.TCManager.controller;

import com.magichear.TCManager.dto.Course.LectureCourseDTO;
import com.magichear.TCManager.service.CourseService;
import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * 课程控制器
 * 提供主讲课程信息的增、删、改、查功能
 */
@RestController
@RequestMapping("/api/courses")
@RequiredArgsConstructor
public class CourseController {

    @Autowired
    private final CourseService courseService;

    /**
     * 添加主讲课程记录    直接使用类级路径，并以Post与Put区分
     * @param lecture 主讲课程信息
     */
    @PostMapping
    public void addLecture(@RequestBody LectureCourseDTO lecture) {
        courseService.addLecture(lecture);
    }

    /**
     * 更新主讲课程记录
     * @param lecture 主讲课程信息
     */
    @PutMapping
    public void updateLecture(@RequestBody LectureCourseDTO lecture) {
        courseService.updateLecture(lecture);
    }

    /**
     * 删除主讲课程记录
     * @param courseId 课程号
     * @param teacherId 教师工号
     */
    @DeleteMapping("/{courseId}/teachers/{teacherId}")
    public void deleteLecture(@PathVariable String courseId, @PathVariable String teacherId) {
        courseService.deleteLecture(courseId, teacherId);
    }

    /**
     * 获取某课程的主讲学时总和
     * @param courseId 课程号
     * @return 主讲学时总和
     */
    @GetMapping("/{courseId}/total-hours")
    public Integer getTotalLectureHours(@PathVariable String courseId) {
        return courseService.getTotalLectureHours(courseId);
    }
}