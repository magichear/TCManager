package com.magichear.TCManager.config;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {

    /**
     * 处理 IllegalArgumentException 异常
     *
     * @param ex 捕获的 IllegalArgumentException 异常
     * @return 包含错误信息和异常类型的 ResponseEntity 响应
     */
    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<?> handleIllegalArgument(IllegalArgumentException ex) {
        ex.printStackTrace(); // 打印异常堆栈
        return ResponseEntity.badRequest().body(Map.of(
                "error", ex.getMessage(),
                "exception", ex.getClass().getSimpleName()
        ));
    }

    /**
     * 处理 RuntimeException 异常
     *
     * @param ex 捕获的 RuntimeException 异常
     * @return 包含错误信息和异常类型的 ResponseEntity 响应
     */
    @ExceptionHandler(RuntimeException.class)
    public ResponseEntity<?> handleRuntimeException(RuntimeException ex) {
        ex.printStackTrace();
        return ResponseEntity.badRequest().body(Map.of(
                "error", ex.getMessage(),
                "exception", ex.getClass().getSimpleName()
        ));
    }

    /**
     * 处理通用 Exception 异常
     *
     * @param ex 捕获的 Exception 异常
     * @return 包含错误信息、异常类型和详细信息的 ResponseEntity 响应
     */
    @ExceptionHandler(Exception.class)
    public ResponseEntity<?> handleGeneralException(Exception ex) {
        ex.printStackTrace();
        return ResponseEntity.internalServerError().body(Map.of(
                "error", "服务器错误",  // 比较安全
                "exception", ex.getClass().getSimpleName(),
                "details", ex.getMessage()
        ));
    }
}