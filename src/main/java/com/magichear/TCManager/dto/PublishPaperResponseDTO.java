package com.magichear.TCManager.dto;

import com.magichear.TCManager.enums.PaperRank;
import com.magichear.TCManager.enums.PaperType;

import lombok.AllArgsConstructor;
import lombok.Data;
import java.util.Date;

/**
 * 发表论文表 (PUBLISH_PAPERS)
 */
@Data
@AllArgsConstructor
public class PublishPaperResponseDTO {
    private String teacherId;        // 教师工号
    private Integer paperNum;        // 论文序号
    private String paperName;        // 论文名称
    private String paperSrc;         // 发表源
    private Date paperYear;          // 发表年份
    private PaperType paperType;     // 类型
    private PaperRank paperRank;     // 级别
    private Integer publishRank;     // 排名
    private Boolean isCorresponding; // 是否通讯作者
}