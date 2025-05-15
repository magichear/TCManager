package com.magichear.TCManager.mapper;

import com.magichear.TCManager.dto.TeacherDTO;

import org.apache.ibatis.annotations.Param;


public interface TeacherMapper {

    TeacherDTO selectTeacherById(@Param("teacherId") String teacherId);

}