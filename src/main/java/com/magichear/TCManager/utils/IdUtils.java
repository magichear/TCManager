package com.magichear.TCManager.utils;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.concurrent.atomic.AtomicInteger;

public class IdUtils {

    private static final AtomicInteger counter = new AtomicInteger(0);
    
    /**
     * 生成整数类型ID（用于论文序号）
     * @return 生成的整数ID
     */
    public static Integer generateIntegerId() {
        // 获取当前时间的时间戳（毫秒级）
        long currentTimeMillis = System.currentTimeMillis();
    
        // 获取时间戳的低 5 位
        int timePart = (int) (currentTimeMillis % 100_000); // 保留时间戳的最后 5 位
    
        // 获取计数器的当前值并递增
        int countPart = counter.getAndIncrement() % 10_000; // 保证计数器部分为 4 位
    
        // 将时间部分和计数器部分组合成一个 9 位整数

        return timePart * 10_000 + countPart;
    }

    /**
     * 生成字符串类型的ID（用于项目ID）
     * @param rawData 拼接后的项目信息字符串
     * @return 生成的字符串ID
     */
    public static String generateStringId(String rawData) {
        try {
            // 获取当前日期时间（月日时  这个感觉更不容易重复）
            Calendar calendar = Calendar.getInstance();
            SimpleDateFormat dateFormat = new SimpleDateFormat("MMddHH");
            String datePrefix = dateFormat.format(calendar.getTime());

            // 计算哈希值（SHA-256）
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hashBytes = digest.digest(rawData.getBytes(StandardCharsets.UTF_8));

            // 转换为十六进制字符串
            StringBuilder hexString = new StringBuilder();
            for (byte b : hashBytes) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }

            // 使用完整的哈希值
            String hashPart = hexString.toString();

            // 拼接日期前缀和哈希部分生成字符串ID
            return datePrefix + hashPart;
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error generating string ID: " + e.getMessage(), e);
        }
    }
}