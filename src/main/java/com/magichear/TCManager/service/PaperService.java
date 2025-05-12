package com.magichear.TCManager.service;

import com.magichear.TCManager.dto.PaperDTO;
import com.magichear.TCManager.dto.PublishPaperResponseDTO;

import java.util.List;
import java.util.Map;

/**
 * 提供教师论文发表信息的增、删、改、查功能。
 * 输入时要求检查：一篇论文只能有一位通讯作者，论文的作者排名不能有重复，
 *                论文的类型和级别只能在约定的取值集合中选取。
 */
public interface PaperService {

    /**
     * 添加论文记录
     * @param paper 论文信息
     * @param authors 作者信息列表
     */
    Map<String, Object> addPaper(PaperDTO paper, List<PublishPaperResponseDTO> authors);

    /**
     * 更新论文记录
     * @param paper 论文信息
     * @param authors 作者信息列表
     */
    void updatePaper(PaperDTO paper, List<PublishPaperResponseDTO> authors);

    /**
     * 删除论文记录
     * @param paperNum 论文序号
     */
    void deletePaper(int paperNum);

    /**
     * 按序号查询论文信息
     * @param paperNum 论文序号
     * @return 论文信息
     */
    PaperDTO getPaperByNum(int paperNum);

    /**
     * 按作者ID查询其发表的所有论文信息并封装为嵌套字典
     * @param teacherId 教师工号
     * @return 按序号封装的论文信息嵌套字典
     */
    Map<Integer, PublishPaperResponseDTO> getPapersByTeacherId(String teacherId);

    /**
     * 按论文序号查询所有作者信息
     * @param paperNum 论文序号
     * @return 作者信息列表
     */
    List<PublishPaperResponseDTO> getAuthorsByPaperNum(int paperNum);
}