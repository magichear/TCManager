package com.magichear.TCManager.mapper;

import com.magichear.TCManager.dto.Course.LectureCourseDTO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface CourseMapper {

    /**
     * 查询课程总学时
     * @param courseId 课程号
     * @return 总学时
     */
    Integer selectCourseHours(@Param("courseId") String courseId);

    /**
     * 插入主讲课程记录
     * @param lecture 主讲课程信息
     * @return 插入的行数
     */
    int insertLecture(LectureCourseDTO lecture);

    /**
     * 更新主讲学时或学期
     * @param lecture 主讲课程信息
     * @return 更新的行数
     */
    int updateLecture(LectureCourseDTO lecture);

    /**
     * 删除主讲课程记录
     * @param courseId 课程号
     * @param teacherId 教师工号
     * @return 删除的行数
     */
    int deleteLecture(@Param("courseId") String courseId, @Param("teacherId") String teacherId);

    /**
     * 计算某课程所有教师的主讲学时总和
     * @param courseId 课程号
     * @return 主讲学时总和
     */
    Integer calculateTotalLectureHours(@Param("courseId") String courseId);
}