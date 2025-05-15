package com.magichear.TCManager.controller;

import com.magichear.TCManager.dto.Login.LoginUserDTO;
import com.magichear.TCManager.dto.Login.LoginResponseDTO;
import com.magichear.TCManager.service.LoginService;

import lombok.RequiredArgsConstructor;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/**
 * 登录控制器
 */
@RestController
@RequestMapping("/api/login")
@RequiredArgsConstructor
public class LoginController {

    private static final Logger logger = LoggerFactory.getLogger(LoginController.class);

    @Autowired
    private final LoginService loginService;

    /**
     * 用户登录
     * @param loginRequest 登录请求
     * @return 登录响应
     */
    @PostMapping
    public LoginResponseDTO login(@RequestBody LoginUserDTO loginRequest) {
        // 记录接收到的登录请求
        if (logger.isDebugEnabled()) {
            logger.debug("Received login request: {}", loginRequest);
        }

        try {
            logger.info("Processing login request for username: {}", loginRequest.getUsername());
            LoginResponseDTO response = loginService.login(loginRequest);
            logger.info("Login successful for username: {}", loginRequest.getUsername());
            return response;
        } catch (Exception e) {
            logger.error("Login failed for username: {}", loginRequest.getUsername(), e);
            throw e; // 继续抛出异常，交由全局异常处理器处理
        }
    }

    /**
     * 返回 404 页面
     * @return 404 HTML 页面
     */
    @GetMapping("/404")
    public ResponseEntity<Void> notFoundPage() {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
                .header("Location", "src/main/resources/static/404.html")
                .build();
    }
}