# 程序执行的逻辑：
# 1. 程序会默认翻译 dir_to_translate 下的所有 Markdown 文件，如果有不需要翻译的文件，请加进 exclude_list 变量中
# 2. 经程序处理过的文件，文件名会被加进自动生成的 `processed_list.txt` 中，下次默认不进行处理。
# 3. 原本就用英文撰写的文章，不会被重新翻译为英文，也不会翻译回中文，会翻译为其他语言。需要在文章中添加字段 `> This post was originally written in English.`（注意上下需各留一个空行），以便程序识别。
# 4. 如果某篇文章需要重新翻译（例如翻译结果不完备，或文章内容有修改），可在文章中加入字段 `[translate]`（注意上下需各留一个空行）。这个操作将不理会 exclude_list 与 processed_list 规则，仅遵守规则3（如果原本为英文，则不会被重新翻译为英语），进行翻译处理

# 缺陷：
# 1. 如果Markdown文件包含 Front Matter，可能也会被翻译而造成问题。我的解决方法是不适用Front Matter，直接用一级标题作为文章标题。
# 2. 如果文章不完整，可能会出现 ChatGPT 帮你翻译并续写的情况，需要手动验证
# 3. 在某些特殊的情况下，可能会出现翻译不正确或某些字段没有翻译的情况，需进行验证并手动调整

# -*- coding: utf-8 -*-

import os
import openai

import env
import sys

# 设置 OpenAI API Key 和 API Base 参数
openai.api_key = os.environ.get("CHATGPT_API_KEY")
openai.api_base = os.environ.get("CHATGPT_API_BASE")

# 设置翻译的路径
## Github Codespaces
dir_to_translate = "to-translate"
dir_translated_en = "docs/en"
dir_translated_es = "docs/es"
dir_translated_ar = "docs/ar"
## GitHub Action
# dir_to_translate = "/home/runner/work/Wiki_MkDocs/Wiki_MkDocs/draft/to-translate_ar"
# dir_translated = "/home/runner/work/Wiki_MkDocs/Wiki_MkDocs/docs/ar"
## local
# dir_to_translate = "../draft/to-translate_ar"
# dir_translated = "../docs/ar"

exclude_list = ["index.md", "Contact-and-Subscribe.md", "WeChat.md"]  # 不进行翻译的文件列表
processed_list = "processed_list.txt"  # 已处理的 Markdown 文件名的列表，会自动生成

# 设置最大输入字段，超出会拆分输入，防止超出输入字数限制
max_length = 1800

# 由 ChatGPT 翻译的提示
tips_translated_by_chatgpt_en = "\n\n> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions."
tips_translated_by_chatgpt_es = "\n\n> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión."
tips_translated_by_chatgpt_ar = "\n\n> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال."

# 文章使用英文撰写的提示，避免本身为英文的文章被重复翻译为英文
marker_written_in_en = "\n> This post was originally written in English.\n"
# 即使在已处理的列表中，仍需要重新翻译的标记
marker_force_translate = "\n[translate]\n"

