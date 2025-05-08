package com.magichear.TCManager.mapper;

import com.magichear.TCManager.dto.PaperDTO;
import com.magichear.TCManager.dto.PublishPaperDTO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface PaperMapper {

    /**
     * 插入论文基本信息
     * @param paper 论文信息
     * @return 插入的行数
     */
    int insertPaper(PaperDTO paper);

    /**
     * 删除论文基本信息
     * @param paperNum 论文序号
     * @return 删除的行数
     */
    int deletePaper(@Param("paperNum") int paperNum);

    /**
     * 更新论文基本信息
     * @param paper 论文信息
     * @return 更新的行数
     */
    int updatePaper(PaperDTO paper);

    /**
     * 按序号查询论文
     * @param paperNum 论文序号
     * @return 论文信息
     */
    PaperDTO selectPaperByNum(@Param("paperNum") int paperNum);

    /**
     * 插入作者关联信息
     * @param author 作者信息
     * @return 插入的行数
     */
    int insertAuthor(PublishPaperDTO author);

    /**
     * 删除作者关联信息
     * @param paperNum 论文序号
     * @param teacherId 教师工号
     * @return 删除的行数
     */
    int deleteAuthor(@Param("paperNum") int paperNum, @Param("teacherId") String teacherId);

    /**
     * 删除某篇论文的所有作者关联信息
     * @param paperNum 论文序号
     * @return 删除的行数
     */
    int deleteAuthorsByPaperNum(@Param("paperNum") int paperNum);

    /**
     * 按论文序号查询所有作者
     * @param paperNum 论文序号
     * @return 作者列表
     */
    List<PublishPaperDTO> selectAuthorsByPaperNum(@Param("paperNum") int paperNum);

    /**
     * 查询某论文是否已有通讯作者
     * @param paperNum 论文序号
     * @return 是否存在通讯作者
     */
    boolean checkCorrespondingAuthorExist(@Param("paperNum") int paperNum);

    /**
     * 查询某论文是否存在重复排名
     * @param paperNum 论文序号
     * @param rank 排名
     * @return 是否存在重复排名
     */
    boolean checkDuplicateRank(@Param("paperNum") int paperNum, @Param("rank") int rank);

    /**
     * 查询某论文是否存在重复排名（忽略指定作者）
     * @param paperNum 论文序号
     * @param rank 排名
     * @param teacherId 教师工号
     * @return 是否存在重复排名
     */
    boolean checkDuplicateRankExcludingAuthor(@Param("paperNum") int paperNum, @Param("rank") int rank, @Param("teacherId") String teacherId);
}