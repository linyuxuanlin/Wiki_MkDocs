# -*- coding: utf-8 -*-

import os
import openai

# Set OpenAI API Key and API Base
openai.api_key = os.environ.get('CHATGPT_API_KEY')
openai.api_base = os.environ.get('CHATGPT_API_BASE')

# 定义翻译函数
def translate_text(text):
    # 使用OpenAI API进行翻译
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Translate the following Chinese article into English, and maintain the original markdown format.\n\n{}\n\nEnglish:".format(
                    text
                ),
            }
        ],
    )

    # 获取翻译结果
    output_text = completion.choices[0].message.content

    return output_text


# 定义文章拆分函数
def split_text(text, max_length):
    # 根据段落拆分文章
    paragraphs = text.split("\n\n")
    output_paragraphs = []
    current_paragraph = ""

    for paragraph in paragraphs:
        if len(current_paragraph) + len(paragraph) + 2 <= max_length:
            # 如果当前段落加上新段落的长度不超过最大长度，就将它们合并
            if current_paragraph:
                current_paragraph += "\n\n"
            current_paragraph += paragraph
        else:
            # 否则将当前段落添加到输出列表中，并重新开始一个新段落
            output_paragraphs.append(current_paragraph)
            current_paragraph = paragraph

    # 将最后一个段落添加到输出列表中
    if current_paragraph:
        output_paragraphs.append(current_paragraph)

    # 将输出段落合并为字符串
    output_text = "\n\n".join(output_paragraphs)

    return output_text

# 定义翻译文件函数
def translate_file(input_file, output_file, max_length=1000):
    # 读取输入文件内容
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read()

    # 拆分文章
    paragraphs = input_text.split("\n\n")
    input_text = ""
    output_paragraphs = []
    current_paragraph = ""

    for paragraph in paragraphs:
        if len(current_paragraph) + len(paragraph) + 2 <= max_length:
            # 如果当前段落加上新段落的长度不超过最大长度，就将它们合并
            if current_paragraph:
                current_paragraph += "\n\n"
            current_paragraph += paragraph
        else:
            # 否则翻译当前段落，并将翻译结果添加到输出列表中
            output_paragraphs.append(translate_text(current_paragraph))
            current_paragraph = paragraph

    # 处理最后一个段落
    if current_paragraph:
        if len(current_paragraph) + len(input_text) <= max_length:
            # 如果当前段落加上之前的文本长度不超过最大长度，就将它们合并
            input_text += "\n\n" + current_paragraph
        else:
            # 否则翻译当前段落，并将翻译结果添加到输出列表中
            output_paragraphs.append(translate_text(current_paragraph))

    # 如果还有未翻译的文本，就将它们添加到输出列表中
    if input_text:
        output_paragraphs.append(translate_text(input_text))

    # 将输出段落合并为字符串
    output_text = "\n\n".join(output_paragraphs)

    # 写入输出文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_text)

# 遍历docs目录下的所有.md文件，并进行翻译
for filename in os.listdir("./gpt/docs"):
    if filename.endswith(".md"):
        input_file = os.path.join("./gpt/docs", filename)
        output_file = os.path.join("./gpt/docs", "en", filename)
        translate_file(input_file, output_file)