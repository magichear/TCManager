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
                "projType": proj_type,  # 修改为直接传递整数值
                "projBalance": proj_balance,
                "projStartYear": proj_start_year,
                "projEndYear": proj_end_year,
            },
            "charges": charges,
        }
        response = requests.put(url, json=project_request)
        return response.json()

    def delete_project(self, proj_id):
        url = f"{self.base_url}/projects/{proj_id}"
        response = requests.delete(url)
        return response.json()

    def get_project(self, proj_id):
        url = f"{self.base_url}/projects/{proj_id}"
        response = requests.get(url)
        return response.json()
