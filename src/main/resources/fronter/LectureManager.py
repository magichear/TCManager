import requests
from Config import Config


class LectureManager:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_lecture(
        self, teacher_id, course_id, lecture_year, lecture_term, lecture_hour
    ):
        url = f"{self.base_url}/courses"
        lecture = {
            "teacherId": teacher_id,
            "courseId": course_id,
            "lectureYear": lecture_year,
            "lectureTerm": lecture_term,  # 修改为直接传递整数值
            "lectureHour": lecture_hour,
        }
        response = requests.post(url, json=lecture)
        return response.json()

    def update_lecture(
        self, teacher_id, course_id, lecture_year, lecture_term, lecture_hour
    ):
        url = f"{self.base_url}/courses"
        lecture = {
            "teacherId": teacher_id,
            "courseId": course_id,
            "lectureYear": lecture_year,
            "lectureTerm": lecture_term,  # 修改为直接传递整数值
            "lectureHour": lecture_hour,
        }
        response = requests.put(url, json=lecture)
        return response.json()

    def delete_lecture(self, course_id, teacher_id):
        url = f"{self.base_url}/courses/{course_id}/teachers/{teacher_id}"
        response = requests.delete(url)
        return response.json()

    def get_total_lecture_hours(self, course_id):
        url = f"{self.base_url}/courses/{course_id}/total-hours"
        response = requests.get(url)
        return response.json()
