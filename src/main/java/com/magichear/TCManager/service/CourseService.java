package com.magichear.TCManager.service;

import java.util.List;
import java.util.Map;

import com.magichear.TCManager.dto.Course.LectureCourseDTO;
import com.magichear.TCManager.dto.Course.LectureCourseResponseDTO;

/**
 * 提供教师主讲课程信息的增、删、改、查功能。
 * 输入时要求检查：一门课程所有教师的主讲学时总额应等于课程的总学时，学期值合法。
 */
public interface CourseService {

    /**
     * 添加主讲课程记录（双方（教师与课程信息）都不允许更改，因此这里无需序号也无需关联其它表）
     * 
     * 新增主讲记录之后需要同时维护课程表中的学时信息，删除同理
     * 
     * @param lecture 主讲课程信息
     */
    Map<String, Object> addLecture(LectureCourseDTO lecture);

    /**
     * 更新主讲课程记录
     * @param lecture 主讲课程信息
     */
    void updateLecture(LectureCourseDTO lecture);

    /**
     * 删除主讲课程记录（同理也仅允许删除中间表）
     * @param courseId 课程号
     * @param teacherId 教师工号
     */
    void deleteLecture(String courseId, String teacherId);
    
    /**
     * 查询教师主讲的所有课程信息
     * @param teacherId 教师工号
     * @return 主讲课程信息列表
     */
    Map<Integer, LectureCourseResponseDTO> getCoursesByTeacherId(String teacherId);

    /**
     * 查询课程的所有主讲记录
     * @param courseId 课程号
     * @return 主讲记录列表
     */
    List<LectureCourseDTO> getLecturesByCourseId(String courseId);
}