package com.magichear.TCManager.dto.Login;

import com.magichear.TCManager.enums.LoginUserType;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * 登录用户信息（系统登录控制）
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class LoginUserDTO {
    private String username;        // 用户名
    private String password;        // 密码
    private LoginUserType userType; // 用户类型

    /**
     * 仅通过用户名和密码构造（用于登录请求）
     * @param username 用户名
     * @param password 密码
     */
    public LoginUserDTO(String username, String password) {
        this.username = username;
        this.password = password;
        this.userType = LoginUserType.GUEST; // 默认访客
    }
}