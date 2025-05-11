package com.magichear.TCManager.utils;

public class EnumUtils {
    /**
     * 根据值获取对应的枚举实例
     *
     * @param enumClass 枚举类
     * @param value     枚举值
     * @param <T>       枚举类型
     * @return 枚举实例
     * @throws IllegalArgumentException 如果未找到对应的枚举实例
     */
    public static <T extends Enum<T>> T fromValue(Class<T> enumClass, int value) {
        for (T enumConstant : enumClass.getEnumConstants()) {
            try {
                int enumValue = (int) enumClass.getMethod("getValue").invoke(enumConstant);
                if (enumValue == value) {
                    return enumConstant;
                }
            } catch (Exception e) {
                throw new IllegalArgumentException("Failed to access getValue method for enum: " + enumClass.getName(), e);
            }
        }
        throw new IllegalArgumentException("No enum constant for value: " + value + " in " + enumClass.getName());
    }

    /**
     * 校验枚举值是否合法
     *
     * @param enumClass 枚举类
     * @param value     枚举值
     * @param <T>       枚举类型
     * @return 是否合法
     */
    public static <T extends Enum<T>> boolean isValidEnumValue(Class<T> enumClass, int value) {
        for (T enumConstant : enumClass.getEnumConstants()) {
            try {
                int enumValue = (int) enumClass.getMethod("getValue").invoke(enumConstant);
                if (enumValue == value) {
                    return true;
                }
            } catch (Exception e) {
                throw new IllegalArgumentException("Failed to access getValue method for enum: " + enumClass.getName(), e);
            }
        }
        return false;
    }
}