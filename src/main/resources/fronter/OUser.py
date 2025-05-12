import gradio as gr
import requests
import datetime

# 后端 API 基础 URL
BASE_URL = "http://localhost:8080/api"

# 动态生成年份选项
current_year = datetime.datetime.now().year
year_choices = [str(year) for year in range(1970, current_year + 1)]


# 论文登记功能
def add_paper(paper_name, paper_src, paper_year, paper_type, paper_rank, authors):
    url = f"{BASE_URL}/papers"

    # 确保年份格式为 "yyyy-01-01"
    formatted_year = f"{paper_year}-01-01"

    paper_request = {
        "paper": {
            "paperName": paper_name,
            "paperSrc": paper_src,
            "paperYear": formatted_year,
            "paperType": paper_type,  # 直接传递整数值
            "paperRank": paper_rank,  # 直接传递整数值
        },
        "authors": authors,
    }

    response = requests.post(url, json=paper_request)
    if response.status_code == 200:
        data = response.json()
        paper_info = data.get("paper", {})
        authors_info = data.get("authors", [])
        return f"论文信息:\n{paper_info}\n\n作者信息:\n{authors_info}\n\n [DEBUG] {paper_year}"
    else:
        return f"提交失败: {response.status_code} - {response.text}"


def update_paper(
    paper_num, paper_name, paper_src, paper_year, paper_type, paper_rank, authors
):
    url = f"{BASE_URL}/papers"
    paper_request = {
        "paper": {
            "paperNum": paper_num,
            "paperName": paper_name,
            "paperSrc": paper_src,
            "paperYear": paper_year,
            "paperType": paper_type,  # 修改为直接传递整数值
            "paperRank": paper_rank,  # 修改为直接传递整数值
        },
        "authors": authors,
    }
    response = requests.put(url, json=paper_request)
    return response.json()


def delete_paper(paper_num):
    url = f"{BASE_URL}/papers/{paper_num}"
    response = requests.delete(url)
    return response.json()


def get_paper(paper_num):
    url = f"{BASE_URL}/papers/{paper_num}"
    response = requests.get(url)
    return response.json()


# 项目登记功能
def add_project(
    proj_name,
    proj_src,
    proj_type,
    proj_balance,
    proj_start_year,
    proj_end_year,
    charges,
):
    url = f"{BASE_URL}/projects"
    project_request = {
        "project": {
            "projName": proj_name,
            "projSrc": proj_src,
            "projType": proj_type,  # 修改为直接传递整数值
            "projBalance": proj_balance,
            "projStartYear": proj_start_year,
            "projEndYear": proj_end_year,
        },
        "charges": charges,
    }
    response = requests.post(url, json=project_request)
    return response.json()


def update_project(
    proj_id,
    proj_name,
    proj_src,
    proj_type,
    proj_balance,
    proj_start_year,
    proj_end_year,
    charges,
):
    url = f"{BASE_URL}/projects"
    project_request = {
        "project": {
            "projId": proj_id,
            "projName": proj_name,
            "projSrc": proj_src,
            "projType": proj_type,  # 修改为直接传递整数值
            "projBalance": proj_balance,
            "projStartYear": proj_start_year,
            "projEndYear": proj_end_year,
        },
        "charges": charges,
    }
    response = requests.put(url, json=project_request)
    return response.json()


def delete_project(proj_id):
    url = f"{BASE_URL}/projects/{proj_id}"
    response = requests.delete(url)
    return response.json()


def get_project(proj_id):
    url = f"{BASE_URL}/projects/{proj_id}"
    response = requests.get(url)
    return response.json()


# 主讲课程登记功能
def add_lecture(teacher_id, course_id, lecture_year, lecture_term, lecture_hour):
    url = f"{BASE_URL}/courses"
    lecture = {
        "teacherId": teacher_id,
        "courseId": course_id,
        "lectureYear": lecture_year,
        "lectureTerm": lecture_term,  # 修改为直接传递整数值
        "lectureHour": lecture_hour,
    }
    response = requests.post(url, json=lecture)
    return response.json()


