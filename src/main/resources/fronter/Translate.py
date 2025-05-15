class Translator:

    @staticmethod
    def get_value(mMap, key):
        """
        前端应对制杖Jackson的方法
        [CAUTION] 所有从本类中取出的映射都必须通过该方法来获取实际值
        """
        return mMap.get(key, 1) - 1

    @staticmethod
    def translate_sex(sex):
        sexes = {
            "MAN": "男",
            "WOMAN": "女",
        }
        return sexes.get(sex, sex)

    @staticmethod
    def translate_title(title):
        titles = {
            "POSTDOC": "博士后",
            "ASSISTANT": "助教",
            "LECTURER": "讲师",
            "ASSOCIATE_PROFESSOR": "副教授",
            "SPECIAL_PROFESSOR": "特任教授",
            "PROFESSOR": "教授",
            "ASSISTANT_RESEARCHER": "助理研究员",
            "SPECIAL_ASSOCIATE_RESEARCHER": "特任副研究员",
            "ASSOCIATE_RESEARCHER": "副研究员",
            "SPECIAL_RESEARCHER": "特任研究员",
            "RESEARCHER": "研究员",
        }
        return titles.get(title, title)

    @staticmethod
    def translate_paper_type(paper_type):
        paper_types = {
            "FULL_PAPER": "full paper",
            "SHORT_PAPER": "short paper",
            "POSTER_PAPER": "poster paper",
            "DEMO_PAPER": "demo paper",
        }
        return paper_types.get(paper_type, paper_type)

    @staticmethod
    def translate_paper_rank(rank):
        ranks = {
            "CCF_A": "CCF-A",
            "CCF_B": "CCF-B",
            "CCF_C": "CCF-C",
            "CHINESE_CCF_A": "中文CCF-A",
            "CHINESE_CCF_B": "中文CCF-B",
            "NONE": "无级别",
        }
        return ranks.get(rank, rank)

    @staticmethod
    def translate_project_type(proj_type):
        types = {
            "NATIONAL": "国家级项目",
            "PROVINCIAL": "省部级项目",
            "MUNICIPAL": "市厅级项目",
            "ENTERPRISE": "企业合作项目",
            "OTHER": "其它类型项目",
        }
        return types.get(proj_type, proj_type)

    @staticmethod
    def translate_rank(rank):
        return f"排名第 {rank}" if rank >= 1 else "未知排名"

    @staticmethod
    def translate_term(term):
        terms = {
            "SPRING": "春季学期",
            "SUMMER": "夏季学期",
            "AUTUMN": "秋季学期",
        }
        return terms.get(term, term)

    @staticmethod
    def translate_course_type(course_type):
        course_types = {
            "UNDERGRADUATE": "本科生课程",
            "POSTGRADUATE": "研究生课程",
        }
        return course_types.get(course_type, course_type)
