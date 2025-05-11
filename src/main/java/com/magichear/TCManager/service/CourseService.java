package com.magichear.TCManager.service;

import com.magichear.TCManager.dto.LectureCourseDTO;

/**
 * 提供教师主讲课程信息的增、删、改、查功能。
 * 输入时要求检查：一门课程所有教师的主讲学时总额应等于课程的总学时，学期值合法。
 */
public interface CourseService {

    /**
     * 添加主讲课程记录
     * @param lecture 主讲课程信息
     */
    void addLecture(LectureCourseDTO lecture);

    /**
     * 更新主讲课程记录
     * @param lecture 主讲课程信息
     */
    void updateLecture(LectureCourseDTO lecture);

    /**
     * 删除主讲课程记录
     * @param courseId 课程号
     * @param teacherId 教师工号
     */
    void deleteLecture(String courseId, String teacherId);

    /**
     * 获取某课程的主讲学时总和
     * @param courseId 课程号
     * @return 主讲学时总和
     */
    Integer getTotalLectureHours(String courseId);
}