import os
import openai

# 设置OpenAI API Key和API Base
openai.api_key = os.environ.get('CHATGPT_API_KEY')
openai.api_base = os.environ.get('CHATGPT_API_BASE')

# 定义翻译函数
def translate_file(input_file, output_file):
    # 读取输入文件内容
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read()
        #print(input_text)

    # 使用OpenAI API进行翻译
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Translate the following Chinese text into English:\n\n{}\n\nEnglish:".format(input_text)}]
    )

    # 获取翻译结果
    output_text = completion.choices[0].message.content

    # 写入输出文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_text)

# 遍历docstest目录下的所有.md文件，并进行翻译
for filename in os.listdir("docstest"):
    if filename.endswith(".md"):
        # 获取文件名和扩展名
        file_name, file_ext = os.path.splitext(filename)

        # 对文件名进行翻译
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Translate the following Chinese text into English:\n\n{}\n\nEnglish:".format(filename)}]
        )

        # 获取翻译结果
        file_name_en = completion.choices[0].message.content

        # 创建新文件
        output_file = os.path.join("docstest", "en", f"{file_name_en}")

        # 进行文件内容翻译
        input_file = os.path.join("docstest", filename)
        translate_file(input_file, output_file)

        print(f"Translated {input_file} to {output_file}")