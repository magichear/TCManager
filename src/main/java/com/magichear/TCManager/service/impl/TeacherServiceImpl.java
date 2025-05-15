package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.Course.LectureCourseResponseDTO;
import com.magichear.TCManager.dto.Project.ProjectResponseDTO;
import com.magichear.TCManager.dto.Paper.PublishPaperResponseDTO;
import com.magichear.TCManager.dto.TeacherDTO;
import com.magichear.TCManager.dto.TeacherSummaryDTO;
import com.magichear.TCManager.mapper.TeacherMapper;
import com.magichear.TCManager.service.CourseService;
import com.magichear.TCManager.service.ProjectService;
import com.magichear.TCManager.service.PaperService;
import com.magichear.TCManager.service.TeacherService;

import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.ZoneId;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class TeacherServiceImpl implements TeacherService {

    @Autowired
    private final TeacherMapper teacherMapper;

    @Autowired
    private final CourseService courseService;

    @Autowired
    private final ProjectService projectService;

    @Autowired
    private final PaperService paperService;

    @Override
    public TeacherSummaryDTO getTeacherSummary(String teacherId, int startYear, int endYear) {
        // 查询教师基本信息
        TeacherDTO teacher = teacherMapper.selectTeacherById(teacherId);

        // 查询主讲课程并筛选年份
        Map<Integer, LectureCourseResponseDTO> lectureCourses = courseService.getCoursesByTeacherId(teacherId);
        List<LectureCourseResponseDTO> lectureCourseList = lectureCourses.values().stream()
            .filter(course -> course.getLectureYear() >= startYear && course.getLectureYear() <= endYear)
            .collect(Collectors.toList());

        // 查询承担项目并筛选年份
        Map<Integer, ProjectResponseDTO> projectMap = projectService.getProjectByTeacherId(teacherId);
        List<ProjectResponseDTO> projects = projectMap.values().stream()
            .filter(project -> project.getProject().getProjStartYear() >= startYear && project.getProject().getProjEndYear() <= endYear)
            .collect(Collectors.toList());

        // 查询发表论文并筛选年份
        Map<Integer, PublishPaperResponseDTO> paperMap = paperService.getPapersByTeacherId(teacherId);
        List<PublishPaperResponseDTO> papers = paperMap.values().stream()
            .filter(paper -> {
                int paperYear = paper.getPaperYear().toInstant().atZone(ZoneId.systemDefault()).toLocalDate().getYear();
                return paperYear >= startYear && paperYear <= endYear;
            })
            .collect(Collectors.toList());

        return new TeacherSummaryDTO(teacher, lectureCourseList, projects, papers);
    }
}