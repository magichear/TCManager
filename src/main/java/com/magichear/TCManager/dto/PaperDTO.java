package com.magichear.TCManager.dto;

import com.magichear.TCManager.enums.PaperRank;
import com.magichear.TCManager.enums.PaperType;
import lombok.Data;
import java.util.Date;

/**
 * 论文表 (PAPER)
 */
@Data
public class PaperDTO {
    private Integer paperNum;    // 序号
    private String paperName;    // 论文名称
    private String paperSrc;     // 发表源
    private Date paperYear;      // 发表年份
    private PaperType paperType; // 类型 1-full paper，2-short paper，3-poster paper，4-demo paper
    private PaperRank paperRank; // 级别 1-CCF-A，2-CCF-B，3-CCF-C，4-中文CCF-A，5-中文CCF-B，6-无级别
}