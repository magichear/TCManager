package com.magichear.TCManager.controller;

import com.magichear.TCManager.dto.Course.LectureCourseDTO;
import com.magichear.TCManager.dto.Course.LectureCourseResponseDTO;
import com.magichear.TCManager.service.CourseService;
import lombok.RequiredArgsConstructor;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * 课程控制器
 * 提供主讲课程信息的增、删、改、查功能
 * 
 * 查询功能也应该同时支持按教师工号查询其所有课程，以及按课程号查询所有主讲记录
 * 
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
    public Map<String, Object> addLecture(@RequestBody LectureCourseDTO lecture) {
        return courseService.addLecture(lecture);
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
     * 查询教师的所有主讲课程记录
     * @param teacherId 教师工号
     * @return 教师的主讲课程列表
     */
    @GetMapping("/teachers/{teacherId}")
    public Map<Integer, LectureCourseResponseDTO> getLecturesByTeacher(@PathVariable String teacherId) {
        return courseService.getCoursesByTeacherId(teacherId);
    }

    /**
     * 查询课程的所有主讲记录
     * @param courseId 课程号
     * @return 主讲记录列表
     */
    @GetMapping("/lectures/{courseId}")
    public List<LectureCourseDTO> getLecturesByCourse(@PathVariable String courseId) {
        return courseService.getLecturesByCourseId(courseId);
    }
}