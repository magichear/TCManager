package com.magichear.TCManager.dto;

import com.magichear.TCManager.enums.ProjType;
import lombok.Data;

/**
 * 项目表 (PROJECTION)
 */
@Data
public class ProjectionDTO {
    private String projId;          // 项目号
    private String projName;        // 项目名称
    private String projSrc;         // 项目来源
    private ProjType projType;      // 项目类型
    private Double projBalance;     // 总经费
    private Integer projStartYear;  // 开始年份
    private Integer projEndYear;    // 结束年份
}