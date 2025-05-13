package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.Project.InChargeDTO;
import com.magichear.TCManager.dto.Project.ProjectRequestDTO;
import com.magichear.TCManager.dto.Project.ProjectionDTO;
import com.magichear.TCManager.enums.Project.ProjType;
import com.magichear.TCManager.mapper.ProjectMapper;
import com.magichear.TCManager.service.ProjectService;
import com.magichear.TCManager.utils.EnumUtils;

import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.*;

@Service
@RequiredArgsConstructor
public class ProjectServiceImpl implements ProjectService {

    @Autowired
    private final ProjectMapper projectMapper;

    @Override
    @Transactional
    public Map<String, Object> addProject(ProjectRequestDTO projectRequest) {
        // 使用工厂方法生成带有项目ID的 ProjectionDTO
        ProjectionDTO newProject = ProjectionDTO.createWithGeneratedId(projectRequest.getProject());

        // 校验项目合法性
        validateProject(projectRequest);

        // 插入项目信息
        projectMapper.insertProject(newProject);

        // 插入承担信息
        for (InChargeDTO charge : projectRequest.getCharges()) {
            charge.setProjId(newProject.getProjId()); // 设置项目号
            projectMapper.insertCharge(charge);
        }

        // 构造返回结果
        Map<String, Object> result = new HashMap<>();
        result.put("project", newProject); // 插入的项目信息
        result.put("charges", projectRequest.getCharges()); // 插入的承担信息

        return result;
    }

    @Override
    @Transactional
    public void updateProject(ProjectRequestDTO projectRequest) {
        // 删除旧的承担记录
        projectMapper.deleteCharge(projectRequest.getProject().getProjId(), null);

        // 校验项目合法性
        validateProject(projectRequest);

        // 更新项目基本信息
        projectMapper.updateProject(projectRequest.getProject());

        // 插入新的承担记录
        for (InChargeDTO charge : projectRequest.getCharges()) {
            charge.setProjId(projectRequest.getProject().getProjId());
            projectMapper.insertCharge(charge);
        }
    }

    @Override
    @Transactional
    public void deleteProject(String projId) {
        projectMapper.deleteCharge(projId, null);
        projectMapper.deleteProject(projId);
    }

    @Override
    public ProjectRequestDTO getProjectById(String projId) {
        return new ProjectRequestDTO(
                projectMapper.selectProjectById(projId),
                projectMapper.selectChargesById(projId, null)
        );
    }

    @Override
    public ProjectRequestDTO getProjectByTeacherId(String teacherId) {
        return new ProjectRequestDTO(
                null,
                projectMapper.selectChargesById(null, teacherId)
        );
    }

    /**
     * 校验项目信息的合法性
     * @param projectRequest 项目信息及承担信息
     */
    private void validateProject(ProjectRequestDTO projectRequest) {
        // 校验项目类型是否合法
        if (!EnumUtils.isValidEnumValue(ProjType.class, projectRequest.getProject().getProjType().getValue())) {
            throw new IllegalArgumentException("Invalid project type.");
        }

        // 计算总承担经费（直接从请求数据中计算）
        double totalCharge = projectRequest.getCharges().stream()
            .mapToDouble(InChargeDTO::getChargeBalance)
            .sum();

        // 校验总承担经费是否与项目余额匹配
        if (Double.compare(totalCharge, projectRequest.getProject().getProjBalance()) != 0) {
            throw new IllegalArgumentException("Total charge does not match project balance.");
        }

        // 校验是否存在重复排名
        projectRequest.getCharges().forEach(charge -> {
            boolean isDuplicate = projectMapper.checkProjectRankDuplicate(
                charge.getProjId(), charge.getChargeRank(), charge.getTeacherId()
            );
            if (isDuplicate) {
                throw new IllegalArgumentException("Duplicate charge rank detected for project: " 
                        + charge.getProjId() + ", Rank: " + charge.getChargeRank());
            }
        });
    }
}