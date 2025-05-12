import requests
from Config import Config


class PaperManager:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_value(self, mMap, key):
        """
        前端应对制杖Jackson的方法
        """
        return mMap.get(key, 1) - 1

    def add_paper(
        self, paper_name, paper_src, paper_year, paper_type, paper_rank, authors
    ):
        url = f"{self.base_url}/papers"

        # 确保年份格式为 "yyyy-01-01"
        formatted_year = f"{paper_year}-01-01"

        paper_request = {
            "paper": {
                "paperName": paper_name,
                "paperSrc": paper_src,
                "paperYear": formatted_year,
                "paperType": self.get_value(Config.pp_type, paper_type),
                "paperRank": self.get_value(Config.pp_rank, paper_rank),
            },
            "authors": authors,
        }

        response = requests.post(url, json=paper_request)
        if response.status_code == 200:
            data = response.json()
            paper_info = data.get("paper", {})
            authors_info = data.get("authors", [])

            # 剔除作者信息中值为 None 的部分
            cleaned_authors_info = [
                {k: v for k, v in author.items() if v is not None}
                for author in authors_info
            ]

            return f"论文信息:\n{paper_info}\n\n作者信息:\n{cleaned_authors_info}\n\n [DEBUG] {paper_year}"
        else:
            return f"提交失败: {response.status_code} - {response.text}"

    def update_paper(
        self,
        paper_num,
        paper_name,
        paper_src,
        paper_year,
        paper_type,
        paper_rank,
        authors,
    ):
        url = f"{self.base_url}/papers"
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

    def delete_paper(self, paper_num):
        url = f"{self.base_url}/papers/{paper_num}"
        response = requests.delete(url)
        return response.json()

    def get_paper(self, paper_num):
        url = f"{self.base_url}/papers/{paper_num}"
        response = requests.get(url)
        return response.json()
