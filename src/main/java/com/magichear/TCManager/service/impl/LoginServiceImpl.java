package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.Login.LoginUserDTO;
import com.magichear.TCManager.dto.Login.LoginResponseDTO;
import com.magichear.TCManager.enums.Login.LoginUserType;
import com.magichear.TCManager.service.LoginService;

import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;

@Service
public class LoginServiceImpl implements LoginService {

    // 暂时先硬编码
    private static final Map<String, LoginUserDTO> USERS = new HashMap<>();

    static {
        USERS.put("333", new LoginUserDTO("333", "333", LoginUserType.GUEST));
        USERS.put("222", new LoginUserDTO("222", "222", LoginUserType.REGULAR_USER));
        USERS.put("111", new LoginUserDTO("111", "111", LoginUserType.SUPER_USER));
    }

    @Override
    public LoginResponseDTO login(LoginUserDTO loginRequest) {
        LoginUserDTO user = USERS.get(loginRequest.getUsername());
        if (user == null || !user.getPassword().equals(loginRequest.getPassword())) {
            return new LoginResponseDTO("登录失败：用户名或密码错误", null);
        }
        return new LoginResponseDTO("登录成功", user.getUserType());
    }
}