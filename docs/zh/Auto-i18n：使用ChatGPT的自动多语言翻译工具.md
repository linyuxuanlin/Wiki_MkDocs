# Auto-i18n：使用 ChatGPT 的自动多语言翻译工具

Auto-i18n 是一个使用 ChatGPT 自动将 Markdown 文件批量翻译为多语言的工具。

它实现了博客文章 i18n(Internationalization) 的完全自动化。你仅需将博文推送至 GitHub 仓库，即可借助 GitHub Actions 实现自动转译为多种语言。（目前支持英语、西班牙语和阿拉伯语，后续将提供更多语言支持）

**项目地址**：[**linyuxuanlin/Auto-i18n**](https://github.com/linyuxuanlin/Auto-i18n)

我的博客实现 i18n 后的效果：

![](https://img.wiki-power.com/d/wiki-media/img/202310151317233.png)

## 快速上手

1. 首先，将仓库克隆到本地。
2. 将 `env_template.py` 重命名为 `env.py`，并填写你的 ChatGPT API 信息。你可以在项目 [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free) 申请免费的 API 密钥。
3. 使用 `pip install openai` 安装必要的依赖。
4. 运行 `auto-translater` 程序，它会自动处理测试目录 `testdir/to-translate` 下的所有 Markdown 文件，批量翻译为英语、西班牙语、阿拉伯语。

## 详细描述

程序 `auto-translater.py` 的运行逻辑如下：

1. 程序会自动处理测试目录 `testdir/to-translate` 下的所有 Markdown 文件，你可以在 `exclude_list` 变量中排除不需要翻译的文件。
2. 处理后的文件名会被记录在自动生成的 `processed_list.txt` 中。下次运行程序时，已处理的文件将不会再次翻译。
3. 对于原本使用英文撰写的文章，程序不会重新翻译成英文，也不会翻译回中文，而会翻译为其他语言。你需要在文章中添加字段 `> This post was originally written in English.`（注意在上下各留一个空行），以便程序识别。请参考 [测试文章\_en.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md)。
4. 如果需要重新翻译特定文章（例如，翻译结果不准确，或文章内容发生更改等），你可以在文章中加入字段 `[translate]`（同样需要在上下各留一个空行）。这将会忽略 `exclude_list` 和 `processed_list` 的规则，强制进行翻译处理。请参考 [测试文章\_force-mark.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md)。

## GitHub Actions 自动化指南

你可以在自己项目仓库下创建 `.github/workflows/ci.yml`，当检测到 GitHub 仓库更新后，可以使用 GitHub Actions 自动进行翻译处理，并自动 commit 回原仓库。

`ci.yml` 的内容可参考模板：[ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml)

你需要在仓库的 `Settings` - `Secrets and variables` - `Repository secrets` 中添加两个 secrets：`CHATGPT_API_BASE` 和 `CHATGPT_API_KEY`，并在程序 `auto-translater.py` 中将 `import env` 语句注释掉。

## 错误排除

1. 如果需要验证 ChatGPT API key 的可用性，可以参考程序 [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py)。
2. 使用 GitHub Actions 遇到问题时，请优先检查路径引用是否正确（例如 `dir_to_translate` `dir_translated_en` `dir_translated_es` `dir_translated_ar` `processed_list`）。

## 待解决的问题

1. 如果 Markdown 文件包含 Front Matter，可能也会被翻译处理而造成问题。我的解决方法是不采用 Front Matter，直接用一级标题作为文章标题。
2. 如果文章不完整，可能会出现 ChatGPT 帮你翻译并自动续写完整的情况（迷）。
3. 在某些特殊的情况下，可能会出现翻译不准确或某些字段没有翻译的情况，翻译后需校验并手动调整。

## 贡献

欢迎你参与本项目的改进！如果您想要贡献代码、报告问题或提出建议，请查看我们的 [贡献指南](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md)。

## 版权和许可

本项目采用 [MIT 许可证](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE)。

## 问题和支持

如果你在使用 Auto-i18n 时遇到任何问题，或者需要技术支持，请随时 [提交问题](https://github.com/linyuxuanlin/Auto-i18n/issues)。

## 参考与致谢

感谢 [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free) 提供的免费 ChatGPT API key。

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
