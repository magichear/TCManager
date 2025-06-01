import os
import re
from collections import defaultdict


def find_java_files(base_dir):
    """递归查找所有 .java 文件"""
    java_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
    return java_files


def parse_java_file(file_path):
    """解析 .java 文件，提取类名和 import 依赖"""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 提取类名
    class_match = re.search(r"public\s+class\s+(\w+)", content)
    class_name = class_match.group(1) if class_match else None

    # 提取 import 语句
    imports = re.findall(r"import\s+([\w\.]+);", content)
    return class_name, imports


def build_dependency_graph(base_dir):
    """构建类之间的依赖关系图"""
    java_files = find_java_files(base_dir)
    dependency_graph = defaultdict(list)

    for java_file in java_files:
        class_name, imports = parse_java_file(java_file)
        if class_name:
            for imp in imports:
                # 只记录项目内部的依赖（排除外部库）
                if imp.startswith("com.magichear"):
                    dependency_graph[class_name].append(
                        imp.split(".")[-1]
                    )  # 只记录类名
    return dependency_graph


def main():
    project_dir = f"D:\Study_Work\Electronic_data\CS\AAAUniversity\DB\Lab\Lab3\TCManager\src\main\java\com\magichear\TCManager"
    dependency_graph = build_dependency_graph(project_dir)

    # 打印依赖关系
    for cls, deps in dependency_graph.items():
        print(f"{cls} depends on: {', '.join(deps)}")


if __name__ == "__main__":
    main()
