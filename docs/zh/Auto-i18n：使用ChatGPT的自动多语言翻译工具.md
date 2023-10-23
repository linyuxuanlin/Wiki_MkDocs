# Auto-i18n：使用 ChatGPT 的自动多语言翻译工具

Auto-i18n 是一个使用 ChatGPT 自动将 Markdown 文件批量翻译为多语言的工具。它实现了博客文章 i18n(Internationalization) 的全自动化。你仅需将博文推送至 GitHub 仓库，即可借助 GitHub Actions 实现自动转译为多种语言。（目前支持英语、西班牙语和阿拉伯语，后续将提供更多语言支持）

Auto-i18n 的主要特性：

- **批量多语言翻译**：Auto-i18n 提供了批量翻译的功能，使你能够将一整个路径下的所有 Markdown 文档一次性翻译多语言，极大地提高了多语言化项目的效率。
- **兼容 Front Matter**：Auto-i18n 兼容 Markdown Front Matter 语法，你可以自定义不同字段的翻译或替换规则。
- **固定内容替换**：Auto-i18n 还支持固定内容替换。如果你希望文档中一些重复字段的译文保持不变，这个功能可以帮助你实现文档的一致性。
- **自动化工作流**：你可以使用 GitHub Actions 实现自动化的翻译流程"。。无需手动干预，翻译工作会自动进行并更新文档，使你能够更专注于内容。

## 快速上手

1. 将仓库克隆到本地，把 `env_template.py` 重命名为 `env.py`，并提供你的 ChatGPT API。如果你没有自己的 API，可以到 [GPT_API_free](https://github.com/chatanywhere/GPT_API_free) 申请到一个免费的；也可也借助 [go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) 把网页版 ChatGPT 转 API 使用。
2. 安装必需的模块：`pip install -r requirements.txt` 。
3. 执行命令 `python auto-translater.py` 运行程序，它将会自动处理测试目录 `testdir/to-translate` 下的所有 Markdown 文件，批量翻译为英语、西班牙语、阿拉伯语。（后续将提供更多语言支持）

## 详细描述

程序 `auto-translater.py` 的运行逻辑如下：

1. 程序将自动处理测试目录 `testdir/to-translate` 下的所有 Markdown 文件，你可以在 `exclude_list` 变量中排除不需要翻译的文件。
2. 处理后的文件名会被记录在自动生成的 `processed_list.txt` 中。下次运行程序时，已处理的文件将不会再次翻译。
3. 对于原本使用英文撰写的文章，程序不会重新翻译成英文，也不会翻译回中文，而会翻译为其他语言。你需要在文章中添加字段 `> This post was originally written in English.`（注意在上下各留一个空行），以便程序识别。请参考 [测试文章\_en.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md)。
4. 如果需要重新翻译指定文章（例如，翻译结果不准确，或文章内容发生更改等），你可以在文章中加入字段 `[translate]`（同样需要在上下各留一个空行）。这将会忽略 `exclude_list` 和 `processed_list` 的规则，强制进行翻译处理。请参考 [测试文章\_force-mark.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md)。
5. 如果 Markdown 文件中包含 Front Matter，将按照程序内的规则 `front_matter_translation_rules` 选择以下处理方式：
   1. 自动翻译：由 ChatGPT 翻译。适用于文章标题或文章描述字段。
   2. 固定字段替换：适用于分类或标签字段。例如同一个中文标签名，不希望被翻译成不同的英文标签造成索引错误。
   3. 不做任何处理：如果字段未出现在以上两种规则中，将保留原文，不做任何处理。适用于日期、url 等。

## GitHub Actions 自动化指南

你可以在自己项目仓库下创建 `.github/workflows/ci.yml`，当检测到 GitHub 仓库更新后，可以使用 GitHub Actions 自动进行翻译处理，并自动 commit 回原仓库。

`ci.yml` 的内容可参考模板：[ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml)

你需要在仓库的 `Settings` - `Secrets and variables` - `Repository secrets` 中添加两个 secrets：`CHATGPT_API_BASE` 和 `CHATGPT_API_KEY`，并在程序 `auto-translater.py` 中将 `import env` 语句注释掉。

## 错误排除

1. 如果需要验证 ChatGPT API key 的可用性，可以使用程序 [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py) 进行测试。如果在国内使用官方 API，需要有本地代理。
2. 如果 Markdown 中的 Front Matter 无法被正常识别，可以使用程序 [detect_front_matter.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/detect_front_matter.py) 测试。
3. 在使用 GitHub Actions 遇到问题时，请优先检查路径引用是否正确（例如 `dir_to_translate` `dir_translated_en` `dir_translated_es` `dir_translated_ar` `processed_list`）。

## 待解决的问题

1. 在某些特殊的情况下，可能会出现翻译不准确、或某些字段没有翻译的情况，建议翻译后手动校验再发布文章。
2. （已解决）~~如果 Markdown 中包含 Front Matter，将保留 Front Matter 的原始内容。Front Matter 部分参数翻译的功能正在开发中。~~

## 贡献

欢迎你参与本项目的改进！如果您想要贡献代码、报告问题或提出建议，请查看 [贡献指南](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md)。

## 版权和许可

本项目采用 [MIT 许可证](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE)。

## 问题和支持

如果你在使用 Auto-i18n 时遇到任何问题，或者需要技术支持，请随时 [提交问题](https://github.com/linyuxuanlin/Auto-i18n/issues)。

我的博客使用 Auto-i18n 实现了多语言支持，你可以到 [Power's Wiki](https://wiki-power.com) 查看 Demo 效果。

[![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202310222223670.png)](https://wiki-power.com)

## 致谢

- 感谢 [chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free) 提供的免费 ChatGPT API key。
- 感谢 [linweiyuan/go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) 提供的把网页版 ChatGPT 转 API 的方法。

[![Star History Chart](https://api.star-history.com/svg?repos=linyuxuanlin/Auto-i18n&type=Date)](https://star-history.com/#linyuxuanlin/Auto-i18n&Date)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
