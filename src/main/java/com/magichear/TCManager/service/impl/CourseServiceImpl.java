package com.magichear.TCManager.service.impl;

import com.magichear.TCManager.mapper.CourseMapper;
import com.magichear.TCManager.service.CourseService;
import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class CourseServiceImpl implements CourseService {

    @Autowired
    private final CourseMapper courseMapper;
}