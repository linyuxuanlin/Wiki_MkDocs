# 需求
# 1. 因为我有些文章本身就是使用英文撰写，它们不需要翻译为英文。（文章中包含字段 "> This post is only available in English."）
# 2. 

# -*- coding: utf-8 -*-

import os
import openai
import env
import sys

# 设置 OpenAI API Key 和 API Base 参数
openai.api_key = os.environ.get('CHATGPT_API_KEY')
openai.api_base = os.environ.get('CHATGPT_API_BASE')

# 设置翻译的路径
## Github Codespaces
dir_to_translate = "/workspaces/Wiki_MkDocs/draft/to-translate"
dir_translated_en = "/workspaces/Wiki_MkDocs/docs/en"
dir_translated_es = "/workspaces/Wiki_MkDocs/docs/es"
dir_translated_ar = "/workspaces/Wiki_MkDocs/docs/ar"
## GitHub Action
#dir_to_translate = "/home/runner/work/Wiki_MkDocs/Wiki_MkDocs/draft/to-translate_ar"
#dir_translated = "/home/runner/work/Wiki_MkDocs/Wiki_MkDocs/docs/ar"
## local
#dir_to_translate = "../draft/to-translate_ar"
#dir_translated = "../docs/ar"

# 不进行翻译的文件列表
exclude_list = ["index.md", "Contact-and-Subscribe.md", "WeChat.md"]

# 最大输入字段，超出会拆分输入，防止超出输入字数限制
max_length = 1800

# 由 ChatGPT 翻译的提示
tips_translated_by_chatgpt_en = "\n\n> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions."

# 文章最初使用英语撰写的提示，用来跳过本身为英语的文章被重复翻译为英文
tips_originally_in_en = "> This post was originally written in English."

# 固定字段替换规则。文章中一些固定的字段，不需要每篇都进行翻译，且翻译结果可能不一致，所以直接替换掉。
replace_rules = [
    {
        # 版权信息
        "orginal_text": "> 原文地址：<https://wiki-power.com/>",
        "replaced_en": "> Original: <https://wiki-power.com/>",
        "replaced_es": "> Dirección original del artículo: <https://wiki-power.com/>",
        "replaced_ar": "> عنوان النص: <https://wiki-power.com/>",
    },
    {
        # 版权信息
        "orginal_text": "> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。",
        "replaced_en": "> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.",
        "replaced_es": "> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.",
        "replaced_ar": "> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.",
    },
    {
        # 文章中的站内链接，跳转为当前相同语言的网页
        "orginal_text": "](https://wiki-power.com/",
        "replaced_en": "](https://wiki-power.com/en/",
        "replaced_es": "](https://wiki-power.com/es/",
        "replaced_ar": "](https://wiki-power.com/ar/",
    },
    # {
    #    # 不同语言使用不同图床
    #    "orginal_text": "![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/",
    #    "replaced_en": "![](https://f004.backblazeb2.com/file/wiki-media/",
    #    "replaced_es": "![](https://f004.backblazeb2.com/file/wiki-media/",
    #    "replaced_ar": "![](https://f004.backblazeb2.com/file/wiki-media/",
    # },
]


# 定义翻译函数
def translate_text(text, lang):
    if lang == "en":
        target_lang = "English"
    elif lang == "es":
        target_lang = "Spanish"
    elif lang == "ar":
        target_lang = "Arabic"

    # 使用OpenAI API进行翻译
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Translate the following article into {}, maintain the original markdown format.\n\n{}\n\n{}:".format(
                    target_lang, text, target_lang
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
def translate_file(input_file, output_file, lang):
    
    # 读取输入文件内容
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read()

    # 创建一个字典来存储占位词和对应的替换文本
    placeholder_dict = {}

    # 使用 for 循环应用替换规则，并将匹配的文本替换为占位词
    for i, rule in enumerate(replace_rules):
        find_text = rule["orginal_text"]
        if lang=="en":
            replace_with = rule["replaced_en"]
        elif lang=="es":
            replace_with = rule["replaced_es"]
        elif lang=="ar":
            replace_with = rule["replaced_ar"]
        placeholder = f"to_be_replace[{i + 1}]"
        input_text = input_text.replace(find_text, placeholder)
        placeholder_dict[placeholder] = replace_with

    # print(input_text) # debug 用，看看输入的是什么

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
            output_paragraphs.append(translate_text(current_paragraph,lang))
            current_paragraph = paragraph

    # 处理最后一个段落
    if current_paragraph:
        if len(current_paragraph) + len(input_text) <= max_length:
            # 如果当前段落加上之前的文本长度不超过最大长度，就将它们合并
            input_text += "\n\n" + current_paragraph
        else:
            # 否则翻译当前段落，并将翻译结果添加到输出列表中
            output_paragraphs.append(translate_text(current_paragraph,lang))

    # 如果还有未翻译的文本，就将它们添加到输出列表中
    if input_text:
        output_paragraphs.append(translate_text(input_text,lang))

    # 将输出段落合并为字符串
    output_text = "\n\n".join(output_paragraphs)

    # 加入由 ChatGPT 翻译的提示
    output_text = output_text + tips_translated_by_chatgpt_en

    # 最后，将占位词替换为对应的替换文本
    for placeholder, replacement in placeholder_dict.items():
        output_text = output_text.replace(placeholder, replacement)

    # 写入输出文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_text)



# 按文件名称顺序排序
file_list = os.listdir(dir_to_translate)
sorted_file_list = sorted(file_list)
# print(sorted_file_list)


try:
    # 遍历目录下的所有.md文件，并进行翻译
    for filename in sorted_file_list:
        if filename.endswith(".md"):

            input_file = os.path.join(dir_to_translate, filename)
            with open(input_file, 'r', encoding='utf-8') as f:
                md_content = f.read()

            # 翻译为英语
            output_file = os.path.join(dir_translated_en, filename)
            if tips_originally_in_en in md_content:
                print("Pass the EN post: ", filename)
            elif filename in exclude_list:
                print("Pass the post in exclude_list: ", filename)
            else:
                print("Translating to en: ", filename)
                translate_file(input_file, output_file, "en")
            sys.stdout.flush()

            # 翻译为西班牙语
            output_file = os.path.join(dir_translated_es, filename)
            if tips_originally_in_en in md_content: # 把这句提示删掉，并继续翻译
                md_content.replace(tips_originally_in_en,"") 
                print("Translating to es: ", filename)
                translate_file(input_file, output_file, "es")
            elif filename in exclude_list:
                print("Pass the post in exclude_list: ", filename)
            else:
                print("Translating to es: ", filename)
                translate_file(input_file, output_file, "es")
            sys.stdout.flush()

            # 翻译为阿拉伯语
            output_file = os.path.join(dir_translated_ar, filename)
            with open(input_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
            if tips_originally_in_en in md_content: # 把这句提示删掉，并继续翻译
                md_content.replace(tips_originally_in_en,"") 
                print("Translating to ar: ", filename)
                translate_file(input_file, output_file, "ar")
                os.remove(input_file)
            elif filename in exclude_list:
                print("Pass the post in exclude_list: ", filename)
                os.remove(input_file)
            else:
                print("Translating to ar: ", filename)
                translate_file(input_file, output_file, "ar")
                os.remove(input_file)
            sys.stdout.flush()
except Exception as e:
    # 捕获异常并输出错误信息
    print(f"An error has occurred: {e}")
    sys.stdout.flush()
    # 可选：在这里添加其他处理异常的代码
    raise SystemExit(1)  # 1 表示非正常退出，可以根据需要更改退出码


            # os.remove(input_file)
