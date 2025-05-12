package com.magichear.TCManager.service;

import com.magichear.TCManager.dto.Login.LoginUserDTO;
import com.magichear.TCManager.dto.Login.LoginResponseDTO;

/**
 * 登录服务接口
 */
public interface LoginService {
    /**
     * 用户登录
     * @param loginRequest 登录请求
     * @return 登录响应
     */
    LoginResponseDTO login(LoginUserDTO loginRequest);
}