import requests
from Config import Config


class LectureManager:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_lecture(
        self, teacher_id, course_id, lecture_year, lecture_term, lecture_hour
    ):
        """
        添加主讲课程记录
        """
        url = f"{self.base_url}/courses"
        lecture = {
            "teacherId": teacher_id,
            "courseId": course_id,
            "lectureYear": lecture_year,
            "lectureTerm": Config.get_value(Config.lecture_term, lecture_term),
            "lectureHour": lecture_hour,
        }
        response = requests.post(url, json=lecture)
        if response.status_code == 200:
            return f"课程 {course_id} 添加成功！"
        else:
            return f"添加失败: {response.status_code} - {response.text}"

    def update_lecture(
        self, teacher_id, course_id, lecture_year, lecture_term, lecture_hour
    ):
        """
        更新主讲课程记录
        """
        url = f"{self.base_url}/courses"
        lecture = {
            "teacherId": teacher_id,
            "courseId": course_id,
            "lectureYear": lecture_year,
            "lectureTerm": Config.get_value(Config.lecture_term, lecture_term),
            "lectureHour": lecture_hour,
        }
        response = requests.put(url, json=lecture)
        if response.status_code == 200:
            return f"课程 {course_id} 修改成功！"
        else:
            return f"修改失败: {response.status_code} - {response.text}"

    def delete_lecture(self, course_id, teacher_id):
        """
        删除主讲课程记录
        """
        url = f"{self.base_url}/courses/{course_id}/teachers/{teacher_id}"
        response = requests.delete(url)
        if response.status_code == 200:
            return f"课程 {course_id} 删除成功！"
        else:
            return f"删除失败: {response.status_code} - {response.text}"

    def get_lectures_by_teacher(self, teacher_id):
        """
        查询教师的所有主讲课程记录
        """
        url = f"{self.base_url}/courses/teachers/{teacher_id}"
        response = requests.get(url)
        if response.status_code == 200:
            lectures = response.json()
            if not lectures:
                return f"教师工号 {teacher_id} 没有主讲任何课程。"

            # 格式化课程信息
            formatted_lectures = []
            for idx, lecture in lectures.items():
                formatted_lectures.append(
                    f"{int(idx) + 1}. 课程号: {lecture['courseId']}, 课程名称: {lecture['courseName']}, "
                    f"课程学时: {lecture['courseHour']}, 课程类型: {lecture['courseType']}, "
                    f"授课年份: {lecture['lectureYear']}, 授课学期: {lecture['lectureTerm']}, "
                    f"授课学时: {lecture['lectureHour']}"
                )
            return "\n".join(formatted_lectures)
        else:
            return f"查询失败: {response.status_code} - {response.text}"
