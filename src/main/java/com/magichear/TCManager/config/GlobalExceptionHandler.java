package com.magichear.TCManager.config;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<?> handleIllegalArgument(IllegalArgumentException ex) {
        ex.printStackTrace(); // 打印异常堆栈
        return ResponseEntity.badRequest().body(Map.of(
                "error", ex.getMessage(),
                "exception", ex.getClass().getSimpleName()
        ));
    }

    @ExceptionHandler(RuntimeException.class)
    public ResponseEntity<?> handleRuntimeException(RuntimeException ex) {
        ex.printStackTrace(); // 打印异常堆栈
        return ResponseEntity.badRequest().body(Map.of(
                "error", ex.getMessage(),
                "exception", ex.getClass().getSimpleName()
        ));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<?> handleGeneralException(Exception ex) {
        ex.printStackTrace(); // 打印异常堆栈
        return ResponseEntity.internalServerError().body(Map.of(
                "error", "服务器错误",
                "exception", ex.getClass().getSimpleName(),
                "details", ex.getMessage()
        ));
    }
}
