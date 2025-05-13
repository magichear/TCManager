package com.magichear.TCManager.controller;

import com.magichear.TCManager.dto.Paper.PaperDTO;
import com.magichear.TCManager.dto.Paper.PublishPaperResponseDTO;
import com.magichear.TCManager.dto.Paper.PaperRequestDTO;
import com.magichear.TCManager.service.PaperService;
import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;
import org.springframework.http.ResponseEntity;
import java.util.*;

/**
 * 论文控制器
 * 提供教师论文发表信息的增、删、改、查功能
 */
@RestController
@RequestMapping("/api/papers")
@RequiredArgsConstructor
public class PaperController {

    @Autowired
    private final PaperService paperService;

    /**
     * 添加论文记录
     * @param paper 论文信息
     * @param authors 作者信息列表
     */
    @PostMapping
    public ResponseEntity<Map<String, Object>> addPaper(@RequestBody PaperRequestDTO paperRequest) {
        Map<String, Object> result = paperService.addPaper(paperRequest.getPaper(), paperRequest.getAuthors());
        return ResponseEntity.ok(result);
    }

    /**
     * 更新论文记录
     * @param paper 论文信息
     * @param authors 作者信息列表
     */
    @PutMapping
    public void updatePaper(@RequestBody PaperRequestDTO paperRequest) {
        paperService.updatePaper(paperRequest.getPaper(), paperRequest.getAuthors());
    }

    /**
     * 删除论文记录
     * @param paperNum 论文序号
     */
    @DeleteMapping("/{paperNum}")
    public void deletePaper(@PathVariable int paperNum) {
        paperService.deletePaper(paperNum);
    }

    /**
     * 按序号查询论文信息
     * @param paperNum 论文序号
     * @return 论文信息
     */
    @GetMapping("/{paperNum}")
    public PaperDTO getPaperByNum(@PathVariable int paperNum) {
        PaperDTO paper = paperService.getPaperByNum(paperNum);
        if (paper == null) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Paper not found");
        }
        return paper;
    }

    /**
     * 按作者ID查询其发表的所有论文信息并封装为嵌套字典
     * @param teacherId 教师工号
     * @return 按序号封装的论文信息嵌套字典
     */
    @GetMapping("/authors/{teacherId}/papers")
    public Map<Integer, PublishPaperResponseDTO> getPapersByTeacherId(@PathVariable String teacherId) {
        return paperService.getPapersByTeacherId(teacherId);
    }

    /**
     * 按论文序号查询所有作者信息
     * @param paperNum 论文序号
     * @return 作者信息列表
     */
    @GetMapping("/{paperNum}/authors")
    public List<PublishPaperResponseDTO> getAuthorsByPaperNum(@PathVariable int paperNum) {
        return paperService.getAuthorsByPaperNum(paperNum);
    }
}