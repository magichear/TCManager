package com.magichear.TCManager.dto.Paper;

import lombok.Data;

@Data
public class PublishPaperDTO {
    private String teacherId;        // 教师工号
    private Integer paperNum;        // 论文序号
    private Integer publishRank;     // 排名
    private Boolean isCorresponding; // 是否通讯作者
}
