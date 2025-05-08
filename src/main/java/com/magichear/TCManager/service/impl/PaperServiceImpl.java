package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.mapper.PaperMapper;
import com.magichear.TCManager.service.PaperService;
import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
@RequiredArgsConstructor
public class PaperServiceImpl implements PaperService {

    @Autowired
    private final PaperMapper paperMapper;
}