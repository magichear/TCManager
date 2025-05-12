import datetime


class Config:
    # 后端 API 基础 URL
    BASE_URL = "http://localhost:8080/api"

    # 动态生成年份选项
    current_year = datetime.datetime.now().year
    year_choices = [str(year) for year in range(1970, current_year + 1)]

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
