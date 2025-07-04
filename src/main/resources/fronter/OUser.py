import gradio as gr
from PaperManager import PaperManager
from LectureManager import LectureManager
from ProjectManager import ProjectManager
from Config import Config
from StatisticsGen import TeacherSummaryGenerator

# 创建 Manager 实例
paper_manager = PaperManager(Config.BASE_URL)
lecture_manager = LectureManager(Config.BASE_URL)
project_manager = ProjectManager(Config.BASE_URL)
statistics_gen = TeacherSummaryGenerator(Config.BASE_URL + "/teacher/summary")


# 点击按钮生成统计报告和 PDF 文件
def generate_statistics_and_pdf(teacher_id, start_year, end_year):
    markdown_content = statistics_gen.generate_teacher_summary(
        teacher_id, start_year, end_year
    )
    if markdown_content:
        pdf_file = statistics_gen.generate_pdf(markdown_content)
        return markdown_content, pdf_file
    else:
        return "生成统计报告失败，请检查输入信息。", None


# 动态调整终止年份的最小值
def update_end_year_options(start_year):
    # 获取起始年份之后的年份列表
    end_year_choices = [
        year for year in Config.year_choices if int(year) >= int(start_year)
    ]
    return gr.update(
        choices=end_year_choices, value=end_year_choices[0]
    )  # 默认选中第一个可用年份


