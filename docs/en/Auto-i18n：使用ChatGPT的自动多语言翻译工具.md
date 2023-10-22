# Auto-i18n: Using ChatGPT's Automatic Multilingual Translation Tool

Auto-i18n is a tool that utilizes ChatGPT to automatically translate Markdown files into multiple languages in bulk.

It achieves complete automation of blog article internationalization (i18n). You simply need to push your blog posts to a GitHub repository, and with the help of GitHub Actions, you can automatically translate them into multiple languages. (Currently supporting English, Spanish, and Arabic, with more language support to come in the future.)

**Project Repository**: [**linyuxuanlin/Auto-i18n**](https://github.com/linyuxuanlin/Auto-i18n)

The effect of implementing i18n on my blog:

![Example Image](https://img.wiki-power.com/d/wiki-media/img/202310151317234.png)

## Quick Start

1. First, clone the repository to your local machine.
2. Rename `env_template.py` to `env.py` and fill in your ChatGPT API information. You can apply for a free API key in the [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free) project.
3. Run `pip install openai` to install the necessary dependencies.
4. Run the `auto-translater` program, which will automatically process all Markdown files in the test directory `testdir/to-translate` and translate them into English, Spanish, and Arabic in bulk.

## Detailed Description

The logic of the `auto-translater.py` program is as follows:

1. The program will automatically process all Markdown files in the test directory `testdir/to-translate`. You can exclude files that do not need translation in the `exclude_list` variable.
2. The processed file names will be recorded in the automatically generated `processed_list.txt`. The next time you run the program, files that have already been processed will not be translated again.
3. For articles originally written in English, the program will not re-translate them into English or back into Chinese; instead, it will translate them into other languages. You need to add the following field in the article: `> This post was originally written in English.` (Note: leave a blank line above and below). Please refer to [Test Article\_en.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md).
4. If you need to retranslate specific articles (e.g., inaccurate translation results or changes in article content), you can add the `[translate]` field in the article (again, leave a blank line above and below). This will override the rules of `exclude_list` and `processed_list` and force the translation process. Please refer to [Test Article\_force-mark.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md).

## GitHub Actions Automation Guide

You can create a `.github/workflows/ci.yml` in your project repository to automatically translate and commit changes to the original repository when GitHub repository updates are detected.

The content of `ci.yml` can be based on the template: [ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml).

You need to add two secrets in the repository's `Settings` - `Secrets and variables` - `Repository secrets`: `CHATGPT_API_BASE` and `CHATGPT_API_KEY`. Also, comment out the `import env` statement in the `auto-translater.py` program.

## Troubleshooting

1. If you need to validate the availability of your ChatGPT API key, you can refer to the [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py) script.

2. When encountering issues with GitHub Actions, please first check if the path references are correct (e.g., `dir_to_translate`, `dir_translated_en`, `dir_translated_es`, `dir_translated_ar`, `processed_list`).

## Pending Issues

1. If a Markdown file contains Front Matter, it might lead to problems during translation. My solution is to avoid using Front Matter and directly use a top-level heading as the article title.

2. If an article is incomplete, there may be situations where ChatGPT helps you translate and automatically complete it (mystery).

3. In certain special cases, there may be inaccuracies in the translation or some fields that are not translated. It's necessary to verify and make manual adjustments after translation.

## Contribution

You are welcome to contribute to the improvement of this project! If you'd like to contribute code, report issues, or provide suggestions, please refer to our [Contribution Guidelines](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md).

## Copyright and License

This project is licensed under the [MIT License](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE).

## Issues and Support

If you encounter any problems while using Auto-i18n or need technical support, please feel free to [submit an issue](https://github.com/linyuxuanlin/Auto-i18n/issues).

## References and Acknowledgments

Special thanks to [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free) for providing the free ChatGPT API key.

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.