package com.magichear.TCManager.enums.Paper;

import lombok.Getter;

import org.apache.ibatis.type.MappedTypes;

import com.magichear.TCManager.utils.EnumUtils;
/**
 * 表示论文的类型：1-full paper，2-short paper，3-poster paper，4-demo paper
 */
@Getter
@MappedTypes(PaperType.class)
public enum PaperType {
    FULL_PAPER(1),   // Full Paper
    SHORT_PAPER(2),  // Short Paper
    POSTER_PAPER(3), // Poster Paper
    DEMO_PAPER(4);   // Demo Paper

    private final int value;

    PaperType(int value) {
        this.value = value;
    }

    public static PaperType fromValue(int value) {
        return EnumUtils.fromValue(PaperType.class, value);
    }
}