package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.PaperDTO;
import com.magichear.TCManager.dto.PublishPaperDTO;
import com.magichear.TCManager.enums.PaperRank;
import com.magichear.TCManager.enums.PaperType;
import com.magichear.TCManager.mapper.PaperMapper;
import com.magichear.TCManager.service.PaperService;
import com.magichear.TCManager.utils.EnumUtils;

import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.*;

@Service
@RequiredArgsConstructor
public class PaperServiceImpl implements PaperService {

    @Autowired
    private final PaperMapper paperMapper;

    @Override
    @Transactional
    public Map<String, Object> addPaper(PaperDTO paper, List<PublishPaperDTO> authors) {
        // 使用工厂方法生成带有自动生成序号的 PaperDTO
        PaperDTO newPaper = PaperDTO.createWithoutNum(paper);
    
        // 验证论文和作者信息
        validatePaper(newPaper, authors);
    
        // 插入论文信息
        paperMapper.insertPaper(newPaper);
    
        // 插入作者信息
        for (PublishPaperDTO author : authors) {
            author.setPaperNum(newPaper.getPaperNum()); // 设置作者关联的论文序号
            paperMapper.insertAuthor(author);
        }
    
        // 构造返回结果
        Map<String, Object> result = new HashMap<>();
        result.put("paper", newPaper); // 插入的论文信息
        result.put("authors", authors); // 插入的作者信息
    
        return result;
    }

    @Override
    @Transactional
    public void updatePaper(PaperDTO paper, List<PublishPaperDTO> authors) {
        validatePaper(paper, authors);
        paperMapper.updatePaper(paper);
        paperMapper.deleteAuthor(paper.getPaperNum(), null);
        for (PublishPaperDTO author : authors) {
            paperMapper.insertAuthor(author);
        }
    }

    @Override
    @Transactional
    public void deletePaper(int paperNum) {
        paperMapper.deleteAuthor(paperNum, null);
        paperMapper.deletePaper(paperNum);
    }

    @Override
    public PaperDTO getPaperByNum(int paperNum) {
        return paperMapper.selectPaperByNum(paperNum);
    }

    @Override
    public List<PublishPaperDTO> getAuthorsByPaperNum(int paperNum) {
        return paperMapper.selectAuthorsByPaperNum(paperNum);
    }

    /**
     * 校验论文信息的合法性
     * @param paper 论文信息
     * @param authors 作者信息列表
     */
    private void validatePaper(PaperDTO paper, List<PublishPaperDTO> authors) {
        if (!EnumUtils.isValidEnumValue(PaperType.class, paper.getPaperType().getValue())) {
            throw new IllegalArgumentException("Invalid paper type: " + paper.getPaperType());
        }
        if (!EnumUtils.isValidEnumValue(PaperRank.class, paper.getPaperRank().getValue())) {
            throw new IllegalArgumentException("Invalid paper rank: " + paper.getPaperRank());
        }
    
        boolean hasCorrespondingAuthor = false;
        Set<Integer> publishRanks = new HashSet<>();
    
        for (PublishPaperDTO author : authors) {
            // 检查是否有重复的 publishRank
            if (!publishRanks.add(author.getPublishRank())) {
                throw new IllegalArgumentException("Duplicate author rank detected in request. PaperNum: " + paper.getPaperNum() +
                        ", Rank: " + author.getPublishRank() + ", TeacherId: " + author.getTeacherId());
            }
    
            // 检查是否有多个通讯作者
            if (author.getIsCorresponding()) {
                if (hasCorrespondingAuthor) {
                    throw new IllegalArgumentException("Only one corresponding author is allowed. Duplicate found for teacherId: " + author.getTeacherId());
                }
                hasCorrespondingAuthor = true;
            }
        }
    
        if (!hasCorrespondingAuthor) {
            throw new IllegalArgumentException("No corresponding author found for paperNum: " + paper.getPaperNum());
        }
    }
}