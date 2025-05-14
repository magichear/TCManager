import gradio as gr
from PaperManager import PaperManager
from LectureManager import LectureManager
from ProjectManager import ProjectManager
from Config import Config

# 创建 Manager 实例
paper_manager = PaperManager(Config.BASE_URL)
lecture_manager = LectureManager(Config.BASE_URL)
project_manager = ProjectManager(Config.BASE_URL)

# Gradio 界面
with gr.Blocks() as demo:
    with gr.Tab("登记发表论文情况"):
        with gr.Tabs():  # 创建下级标签页
            # 新增三个同级空白标签页
            with gr.Tab("修改"):
                paper_num = gr.Number(label="论文序号", precision=0)
                paper_name = gr.Textbox(label="论文名称")
                paper_src = gr.Textbox(label="发表源")
                paper_year = gr.Dropdown(choices=Config.year_choices, label="发表年份")
                paper_type = gr.Dropdown(choices=Config.pp_type_keys, label="论文类型")
                paper_rank = gr.Dropdown(choices=Config.pp_rank_keys, label="论文级别")

                # 动态表单：作者信息
                with gr.Row():
                    teacher_id = gr.Textbox(label="教师工号")
                    publish_rank = gr.Dropdown(
                        choices=["1", "2", "3", "4", "5", "6", "7"], label="作者排名"
                    )
                    is_corresponding = gr.Checkbox(label="是否通讯作者")
                    add_author_btn = gr.Button("添加作者")

                authors_list = gr.State([])  # 用于存储作者信息的状态
                authors_display = gr.Textbox(
                    label="作者列表", interactive=False, lines=5
                )

                # 添加作者到列表
                def add_author(
                    teacher_id, publish_rank, is_corresponding, authors_list
                ):
                    new_author = {
                        "teacherId": teacher_id,
                        "publishRank": int(publish_rank),
                        "isCorresponding": is_corresponding,
                    }
                    authors_list.append(new_author)
                    return authors_list, format_authors(authors_list)

                # 格式化作者列表为美观的字符串
                def format_authors(authors_list):
                    formatted = []
                    for idx, author in enumerate(authors_list):
                        corresponding = "是" if author["isCorresponding"] else "否"
                        formatted.append(
                            f"{idx + 1}. 工号: {author['teacherId']}, 排名: {author['publishRank']}, 通讯作者: {corresponding}"
                        )
                    return "\n".join(formatted)

                add_author_btn.click(
                    add_author,
                    inputs=[teacher_id, publish_rank, is_corresponding, authors_list],
                    outputs=[authors_list, authors_display],
                )

                # 删除作者
                def delete_author(index, authors_list):
                    if 0 <= index < len(authors_list):
                        authors_list.pop(index)
                    return authors_list, format_authors(authors_list)

                delete_index = gr.Number(label="删除作者索引（从1开始）", precision=0)
                delete_author_btn = gr.Button("删除作者")

                delete_author_btn.click(
                    delete_author,
                    inputs=[delete_index, authors_list],
                    outputs=[authors_list, authors_display],
                )

                # 提交修改
                submit_btn = gr.Button("提交修改")
                result = gr.Textbox(label="修改结果", lines=10)

                submit_btn.click(
                    paper_manager.update_paper,
                    inputs=[
                        paper_num,
                        paper_name,
                        paper_src,
                        paper_year,
                        paper_type,
                        paper_rank,
                        authors_list,
                    ],
                    outputs=result,
                )

            with gr.Tab("删除"):
                paper_num_input = gr.Number(label="论文序号", precision=0)
                delete_btn = gr.Button("删除论文")
                delete_result = gr.Textbox(label="删除结果", lines=5, interactive=False)

                # 调用 PaperManager 中的 delete_paper 方法
                delete_btn.click(
                    paper_manager.delete_paper,
                    inputs=[paper_num_input],
                    outputs=[delete_result],
                )

            with gr.Tab("查询"):
                teacher_id_input = gr.Textbox(
                    label="教师工号", placeholder="请输入教师工号"
                )
                query_btn = gr.Button("查询")
                query_result = gr.Textbox(label="查询结果", lines=10, interactive=False)

                # 调用 PaperManager 中的 query_papers_by_teacher 方法
                query_btn.click(
                    paper_manager.query_papers_by_teacher,
                    inputs=[teacher_id_input],
                    outputs=[query_result],
                )

            with gr.Tab("新增"):
                paper_name = gr.Textbox(label="论文名称")
                paper_src = gr.Textbox(label="发表源")
                paper_year = gr.Dropdown(choices=Config.year_choices, label="发表年份")
                paper_type = gr.Dropdown(choices=Config.pp_type_keys, label="论文类型")
                paper_rank = gr.Dropdown(choices=Config.pp_rank_keys, label="论文级别")

                # 动态表单：作者信息
                with gr.Row():
                    teacher_id = gr.Textbox(label="教师工号")
                    publish_rank = gr.Dropdown(
                        choices=["1", "2", "3", "4", "5", "6", "7"], label="作者排名"
                    )
                    is_corresponding = gr.Checkbox(label="是否通讯作者")
                    add_author_btn = gr.Button("添加作者")

                authors_list = gr.State([])  # 用于存储作者信息的状态
                authors_display = gr.Textbox(
                    label="作者列表", interactive=False, lines=5
                )

                # 添加作者到列表
                def add_author(
                    teacher_id, publish_rank, is_corresponding, authors_list
                ):
                    new_author = {
                        "teacherId": teacher_id,
                        "publishRank": int(publish_rank),
                        "isCorresponding": is_corresponding,
                    }
                    authors_list.append(new_author)
                    return authors_list, format_authors(authors_list)

                # 格式化作者列表为美观的字符串
                def format_authors(authors_list):
                    formatted = []
                    for idx, author in enumerate(authors_list):
                        corresponding = "是" if author["isCorresponding"] else "否"
                        formatted.append(
                            f"{idx + 1}. 工号: {author['teacherId']}, 排名: {author['publishRank']}, 通讯作者: {corresponding}"
                        )
                    return "\n".join(formatted)

                add_author_btn.click(
                    add_author,
                    inputs=[teacher_id, publish_rank, is_corresponding, authors_list],
                    outputs=[authors_list, authors_display],
                )

                # 删除作者
                def delete_author(index, authors_list):
                    if 0 <= index < len(authors_list):
                        authors_list.pop(index)
                    return authors_list, format_authors(authors_list)

                delete_index = gr.Number(label="删除作者索引（从1开始）", precision=0)
                delete_author_btn = gr.Button("删除作者")

                delete_author_btn.click(
                    delete_author,
                    inputs=[delete_index, authors_list],
                    outputs=[authors_list, authors_display],
                )

                # 提交论文信息
                submit_btn = gr.Button("提交论文")
                result = gr.Textbox(label="提交结果", lines=10)

                submit_btn.click(
                    paper_manager.add_paper,
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
        with gr.Tabs():  # 创建下级标签页
            # 新增三个同级空白标签页
            with gr.Tab("修改"):
                proj_id = gr.Textbox(label="项目号")
                proj_name = gr.Textbox(label="项目名称")
                proj_src = gr.Textbox(label="项目来源")
                proj_type = gr.Dropdown(
                    choices=Config.project_type_keys, label="项目类型"
                )
                proj_balance = gr.Number(label="项目经费")
                proj_start_year = gr.Dropdown(
                    choices=Config.year_choices, label="开始年份"
                )
                proj_end_year = gr.Dropdown(
                    choices=Config.year_choices, label="结束年份"
                )

                # 动态表单：承担信息
                with gr.Row():
                    teacher_id = gr.Textbox(label="教师工号")
                    charge_rank = gr.Dropdown(
                        choices=["1", "2", "3", "4", "5"], label="承担排名"
                    )
                    charge_balance = gr.Number(label="承担经费")
                    add_charge_btn = gr.Button("添加承担信息")

                charges_list = gr.State([])  # 用于存储承担信息的状态
                charges_display = gr.Textbox(
                    label="承担信息列表", interactive=False, lines=5
                )

                # 添加承担信息到列表
                def add_charge(teacher_id, charge_rank, charge_balance, charges_list):
                    new_charge = {
                        "teacherId": teacher_id,
                        "chargeRank": int(charge_rank),
                        "chargeBalance": charge_balance,
                    }
                    charges_list.append(new_charge)
                    return charges_list, format_charges(charges_list)

                # 格式化承担信息列表为美观的字符串
                def format_charges(charges_list):
                    formatted = []
                    for idx, charge in enumerate(charges_list):
                        formatted.append(
                            f"{idx + 1}. 工号: {charge['teacherId']}, 排名: {charge['chargeRank']}, 经费: {charge['chargeBalance']}"
                        )
                    return "\n".join(formatted)

                add_charge_btn.click(
                    add_charge,
                    inputs=[teacher_id, charge_rank, charge_balance, charges_list],
                    outputs=[charges_list, charges_display],
                )

                # 删除承担信息
                def delete_charge(index, charges_list):
                    if 0 <= index < len(charges_list):
                        charges_list.pop(index)
                    return charges_list, format_charges(charges_list)

                delete_index = gr.Number(
                    label="删除承担信息索引（从1开始）", precision=0
                )
                delete_charge_btn = gr.Button("删除承担信息")

                delete_charge_btn.click(
                    delete_charge,
                    inputs=[delete_index, charges_list],
                    outputs=[charges_list, charges_display],
                )

                # 提交修改
                submit_btn = gr.Button("提交修改")
                result = gr.Textbox(label="修改结果", lines=10)

                submit_btn.click(
                    project_manager.update_project,
                    inputs=[
                        proj_id,
                        proj_name,
                        proj_src,
                        proj_type,
                        proj_balance,
                        proj_start_year,
                        proj_end_year,
                        charges_list,
                    ],
                    outputs=result,
                )

            with gr.Tab("删除"):
                proj_id_input = gr.Textbox(label="项目号")
                delete_btn = gr.Button("删除项目")
                delete_result = gr.Textbox(label="删除结果", lines=5, interactive=False)

                # 调用 ProjectManager 中的 delete_project 方法
                delete_btn.click(
                    project_manager.delete_project,
                    inputs=[proj_id_input],
                    outputs=[delete_result],
                )

            with gr.Tab("查询"):
                proj_id_input = gr.Textbox(label="项目号", placeholder="请输入项目号")
                query_btn = gr.Button("查询")
                query_result = gr.Textbox(label="查询结果", lines=10, interactive=False)

                # 调用 ProjectManager 中的 get_project 方法
                query_btn.click(
                    project_manager.get_project,
                    inputs=[proj_id_input],
                    outputs=[query_result],
                )

            with gr.Tab("新增"):
                proj_name = gr.Textbox(label="项目名称")
                proj_src = gr.Textbox(label="项目来源")
                proj_type = gr.Dropdown(
                    choices=Config.project_type_keys, label="项目类型"
                )
                proj_balance = gr.Number(label="项目经费")
                proj_start_year = gr.Dropdown(
                    choices=Config.year_choices, label="开始年份"
                )
                proj_end_year = gr.Dropdown(
                    choices=Config.year_choices, label="结束年份"
                )

                # 动态表单：承担信息
                with gr.Row():
                    teacher_id = gr.Textbox(label="教师工号")
                    charge_rank = gr.Dropdown(
                        choices=["1", "2", "3", "4", "5"], label="承担排名"
                    )
                    charge_balance = gr.Number(label="承担经费")
                    add_charge_btn = gr.Button("添加承担信息")

                charges_list = gr.State([])  # 用于存储承担信息的状态
                charges_display = gr.Textbox(
                    label="承担信息列表", interactive=False, lines=5
                )

                # 添加承担信息到列表
                def add_charge(teacher_id, charge_rank, charge_balance, charges_list):
                    new_charge = {
                        "teacherId": teacher_id,
                        "chargeRank": int(charge_rank),
                        "chargeBalance": charge_balance,
                    }
                    charges_list.append(new_charge)
                    return charges_list, format_charges(charges_list)

                # 格式化承担信息列表为美观的字符串
                def format_charges(charges_list):
                    formatted = []
                    for idx, charge in enumerate(charges_list):
                        formatted.append(
                            f"{idx + 1}. 工号: {charge['teacherId']}, 排名: {charge['chargeRank']}, 经费: {charge['chargeBalance']}"
                        )
                    return "\n".join(formatted)

                add_charge_btn.click(
                    add_charge,
                    inputs=[teacher_id, charge_rank, charge_balance, charges_list],
                    outputs=[charges_list, charges_display],
                )

                # 删除承担信息
                def delete_charge(index, charges_list):
                    if 0 <= index < len(charges_list):
                        charges_list.pop(index)
                    return charges_list, format_charges(charges_list)

                delete_index = gr.Number(
                    label="删除承担信息索引（从1开始）", precision=0
                )
                delete_charge_btn = gr.Button("删除承担信息")

                delete_charge_btn.click(
                    delete_charge,
                    inputs=[delete_index, charges_list],
                    outputs=[charges_list, charges_display],
                )

                # 提交项目信息
                submit_btn = gr.Button("提交项目")
                result = gr.Textbox(label="提交结果", lines=10)

                submit_btn.click(
                    project_manager.add_project,
                    inputs=[
                        proj_name,
                        proj_src,
                        proj_type,
                        proj_balance,
                        proj_start_year,
                        proj_end_year,
                        charges_list,
                    ],
                    outputs=result,
                )

    # Gradio 界面 - 登记主讲课程情况
    with gr.Tab("登记主讲课程情况"):
        with gr.Tabs():  # 创建下级标签页
            # 修改主讲课程
            with gr.Tab("修改"):
                course_id = gr.Textbox(label="课程号")
                teacher_id = gr.Textbox(label="教师工号")
                lecture_year = gr.Dropdown(
                    choices=Config.year_choices, label="授课年份"
                )
                lecture_term = gr.Dropdown(
                    choices=Config.lecture_term_keys, label="授课学期"
                )
                lecture_hour = gr.Number(label="授课学时")

                # 提交修改
                submit_btn = gr.Button("提交修改")
                result = gr.Textbox(label="修改结果", lines=5)

                submit_btn.click(
                    lecture_manager.update_lecture,
                    inputs=[
                        teacher_id,
                        course_id,
                        lecture_year,
                        lecture_term,
                        lecture_hour,
                    ],
                    outputs=result,
                )

            # 删除主讲课程
            with gr.Tab("删除"):
                course_id_input = gr.Textbox(label="课程号")
                teacher_id_input = gr.Textbox(label="教师工号")
                delete_btn = gr.Button("删除课程")
                delete_result = gr.Textbox(label="删除结果", lines=5, interactive=False)

                delete_btn.click(
                    lecture_manager.delete_lecture,
                    inputs=[course_id_input, teacher_id_input],
                    outputs=[delete_result],
                )

            # 查询主讲课程
            with gr.Tab("查询"):
                teacher_id_input = gr.Textbox(
                    label="教师工号", placeholder="请输入教师工号"
                )
                query_btn = gr.Button("查询")
                query_result = gr.Textbox(label="查询结果", lines=10, interactive=False)

                query_btn.click(
                    lecture_manager.get_lectures_by_teacher,
                    inputs=[teacher_id_input],
                    outputs=[query_result],
                )

            # 新增主讲课程
            with gr.Tab("新增"):
                course_id = gr.Textbox(label="课程号")
                teacher_id = gr.Textbox(label="教师工号")
                lecture_year = gr.Dropdown(
                    choices=Config.year_choices, label="授课年份"
                )
                lecture_term = gr.Dropdown(
                    choices=Config.lecture_term_keys, label="授课学期"
                )
                lecture_hour = gr.Number(label="授课学时")

                # 提交新增
                submit_btn = gr.Button("提交课程")
                result = gr.Textbox(label="提交结果", lines=5)

                submit_btn.click(
                    lecture_manager.add_lecture,
                    inputs=[
                        teacher_id,
                        course_id,
                        lecture_year,
                        lecture_term,
                        lecture_hour,
                    ],
                    outputs=result,
                )

demo.launch()
