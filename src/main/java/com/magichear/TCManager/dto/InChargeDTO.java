package com.magichear.TCManager.dto;

import lombok.Data;

/**
 * 承担项目表 (IN_CHARGE)
 */
@Data
public class InChargeDTO {
    private String teacherId;       // 教师工号
    private String projId;          // 项目号
    private Integer chargeRank;     // 排名 1-表示排名第一，以此类推
    private Double chargeBalance;   // 承担经费
}