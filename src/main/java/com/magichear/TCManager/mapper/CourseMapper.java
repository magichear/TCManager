package com.magichear.TCManager.mapper;

import com.magichear.TCManager.dto.Course.CourseDTO;
import com.magichear.TCManager.dto.Course.LectureCourseDTO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface CourseMapper {

    /**
     * 插入课程基本信息
     *
     * @param course 课程信息
     */
    void insertLectureCourse(CourseDTO course);

    /**
     * 按课程号查询课程信息
     *
     * @param courseId 课程号
     * @return 课程信息
     */
    CourseDTO selectCourseById(@Param("courseId") String courseId);

    /**
     * 插入主讲课程关联信息
     *
     * @param lecture 主讲课程信息
     */
    void insertLectureCourse(LectureCourseDTO lecture);

    /**
     * 删除主讲课程关联信息
     *
     * @param courseId  课程号
     * @param teacherId 教师工号
     */
    void deleteLectureCourse(@Param("courseId") String courseId, @Param("teacherId") String teacherId);

    /**
     * 按教师ID查询主讲课程表中的所有相关记录
     *
     * @param teacherId 教师工号
     * @return 主讲课程记录列表
     */
    List<LectureCourseDTO> selectLectureCoursesByTeacherId(@Param("teacherId") String teacherId);

    /**
     * 按课程号查询主讲课程表中的所有相关记录
     *
     * @param courseId 课程号
     * @return 主讲课程记录列表
     */
    List<LectureCourseDTO> selectLectureCoursesByCourseId(@Param("courseId") String courseId);

    int getCourseHour(@Param("courseId") String courseId);

    int getLectureHour(@Param("courseId") String courseId, @Param("teacherId") String teacherId);

    /**
     * 更新课程学时数
     *
     * @param courseId 课程号
     * @param updatedCourseHour 更新后的课程学时数
     */
    void updateCourseHour(String courseId, Integer updatedCourseHour);
}