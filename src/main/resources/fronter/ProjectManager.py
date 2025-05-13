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
        proj_balance,
        proj_start_year,
        proj_end_year,
        charges,
    ):
        url = f"{self.base_url}/projects"
        project_request = {
            "project": {
                "projName": proj_name,
                "projSrc": proj_src,
                "projType": int(proj_type),  # 确保传递整数值
                "projBalance": proj_balance,
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
        proj_balance,
        proj_start_year,
        proj_end_year,
        charges,
    ):
        url = f"{self.base_url}/projects"
        project_request = {
            "project": {
                "projId": proj_id,
                "projName": proj_name,
                "projSrc": proj_src,
                "projType": int(proj_type),  # 确保传递整数值
                "projBalance": proj_balance,
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
