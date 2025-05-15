import requests
from datetime import datetime
from markdown import markdown  # 用于将 Markdown 转换为 HTML
from fpdf import FPDF, HTMLMixin  # 使用 fpdf2 的 HTML 渲染功能
from Translate import Translator  # 导入 Translator 类


class PDFWithHTML(FPDF, HTMLMixin):
    """
    扩展 FPDF 类以支持 HTML 渲染
    """

    pass


class TeacherSummaryGenerator:
    def __init__(self, base_url):
        self.base_url = base_url

    def generate_markdown(self, data):
        teacher = data["teacher"]
        lecture_courses = data["lectureCourses"]
        projects = data["projects"]
        papers = data["papers"]

        # 教师基本信息
        teacher_info = f"""

---

<h3>教师基本信息</h3>

<div style="display: flex; justify-content: space-between; white-space: pre;">
    <span>工号：{teacher['teacherId']}</span>
    <span>姓名：{teacher['teacherName']}</span>
    <span>性别：{Translator.translate_sex(teacher['teacherSex'])}</span>
    <span>职称：{Translator.translate_title(teacher['teacherTitle'])}</span>
</div>
"""

        # 教学情况
        teaching_info = '\n\n---\n\n<h3>教学情况</h3>\n<div style="display: flex; flex-direction: column; gap: 10px;">\n'
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
        paper_info = "\n\n---\n\n<h3>发表论文情况</h3>\n"
        for i, paper in enumerate(papers, start=1):
            paper_year = datetime.fromisoformat(
                paper["paperYear"].replace("Z", "+00:00")
            ).year
            paper_info += f"{i}. {paper['paperName']}，{paper['paperSrc']}，{paper_year}，{Translator.translate_paper_rank(paper['paperRank'])}，排名第 {paper['publishRank']}，{'通讯作者' if paper['isCorresponding'] else '非通讯作者'}\n\n"

        # 承担项目情况
        project_info = "\n\n---\n\n<h3>承担项目情况</h3>\n"
        for i, project in enumerate(projects, start=1):
            proj = project["project"]
            project_info += f"{i}. {proj['projName']}，{proj['projSrc']}，{Translator.translate_project_type(proj['projType'])}，{proj['projStartYear']} - {proj['projEndYear']}，总经费：{proj['projBalance']}，承担经费：{project['chargeBalance']}\n\n"

        # 合并所有部分
        markdown_content = (
            teacher_info
            + "\n"
            + teaching_info
            + "\n"
            + paper_info
            + "\n"
            + project_info
        )
        return markdown_content

    def generate_teacher_summary(self, teacher_id, start_year=1999, end_year=2023):
        params = {
            "teacherId": teacher_id,
            "startYear": start_year,
            "endYear": end_year,
        }

        try:
            response = requests.get(self.base_url, params=params)

            # 检查响应状态码
            if response.status_code == 200:
                print("请求成功，生成 Markdown 内容...")
                data = response.json()
                return self.generate_markdown(data)
            else:
                print(f"请求失败，状态码：{response.status_code}")
                print("错误信息：", response.text)
                return None

        except requests.exceptions.RequestException as e:
            print("请求发生异常：", e)
            return None

    def generate_pdf(self, markdown_content, file_name="teacher_report.pdf"):
        """
        将 Markdown 内容生成 PDF 文件
        """
        # 将 Markdown 转换为 HTML
        html_content = markdown(markdown_content)

        pdf = PDFWithHTML()
        pdf.add_page()

        # 使用华文楷体字体
        pdf.add_font("STKAITI", "", "C:/Windows/Fonts/STKAITI.TTF", uni=True)
        pdf.set_font("STKAITI", size=12)

        # 渲染 HTML 内容
        pdf.write_html(html_content)

        pdf.output(file_name)
        return file_name


if __name__ == "__main__":
    generator = TeacherSummaryGenerator("http://localhost:8080/api/teacher/summary")
    teacher_id = "T0003"
    markdown_content = generator.generate_teacher_summary(teacher_id)
    if markdown_content:
        print(markdown_content)
        pdf_file = generator.generate_pdf(markdown_content)
        print(f"PDF 文件已生成：{pdf_file}")
