import requests
from Config import Config


class ProjectManager:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_project(
        self,
        proj_name,
        proj_src,
        proj_type,
        proj_start_year,
        proj_end_year,
        charges,
    ):
        """
        添加项目记录
        """
        url = f"{self.base_url}/projects"
        project_request = {
            "project": {
                "projName": proj_name,
                "projSrc": proj_src,
                "projType": Config.get_value(Config.project_type, proj_type),
                "projStartYear": proj_start_year,
                "projEndYear": proj_end_year,
            },
            "charges": charges,
        }

        response = requests.post(url, json=project_request)
        if response.status_code == 200:
            data = response.json()
            project_info = data.get("project", {})
            charges_info = data.get("charges", [])

            # 格式化承担信息
            formatted_charges = [
                {k: v for k, v in charge.items() if v is not None}
                for charge in charges_info
            ]

            return f"项目信息:\n{project_info}\n\n承担信息:\n{formatted_charges}"
        else:
            return f"提交失败: {response.status_code} - {response.text}"

    def update_project(
        self,
        proj_id,
        proj_name,
        proj_src,
        proj_type,
        proj_start_year,
        proj_end_year,
        charges,
    ):
        """
        更新项目记录
        """
        url = f"{self.base_url}/projects"
        project_request = {
            "project": {
                "projId": proj_id,
                "projName": proj_name,
                "projSrc": proj_src,
                "projType": Config.get_value(Config.project_type, proj_type),
                "projStartYear": proj_start_year,
                "projEndYear": proj_end_year,
            },
            "charges": charges,
        }

        try:
            response = requests.put(url, json=project_request)
            if response.status_code == 200:
                return f"项目号 {proj_id} 修改成功！"
            elif response.status_code == 404:
                return f"项目号 {proj_id} 不存在，无法修改。"
            else:
                return f"修改失败: {response.status_code} - {response.text}"
        except Exception as e:
            return f"修改时发生错误: {str(e)}"

    def delete_project(self, proj_id):
        """
        删除项目记录
        """
        url = f"{self.base_url}/projects/{proj_id}"
        try:
            response = requests.delete(url)
            if response.status_code == 200:
                return f"项目号 {proj_id} 删除成功！"
            elif response.status_code == 404:
                return f"项目号 {proj_id} 不存在，无法删除。"
            else:
                return f"删除失败: {response.status_code} - {response.text}"
        except Exception as e:
            return f"删除时发生错误: {str(e)}"

    def get_project(self, proj_id):
        """
        查询项目记录
        """
        url = f"{self.base_url}/projects/{proj_id}"
        response = requests.get(url)
        if response.status_code == 200:
            project_data = response.json()
            project_info = project_data.get("project", {})
            charges_info = project_data.get("charges", [])

            # 格式化承担信息
            formatted_charges = [
                f"工号: {charge['teacherId']}, 排名: {charge['chargeRank']}, 经费: {charge['chargeBalance']}"
                for charge in charges_info
            ]

            return f"项目信息:\n{project_info}\n\n承担信息:\n{formatted_charges}"
        else:
            return f"查询失败: {response.status_code} - {response.text}"

    def query_projects_by_teacher(self, teacher_id):
        """
        按教师工号查询其承担的所有项目信息
        """
        if not teacher_id.strip():
            return "教师工号不能为空！"

        url = f"{self.base_url}/projects/teachers/{teacher_id}/projects"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                projects = response.json()
                if not projects:
                    return f"教师工号 {teacher_id} 没有承担任何项目。"

                # 格式化项目信息
                formatted_projects = []
                for idx, project in projects.items():
                    formatted_projects.append(
                        f"{int(idx) + 1}. 项目号: {project['project']['projId']}, 项目名称: {project['project']['projName']}, "
                        f"来源: {project['project']['projSrc']}, 类型: {project['project']['projType']}, "
                        f"经费: {project['project']['projBalance']}, 开始年份: {project['project']['projStartYear']}, "
                        f"结束年份: {project['project']['projEndYear']}, 排名: {project['chargeRank']}, "
                        f"承担经费: {project['chargeBalance']}"
                    )
                return "\n".join(formatted_projects)
            else:
                return f"查询失败: {response.status_code} - {response.text}"
        except Exception as e:
            return f"查询时发生错误: {str(e)}"
