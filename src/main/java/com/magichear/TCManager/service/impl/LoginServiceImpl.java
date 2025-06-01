package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.Login.LoginUserDTO;
import com.magichear.TCManager.dto.Login.LoginResponseDTO;
import com.magichear.TCManager.enums.Login.LoginUserType;
import com.magichear.TCManager.service.LoginService;

import org.springframework.stereotype.Service;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

@Service
public class LoginServiceImpl implements LoginService {

    // 暂时先硬编码
    private static final Map<String, String> USERS = new HashMap<>();
    private static final Map<String, LoginUserType> USER_TYPES = new HashMap<>();
    private static final String SALT = "MAGICHEAR_SALT"; // 固定盐值

    static {
        try {
            // 存储哈希加盐后的密码，这里因为不接入数据库，属于附加功能测试阶段，所以先硬编码，若引入数据库可以删掉
            USERS.put("333", hashPassword("333"));
            USERS.put("222", hashPassword("222"));
            USERS.put("111", hashPassword("111"));

            // 存储用户类型
            USER_TYPES.put("333", LoginUserType.GUEST);
            USER_TYPES.put("222", LoginUserType.REGULAR_USER);
            USER_TYPES.put("111", LoginUserType.SUPER_USER);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error initializing user data", e);
        }
    }

    @Override
    public LoginResponseDTO login(LoginUserDTO loginRequest) {
        String hashedInputPassword;
        try {
            // 对用户输入的密码进行哈希加盐
            hashedInputPassword = hashPassword(loginRequest.getPassword());
        } catch (NoSuchAlgorithmException e) {
            return new LoginResponseDTO("登录失败：服务器内部错误", null);
        }

        // 验证用户名和密码
        String storedHashedPassword = USERS.get(loginRequest.getUsername());
        if (storedHashedPassword == null || !storedHashedPassword.equals(hashedInputPassword)) {
            return new LoginResponseDTO("登录失败：用户名或密码错误", null);
        }

        // 获取用户类型
        LoginUserType userType = USER_TYPES.get(loginRequest.getUsername());
        return new LoginResponseDTO("登录成功", userType);
    }

    /**
     * 对密码进行哈希加盐处理
     * @param password 原始密码
     * @return 哈希加盐后的密码
     * @throws NoSuchAlgorithmException 如果哈希算法不可用
     */
    private static String hashPassword(String password) throws NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        String saltedPassword = SALT + password;
        byte[] hash = digest.digest(saltedPassword.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(hash);
    }
}