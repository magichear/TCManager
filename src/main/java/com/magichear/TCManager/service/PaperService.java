package com.magichear.TCManager.service;

import com.magichear.TCManager.dto.PaperDTO;
import com.magichear.TCManager.dto.PublishPaperDTO;

import java.util.List;

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
    void addPaper(PaperDTO paper, List<PublishPaperDTO> authors);

    /**
     * 更新论文记录
     * @param paper 论文信息
     * @param authors 作者信息列表
     */
    void updatePaper(PaperDTO paper, List<PublishPaperDTO> authors);

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
     * 按论文序号查询所有作者信息
     * @param paperNum 论文序号
     * @return 作者信息列表
     */
    List<PublishPaperDTO> getAuthorsByPaperNum(int paperNum);
}