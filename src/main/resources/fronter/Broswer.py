import gradio as gr
import os
from OUser import get_regular_user_interface  # 导入普通用户界面函数
import requests

# 后端登录接口地址
LOGIN_API_URL = "http://localhost:8080/api/login"

# 定义全局变量存储用户权限级别
user_permission_level = None
has_switched_to_regular_user = False  # 标记是否已从管理员页面跳转到普通用户页面

# 404 页面相对路径
RELATIVE_404_PATH = "../static/404.html"  # 相对于 Broswer.py 的路径


# 登录函数
def login(username, password):
    global user_permission_level
    # 构造请求数据
    login_data = {"username": username, "password": password}
    try:
        # 向后端发送登录请求
        response = requests.post(LOGIN_API_URL, json=login_data)
        if response.status_code == 200:
            result = response.json()
            print("[DEBUG] 后端返回的数据：", result)
            if "message" in result and "role" in result:
                if "登录成功" in result["message"]:
                    # 根据返回的用户类型设置权限级别
                    user_role = result["role"]
                    if user_role == "SUPER_USER":
                        user_permission_level = 1
                    elif user_role == "REGULAR_USER":
                        user_permission_level = 2
                    elif user_role == "GUEST":
                        user_permission_level = 3
                    return (
                        gr.update(visible=False),
                        gr.update(visible=True),
                        f"登录成功！您的权限级别为：{user_permission_level}",
                    )
                else:
                    return (
                        gr.update(visible=True),
                        gr.update(visible=False),
                        "登录失败：" + result["message"],
                    )
            else:
                return (
                    gr.update(visible=True),
                    gr.update(visible=False),
                    "登录失败：后端返回数据格式错误",
                )
        else:
            return (
                gr.update(visible=True),
                gr.update(visible=False),
                f"登录失败：HTTP {response.status_code}",
            )
    except Exception as e:
        return gr.update(visible=True), gr.update(visible=False), f"登录失败：{str(e)}"


# 获取 404 页面内容
def get_404_page_content():
    # 获取 404 页面绝对路径
    abs_404_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), RELATIVE_404_PATH)
    )
    if os.path.exists(abs_404_path):
        # print(f"[DEBUG] 404 页面路径：{abs_404_path}")
        with open(abs_404_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print("[ERROR] 404 页面不存在！")
        return "404 页面未找到！"


# 主界面
def main_interface():
    global has_switched_to_regular_user

    with gr.Blocks() as demo:
        # 主界面
        with gr.Row(visible=False) as main_view:
            # 根据权限级别动态显示内容
            admin_view = gr.Column(visible=False)
            regular_user_view = gr.Column(visible=False)
            guest_view = gr.Column(visible=False)  # 访客界面

            # 管理员页面
            with admin_view:
                gr.Textbox(label="管理员页面：这里可以展示所有用户的资源")

                # 添加跳转按钮
                def switch_to_regular_user():
                    global has_switched_to_regular_user
                    has_switched_to_regular_user = True
                    return gr.update(visible=False), gr.update(visible=True)

                gr.Button("跳转到普通用户界面").click(
                    switch_to_regular_user,
                    inputs=[],
                    outputs=[admin_view, regular_user_view],
                )

            # 普通用户页面
            with regular_user_view:
                get_regular_user_interface(is_called=True)

            # 访客页面
            with guest_view:
                gr.HTML(
                    value=get_404_page_content(),
                )

        # 登录界面
        with gr.Row(visible=True) as login_view:
            username = gr.Textbox(label="用户名")
            password = gr.Textbox(label="密码", type="password")
            login_btn = gr.Button("登录")
            login_result = gr.Textbox(label="登录结果", interactive=False)

            login_btn.click(
                login,
                inputs=[username, password],
                outputs=[login_view, main_view, login_result],
            )

        # 动态切换页面逻辑
        def switch_view():
            if user_permission_level == 1:  # 管理员
                return (
                    gr.update(visible=True),
                    gr.update(visible=False),
                    gr.update(visible=False),
                )
            elif user_permission_level == 2:  # 普通用户
                return (
                    gr.update(visible=False),
                    gr.update(visible=True),
                    gr.update(visible=False),
                )
            elif user_permission_level == 3:  # 访客
                return (
                    gr.update(visible=False),
                    gr.update(visible=False),
                    gr.update(visible=True),
                )
            else:
                return (
                    gr.update(visible=False),
                    gr.update(visible=False),
                    gr.update(visible=False),
                )

        # 登录后根据权限显示对应页面
        load_page_btn = gr.Button("加载页面")
        load_page_btn.click(
            switch_view,
            inputs=[],
            outputs=[admin_view, regular_user_view, guest_view],
        )

    demo.launch()


if __name__ == "__main__":
    main_interface()
