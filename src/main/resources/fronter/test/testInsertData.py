import requests

BASE_URL = "http://localhost:8080/api"


def insert_courses():
    url = f"{BASE_URL}/courses"
    for i in range(1, 11):
        data = {
            "teacherId": f"T000{i % 9 + 1}",  # 确保教师ID长度符合数据库限制
            "courseId": f"C000{i}",
            "lectureYear": 2020 + (i % 3),  # 随机年份
            "lectureTerm": i % 2 + 1,  # 学期 1-春季, 2-夏季
            "lectureHour": 30 + i * 5,  # 学时
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"课程记录插入成功: {data}")
        else:
            print(f"课程记录插入失败: {response.status_code} - {response.text}")


def insert_papers():
    url = f"{BASE_URL}/papers"
    for i in range(1, 11):
        data = {
            "paper": {
                "paperName": f"论文标题-{i}",
                "paperSrc": f"期刊-{i}",
                "paperYear": f"202{i % 3}-01-01",  # 随机年份
                "paperType": i % 3
                + 1,  # 类型 1-full paper, 2-short paper, 3-poster paper
                "paperRank": i % 5 + 1,  # 级别 1-CCF-A, 2-CCF-B, ..., 5-中文CCF-B
            },
            "authors": [
                {
                    "teacherId": f"T000{i % 9 + 1}",  # 确保教师ID长度符合数据库限制
                    "publishRank": 1,  # 第一作者
                    "isCorresponding": 1,  # 通讯作者
                },
                {
                    "teacherId": f"T000{i % 8 + 2}",  # 确保教师ID长度符合数据库限制
                    "publishRank": 2,  # 第二作者
                    "isCorresponding": 0,  # 非通讯作者
                },
            ],
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"论文记录插入成功: {data}")
        else:
            print(f"论文记录插入失败: {response.status_code} - {response.text}")


def insert_projects():
    url = f"{BASE_URL}/projects"
    for i in range(1, 11):
        data = {
            "project": {
                "projName": f"项目名称-{i}",
                "projSrc": f"来源-{i}",
                "projType": i % 4 + 1,  # 类型 1-国家级项目, ..., 4-企业合作项目
                "projStartYear": 2018 + (i % 5),  # 随机开始年份
                "projEndYear": 2019 + (i % 5),  # 随机结束年份
            },
            "charges": [
                {
                    "teacherId": f"T000{i % 9 + 1}",  # 确保教师ID长度符合数据库限制
                    "chargeRank": 1,  # 项目负责人
                    "chargeBalance": 10000 + i * 500,  # 经费
                },
                {
                    "teacherId": f"T000{i % 8 + 2}",  # 确保教师ID长度符合数据库限制
                    "chargeRank": 2,  # 第二负责人
                    "chargeBalance": 8000 + i * 400,  # 经费
                },
            ],
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"项目记录插入成功: {data}")
        else:
            print(f"项目记录插入失败: {response.status_code} - {response.text}")


if __name__ == "__main__":
    print("插入课程记录...")
    insert_courses()
    print("\n插入论文记录...")
    insert_papers()
    print("\n插入项目记录...")
    insert_projects()
