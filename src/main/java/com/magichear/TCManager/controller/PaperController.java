package com.magichear.TCManager.controller;

import com.magichear.TCManager.service.PaperService;
import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;


/**
 * 论文控制器
 * 提供教师论文发表信息的增、删、改、查功能
 */
@RestController
@RequestMapping("/api/papers")
@RequiredArgsConstructor
public class PaperController {
    @Autowired
    private final PaperService paperService;

}