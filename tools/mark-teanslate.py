# -*- coding: utf-8 -*-

import os

# 设置路径
dir_to_translate = "../draft/to-translate"
dir_translated = "../docs/en"

# 按文件名称顺序排序
file_list = os.listdir(dir_to_translate)
sorted_file_list = sorted(file_list)

# 遍历目录下的所有.md文件，并进行翻译
for filename in sorted_file_list:
    if filename.endswith(".md"):
        input_file = os.path.join(dir_to_translate, filename)
        output_file = os.path.join(dir_translated, filename)
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        if "> This post is only available in English." in md_content:
            print("Pass the EN post: ", filename)
            os.remove(input_file)
        elif filename=="index.md" or filename=="Contact-and-Subscribe.md" or filename=="WeChat.md":
            os.remove(input_file)
            print("Pass the post: ", filename)
        else:
            print("Translating: ", filename)
            translate_file(input_file, output_file)