def update_lecture(teacher_id, course_id, lecture_year, lecture_term, lecture_hour):
    url = f"{BASE_URL}/courses"
    lecture = {
        "teacherId": teacher_id,
        "courseId": course_id,
        "lectureYear": lecture_year,
        "lectureTerm": lecture_term,  # 修改为直接传递整数值
        "lectureHour": lecture_hour,
    }
    response = requests.put(url, json=lecture)
    return response.json()


def delete_lecture(course_id, teacher_id):
    url = f"{BASE_URL}/courses/{course_id}/teachers/{teacher_id}"
    response = requests.delete(url)
    return response.json()


def get_total_lecture_hours(course_id):
    url = f"{BASE_URL}/courses/{course_id}/total-hours"
    response = requests.get(url)
    return response.json()


# Gradio 界面
with gr.Blocks() as demo:
    with gr.Tab("登记发表论文情况"):
        paper_name = gr.Textbox(label="论文名称")
        paper_src = gr.Textbox(label="发表源")
        paper_year = gr.Dropdown(
            choices=year_choices, label="发表年份"
        )  # 修改为下拉框选择
        paper_type = gr.Dropdown(choices=["1", "2", "3", "4"], label="论文类型")
        paper_rank = gr.Dropdown(
            choices=["1", "2", "3", "4", "5", "6"], label="论文级别"
        )

        # 动态表单：作者信息
        with gr.Row():
            teacher_id = gr.Textbox(label="教师工号")
            publish_rank = gr.Number(label="作者排名")
            is_corresponding = gr.Checkbox(label="是否通讯作者")
            add_author_btn = gr.Button("添加作者")

        authors_list = gr.State([])  # 用于存储作者信息的状态
        authors_display = gr.Textbox(
            label="作者列表", interactive=False
        )  # 显示作者列表

        # 添加作者到列表
        def add_author(teacher_id, publish_rank, is_corresponding, authors_list):
            new_author = {
                "teacherId": teacher_id,
                "publishRank": publish_rank,
                "isCorresponding": is_corresponding,
            }
            authors_list.append(new_author)
            return authors_list, str(authors_list)

        add_author_btn.click(
            add_author,
            inputs=[teacher_id, publish_rank, is_corresponding, authors_list],
            outputs=[authors_list, authors_display],
        )

        # 提交论文信息
        submit_btn = gr.Button("提交论文")
        result = gr.Textbox(label="提交结果", lines=10)

        submit_btn.click(
            add_paper,
            inputs=[
                paper_name,
                paper_src,
                paper_year,
                paper_type,
                paper_rank,
                authors_list,
            ],
            outputs=result,
        )

    with gr.Tab("登记承担项目情况"):
        proj_name = gr.Textbox(label="项目名称")
        proj_src = gr.Textbox(label="项目来源")
        proj_type = gr.Dropdown(choices=["1", "2", "3", "4", "5"], label="项目类型")
        proj_balance = gr.Number(label="项目总经费")
        proj_start_year = gr.Number(label="开始年份")
        proj_end_year = gr.Number(label="结束年份")
        charges = gr.Textbox(label="承担信息(JSON格式)")
        add_project_btn = gr.Button("添加项目")
        add_project_btn.click(
            add_project,
            inputs=[
                proj_name,
                proj_src,
                proj_type,
                proj_balance,
                proj_start_year,
                proj_end_year,
                charges,
            ],
            outputs=gr.Textbox(label="结果"),
        )

    with gr.Tab("登记主讲课程情况"):
        teacher_id = gr.Textbox(label="教师工号")
        course_id = gr.Textbox(label="课程号")
        lecture_year = gr.Number(label="年份")
        lecture_term = gr.Dropdown(choices=["1", "2", "3"], label="学期")
        lecture_hour = gr.Number(label="承担学时")
        add_lecture_btn = gr.Button("添加主讲课程")
        add_lecture_btn.click(
            add_lecture,
            inputs=[teacher_id, course_id, lecture_year, lecture_term, lecture_hour],
            outputs=gr.Textbox(label="结果"),
        )

demo.launch()
