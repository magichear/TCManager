import requests

BASE_URL = "http://localhost:8080/api"


# 测试论文功能
def test_paper_controller():
    print("Testing PaperController...")

    # 添加论文
    paper_request = {
        "paper": {
            "paperNum": 1,
            "paperName": "深度学习在图像处理中的应用",
            "paperSrc": "IEEE Transactions on Image Processing",
            "paperYear": "2023-05-01",
            "paperType": 1,
            "paperRank": 1,
        },
        "authors": [
            {
                "teacherId": "T001",
                "paperNum": 1,
                "publishRank": 1,
                "isCorresponding": True,
            },
            {
                "teacherId": "T002",
                "paperNum": 1,
                "publishRank": 2,
                "isCorresponding": False,
            },
        ],
    }
    response = requests.post(f"{BASE_URL}/papers", json=paper_request)
    print(
        "Add Paper:", response.status_code, response.json() if response.content else ""
    )

    # 查询论文
    response = requests.get(f"{BASE_URL}/papers/1")
    if response.status_code == 200:
        print("Get Paper:", response.status_code, response.json())
    else:
        print("Get Paper Failed:", response.status_code, response.text)

    # 查询论文作者
    response = requests.get(f"{BASE_URL}/papers/1/authors")
    print("Get Paper Authors:", response.status_code, response.json())

    # 更新论文
    updated_paper_request = {
        "paper": {
            "paperNum": 1,
            "paperName": "深度学习在医学图像中的应用",
            "paperSrc": "IEEE Transactions on Medical Imaging",
            "paperYear": "2023-06-01",
            "paperType": 2,
            "paperRank": 2,
        },
        "authors": [
            {
                "teacherId": "T001",
                "paperNum": 1,
                "publishRank": 3,  # 修改为不冲突的排名
                "isCorresponding": False,
            },
            {
                "teacherId": "T002",
                "paperNum": 1,
                "publishRank": 1,
                "isCorresponding": True,
            },
        ],
    }
    response = requests.put(f"{BASE_URL}/papers", json=updated_paper_request)
    print(
        "Update Paper:",
        response.status_code,
        response.json() if response.content else "",
    )

    # 查询更新后的论文
    response = requests.get(f"{BASE_URL}/papers/1")
    if response.status_code == 200:
        print("Get Updated Paper:", response.status_code, response.json())
    else:
        print("Get Updated Paper Failed:", response.status_code, response.text)

    # 查询更新后的论文作者
    response = requests.get(f"{BASE_URL}/papers/1/authors")
    print("Get Updated Paper Authors:", response.status_code, response.json())

    # 删除论文
    response = requests.delete(f"{BASE_URL}/papers/1")
    print("Delete Paper:", response.status_code)


# 测试项目功能
def test_project_controller():
    print("Testing ProjectController...")

    # 添加项目
    project = {
        "projId": "P001",
        "projName": "国家自然科学基金项目",
        "projSrc": "国家自然科学基金委员会",
        "projType": 1,
        "projBalance": 1000000.0,
        "projStartYear": 2022,
        "projEndYear": 2025,
    }
    charges = [
        {
            "teacherId": "T001",
            "projId": "P001",
            "chargeRank": 1,
            "chargeBalance": 600000.0,
        },
        {
            "teacherId": "T002",
            "projId": "P001",
            "chargeRank": 2,
            "chargeBalance": 400000.0,
        },
    ]
    response = requests.post(
        f"{BASE_URL}/projects", json={"project": project, "charges": charges}
    )
    print(
        "Add Project:",
        response.status_code,
        response.json() if response.content else "",
    )

    # 查询项目
    response = requests.get(f"{BASE_URL}/projects/P001")
    print("Get Project:", response.status_code, response.json())

    # 更新项目
    project["projName"] = "国家重点研发计划项目"
    response = requests.put(
        f"{BASE_URL}/projects", json={"project": project, "charges": charges}
    )
    print(
        "Update Project:",
        response.status_code,
        response.json() if response.content else "",
    )

    # 删除项目
    response = requests.delete(f"{BASE_URL}/projects/P001")
    print("Delete Project:", response.status_code)


# 测试课程功能
def test_course_controller():
    print("Testing CourseController...")

    # 添加主讲课程记录
    lecture = {
        "teacherId": "T001",
        "courseId": "C001",
        "lectureYear": 2023,
        "lectureTerm": 1,
        "lectureHour": 24,
    }
    response = requests.post(f"{BASE_URL}/courses", json=lecture)
    print(
        "Add Lecture:",
        response.status_code,
        response.json() if response.content else "",
    )

    # 查询课程总学时
    response = requests.get(f"{BASE_URL}/courses/C001/total-hours")
    print("Get Total Lecture Hours:", response.status_code, response.json())

    # 更新主讲课程记录
    lecture["lectureHour"] = 30
    response = requests.put(f"{BASE_URL}/courses", json=lecture)
    print(
        "Update Lecture:",
        response.status_code,
        response.json() if response.content else "",
    )

    # 删除主讲课程记录
    response = requests.delete(f"{BASE_URL}/courses/C001/teachers/T001")
    print("Delete Lecture:", response.status_code)


# 执行测试
if __name__ == "__main__":
    test_paper_controller()
    # test_project_controller()
    # test_course_controller()
