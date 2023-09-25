import os
import openai

# Set OpenAI API Key and API Base
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

# 遍历docs目录下的所有.md文件，并进行翻译
for filename in os.listdir("docs"):
    if filename.endswith(".md"):
        input_file = os.path.join("docs", filename)
        output_file = os.path.join("docs", "en", filename)
        translate_file(input_file, output_file)
        print(f"Translated {input_file} to {output_file}")