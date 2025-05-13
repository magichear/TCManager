package com.magichear.TCManager.dto.Project;

import java.util.List;

import lombok.Data;

/**
 * 项目请求 (组合了项目表和承担项目表)
 * Data 注解只会生成无参构造和get/set
 */
@Data
public class ProjectRequestDTO {
    private ProjectionDTO project;      // 项目表信息
    private List<InChargeDTO> charges;  // 承担项目表信息

    /**
     * 带参数的构造函数
     * @param project 项目表信息
     * @param charges 承担项目表信息
     */
    public ProjectRequestDTO(ProjectionDTO project, List<InChargeDTO> charges) {
        this.project = project;
        this.charges = charges;
    }
}