package com.magichear.TCManager.service;

import com.magichear.TCManager.dto.TeacherSummaryDTO;

public interface TeacherService {
    /**
     * 查询教师的教学科研情况
     * @param teacherId 教师工号
     * @param startYear 开始年份
     * @param endYear 结束年份
     * @return 教师综合信息 DTO
     */
    TeacherSummaryDTO getTeacherSummary(String teacherId, int startYear, int endYear);
}