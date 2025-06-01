USE TCManager;

/*==============================================================*/
/* DBMS name:      MySQL 8.4                                    */
/* Created on:     5/8/2025 10:29:50 AM                         */
/*==============================================================*/

START TRANSACTION;

CREATE DATABASE IF NOT EXISTS TCManager;
USE TCManager;

SET FOREIGN_KEY_CHECKS = 0; -- 禁用外键约束，不然删不掉，后面再启用

drop table if exists COURCE;

drop table if exists IN_CHARGE;

drop table if exists LECTRUE_COURSE;

drop table if exists PAPER;

drop table if exists PROJECTION;

drop table if exists PUBLISH_PAPERS;

drop table if exists TEACHER;

SET FOREIGN_KEY_CHECKS = 1;

/*==============================================================*/
/* Table: COURCE               课程                             */
/*==============================================================*/
create table COURCE
(
   COURSE_ID            varchar(256) not null, /* 课程号   */
   COURSE_NAME          varchar(256),          /* 课程名称 */
   COURSE_HOUR          int,                   /* 学时数   */
   COURSE_TYPE          int,                   /* 课程性质  1-本科生课程，2-研究生课程  */
   primary key (COURSE_ID)
);

/*==============================================================*/
/* Table: IN_CHARGE               承担项目（中间表）             */
/*==============================================================*/
create table IN_CHARGE
(
   TEACHER_ID           char(5) not null,      /* 教师工号   */
   PROJ_ID              varchar(256) not null, /* 项目号     */
   CHARGE_RANK          int,                   /* 排名  1-表示排名第一，以此类推。排名第一即为项目负责人*/
   CHARGE_BALANCE       double,
   primary key (TEACHER_ID, PROJ_ID)
);

/*==============================================================*/
/* Table: LECTRUE_COURSE            主讲课程（中间表）           */
/*==============================================================*/
create table LECTRUE_COURSE
(
   TEACHER_ID           char(5) not null,      /* 教师工号   */
   COURSE_ID            varchar(256) not null, /* 课程号     */
   LECTRUE_YEAR         int,                   /* 年份   */
   LECTRUE_TERM         int,                   /* 学期   1-春季学期，2-夏季学期，3-秋季学期 */
   LECTRUE_HOUR         int,                   /* 承担学时 */
   primary key (TEACHER_ID, COURSE_ID)
);

/*==============================================================*/
/* Table: PAPER              论文                               */
/*==============================================================*/
create table PAPER
(
   PAPER_NUM            int not null,       /* 序号   */
   PAPER_NAME           varchar(256),       /* 论文名称 */
   PAPER_SRC            varchar(256),       /* 发表源 */
   PAPER_YEAR           date,               /* 发表年份 */
   PAPER_TYPE           int,                /* 类型 1-full paper，2-short paper，3-poster paper，4-demo paper */
   PAPER_RANK           int,                /* 级别  1-CCF-A，2-CCF-B，3-CCF-C，4-中文CCF-A，5-中文CCF-B，6-无级别*/
   primary key (PAPER_NUM)
);

/*==============================================================*/
/* Table: PROJECTION                项目                        */
/*==============================================================*/
create table PROJECTION
(
   PROJ_ID              varchar(256) not null, /* 项目号   */
   PROJ_NAME            varchar(256),          /* 项目名称 */
   PROJ_SRC             varchar(256),          /* 项目来源 */
   PROJ_TYPE            int,                   /* 项目类型 1-国家级项目，2-省部级项目，3-市厅级项目，4-企业合作项目，5-其它类型项目 */
   PROJ_BALANCE         double,                /* 总经费   */
   PROJ_START_YEAR      int,                   /* 开始年份 */
   PROJ_END_YEAR        int,                   /* 结束年份 */
   primary key (PROJ_ID)
);

/*==============================================================*/
/* Table: PUBLISH_PAPERS        发表论文（中间表）               */
/*==============================================================*/
create table PUBLISH_PAPERS
(
   TEACHER_ID           char(5) not null,   /* 教师工号   */
   PAPER_NUM            int not null,       /* 论文序号   */
   PUBLISH_RANK         int,                /* 排名  1-表示排名第一，以此类推。排名第一即为第一作者*/
   PUBLISH_ISCORRESPONDING TINYINT(1),      /* 是否通讯作者  替换掉bool类型*/
   primary key (TEACHER_ID, PAPER_NUM)
);

