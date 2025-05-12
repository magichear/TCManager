import requests

# 定义请求的 URL 和参数
base_url = "http://localhost:8080/api/papers/authors"
teacher_id = "T001"  # 替换为实际的教师工号
url = f"{base_url}/{teacher_id}/papers"

try:
    # 发送 GET 请求
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 成功，解析 JSON 数据
        data = response.json()
        print("查询结果：")
        print(data)
    else:
        # 处理错误响应
        print(f"查询失败，状态码：{response.status_code}")
        print("错误信息：", response.text)
except requests.exceptions.RequestException as e:
    # 捕获请求异常
    print("请求失败：", e)
