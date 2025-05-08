package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.PaperDTO;
import com.magichear.TCManager.dto.PublishPaperDTO;
import com.magichear.TCManager.enums.PaperRank;
import com.magichear.TCManager.enums.PaperType;
import com.magichear.TCManager.mapper.PaperMapper;
import com.magichear.TCManager.service.PaperService;
import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Service
@RequiredArgsConstructor
public class PaperServiceImpl implements PaperService {

    @Autowired
    private final PaperMapper paperMapper;

    @Override
    @Transactional
    public void addPaper(PaperDTO paper, List<PublishPaperDTO> authors) {
        validatePaper(paper, authors);
        paperMapper.insertPaper(paper);
        for (PublishPaperDTO author : authors) {
            paperMapper.insertAuthor(author);
        }
    }

    @Override
    @Transactional
    public void updatePaper(PaperDTO paper, List<PublishPaperDTO> authors) {
        validatePaper(paper, authors);
        paperMapper.updatePaper(paper);
        paperMapper.deleteAuthorsByPaperNum(paper.getPaperNum());
        for (PublishPaperDTO author : authors) {
            paperMapper.insertAuthor(author);
        }
    }

    @Override
    @Transactional
    public void deletePaper(int paperNum) {
        paperMapper.deleteAuthorsByPaperNum(paperNum);
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
        if (!isValidEnumValue(PaperType.class, paper.getPaperType().getValue())) {
            throw new IllegalArgumentException("Invalid paper type: " + paper.getPaperType());
        }
        if (!isValidEnumValue(PaperRank.class, paper.getPaperRank().getValue())) {
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

    /**
     * 校验枚举值是否合法
     * @param enumClass 枚举类
     * @param value 枚举值
     * @param <E> 枚举类型
     * @return 是否合法
     */
    private <E extends Enum<E>> boolean isValidEnumValue(Class<E> enumClass, int value) {
        for (E enumConstant : enumClass.getEnumConstants()) {
            if (((Enum<?>) enumConstant).ordinal() + 1 == value) {
                return true;
            }
        }
        return false;
    }
}