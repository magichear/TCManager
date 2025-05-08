package com.magichear.TCManager.dto;

import java.util.List;
import lombok.Data;

/**
 * 项目请求 (组合了项目表和承担项目表)
 */
@Data
public class ProjectRequestDTO {
    private ProjectionDTO project;      // 项目表信息
    private List<InChargeDTO> charges;  // 承担项目表信息
}