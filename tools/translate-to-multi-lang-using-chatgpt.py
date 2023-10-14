# 需求
# 1. 因为我有些文章本身就是使用英文撰写，它们不需要翻译为英文。（文章中包含字段 "> This post is only available in English."）
# 2. 

# -*- coding: utf-8 -*-

import os
import openai
#import env
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

# 创建一个包含多个替换规则的列表。文章中一些固定的字段，不需要每篇都进行翻译，且翻译结果可能不一致，所以直接替换掉。
replace_rules_ar = [
    {"find": "> 原文地址：<https://wiki-power.com/>", "replace_with": "> عنوان النص: <https://wiki-power.com/>"},
    {"find": "> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。", "replace_with": "> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر."},
    {"find": "](https://wiki-power.com/", "replace_with": "](https://wiki-power.com/ar/"},
    {"find": "![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/", "replace_with": "![](https://f004.backblazeb2.com/file/wiki-media/"},
]