# Gradio 界面
def get_regular_user_interface(is_called=True):
    with gr.Blocks() as demo:
        with gr.Tab("登记发表论文情况"):
            with gr.Tabs():  # 创建下级标签页
                # 新增三个同级空白标签页
                with gr.Tab("修改"):
                    paper_num = gr.Number(label="论文序号", precision=0)
                    paper_name = gr.Textbox(label="论文名称")
                    paper_src = gr.Textbox(label="发表源")
                    paper_year = gr.Dropdown(
                        choices=Config.year_choices, label="发表年份"
                    )
                    paper_type = gr.Dropdown(
                        choices=Config.pp_type_keys, label="论文类型"
                    )
                    paper_rank = gr.Dropdown(
                        choices=Config.pp_rank_keys, label="论文级别"
                    )

                    # 动态表单：作者信息
                    with gr.Row():
                        teacher_id = gr.Textbox(label="教师工号")
                        publish_rank = gr.Dropdown(
                            choices=["1", "2", "3", "4", "5", "6", "7"],
                            label="作者排名",
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
                        # 检查排名是否重复
                        if any(
                            author["publishRank"] == int(publish_rank)
                            for author in authors_list
                        ):
                            return authors_list, "排名重复，请选择其他排名！"

                        new_author = {
                            "teacherId": teacher_id,
                            "publishRank": int(publish_rank),
                            "isCorresponding": is_corresponding,
                        }
                        authors_list.append(new_author)

                        # 调整排名以确保连续
                        authors_list = adjust_author_ranks(authors_list)
                        feedback = (
                            "添加成功！排名已调整为连续。"
                            if len(authors_list) > 1
                            else "添加成功！"
                        )
                        return (
                            authors_list,
                            format_authors(authors_list) + f"\n\n{feedback}",
                        )

                    # 格式化作者列表为美观的字符串
                    def format_authors(authors_list):
                        formatted = []
                        for idx, author in enumerate(authors_list):
                            corresponding = "是" if author["isCorresponding"] else "否"
                            formatted.append(
                                f"{idx + 1}. 工号: {author['teacherId']}, 排名: {author['publishRank']}, 通讯作者: {corresponding}"
                            )
                        return "\n".join(formatted)

                    # 调整作者排名以确保连续
                    def adjust_author_ranks(authors_list):
                        authors_list.sort(key=lambda x: x["publishRank"])  # 按排名排序
                        for idx, author in enumerate(authors_list):
                            author["publishRank"] = idx + 1  # 从 1 开始重新编号
                        return authors_list

                    add_author_btn.click(
                        add_author,
                        inputs=[
                            teacher_id,
                            publish_rank,
                            is_corresponding,
                            authors_list,
                        ],
                        outputs=[authors_list, authors_display],
                    )

                    # 删除作者
                    def delete_author(index, authors_list):
                        if 0 <= index < len(authors_list):
                            authors_list.pop(index)

                        # 调整排名以确保连续
                        authors_list = adjust_author_ranks(authors_list)
                        return authors_list, format_authors(authors_list)

                    delete_index = gr.Number(
                        label="删除作者索引（从1开始）", precision=0
                    )
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
                    delete_result = gr.Textbox(
                        label="删除结果", lines=5, interactive=False
                    )

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
                    query_result = gr.Textbox(
                        label="查询结果", lines=10, interactive=False
                    )

                    # 调用 PaperManager 中的 query_papers_by_teacher 方法
                    query_btn.click(
                        paper_manager.query_papers_by_teacher,
                        inputs=[teacher_id_input],
                        outputs=[query_result],
                    )

                with gr.Tab("新增"):
                    paper_name = gr.Textbox(label="论文名称")
                    paper_src = gr.Textbox(label="发表源")
                    paper_year = gr.Dropdown(
                        choices=Config.year_choices, label="发表年份"
                    )
                    paper_type = gr.Dropdown(
                        choices=Config.pp_type_keys, label="论文类型"
                    )
                    paper_rank = gr.Dropdown(
                        choices=Config.pp_rank_keys, label="论文级别"
                    )

                    # 动态表单：作者信息
                    with gr.Row():
                        teacher_id = gr.Textbox(label="教师工号")
                        publish_rank = gr.Dropdown(
                            choices=["1", "2", "3", "4", "5", "6", "7"],
                            label="作者排名",
                        )
                        is_corresponding = gr.Checkbox(label="是否通讯作者")
                        add_author_btn = gr.Button("添加作者")

                    authors_list = gr.State([])  # 用于存储作者信息的状态
                    authors_display = gr.Textbox(
                        label="作者列表", interactive=False, lines=5
                    )

                    add_author_btn.click(
                        add_author,
                        inputs=[
                            teacher_id,
                            publish_rank,
                            is_corresponding,
                            authors_list,
                        ],
                        outputs=[authors_list, authors_display],
                    )

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
                    proj_start_year = gr.Dropdown(
                        choices=Config.year_choices, label="开始年份"
                    )
                    proj_end_year = gr.Dropdown(
                        choices=Config.year_choices, label="结束年份"
                    )

                    # 动态调整终止年份的最小值
                    proj_start_year.change(
                        update_end_year_options,
                        inputs=[proj_start_year],
                        outputs=[proj_end_year],
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
                    def add_charge(
                        teacher_id, charge_rank, charge_balance, charges_list
                    ):
                        # 检查排名是否重复
                        if any(
                            charge["chargeRank"] == int(charge_rank)
                            for charge in charges_list
                        ):
                            return charges_list, "排名重复，请选择其他排名！"

                        new_charge = {
                            "teacherId": teacher_id,
                            "chargeRank": int(charge_rank),
                            "chargeBalance": charge_balance,
                        }
                        charges_list.append(new_charge)

                        # 调整排名以确保连续
                        charges_list = adjust_charge_ranks(charges_list)
                        feedback = (
                            "添加成功！排名已调整为连续。"
                            if len(charges_list) > 1
                            else "添加成功！"
                        )
                        return (
                            charges_list,
                            format_charges(charges_list) + f"\n\n{feedback}",
                        )

                    # 格式化承担信息列表为美观的字符串
                    def format_charges(charges_list):
                        formatted = []
                        for idx, charge in enumerate(charges_list):
                            formatted.append(
                                f"{idx + 1}. 工号: {charge['teacherId']}, 排名: {charge['chargeRank']}, 经费: {charge['chargeBalance']}"
                            )
                        return "\n".join(formatted)

                    # 调整排名以确保连续
                    def adjust_charge_ranks(charges_list):
                        charges_list.sort(key=lambda x: x["chargeRank"])  # 按排名排序
                        for idx, charge in enumerate(charges_list):
                            charge["chargeRank"] = idx + 1  # 从 1 开始重新编号
                        return charges_list

                    add_charge_btn.click(
                        add_charge,
                        inputs=[teacher_id, charge_rank, charge_balance, charges_list],
                        outputs=[charges_list, charges_display],
                    )

                    # 删除承担信息
                    def delete_charge(index, charges_list):
                        if 0 <= index < len(charges_list):
                            charges_list.pop(index)

                        # 调整排名以确保连续
                        charges_list = adjust_charge_ranks(charges_list)
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
                    def submit_project(
                        proj_id,
                        proj_name,
                        proj_src,
                        proj_type,
                        proj_start_year,
                        proj_end_year,
                        charges_list,
                    ):
                        # 调整排名以确保连续
                        adjusted_charges = adjust_charge_ranks(charges_list)
                        feedback = (
                            "提交成功！排名已调整为连续。"
                            if adjusted_charges != charges_list
                            else "提交成功！"
                        )

                        # 调用后端接口提交数据
                        result = project_manager.update_project(
                            proj_id,
                            proj_name,
                            proj_src,
                            proj_type,
                            proj_start_year,
                            proj_end_year,
                            adjusted_charges,
                        )
                        return result + f"\n\n{feedback}"

                    submit_btn = gr.Button("提交修改")
                    result = gr.Textbox(label="修改结果", lines=10)

                    submit_btn.click(
                        submit_project,
                        inputs=[
                            proj_id,
                            proj_name,
                            proj_src,
                            proj_type,
                            proj_start_year,
                            proj_end_year,
                            charges_list,
                        ],
                        outputs=result,
                    )

                with gr.Tab("新增"):
                    proj_name = gr.Textbox(label="项目名称")
                    proj_src = gr.Textbox(label="项目来源")
                    proj_type = gr.Dropdown(
                        choices=Config.project_type_keys, label="项目类型"
                    )
                    proj_start_year = gr.Dropdown(
                        choices=Config.year_choices, label="开始年份"
                    )
                    proj_end_year = gr.Dropdown(
                        choices=Config.year_choices, label="结束年份"
                    )

                    # 动态调整终止年份的最小值
                    proj_start_year.change(
                        update_end_year_options,
                        inputs=[proj_start_year],
                        outputs=[proj_end_year],
                    )

                    # 动态表单：承担信息
                    with gr.Row():
                        teacher_id = gr.Textbox(label="教师工号")
                        charge_rank = gr.Dropdown(
                            choices=["1", "2", "3", "4", "5", "6", "7"],
                            label="承担排名（仅代表人物重要性，无关经费）",
                        )
                        charge_balance = gr.Number(label="承担经费")
                        add_charge_btn = gr.Button("添加承担信息")

                    charges_list = gr.State([])  # 用于存储承担信息的状态
                    charges_display = gr.Textbox(
                        label="承担信息列表", interactive=False, lines=5
                    )

                    # 添加承担信息到列表
                    def add_charge(
                        teacher_id, charge_rank, charge_balance, charges_list
                    ):
                        # 检查排名是否重复
                        if any(
                            charge["chargeRank"] == int(charge_rank)
                            for charge in charges_list
                        ):
                            return charges_list, "排名重复，请选择其他排名！"

                        new_charge = {
                            "teacherId": teacher_id,
                            "chargeRank": int(charge_rank),
                            "chargeBalance": charge_balance,
                        }
                        charges_list.append(new_charge)

                        # 调整排名以确保连续
                        charges_list = adjust_charge_ranks(charges_list)
                        feedback = (
                            "添加成功！排名已调整为连续。"
                            if len(charges_list) > 1
                            else "添加成功！"
                        )
                        return (
                            charges_list,
                            format_charges(charges_list) + f"\n\n{feedback}",
                        )

                    # 格式化承担信息列表为美观的字符串
                    def format_charges(charges_list):
                        formatted = []
                        for idx, charge in enumerate(charges_list):
                            formatted.append(
                                f"{idx + 1}. 工号: {charge['teacherId']}, 排名: {charge['chargeRank']}, 经费: {charge['chargeBalance']}"
                            )
                        return "\n".join(formatted)

                    # 调整排名以确保连续
                    def adjust_charge_ranks(charges_list):
                        charges_list.sort(key=lambda x: x["chargeRank"])  # 按排名排序
                        for idx, charge in enumerate(charges_list):
                            charge["chargeRank"] = idx + 1  # 从 1 开始重新编号
                        return charges_list

                    add_charge_btn.click(
                        add_charge,
                        inputs=[teacher_id, charge_rank, charge_balance, charges_list],
                        outputs=[charges_list, charges_display],
                    )

                    # 删除承担信息
                    def delete_charge(index, charges_list):
                        if 0 <= index < len(charges_list):
                            charges_list.pop(index)

                        # 调整排名以确保连续
                        charges_list = adjust_charge_ranks(charges_list)
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
                    def submit_project(
                        proj_name,
                        proj_src,
                        proj_type,
                        proj_start_year,
                        proj_end_year,
                        charges_list,
                    ):
                        # 调整排名以确保连续
                        adjusted_charges = adjust_charge_ranks(charges_list)
                        feedback = (
                            "提交成功！排名已调整为连续。"
                            if adjusted_charges != charges_list
                            else "提交成功！"
                        )

                        # 调用后端接口提交数据
                        result = project_manager.add_project(
                            proj_name,
                            proj_src,
                            proj_type,
                            proj_start_year,
                            proj_end_year,
                            adjusted_charges,
                        )
                        return result + f"\n\n{feedback}"

                    submit_btn = gr.Button("提交项目")
                    result = gr.Textbox(label="提交结果", lines=10)

                    submit_btn.click(
                        submit_project,
                        inputs=[
                            proj_name,
                            proj_src,
                            proj_type,
                            proj_start_year,
                            proj_end_year,
                            charges_list,
                        ],
                        outputs=result,
                    )

                with gr.Tab("删除"):
                    proj_id_input = gr.Textbox(label="项目号")
                    delete_btn = gr.Button("删除项目")
                    delete_result = gr.Textbox(
                        label="删除结果", lines=5, interactive=False
                    )

                    # 调用 ProjectManager 中的 delete_project 方法
                    delete_btn.click(
                        project_manager.delete_project,
                        inputs=[proj_id_input],
                        outputs=[delete_result],
                    )

                with gr.Tab("查询"):
                    # 按项目号查询
                    proj_id_input = gr.Textbox(
                        label="项目号", placeholder="请输入项目号"
                    )
                    query_proj_btn = gr.Button("按项目号查询")
                    query_proj_result = gr.Textbox(
                        label="查询结果", lines=10, interactive=False
                    )

                    query_proj_btn.click(
                        project_manager.get_project,
                        inputs=[proj_id_input],
                        outputs=[query_proj_result],
                    )

                    # 按教师工号查询
                    teacher_id_input = gr.Textbox(
                        label="教师工号", placeholder="请输入教师工号"
                    )
                    query_teacher_btn = gr.Button("按教师工号查询")
                    query_teacher_result = gr.Textbox(
                        label="查询结果", lines=10, interactive=False
                    )

                    query_teacher_btn.click(
                        project_manager.query_projects_by_teacher,
                        inputs=[teacher_id_input],
                        outputs=[query_teacher_result],
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
                    delete_result = gr.Textbox(
                        label="删除结果", lines=5, interactive=False
                    )

                    delete_btn.click(
                        lecture_manager.delete_lecture,
                        inputs=[course_id_input, teacher_id_input],
                        outputs=[delete_result],
                    )

                # 查询主讲课程
                with gr.Tab("查询"):
                    # 按教师工号查询
                    teacher_id_input = gr.Textbox(
                        label="教师工号", placeholder="请输入教师工号"
                    )
                    query_teacher_btn = gr.Button("按教师工号查询")
                    query_teacher_result = gr.Textbox(
                        label="查询结果", lines=10, interactive=False
                    )

                    query_teacher_btn.click(
                        lecture_manager.get_lectures_by_teacher,
                        inputs=[teacher_id_input],
                        outputs=[query_teacher_result],
                    )

                    # 按课程号查询
                    course_id_input = gr.Textbox(
                        label="课程号", placeholder="请输入课程号"
                    )
                    query_course_btn = gr.Button("按课程号查询")
                    query_course_result = gr.Textbox(
                        label="查询结果", lines=10, interactive=False
                    )

                    query_course_btn.click(
                        lecture_manager.get_lectures_by_course,
                        inputs=[course_id_input],
                        outputs=[query_course_result],
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
        with gr.Tab("生成教师统计报告"):
            teacher_id_input = gr.Textbox(
                label="教师工号", placeholder="请输入教师工号"
            )
            start_year = gr.Dropdown(choices=Config.year_choices, label="起始年份")
            end_year = gr.Dropdown(choices=Config.year_choices, label="结束年份")
            generate_btn = gr.Button("生成统计报告")
            markdown_output = gr.Markdown(label="统计报告内容")
            pdf_download = gr.File(label="下载 PDF 文件")

            # 动态调整终止年份的最小值
            start_year.change(
                update_end_year_options,
                inputs=[start_year],
                outputs=[end_year],
            )

            generate_btn.click(
                generate_statistics_and_pdf,
                inputs=[teacher_id_input, start_year, end_year],
                outputs=[markdown_output, pdf_download],
            )
    if not is_called:
        demo.launch()


if __name__ == "__main__":
    get_regular_user_interface(False)
