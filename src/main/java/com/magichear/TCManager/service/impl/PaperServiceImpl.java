package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.Paper.PaperDTO;
import com.magichear.TCManager.dto.Paper.PublishPaperDTO;
import com.magichear.TCManager.dto.Paper.PublishPaperResponseDTO;
import com.magichear.TCManager.enums.Paper.PaperRank;
import com.magichear.TCManager.enums.Paper.PaperType;
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
    public Map<String, Object> addPaper(PaperDTO paper, List<PublishPaperResponseDTO> authors) {
        // 使用工厂方法生成带有自动生成序号的 PaperDTO
        PaperDTO newPaper = PaperDTO.createWithoutNum(paper);
    
        // 验证论文和作者信息
        validatePaper(newPaper, authors);
    
        // 插入论文信息
        paperMapper.insertPaper(newPaper);
    
        // 插入作者信息
        for (PublishPaperResponseDTO author : authors) {
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
    public void updatePaper(PaperDTO paper, List<PublishPaperResponseDTO> authors) {
        // 删除对应论文的所有信息
        paperMapper.deleteAuthor(paper.getPaperNum(), null);
        paperMapper.deletePaper(paper.getPaperNum());
    
        // 验证论文和作者信息
        validatePaper(paper, authors);
    
        // 插入新的论文信息
        paperMapper.insertPaper(paper);
    
        // 插入新的作者信息
        for (PublishPaperResponseDTO author : authors) {
            author.setPaperNum(paper.getPaperNum()); // 设置作者关联的论文序号
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
    public Map<Integer, PublishPaperResponseDTO> getPapersByTeacherId(String teacherId) {
        // 查询作者发表的所有论文基本信息
        List<PublishPaperDTO> basicPaperInfoList = paperMapper.selectPapersByTeacherId(teacherId);
    
        // 封装结果字典
        Map<Integer, PublishPaperResponseDTO> result = new HashMap<>();
        int idx = 0;
        for (PublishPaperDTO basicInfo : basicPaperInfoList) {
            // 查询每篇论文的详细信息
            PaperDTO paper = paperMapper.selectPaperByNum(basicInfo.getPaperNum());
    
            if (paper != null) {
                PublishPaperResponseDTO publishPaperResponseDTO = new PublishPaperResponseDTO(
                    basicInfo.getTeacherId(), 
                    paper.getPaperNum(), 
                    paper.getPaperName(),
                    paper.getPaperSrc(), 
                    paper.getPaperYear(), 
                    paper.getPaperType(), 
                    paper.getPaperRank(), 
                    basicInfo.getPublishRank(), 
                    basicInfo.getIsCorresponding()
                );
    
                result.put(idx, publishPaperResponseDTO);
                ++idx;
            }
        }
    
        return result;
    }

    @Override
    public List<PublishPaperResponseDTO> getAuthorsByPaperNum(int paperNum) {
        return paperMapper.selectAuthorsByPaperNum(paperNum);
    }

    /**
     * 校验论文信息的合法性
     * @param paper 论文信息
     * @param authors 作者信息列表
     */
    private void validatePaper(PaperDTO paper, List<PublishPaperResponseDTO> authors) {
        if (!EnumUtils.isValidEnumValue(PaperType.class, paper.getPaperType().getValue())) {
            throw new IllegalArgumentException("Invalid paper type: " + paper.getPaperType());
        }
        if (!EnumUtils.isValidEnumValue(PaperRank.class, paper.getPaperRank().getValue())) {
            throw new IllegalArgumentException("Invalid paper rank: " + paper.getPaperRank());
        }
    
        boolean hasCorrespondingAuthor = false;
        Set<Integer> publishRanks = new HashSet<>();
    
        for (PublishPaperResponseDTO author : authors) {
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
    
        // 如果没有设置通讯作者，自动将排名第一的作者设置为通讯作者
        if (!hasCorrespondingAuthor) {
            for (PublishPaperResponseDTO author : authors) {
                if (author.getPublishRank() == 1) {
                    author.setIsCorresponding(true); // 设置为通讯作者
                    hasCorrespondingAuthor = true;
                    break;
                }
            }
    
            // 如果没有找到排名第一的作者，抛出异常（理论上不应该发生）
            if (!hasCorrespondingAuthor) {
                throw new IllegalArgumentException("No corresponding author found or no author with rank 1 for paperNum: " + paper.getPaperNum());
            }
        }
    }
}