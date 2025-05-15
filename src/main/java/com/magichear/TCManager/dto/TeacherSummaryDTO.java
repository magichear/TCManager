package com.magichear.TCManager.dto;

import com.magichear.TCManager.dto.Course.LectureCourseResponseDTO;
import com.magichear.TCManager.dto.Project.ProjectResponseDTO;
import com.magichear.TCManager.dto.Paper.PublishPaperResponseDTO;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.List;

/**
 * 教师综合信息 DTO
 */
@Data
@AllArgsConstructor
public class TeacherSummaryDTO {
    private TeacherDTO teacher; // 教师信息
    private List<LectureCourseResponseDTO> lectureCourses; // 主讲课程信息
    private List<ProjectResponseDTO> projects; // 承担项目信息
    private List<PublishPaperResponseDTO> papers; // 发表论文信息
}