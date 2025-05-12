package com.magichear.TCManager.dto;

import com.magichear.TCManager.enums.PaperRank;
import com.magichear.TCManager.enums.PaperType;
import com.magichear.TCManager.utils.IdUtils;

import lombok.Getter;
import lombok.ToString;

import java.util.Date;

/**
 * 论文表 (PAPER)
 */
@Getter
@ToString
public class PaperDTO {
    private final Integer paperNum;    // 序号（只读）
    private final String paperName;    // 论文名称
    private final String paperSrc;     // 发表源
    private final Date paperYear;      // 发表年份
    private final PaperType paperType; // 类型 1-full paper，2-short paper，3-poster paper，4-demo paper
    private final PaperRank paperRank; // 级别 1-CCF-A，2-CCF-B，3-CCF-C，4-中文CCF-A，5-中文CCF-B，6-无级别

    // 私有构造方法，仅允许通过工厂方法创建
    private PaperDTO(Integer paperNum, String paperName, String paperSrc, Date paperYear, PaperType paperType, PaperRank paperRank) {
        this.paperNum = paperNum;
        this.paperName = paperName;
        this.paperSrc = paperSrc;
        this.paperYear = paperYear;
        this.paperType = paperType;
        this.paperRank = paperRank;
    }

    // 工厂方法：用于新增论文自动生成序号
    public static PaperDTO createWithoutNum(PaperDTO paper) {
        return new PaperDTO(IdUtils.generateIntegerId(), paper.getPaperName(), paper.getPaperSrc(), paper.getPaperYear(), paper.getPaperType(), paper.getPaperRank());
    }
}