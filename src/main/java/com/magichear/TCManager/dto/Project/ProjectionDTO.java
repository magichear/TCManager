package com.magichear.TCManager.dto.Project;

import com.magichear.TCManager.enums.Project.ProjType;
import com.magichear.TCManager.utils.IdUtils;

import lombok.Data;

/**
 * 项目表 (PROJECTION)
 */
@Data
public class ProjectionDTO {
    private String projId;          // 项目号
    private String projName;        // 项目名称
    private String projSrc;         // 项目来源
    private ProjType projType;      // 项目类型
    private Double projBalance=0.0;     // 总经费
    private Integer projStartYear;  // 开始年份
    private Integer projEndYear;    // 结束年份

    /**
     * 工厂方法：根据项目信息生成 ProjectionDTO 对象
     * @param project 项目信息
     * @return 构造好的 ProjectionDTO 对象
     */
    public static ProjectionDTO createWithoutId(ProjectionDTO project) {
        // 提取项目信息
        String projName = project.getProjName();
        String projSrc = project.getProjSrc();
        ProjType projType = project.getProjType();
        Double projBalance = project.getProjBalance();
        Integer projStartYear = project.getProjStartYear();
        Integer projEndYear = project.getProjEndYear();

        // 拼接项目信息为字符串
        String rawData = projName + projSrc + projType + projBalance + projStartYear + projEndYear;

        // 构造新的 ProjectionDTO 对象
        ProjectionDTO newProject = new ProjectionDTO();
        newProject.setProjId(IdUtils.generateStringId(rawData)); // 根据哈希与时间自动生成项目ID
        newProject.setProjName(projName);
        newProject.setProjSrc(projSrc);
        newProject.setProjType(projType);
        newProject.setProjBalance(projBalance);
        newProject.setProjStartYear(projStartYear);
        newProject.setProjEndYear(projEndYear);

        return newProject;
    }
}