package com.magichear.TCManager.service;

import com.magichear.TCManager.dto.ProjectRequestDTO;

/**
 * 提供教师承担项目信息的增、删、改、查功能。
 * 输入时要求检查：排名不能有重复，一个项目中所有教师的承担经费总额应等于项目的总经费，项目类型只能在约定的取值集合中选取。
 */
public interface ProjectService {

    /**
     * 添加项目记录
     * @param projectRequest 项目信息及承担信息
     */
    void addProject(ProjectRequestDTO projectRequest);

    /**
     * 删除项目记录
     * @param projId 项目号
     */
    void deleteProject(String projId);

    /**
     * 更新项目记录
     * @param projectRequest 项目信息及承担信息
     */
    void updateProject(ProjectRequestDTO projectRequest);

    /**
     * 按项目号查询项目信息
     * @param projId 项目号
     * @return 项目信息及承担信息
     */
    ProjectRequestDTO getProjectById(String projId);

    /**
     * 按教师工号查询承担信息
     */
    ProjectRequestDTO getProjectByTeacherId(String teacherId);
}