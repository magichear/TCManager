package com.magichear.TCManager.enums;

/**
 * 表示论文的级别：1-CCF-A，2-CCF-B，3-CCF-C，4-中文CCF-A，5-中文CCF-B，6-无级别
 */
public enum PaperRank {
    CCF_A(1),          // CCF-A级
    CCF_B(2),          // CCF-B级
    CCF_C(3),          // CCF-C级
    CHINESE_CCF_A(4),  // 中文CCF-A级
    CHINESE_CCF_B(5),  // 中文CCF-B级
    NONE(6);           // 无级别

    private final int value;

    PaperRank(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}