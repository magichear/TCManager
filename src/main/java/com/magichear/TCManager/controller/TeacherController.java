package com.magichear.TCManager.controller;

import com.magichear.TCManager.dto.TeacherSummaryDTO;
import com.magichear.TCManager.service.TeacherService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/teacher")
public class TeacherController {

    @Autowired
    private TeacherService teacherService;

    /**
     * 查询教师的教学科研情况
     * @param teacherId 教师工号
     * @param startYear 开始年份
     * @param endYear 结束年份
     * @return 教师综合信息 DTO
     */
    @GetMapping("/summary")
    public TeacherSummaryDTO getTeacherSummary(
            @RequestParam String teacherId,
            @RequestParam int startYear,
            @RequestParam int endYear) {
        return teacherService.getTeacherSummary(teacherId, startYear, endYear);
    }
}