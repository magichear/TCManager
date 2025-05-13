package com.magichear.TCManager.enums.Login;
import org.apache.ibatis.type.MappedTypes;

import com.magichear.TCManager.utils.EnumUtils;
import lombok.Getter;
/**
 * 表示用户的权限类型: 1-管理员, 2-普通用户, 3-访客
 */
@Getter
@MappedTypes(LoginUserType.class)
public enum LoginUserType {
    SUPER_USER(1), // 管理员
    REGULAR_USER(2),  // 普通用户
    GUEST(3); // 访客

    private final int value;

    LoginUserType(int value) {
        this.value = value;
    }

    public static LoginUserType fromValue(int value) {
        return EnumUtils.fromValue(LoginUserType.class, value);
    }
}
