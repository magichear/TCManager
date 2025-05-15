package com.magichear.TCManager.controller;

import com.magichear.TCManager.dto.Paper.PaperDTO;
import com.magichear.TCManager.dto.Paper.PublishPaperResponseDTO;
import com.magichear.TCManager.dto.Paper.PaperRequestDTO;
import com.magichear.TCManager.service.PaperService;
import lombok.RequiredArgsConstructor;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
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

    private static final Logger logger = LoggerFactory.getLogger(PaperController.class);

    @Autowired
    private final PaperService paperService;

    /**
     * 添加论文记录
     * @param paperRequest 论文信息及作者信息
     */
    @PostMapping
    public ResponseEntity<Map<String, Object>> addPaper(@RequestBody PaperRequestDTO paperRequest) {
        logger.info("Received request to add paper: {}", paperRequest.getPaper().getPaperName());
        Map<String, Object> result = paperService.addPaper(paperRequest.getPaper(), paperRequest.getAuthors());
        logger.info("Paper added successfully: {}", result.get("paper"));
        return ResponseEntity.ok(result);
    }

    /**
     * 更新论文记录
     * @param paperRequest 论文信息及作者信息
     */
    @PutMapping
    public void updatePaper(@RequestBody PaperRequestDTO paperRequest) {
        logger.info("Received request to update paper: {}", paperRequest.getPaper().getPaperNum());
        paperService.updatePaper(paperRequest.getPaper(), paperRequest.getAuthors());
        logger.info("Paper updated successfully: {}", paperRequest.getPaper().getPaperNum());
    }

    /**
     * 删除论文记录
     * @param paperNum 论文序号
     */
    @DeleteMapping("/{paperNum}")
    public void deletePaper(@PathVariable int paperNum) {
        logger.info("Received request to delete paper with number: {}", paperNum);
        paperService.deletePaper(paperNum);
        logger.info("Paper deleted successfully: {}", paperNum);
    }

    /**
     * 按序号查询论文信息
     * @param paperNum 论文序号
     * @return 论文信息
     */
    @GetMapping("/{paperNum}")
    public PaperDTO getPaperByNum(@PathVariable int paperNum) {
        logger.info("Received request to fetch paper by number: {}", paperNum);
        PaperDTO paper = paperService.getPaperByNum(paperNum);
        if (paper == null) {
            logger.warn("Paper not found with number: {}", paperNum);
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Paper not found");
        }
        logger.info("Fetched paper successfully: {}", paper.getPaperName());
        return paper;
    }

    /**
     * 按作者ID查询其发表的所有论文信息并封装为嵌套字典
     * @param teacherId 教师工号
     * @return 按序号封装的论文信息嵌套字典
     */
    @GetMapping("/authors/{teacherId}/papers")
    public Map<Integer, PublishPaperResponseDTO> getPapersByTeacherId(@PathVariable String teacherId) {
        logger.info("Received request to fetch papers for teacher ID: {}", teacherId);
        Map<Integer, PublishPaperResponseDTO> papers = paperService.getPapersByTeacherId(teacherId);
        logger.info("Fetched {} papers for teacher ID: {}", papers.size(), teacherId);
        return papers;
    }

    /**
     * 按论文序号查询所有作者信息
     * @param paperNum 论文序号
     * @return 作者信息列表
     */
    @GetMapping("/{paperNum}/authors")
    public List<PublishPaperResponseDTO> getAuthorsByPaperNum(@PathVariable int paperNum) {
        logger.info("Received request to fetch authors for paper number: {}", paperNum);
        List<PublishPaperResponseDTO> authors = paperService.getAuthorsByPaperNum(paperNum);
        logger.info("Fetched {} authors for paper number: {}", authors.size(), paperNum);
        return authors;
    }
}