/*==============================================================*/
/* Table: TEACHER                   教师                        */
/*==============================================================*/
create table TEACHER
(
   TEACHER_ID           char(5) not null,   /* 工号   */
   TEACHER_NAME         varchar(256),       /* 姓名   */
   TEACHER_SEX          int,                /* 性别  1-男，2-女 */
   TEACHER_TITLE        int,                /* 职称  1-博士后，2-助教，3-讲师，4-副教授，5-特任教授，6-教授，7-助理研究员，8-特任副研究员，9-副研究员，10-特任研究员，11-研究员 */
   primary key (TEACHER_ID)
);

alter table IN_CHARGE add constraint FK_IN_CHARGE foreign key (TEACHER_ID)
      references TEACHER (TEACHER_ID) on delete restrict on update restrict;

alter table IN_CHARGE add constraint FK_IN_CHARGE2 foreign key (PROJ_ID)
      references PROJECTION (PROJ_ID) on delete restrict on update restrict;

alter table LECTRUE_COURSE add constraint FK_LECTRUE_COURSE foreign key (TEACHER_ID)
      references TEACHER (TEACHER_ID) on delete restrict on update restrict;

alter table LECTRUE_COURSE add constraint FK_LECTRUE_COURSE2 foreign key (COURSE_ID)
      references COURCE (COURSE_ID) on delete restrict on update restrict;

alter table PUBLISH_PAPERS add constraint FK_PUBLISH_PAPERS foreign key (TEACHER_ID)
      references TEACHER (TEACHER_ID) on delete restrict on update restrict;

alter table PUBLISH_PAPERS add constraint FK_PUBLISH_PAPERS2 foreign key (PAPER_NUM)
      references PAPER (PAPER_NUM) on delete restrict on update restrict;

ALTER TABLE LECTRUE_COURSE
ADD CONSTRAINT CHECK_LECTRUE_TERM
CHECK (LECTRUE_TERM IN (1, 2, 3));

COMMIT;

-- CREATE INDEX idx_teacher_year ON LECTRUE_COURSE (TEACHER_ID, LECTRUE_YEAR);

-- CREATE INDEX idx_teacher_id ON IN_CHARGE (TEACHER_ID);

-- CREATE INDEX idx_teacher_publish_year ON PAPER (PAPER_YEAR);


-- 插入教师表数据
INSERT INTO TEACHER (TEACHER_ID, TEACHER_NAME, TEACHER_SEX, TEACHER_TITLE) VALUES
('T0001', '张三', 1, 3), -- 男性，讲师
('T0002', '李四', 2, 4), -- 女性，副教授
('T0003', '王五', 1, 5), -- 男性，特任教授
('T0004', '赵六', 2, 6), -- 女性，教授
('T0005', '孙七', 1, 2), -- 男性，助教
('T0006', '周八', 2, 1), -- 女性，博士后
('T0007', '吴九', 1, 4), -- 男性，副教授
('T0008', '郑十', 2, 3), -- 女性，讲师
('T0009', '冯十一', 1, 5), -- 男性，特任教授
('T0010', '陈十二', 2, 6); -- 女性，教授

-- 插入课程表数据
INSERT INTO COURCE (COURSE_ID, COURSE_NAME, COURSE_HOUR, COURSE_TYPE) VALUES
('C0001', '高等数学', 0, 1), -- 本科生课程
('C0002', '线性代数', 0, 1), -- 本科生课程
('C0003', '概率论与数理统计', 0, 1), -- 本科生课程
('C0004', '数据结构', 0, 1), -- 本科生课程
('C0005', '操作系统', 0, 1), -- 本科生课程
('C0006', '计算机网络', 0, 1), -- 本科生课程
('C0007', '人工智能', 0, 2), -- 研究生课程
('C0008', '机器学习', 0, 2), -- 研究生课程
('C0009', '深度学习', 0, 2), -- 研究生课程
('C0010', '自然语言处理', 0, 2); -- 研究生课程



