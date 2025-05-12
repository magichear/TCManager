package com.magichear.TCManager.controller;

import com.magichear.TCManager.dto.Login.LoginUserDTO;
import com.magichear.TCManager.dto.Login.LoginResponseDTO;
import com.magichear.TCManager.service.LoginService;

import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * 登录控制器
 */
@RestController
@RequestMapping("/api/login")
@RequiredArgsConstructor
public class LoginController {

    @Autowired
    private final LoginService loginService;

    /**
     * 用户登录
     * @param loginRequest 登录请求
     * @return 登录响应
     */
    @PostMapping
    public LoginResponseDTO login(@RequestBody LoginUserDTO loginRequest) {
        return loginService.login(loginRequest);
    }
}