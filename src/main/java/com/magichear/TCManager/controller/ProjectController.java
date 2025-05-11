package com.magichear.TCManager.controller;

import com.magichear.TCManager.dto.ProjectRequestDTO;
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

    /**
     * 添加项目记录
     * @param projectRequest 项目信息及承担信息
     */
    @PostMapping
    public void addProject(@RequestBody ProjectRequestDTO projectRequest) {
        projectService.addProject(projectRequest);
    }

    /**
     * 更新项目记录
     * @param projectRequest 项目信息及承担信息
     */
    @PutMapping
    public void updateProject(@RequestBody ProjectRequestDTO projectRequest) {
        projectService.updateProject(projectRequest);
    }

    /**
     * 删除项目记录
     * @param projId 项目号
     */
    @DeleteMapping("/{projId}")
    public void deleteProject(@PathVariable String projId) {
        projectService.deleteProject(projId);
    }

    /**
     * 按项目号查询项目信息
     * @param projId 项目号
     * @return 项目信息及承担信息
     */
    @GetMapping("/{projId}")
    public ProjectRequestDTO getProjectById(@PathVariable String projId) {
        return projectService.getProjectById(projId);
    }
}