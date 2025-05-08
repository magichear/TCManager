package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.dto.ProjectRequestDTO;
import com.magichear.TCManager.enums.ProjType;
import com.magichear.TCManager.mapper.ProjectMapper;
import com.magichear.TCManager.service.ProjectService;
import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ProjectServiceImpl implements ProjectService {

    @Autowired
    private final ProjectMapper projectMapper;
}