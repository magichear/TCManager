package com.magichear.TCManager.dto.Login;

import com.magichear.TCManager.enums.LoginUserType;
import lombok.AllArgsConstructor;
import lombok.Data;

/**
 * 登录响应类
 */
@Data
@AllArgsConstructor
public class LoginResponseDTO {
    private String message;         // 登录结果消息
    private LoginUserType role;     // 用户权限
}