import requests

# 设置基础 URL
BASE_URL = "http://localhost:8080/api/papers"

# 测试数据
paper_data = {
    "paper": {
        "paperName": "AI Research Paper",
        "paperSrc": "Nature",
        "paperYear": "2023-01-01",
        "paperType": 1,
        "paperRank": 1,
    },
    "authors": [
        {"teacherId": "T0001", "publishRank": 1, "isCorresponding": True},
        {"teacherId": "T0002", "publishRank": 2, "isCorresponding": False},
    ],
}

# 1. 添加论文记录
print("Adding paper...")
response = requests.post(BASE_URL, json=paper_data)
if response.status_code == 200:
    print("Paper added successfully:", response.json())
    paper_id = response.json()["paper"]["paperNum"]  # 获取返回的论文序号
else:
    print("Failed to add paper:", response.status_code, response.text)
    exit()

# 2. 查询论文记录
print(f"\nFetching paper with ID {paper_id}...")
response = requests.get(f"{BASE_URL}/{paper_id}")
if response.status_code == 200:
    paper = response.json()
    print("Paper fetched successfully:")
    print(f"  Paper Name: {paper['paperName']}")
    print(f"  Paper Source: {paper['paperSrc']}")
    print(f"  Paper Year: {paper['paperYear']}")
    print(f"  Paper Type: {paper['paperType']}")
    print(f"  Paper Rank: {paper['paperRank']}")
else:
    print("Failed to fetch paper:", response.status_code, response.text)

# 3. 查询论文的作者信息
print(f"\nFetching authors for paper with ID {paper_id}...")
response = requests.get(f"{BASE_URL}/{paper_id}/authors")
if response.status_code == 200:
    authors = response.json()
    print("Authors fetched successfully:")
    for author in authors:
        print(f"  Teacher ID: {author['teacherId']}")
        print(f"  Publish Rank: {author['publishRank']}")
        print(f"  Is Corresponding: {author['isCorresponding']}")
else:
    print("Failed to fetch authors:", response.status_code, response.text)

# 4. 更新论文记录
updated_paper_data = {
    "paper": {
        "paperNum": paper_id,
        "paperName": "Updated AI Research Paper",
        "paperSrc": "Science",
        "paperYear": "2024-01-01",
        "paperType": 2,
        "paperRank": 2,
    },
    "authors": [
        {"teacherId": "T0001", "publishRank": 1, "isCorresponding": True},
        {"teacherId": "T0003", "publishRank": 2, "isCorresponding": False},
    ],
}
print("\nUpdating paper...")
response = requests.put(BASE_URL, json=updated_paper_data)
if response.status_code == 200:
    print("Paper updated successfully")
else:
    print("Failed to update paper:", response.status_code, response.text)

# 5. 删除论文记录
print(f"\nDeleting paper with ID {paper_id}...")
response = requests.delete(f"{BASE_URL}/{paper_id}")
if response.status_code == 200:
    print("Paper deleted successfully")
else:
    print("Failed to delete paper:", response.status_code, response.text)
