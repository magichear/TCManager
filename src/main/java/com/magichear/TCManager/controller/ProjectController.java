package com.magichear.TCManager.controller;

import com.magichear.TCManager.dto.Project.ProjectRequestDTO;
import com.magichear.TCManager.dto.Project.ProjectResponseDTO;
import com.magichear.TCManager.service.ProjectService;
import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

/**
 * 项目控制器
 * 提供教师承担项目信息的增、删、改、查功能
 * 
 * 项目经费应该做修改，要求根据传入的每个老师各自承担的经费进行动态计算与排名，
 *      不再对外提供总经费的填写与校验（“新增”与“修改”都需要这样处理）
 * 排名重复情况应该在前端直接进行阻止
 * 
 * 
 * 查询功能应该同时提供：
 *      根据项目号查询指定项目的功能，
 *      根据教师工号查询其承担的所有项目的功能
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
    public ResponseEntity<Map<String, Object>> addProject(@RequestBody ProjectRequestDTO projectRequest) {
        Map<String, Object> result = projectService.addProject(projectRequest);
        return ResponseEntity.ok(result);
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

    /**
     * 按教师工号查询其承担的所有项目信息
     * @param teacherId 教师工号
     * @return 项目信息及承担信息
     */
    @GetMapping("/teachers/{teacherId}/projects")
    public Map<Integer, ProjectResponseDTO> getProjectByTeacherId(@PathVariable String teacherId) {
        return projectService.getProjectByTeacherId(teacherId);
    }
}