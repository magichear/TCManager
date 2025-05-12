package com.magichear.TCManager.dto;

import com.magichear.TCManager.enums.PaperRank;
import com.magichear.TCManager.enums.PaperType;
import com.magichear.TCManager.utils.IdUtils;

import lombok.Builder;
import lombok.Getter;
import lombok.ToString;

import java.util.Date;

/**
 * 论文表 (PAPER)
 */
@Getter
@ToString
@Builder
public class PaperDTO {
    private Integer paperNum;    // 序号（只读）
    private String paperName;    // 论文名称
    private String paperSrc;     // 发表源
    private Date paperYear;      // 发表年份
    private PaperType paperType; // 类型 1-full paper，2-short paper，3-poster paper，4-demo paper
    private PaperRank paperRank; // 级别 1-CCF-A，2-CCF-B，3-CCF-C，4-中文CCF-A，5-中文CCF-B，6-无级别

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
    // 工厂方法：用于更新论文信息（序号不变）
    public static PaperDTO createWithAllParams(Integer paperNum, String paperName, String paperSrc, Date paperYear, PaperType paperType, PaperRank paperRank) {
        return new PaperDTO(paperNum, paperName, paperSrc, paperYear, paperType, paperRank);
    }
}