# Auto-i18n: Automatic Multilingual Translation Tool using ChatGPT

Auto-i18n is a tool that uses ChatGPT to automatically translate Markdown files into multiple languages.

It fully automates the i18n (Internationalization) of blog articles. You only need to push your blog post to a GitHub repository, and with the help of GitHub Actions, it will automatically translate into multiple languages. (Currently supports English, Spanish, and Arabic, with more language support to come)

**Project Address**: [**linyuxuanlin/Auto-i18n**](https://github.com/linyuxuanlin/Auto-i18n)

The effect of implementing i18n on my blog:

![](https://img.wiki-power.com/d/wiki-media/img/202310151317234.png)

## Quick Start

1. First, clone the repository to your local machine.
2. Rename `env_template.py` to `env.py` and fill in your ChatGPT API information. You can apply for a free API key at [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free).
3. Run `pip install openai` to install the necessary dependencies.
4. Run the `auto-translater` program, which will automatically process all Markdown files in the `testdir/to-translate` test directory and translate them in bulk into English, Spanish, and Arabic.

## Detailed Description

The `auto-translater.py` program runs as follows:

1. The program will automatically process all Markdown files in the `testdir/to-translate` test directory. You can exclude files that do not need to be translated in the `exclude_list` variable.
2. The processed file names will be recorded in the automatically generated `processed_list.txt`. The next time the program is run, files that have already been processed will not be translated again.
3. For articles originally written in English, the program will not re-translate them into English or translate them back into Chinese, but will translate them into other languages. You need to add the field `> This post was originally written in English.` (Note to leave a blank line above and below) in the article for the program to recognize. Please refer to [test article_en.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md).
4. If you need to re-translate a specific article (for example, if the translation result is inaccurate or the article content has changed), you can add the field `[translate]` in the article (also need to leave a blank line above and below). This will ignore the rules of `exclude_list` and `processed_list` and force translation processing. Please refer to [test article_force-mark.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md).

## GitHub Actions Automation Guide

You can create `.github/workflows/ci.yml` in your project repository, which will automatically translate and commit back to the original repository when a GitHub repository update is detected.

The contents of `ci.yml` can refer to the template: [ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml)

You need to add two secrets in the repository's `Settings` - `Secrets and variables` - `Repository secrets`: `CHATGPT_API_BASE` and `CHATGPT_API_KEY`, and comment out the `import env` statement in the `auto-translater.py` program.

## Troubleshooting

1. If you need to verify the availability of the ChatGPT API key, you can refer to the program [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py).
2. When using GitHub Actions and encountering problems, please check the path references first (such as `dir_to_translate`, `dir_translated_en`, `dir_translated_es`, `dir_translated_ar`, `processed_list`).

## Pending Issues

1. If the Markdown file contains Front Matter, it may also cause problems when translated. My solution is to not use Front Matter and use the first-level heading as the article title directly.
2. If the article is incomplete, it may cause ChatGPT to help you translate and automatically continue writing (mystery).
3. In some special cases, inaccurate translations or untranslated fields may occur, and manual adjustment is required after translation.

## Contribution

You are welcome to contribute to the improvement of this project! If you want to contribute code, report issues, or make suggestions, please refer to our [contribution guide](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md).

## Copyright and License

This project is licensed under the [MIT License](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE).

## Issues and Support

If you encounter any problems while using Auto-i18n, or need technical support, please feel free to [submit an issue](https://github.com/linyuxuanlin/Auto-i18n/issues).

## Reference and Acknowledgments

Thanks to [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free) for providing a free ChatGPT API key.

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.