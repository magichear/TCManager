package com.magichear.TCManager.enums;

import lombok.Getter;

/**
 * 表示学期的类型：1-春季学期，2-夏季学期，3-秋季学期
 */
@Getter
public enum Sex {
    MAN(1),     // 男
    WOMAN(2);   // 女

    private final int value;

    Sex(int value) {
        this.value = value;
    }
}
