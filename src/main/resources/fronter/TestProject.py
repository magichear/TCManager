import requests

# 设置基础 URL
BASE_URL = "http://localhost:8080/api/projects"

# 测试数据
project_data = {
    "project": {
        "projId": "P001",
        "projName": "AI Research Project",
        "projSrc": "National Science Foundation",
        "projType": 1,  # 修改为直接传递枚举值
        "projBalance": 100000.0,
        "projStartYear": 2023,
        "projEndYear": 2025,
    },
    "charges": [
        {"teacherId": "T001", "chargeRank": 1, "chargeBalance": 50000.0},
        {"teacherId": "T002", "chargeRank": 2, "chargeBalance": 50000.0},
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
proj_id = project_data["project"]["projId"]
print(f"\nFetching project with ID {proj_id}...")
response = requests.get(f"{BASE_URL}/{proj_id}")
if response.status_code == 200:
    print("Project fetched successfully:", response.json())
else:
    print("Failed to fetch project:", response.status_code, response.text)

# 3. 更新项目记录
updated_project_data = {
    "project": {
        "projId": "P001",
        "projName": "Updated AI Research Project",
        "projSrc": "Updated Source",
        "projType": {"value": 2},  # 省部级项目
        "projBalance": 120000.0,
        "projStartYear": 2023,
        "projEndYear": 2026,
    },
    "charges": [
        {"teacherId": "T001", "chargeRank": 1, "chargeBalance": 60000.0},
        {"teacherId": "T002", "chargeRank": 2, "chargeBalance": 60000.0},
    ],
}
print("\nUpdating project...")
response = requests.put(BASE_URL, json=updated_project_data)
if response.status_code == 200:
    print("Project updated successfully")
else:
    print("Failed to update project:", response.status_code, response.text)

# 4. 删除项目记录
print(f"\nDeleting project with ID {proj_id}...")
response = requests.delete(f"{BASE_URL}/{proj_id}")
if response.status_code == 200:
    print("Project deleted successfully")
else:
    print("Failed to delete project:", response.status_code, response.text)

# 5. 确认删除
print(f"\nConfirming deletion of project with ID {proj_id}...")
response = requests.get(f"{BASE_URL}/{proj_id}")
if response.status_code == 404:
    print("Project deletion confirmed: Not Found")
else:
    print("Project still exists:", response.status_code, response.text)
