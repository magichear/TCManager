package com.magichear.TCManager.enums;

import lombok.Getter;
import com.magichear.TCManager.utils.EnumUtils;
/**
 * 表示学期的类型：1-男，2-女
 */
@Getter
public enum Sex {
    MAN(1),     // 男
    WOMAN(2);   // 女

    private final int value;

    Sex(int value) {
        this.value = value;
    }

    public static Sex fromValue(int value) {
        return EnumUtils.fromValue(Sex.class, value);
    }
}
