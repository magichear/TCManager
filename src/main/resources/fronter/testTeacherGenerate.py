import requests
import json
from datetime import datetime
from Translate import Translator  # 导入 Translator 类

# 定义接口的 URL
BASE_URL = "http://localhost:8080/api/teacher/summary"

# 定义测试参数
params = {
    "teacherId": "T0003",  # 教师工号
    "startYear": 1999,  # 开始年份
    "endYear": 2023,  # 结束年份
}


# 定义 Markdown 模板
def generate_markdown(data):
    teacher = data["teacher"]
    lecture_courses = data["lectureCourses"]
    projects = data["projects"]
    papers = data["papers"]

    # 教师基本信息
    teacher_info = f"""
<h3>教师基本信息</h3>

---

<div style="display: flex; justify-content: space-between; white-space: pre;">
    <span>工号：{teacher['teacherId']}</span>
    <span>姓名：{teacher['teacherName']}</span>
    <span>性别：{Translator.translate_sex(teacher['teacherSex'])}</span>
    <span>职称：{Translator.translate_title(teacher['teacherTitle'])}</span>
</div>
"""

    # 教学情况
    teaching_info = '<h3>教学情况</h3>\n\n---\n\n<div style="display: flex; flex-direction: column; gap: 10px;">\n'
    for course in lecture_courses:
        term = Translator.translate_term(course["lectureTerm"])
        teaching_info += f"""   <div style="display: flex; justify-content: space-between; text-align: left;">
        <div style="flex: 1;">课程号：{course['courseId']}</div>
        <div style="flex: 1;">课程名：{course['courseName']}</div>
        <div style="flex: 1;">主讲学时：{course['lectureHour']}</div>
        <div style="flex: 1;">学期：{course['lectureYear']} {term}</div>
    </div>
"""
    teaching_info += "</div>"

    # 发表论文情况
    paper_info = "<h3>发表论文情况</h3>\n\n---\n\n"
    for i, paper in enumerate(papers, start=1):
        paper_year = datetime.fromisoformat(
            paper["paperYear"].replace("Z", "+00:00")
        ).year
        paper_info += f"{i}. {paper['paperName']}，{paper['paperSrc']}，{paper_year}，{Translator.translate_paper_rank(paper['paperRank'])}，排名第 {paper['publishRank']}，{'通讯作者' if paper['isCorresponding'] else '非通讯作者'}\n\n"

    # 承担项目情况
    project_info = "<h3>承担项目情况</h3>\n\n---\n\n"
    for i, project in enumerate(projects, start=1):
        proj = project["project"]
        project_info += f"{i}. {proj['projName']}，{proj['projSrc']}，{Translator.translate_project_type(proj['projType'])}，{proj['projStartYear']} - {proj['projEndYear']}，总经费：{proj['projBalance']}，承担经费：{project['chargeBalance']}\n\n"

    # 合并所有部分
    markdown_content = (
        teacher_info + "\n" + teaching_info + "\n" + paper_info + "\n" + project_info
    )
    return markdown_content


# 发送 GET 请求并生成 Markdown 文件
try:
    response = requests.get(BASE_URL, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        print("请求成功，生成 Markdown 文件...")
        data = response.json()
        markdown_content = generate_markdown(data)

        # 保存到文件
        with open("teacher_summary.md", "w", encoding="utf-8") as file:
            file.write(markdown_content)
        print("Markdown 文件已生成：teacher_summary.md")
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print("错误信息：", response.text)

except requests.exceptions.RequestException as e:
    print("请求发生异常：", e)
