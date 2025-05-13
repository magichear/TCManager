import requests

# 设置基础 URL
BASE_URL = "http://localhost:8080/api/projects"

# 测试数据
project_data = {
    "project": {
        "projId": "05131031570728509ee747e9c8a4747ca342aa33bfb4597ef29fd8ec232a90d6c830db",
        "projName": "AI ResASDADrch Project",
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

## 1. 添加项目记录
# print("Adding project...")
# response = requests.post(f"{BASE_URL}/project", json=project_data)
# if response.status_code == 200:
#    print("Project added successfully:", response.json())
# else:
#    print("Failed to add project:", response.status_code, response.text)

# 2. 查询项目记录
# teacher_id = project_data["charges"][0]["teacherId"]
# print(f"\nFetching projects for Teacher ID {teacher_id}...")
# response = requests.get(f"{BASE_URL}/teachers/{teacher_id}/projects")
#
# if response.status_code == 200:
#    projects = response.json()
#    print("Projects fetched successfully:")
#    for idx, project in projects.items():
#        print(f"Project {idx}:")
#        print(f"  Charge Rank: {project['chargeRank']}")
#        print(f"  Charge Balance: {project['chargeBalance']}")
#        print(f"  Project ID: {project['project']['projId']}")
#        print(f"  Project Name: {project['project']['projName']}")
#        print(f"  Project Source: {project['project']['projSrc']}")
#        print(f"  Project Type: {project['project']['projType']}")
#        print(f"  Project Balance: {project['project']['projBalance']}")
#        print(f"  Project Start Year: {project['project']['projStartYear']}")
#        print(f"  Project End Year: {project['project']['projEndYear']}")
# else:
#    print("Failed to fetch projects:", response.status_code, response.text)
## 3. 更新项目记录
updated_project_data = {
    "project": {
        "projId": "051310691556a94bf735fb287934a0574022f3ace715036135f89ad466b5a9c5514460",
        "projName": "Updated AI Research Project",
        "projSrc": "Updated Source",
        "projType": 2,
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
## 4. 删除项目记录
# print(
#    f"\nDeleting project with ID 05131031570728509ee747e9c8a4747ca342aa33bfb4597ef29fd8ec232a90d6c830db ..."
# )
# response = requests.delete(
#    f"{BASE_URL}/05131031570728509ee747e9c8a4747ca342aa33bfb4597ef29fd8ec232a90d6c830db"
# )
# if response.status_code == 200:
#    print("Project deleted successfully")
# else:
#    print("Failed to delete project:", response.status_code, response.text)
