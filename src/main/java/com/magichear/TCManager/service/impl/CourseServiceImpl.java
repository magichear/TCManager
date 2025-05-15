package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.Course.*;
import com.magichear.TCManager.mapper.CourseMapper;
import com.magichear.TCManager.service.CourseService;

import lombok.RequiredArgsConstructor;

import java.util.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class CourseServiceImpl implements CourseService {

    @Autowired
    private final CourseMapper courseMapper;

    @Override
    @Transactional
    public Map<String, Object> addLecture(LectureCourseDTO lecture) {
        // 插入主讲课程记录
        courseMapper.insertLectureCourse(lecture);
    
        // 更新课程表的学时信息
        updateCourseHour(lecture.getCourseId(), lecture.getLectureHour());

        Map<String, Object> result = new HashMap<>();
        result.put("lecture", lecture);
        return result;
    }
    
    @Override
    @Transactional
    public void deleteLecture(String courseId, String teacherId) {
        // 查询要删除的主讲课程记录的学时
        Integer lectureHour = courseMapper.getLectureHour(courseId, teacherId);
    
        // 删除主讲课程记录
        courseMapper.deleteLectureCourse(courseId, teacherId);
    
        // 更新课程表的学时信息
        updateCourseHour(courseId, -lectureHour);
    }

    @Override
    @Transactional
    public void updateLecture(LectureCourseDTO lecture) {
        deleteLecture(lecture.getCourseId(), lecture.getTeacherId());
        addLecture(lecture);
        validateLecture(lecture, true);
    }

    @Override
    public Map<Integer, LectureCourseResponseDTO> getCoursesByTeacherId(String teacherId) {
        // 查询主讲课程记录
        List<LectureCourseDTO> lectureCourses = courseMapper.selectLectureCoursesByTeacherId(teacherId);
    
        // 封装结果
        Map<Integer, LectureCourseResponseDTO> result = new HashMap<>();
        int idx = 0;
    
        for (LectureCourseDTO lecture : lectureCourses) {
            // 查询课程详细信息
            CourseDTO course = courseMapper.selectCourseById(lecture.getCourseId());
    
            if (course != null) {
                // 封装 LectureCourseResponseDTO
                LectureCourseResponseDTO responseDTO = new LectureCourseResponseDTO(
                    course.getCourseId(),
                    course.getCourseName(),
                    course.getCourseHour(),
                    course.getCourseType(),
                    lecture.getLectureYear(),
                    lecture.getLectureTerm(),
                    lecture.getLectureHour()
                );
    
                // 添加到结果 Map
                result.put(idx, responseDTO);
                idx++;
            }
        }
    
        return result;
    }

    @Override
    public List<LectureCourseDTO> getLecturesByCourseId(String courseId) {
        // 查询主讲课程记录
        return courseMapper.selectLectureCoursesByCourseId(courseId);
    }

    /**
     * 更新课程表的学时信息
     * @param courseId 课程号
     * @param hourChange 学时变化值（正数表示增加，负数表示减少）
     */
    private void updateCourseHour(String courseId, int hourChange) {
        // 查询当前课程的总学时
        Integer currentCourseHour = courseMapper.getCourseHour(courseId);
    
        // 计算新的总学时
        int updatedCourseHour = currentCourseHour + hourChange;
    
        if (updatedCourseHour < 0) {
            throw new IllegalArgumentException("Total course hours cannot be negative.");
        }
    
        // 更新课程表的学时信息
        if (currentCourseHour != updatedCourseHour)
            courseMapper.updateCourseHour(courseId, updatedCourseHour);
    }

    /**
     * 校验主讲课程信息的合法性
     * @param lecture 主讲课程信息
     */
    private void validateLecture(LectureCourseDTO lecture, boolean isUpdate) {
        
    }
}