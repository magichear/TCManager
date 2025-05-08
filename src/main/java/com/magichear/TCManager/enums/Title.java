package com.magichear.TCManager.enums;

import com.magichear.TCManager.utils.EnumUtils;
import lombok.Getter;

/**
 * 表示教师的职称：1-博士后，2-助教，3-讲师，4-副教授，5-特任教授，6-教授，7-助理研究员，
 *                8-特任副研究员，9-副研究员，10-特任研究员，11-研究员
 */
@Getter
public enum Title {
    POSTDOC(1),                         // 博士后
    ASSISTANT(2),                       // 助教
    LECTURER(3),                        // 讲师
    ASSOCIATE_PROFESSOR(4),             // 副教授
    SPECIAL_PROFESSOR(5),               // 特任教授
    PROFESSOR(6),                       // 教授
    ASSISTANT_RESEARCHER(7),            // 助理研究员
    SPECIAL_ASSOCIATE_RESEARCHER(8),    // 特任副研究员
    ASSOCIATE_RESEARCHER(9),            // 副研究员
    SPECIAL_RESEARCHER(10),             // 特任研究员
    RESEARCHER(11);                     // 研究员

    private final int value;

    Title(int value) {
        this.value = value;
    }

    public static Title fromValue(int value) {
        return EnumUtils.fromValue(Title.class, value);
    }
}