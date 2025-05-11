package com.magichear.TCManager.mapper;

import com.magichear.TCManager.dto.ProjectionDTO;
import com.magichear.TCManager.dto.InChargeDTO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface ProjectMapper {

    /**
     * 插入项目基本信息
     * @param project 项目信息
     * @return 插入的行数
     */
    int insertProject(ProjectionDTO project);

    /**
     * 删除项目基本信息
     * @param projId 项目号
     * @return 删除的行数
     */
    int deleteProject(@Param("projId") String projId);

    /**
     * 更新项目基本信息
     * @param project 项目信息
     * @return 更新的行数
     */
    int updateProject(ProjectionDTO project);


    /**
     * 按项目号查询项目
     * @param projId 项目号
     * @return 项目信息
     */
    ProjectionDTO selectProjectById(@Param("projId") String projId);

    /**
     * 插入教师承担信息
     * @param charge 承担信息
     * @return 插入的行数
     */
    int insertCharge(InChargeDTO charge);

    /**
     * 删除教师承担信息
     * @param projId 项目号
     * @param teacherId 教师工号
     * @return 删除的行数
     */
    int deleteCharge(@Param("projId") String projId, @Param("teacherId") String teacherId);

    /**
     * 按项目号查询所有承担记录
     * @param projId 项目号
     * @return 承担记录列表
     */
    List<InChargeDTO> selectChargesById(@Param("projId") String projId, @Param("teacherId") String teacherId);

    /**
     * 查询某项目是否存在重复排名
     * @param projId 项目号
     * @param rank 排名
     * @return 是否存在重复排名
     */
    boolean checkProjectRankDuplicate(@Param("projId") String projId, @Param("rank") int rank, @Param("teacherId") String teacherId);

    /**
     * 计算某项目所有教师的承担经费总和
     * @param projId 项目号
     * @return 经费总和
     */
    Double calculateTotalCharge(@Param("projId") String projId);
}