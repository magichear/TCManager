import gradio as gr
import requests

# 后端登录接口地址
LOGIN_API_URL = "http://localhost:8080/api/login"

# 定义全局变量存储用户权限级别
user_permission_level = None


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
            if "登录成功" in result["message"]:
                # 根据返回的用户类型设置权限级别
                user_type = result["data"]
                if user_type == "SUPER_USER":
                    user_permission_level = 1
                elif user_type == "REGULAR_USER":
                    user_permission_level = 2
                elif user_type == "GUEST":
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
                f"登录失败：HTTP {response.status_code}",
            )
    except Exception as e:
        return gr.update(visible=True), gr.update(visible=False), f"登录失败：{str(e)}"


# 构建 Gradio 界面
with gr.Blocks() as demo:
    # 登录页面
    with gr.Row(visible=True) as login_page:
        gr.Markdown("### 用户登录系统")
        username = gr.Textbox(label="用户名")
        password = gr.Textbox(label="密码", type="password")
        login_button = gr.Button("登录")
        login_output = gr.Textbox(label="登录结果", interactive=False)

    # 资源页面
    with gr.Row(visible=False) as resource_page:
        gr.Markdown("### 资源页面")
        with gr.Tab("Tab 1", visible=False) as tab1:
            gr.Markdown("这是 Tab 1 的内容")
        with gr.Tab("Tab 2", visible=False) as tab2:
            gr.Markdown("这是 Tab 2 的内容")
        with gr.Tab("Tab 3", visible=False) as tab3:
            gr.Markdown("这是 Tab 3 的内容")

    # 登录按钮点击事件
    def handle_login(username, password):
        global user_permission_level
        login_result = login(username, password)
        if user_permission_level == 1:  # 超级用户
            return (
                login_result[0],
                login_result[1],
                login_result[2],
                gr.update(visible=True),
                gr.update(visible=True),
                gr.update(visible=True),
            )
        elif user_permission_level == 2:  # 普通用户
            return (
                login_result[0],
                login_result[1],
                login_result[2],
                gr.update(visible=True),
                gr.update(visible=True),
                gr.update(visible=False),
            )
        elif user_permission_level == 3:  # 访客
            return (
                login_result[0],
                login_result[1],
                login_result[2],
                gr.update(visible=True),
                gr.update(visible=False),
                gr.update(visible=False),
            )
        else:  # 登录失败或未登录
            return (
                login_result[0],
                login_result[1],
                login_result[2],
                gr.update(visible=False),
                gr.update(visible=False),
                gr.update(visible=False),
            )

    login_button.click(
        handle_login,
        inputs=[username, password],
        outputs=[login_page, resource_page, login_output, tab1, tab2, tab3],
    )

demo.launch()
