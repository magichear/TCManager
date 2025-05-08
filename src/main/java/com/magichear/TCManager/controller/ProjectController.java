package com.magichear.TCManager.controller;

import com.magichear.TCManager.service.ProjectService;
import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * 项目控制器
 * 提供教师承担项目信息的增、删、改、查功能
 */
@RestController
@RequestMapping("/api/projects")
@RequiredArgsConstructor
public class ProjectController {
    @Autowired
    private final ProjectService projectService;

}