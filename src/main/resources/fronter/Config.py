import datetime


class Config:

    @staticmethod
    def get_value(mMap, key):
        """
        前端应对制杖Jackson的方法
        [CAUTION] 所有从本类中取出的映射都必须通过该方法来获取实际值
        """
        return mMap.get(key, 1) - 1

    # 后端 API 基础 URL
    BASE_URL = "http://localhost:8080/api"

    # 动态生成年份选项
    current_year = datetime.datetime.now().year
    year_choices = [str(year) for year in range(1970, current_year + 1)]

    # 性别映射
    gender = {
        "男": 1,
        "女": 2,
    }
    gender_keys = list(gender.keys())

    # 教师职称映射
    teacher_title = {
        "博士后": 1,
        "助教": 2,
        "讲师": 3,
        "副教授": 4,
        "特任教授": 5,
        "教授": 6,
        "助理研究员": 7,
        "特任副研究员": 8,
        "副研究员": 9,
        "特任研究员": 10,
        "研究员": 11,
    }
    teacher_title_keys = list(teacher_title.keys())

    # 论文类型映射
    pp_type = {
        "Full Paper": 1,
        "Short Paper": 2,
        "Poster Paper": 3,
        "Demo Paper": 4,
    }
    pp_type_keys = list(pp_type.keys())

    # 论文级别映射
    pp_rank = {
        "CCF-A": 1,
        "CCF-B": 2,
        "CCF-C": 3,
        "中文CCF-A": 4,
        "中文CCF-B": 5,
        "无级别": 6,
    }
    pp_rank_keys = list(pp_rank.keys())

    # 项目类型映射
    project_type = {
        "国家级项目": 1,
        "省部级项目": 2,
        "市厅级项目": 3,
        "企业合作项目": 4,
        "其它类型项目": 5,
    }
    project_type_keys = list(project_type.keys())

    # 排名映射
    ranking = {
        "第一作者": 1,
        "第二作者": 2,
        "第三作者": 3,
        "第四作者": 4,
        "第五作者": 5,
    }
    ranking_keys = list(ranking.keys())

    # 主讲课程学期映射
    lecture_term = {
        "春季学期": 1,
        "夏季学期": 2,
        "秋季学期": 3,
    }
    lecture_term_keys = list(lecture_term.keys())

    # 课程性质映射
    course_type = {
        "本科生课程": 1,
        "研究生课程": 2,
    }
    course_type_keys = list(course_type.keys())
