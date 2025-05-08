import requests

BASE_URL = "http://localhost:8080/api"


def test_query_courses():

    # 查询所有课程信息
    response = requests.get(f"{BASE_URL}/courses")
    if response.status_code == 200:
        print("All Courses:", response.json())
    else:
        print("Failed to fetch all courses:", response.status_code, response.json())

    # 查询单门课程信息
    course_id = "C001"
    response = requests.get(f"{BASE_URL}/courses/{course_id}")
    if response.status_code == 200:
        print(f"Course {course_id}:", response.json())
    else:
        print(
            f"Failed to fetch course {course_id}:",
            response.status_code,
            response.json(),
        )


if __name__ == "__main__":
    test_query_courses()
