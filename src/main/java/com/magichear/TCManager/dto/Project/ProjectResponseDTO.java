package com.magichear.TCManager.dto.Project;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class ProjectResponseDTO {
    private Integer chargeRank;         // 排名 1-表示排名第一，以此类推
    private Double chargeBalance;       // 承担经费
    private ProjectionDTO project;      // 项目表信息
}
