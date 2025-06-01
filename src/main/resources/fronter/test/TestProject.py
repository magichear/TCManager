import requests

# 设置基础 URL
BASE_URL = "http://localhost:8080/api/projects"

# 测试数据
project_data = {
    "project": {
        "projName": "AI Research Project",
        "projSrc": "National Science Foundation",
        "projType": 1,
        "projStartYear": 2023,
        "projEndYear": 2025,
    },
    "charges": [
        {"teacherId": "T0001", "chargeRank": 1, "chargeBalance": 50000.0},
        {"teacherId": "T0002", "chargeRank": 2, "chargeBalance": 50000.0},
    ],
}

# 1. 添加项目记录
print("Adding project...")
response = requests.post(BASE_URL, json=project_data)
if response.status_code == 200:
    print("Project added successfully:", response.json())
else:
    print("Failed to add project:", response.status_code, response.text)

# 2. 查询项目记录
teacher_id = project_data["charges"][0]["teacherId"]
print(f"\nFetching projects for Teacher ID {teacher_id}...")
response = requests.get(f"{BASE_URL}/teachers/{teacher_id}/projects")

if response.status_code == 200:
    projects = response.json()
    print("Projects fetched successfully:")
    for idx, project in projects.items():
        print(f"Project {idx}:")
        print(f"  Charge Rank: {project['chargeRank']}")
        print(f"  Charge Balance: {project['chargeBalance']}")
        print(f"  Project ID: {project['project']['projId']}")
        print(f"  Project Name: {project['project']['projName']}")
        print(f"  Project Source: {project['project']['projSrc']}")
        print(f"  Project Type: {project['project']['projType']}")
        print(f"  Project Start Year: {project['project']['projStartYear']}")
        print(f"  Project End Year: {project['project']['projEndYear']}")
        A_lucky_ID = project["project"]["projId"]
else:
    print("Failed to fetch projects:", response.status_code, response.text)

# 3. 更新项目记录
updated_project_data = {
    "project": {
        "projId": A_lucky_ID,
        "projName": "Updated AI Research Project",
        "projSrc": "Updated Source",
        "projType": 2,
        "projStartYear": 2023,
        "projEndYear": 2026,
    },
    "charges": [
        {"teacherId": "T0001", "chargeRank": 1, "chargeBalance": 60000.0},
        {"teacherId": "T0002", "chargeRank": 2, "chargeBalance": 60000.0},
    ],
}
print("\nUpdating project...")
response = requests.put(BASE_URL, json=updated_project_data)
if response.status_code == 200:
    print("Project updated successfully")
else:
    print("Failed to update project:", response.status_code, response.text)

# 4. 删除项目记录
print(f"\nDeleting project with ID {A_lucky_ID} ...")
response = requests.delete(f"{BASE_URL}/{A_lucky_ID}")
if response.status_code == 200:
    print("Project deleted successfully")
else:
    print("Failed to delete project:", response.status_code, response.text)
