package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.Course.LectureCourseDTO;
import com.magichear.TCManager.enums.Course.Term;
import com.magichear.TCManager.mapper.CourseMapper;
import com.magichear.TCManager.service.CourseService;
import com.magichear.TCManager.utils.EnumUtils;

import lombok.RequiredArgsConstructor;

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
    public void addLecture(LectureCourseDTO lecture) {
        validateLecture(lecture, false);
        courseMapper.insertLecture(lecture);
    }

    @Override
    @Transactional
    public void updateLecture(LectureCourseDTO lecture) {
        validateLecture(lecture, true);
        courseMapper.updateLecture(lecture);
    }

    @Override
    @Transactional
    public void deleteLecture(String courseId, String teacherId) {
        // 删除主讲课程记录
        courseMapper.deleteLecture(courseId, teacherId);
    }

    @Override
    public Integer getTotalLectureHours(String courseId) {
        // 获取课程的总学时数，处理可能的 null 返回值
        Integer totalHours = courseMapper.calculateTotalLectureHours(courseId);
        return totalHours != null ? totalHours : 0;
    }

    /**
     * 校验主讲课程信息的合法性
     * @param lecture 主讲课程信息
     */
    private void validateLecture(LectureCourseDTO lecture, boolean isUpdate) {
        // 校验学期是否合法
        if (!EnumUtils.isValidEnumValue(Term.class, lecture.getLectureTerm().getValue())) {
            throw new IllegalArgumentException("Invalid term.");
        }
    
        // 获取当前课程的总学时数
        Integer totalHours = courseMapper.calculateTotalLectureHours(lecture.getCourseId());
        if (totalHours == null) {
            totalHours = 0;
        }
    
        // 如果是更新操作，减去当前记录的学时
        if (isUpdate) {
            Integer currentLectureHours = courseMapper.calculateTotalLectureHours(lecture.getCourseId());
            if (currentLectureHours != null) {
                totalHours -= currentLectureHours;
            }
        }
    
        // 获取课程的总学时限制
        Integer courseHours = courseMapper.selectCourseHours(lecture.getCourseId());
        if (courseHours == null) {
            throw new IllegalArgumentException("Course not found: " + lecture.getCourseId());
        }
    
        // 校验总学时是否超出课程限制
        if (totalHours + lecture.getLectureHour() > courseHours) {
            throw new IllegalArgumentException("Total lecture hours exceed course hours.");
        }
    }
}