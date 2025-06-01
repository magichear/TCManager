import os
import ast
from graphviz import Digraph


def is_user_defined_module(module_name, project_root):
    """
    判断模块是否为用户定义的模块
    """
    # 检查模块是否在项目根目录下
    module_path = os.path.join(project_root, *module_name.split(".")) + ".py"
    return os.path.exists(module_path)


def parse_imports_from_file(file_path, project_root):
    """
    解析单个文件的导入语句，并过滤非用户定义的库
    """
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    user_defined_imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if is_user_defined_module(alias.name, project_root):
                    user_defined_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and is_user_defined_module(node.module, project_root):
                user_defined_imports.append(node.module)
    return user_defined_imports


def parse_imports_from_directory(directory_path):
    """
    递归解析目录中的所有 Python 文件的导入语句
    """
    all_imports = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                imports = parse_imports_from_file(file_path, directory_path)
                all_imports[file_path] = imports
    return all_imports


def generate_graph(imports_dict):
    """
    根据解析的导入关系生成依赖关系图
    """
    dot = Digraph(comment="Project Module Imports")
    for file, imports in imports_dict.items():
        file_node = os.path.basename(file)
        dot.node(file_node, file_node)
        for module in imports:
            dot.node(module, module)
            dot.edge(file_node, module)
    return dot


if __name__ == "__main__":
    # 项目目录路径
    project_dir = f"src\main\resources\fronter"
    imports = parse_imports_from_directory(project_dir)
    graph = generate_graph(imports)
    graph.render("project_dependencies", format="png", cleanup=True)
