package com.magichear.TCManager.enums;

import lombok.Getter;

/**
 * 表示学期的类型：1-春季学期，2-夏季学期，3-秋季学期
 */
@Getter
public enum Term {
    SPRING(1), // 春季学期
    SUMMER(2), // 夏季学期
    AUTUMN(3); // 秋季学期

    private final int value;

    Term(int value) {
        this.value = value;
    }
}