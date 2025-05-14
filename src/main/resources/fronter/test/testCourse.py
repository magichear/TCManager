import requests

# 设置基础 URL
BASE_URL = "http://localhost:8080/api/courses"

# 测试数据
lecture_data = {
    "courseId": "C001",
    "teacherId": "T001",
    "lectureYear": 2023,
    "lectureTerm": 0,
    "lectureHour": 40,
}

updated_lecture_data = {
    "courseId": "C001",
    "teacherId": "T001",
    "lectureYear": 2024,
    "lectureTerm": 1,
    "lectureHour": 50,
}

# 1. 添加主讲课程记录
print("Adding lecture...")
response = requests.post(BASE_URL, json=lecture_data)
if response.status_code == 200:
    result = response.json()  # 接收返回值
    print("Lecture added successfully:", result)  # 打印返回值
    # 值为 Lecture added successfully: {'lecture': {'teacherId': 'T001', 'courseId': 'C001', 'lectureYear': 2023, 'lectureTerm': 'SUMMER', 'lectureHour': 40}}
else:
    print("Failed to add lecture:", response.status_code, response.text)

# 2. 更新主讲课程记录
print("\nUpdating lecture...")
response = requests.put(BASE_URL, json=updated_lecture_data)
if response.status_code == 200:
    print("Lecture updated successfully")
else:
    print("Failed to update lecture:", response.status_code, response.text)

# 3. 查询教师的所有主讲课程记录
teacher_id = lecture_data["teacherId"]
print(f"\nFetching lectures for Teacher ID {teacher_id}...")
response = requests.get(f"{BASE_URL}/teachers/{teacher_id}")
if response.status_code == 200:
    lectures = response.json()
    print("Lectures fetched successfully:")
    for idx, lecture in lectures.items():
        print(f"Lecture {idx}:")
        print(f"  Course ID: {lecture['courseId']}")
        print(f"  Course Name: {lecture['courseName']}")
        print(f"  Course Hour: {lecture['courseHour']}")
        print(f"  Course Type: {lecture['courseType']}")
        print(f"  Lecture Year: {lecture['lectureYear']}")
        print(f"  Lecture Term: {lecture['lectureTerm']}")
        print(f"  Lecture Hour: {lecture['lectureHour']}")
else:
    print("Failed to fetch lectures:", response.status_code, response.text)
## 4. 删除主讲课程记录
course_id = lecture_data["courseId"]
teacher_id = lecture_data["teacherId"]
print(f"\nDeleting lecture for Course ID {course_id} and Teacher ID {teacher_id}...")
response = requests.delete(f"{BASE_URL}/{course_id}/teachers/{teacher_id}")
if response.status_code == 200:
    print("Lecture deleted successfully")
else:
    print("Failed to delete lecture:", response.status_code, response.text)