# 固定字段替换规则。文章中一些固定的字段，不需要每篇都进行翻译，且翻译结果可能不一致，所以直接替换掉。
replace_rules = [
    {
        # 版权信息手动翻译
        "orginal_text": "> 原文地址：<https://wiki-power.com/>",
        "replaced_en": "> Original: <https://wiki-power.com/>",
        "replaced_es": "> Dirección original del artículo: <https://wiki-power.com/>",
        "replaced_ar": "> عنوان النص: <https://wiki-power.com/>",
    },
    {
        # 版权信息手动翻译
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
def translate_file(input_file, filename, lang):
    print("Translating into {}: ".format(lang), filename)

    # 定义输出文件
    if lang == "en":
        if not os.path.exists(dir_translated_en):
            os.makedirs(dir_translated_en)
        output_file = os.path.join(dir_translated_en, filename)
    elif lang == "es":
        if not os.path.exists(dir_translated_es):
            os.makedirs(dir_translated_es)
        output_file = os.path.join(dir_translated_es, filename)
    elif lang == "ar":
        if not os.path.exists(dir_translated_ar):
            os.makedirs(dir_translated_ar)
        output_file = os.path.join(dir_translated_ar, filename)

    # 读取输入文件内容
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read()

    # 创建一个字典来存储占位词和对应的替换文本
    placeholder_dict = {}

    # 使用 for 循环应用替换规则，并将匹配的文本替换为占位词
    for i, rule in enumerate(replace_rules):
        find_text = rule["orginal_text"]
        if lang == "en":
            replace_with = rule["replaced_en"]
        elif lang == "es":
            replace_with = rule["replaced_es"]
        elif lang == "ar":
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
            output_paragraphs.append(translate_text(current_paragraph, lang))
            current_paragraph = paragraph

    # 处理最后一个段落
    if current_paragraph:
        if len(current_paragraph) + len(input_text) <= max_length:
            # 如果当前段落加上之前的文本长度不超过最大长度，就将它们合并
            input_text += "\n\n" + current_paragraph
        else:
            # 否则翻译当前段落，并将翻译结果添加到输出列表中
            output_paragraphs.append(translate_text(current_paragraph, lang))

    # 如果还有未翻译的文本，就将它们添加到输出列表中
    if input_text:
        output_paragraphs.append(translate_text(input_text, lang))

    # 将输出段落合并为字符串
    output_text = "\n\n".join(output_paragraphs)

    # 加入由 ChatGPT 翻译的提示
    if lang == "en":
        output_text = output_text + tips_translated_by_chatgpt_en
    elif lang == "es":
        output_text = output_text + tips_translated_by_chatgpt_es
    elif lang == "ar":
        output_text = output_text + tips_translated_by_chatgpt_ar

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
    # 创建一个外部列表文件，存放已处理的 Markdown 文件名列表
    if not os.path.exists(processed_list):
        with open(processed_list, "w", encoding="utf-8") as f:
            pass
    # 遍历目录下的所有.md文件，并进行翻译
    for filename in sorted_file_list:
        if filename.endswith(".md"):
            input_file = os.path.join(dir_to_translate, filename)

            # 读取 Markdown 文件的内容
            with open(input_file, "r", encoding="utf-8") as f:
                md_content = f.read()

            # 读取processed_list内容
            with open(processed_list, "r", encoding="utf-8") as f:
                processed_list_content = f.read()

            if marker_force_translate in md_content:  # 如果有强制翻译的标识，则执行这部分的代码
                # 删除这个提示字段
                md_content = md_content.replace(marker_force_translate, "")
                # 将删除marker_force_translate后的内容写回原文件
                # with open(filename, "w", encoding="utf-8") as f:
                #    f.write(md_content)
                if marker_written_in_en in md_content:  # 翻译为除英文之外的语言
                    print("Pass the en-en translation: ", filename)  # 删除这个字段
                    md_content = md_content.replace(marker_written_in_en, "")
                    translate_file(input_file, filename, "es")
                    translate_file(input_file, filename, "ar")
                else:  # 翻译为所有语言
                    translate_file(input_file, filename, "en")
                    translate_file(input_file, filename, "es")
                    translate_file(input_file, filename, "ar")
            elif filename in exclude_list:  # 不进行翻译
                print("Pass the post in exclude_list: ", filename)
            elif filename in processed_list_content:  # 不进行翻译
                print("Pass the post in processed_list: ", filename)
            elif marker_written_in_en in md_content:  # 翻译为除英文之外的语言
                print("Pass the en-en translation: ", filename)
                md_content = md_content.replace(marker_written_in_en, "")  # 删除这个字段
                translate_file(input_file, filename, "es")
                translate_file(input_file, filename, "ar")
            else:  # 翻译为所有语言
                translate_file(input_file, filename, "en")
                translate_file(input_file, filename, "es")
                translate_file(input_file, filename, "ar")

            # 将处理完成的文件名加到列表，下次跳过不处理
            if filename not in processed_list_content:
                print("Added into processed_list: ", filename)
                with open(processed_list, "a", encoding="utf-8") as f:
                    # 写入字符串到文件中
                    f.write(filename)
                    f.write("\n")

            # 强制将缓冲区中的数据刷新到终端中，使用 GitHub Action 时方便实时查看过程
            sys.stdout.flush()

except Exception as e:
    # 捕获异常并输出错误信息
    print(f"An error has occurred: {e}")
    sys.stdout.flush()
    # 可选：在这里添加其他处理异常的代码
    raise SystemExit(1)  # 1 表示非正常退出，可以根据需要更改退出码
    # os.remove(input_file)  # 删除源文件
