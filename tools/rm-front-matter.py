import os
import re

# 定义要处理的目录路径
directory_path = "../docs/zh"

# 正则表达式模式，用于匹配包含id和title字段的Markdown头部
pattern = r"---\s*id:\s*(.*?)\s*title:\s*(.*?)\s*---\s"

# 遍历指定目录下的所有Markdown文件
for root, dirs, files in os.walk(directory_path):
    for file_name in files:
        if file_name.endswith(".md") and file_name != "index.md":  # 排除index.md
            file_path = os.path.join(root, file_name)

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # 使用正则表达式查找匹配的头部信息
            match = re.search(pattern, content, re.DOTALL)

            if match:
                id_text = match.group(1)
                title_text = match.group(2)

                # 构建替换后的标题行
                replacement = f"# {title_text}\n"

                # 替换Markdown文件中的头部信息
                updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

                # 将更新后的内容写回文件
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(updated_content)

                # 打印已处理的文件名
                print(f"已处理文件: {file_path}")

