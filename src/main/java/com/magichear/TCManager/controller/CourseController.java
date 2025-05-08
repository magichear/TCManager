package com.magichear.TCManager.controller;

import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.magichear.TCManager.service.CourseService;

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
}