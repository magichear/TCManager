import requests

# 定义接口的 URL
BASE_URL = "http://localhost:8080/api/teacher/summary"

# 定义测试参数
params = {
    "teacherId": "T0002",  # 教师工号
    "startYear": 2020,  # 开始年份
    "endYear": 2023,  # 结束年份
}

# 发送 GET 请求
try:
    response = requests.get(BASE_URL, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        print("请求成功，返回结果如下：")
        print(response.json())
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print("错误信息：", response.text)

except requests.exceptions.RequestException as e:
    print("请求发生异常：", e)
