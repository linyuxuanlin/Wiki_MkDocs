# Auto-i18n: Using ChatGPT's Automatic Multilingual Translation Tool

Auto-i18n is a tool that leverages ChatGPT to automatically translate Markdown files into multiple languages in bulk. It achieves full automation of blog article internationalization (i18n). You simply need to push your blog posts to a GitHub repository, and with the help of GitHub Actions, it will automatically translate them into various languages. (Currently supports English, Spanish, and Arabic, with more language support coming soon.)

Key features of Auto-i18n:

- **Batch Multilingual Translation**: Auto-i18n provides a batch translation feature, allowing you to translate multiple Markdown documents in a whole path into multiple languages simultaneously, greatly improving the efficiency of multilingual projects.

- **Front Matter Compatibility**: Auto-i18n is compatible with Markdown Front Matter syntax, allowing you to customize translation or replacement rules for different fields.

- **Fixed Content Replacement**: Auto-i18n also supports fixed content replacement. If you want the translations of certain repeated fields in your documents to remain consistent, this feature can help you achieve document consistency.

- **Automated Workflow**: You can automate the translation process using GitHub Actions. No manual intervention is required; the translation work will automatically proceed and update the documents, allowing you to focus more on the content.

## Getting Started

1. Clone the repository to your local machine, rename `env_template.py` to `env.py`, and provide your ChatGPT API. If you don't have your API, you can apply for a free one at [GPT_API_free](https://github.com/chatanywhere/GPT_API_free). Alternatively, you can use [go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) to convert the web-based ChatGPT into an API.

2. Install the required modules: `pip install -r requirements.txt`.

3. Execute the command `python auto-translator.py` to run the program. It will automatically process all Markdown files in the test directory `testdir/to-translate` in bulk, translating them into English, Spanish, and Arabic. (More language support will be added in the future.)

## Detailed Description

The logic of the `auto-translator.py` program is as follows:

1. The program will automatically process all Markdown files in the test directory `testdir/to-translate`, and you can exclude files that don't need translation in the `exclude_list` variable.

2. The processed file names will be recorded in the automatically generated `processed_list.txt`. When you run the program next time, files that have already been processed will not be translated again.

3. For articles originally written in English, the program will not re-translate them into English or back into Chinese but will translate them into other languages. You need to add the field `> This post was originally written in English.` in the article (with an empty line above and below) for the program to recognize. Please refer to [测试文章\_en.md](testdir/to-translate/测试文章_en.md).

4. If you need to re-translate a specific article (e.g., if the translation results are inaccurate or if the content has changed), you can add the field `[translate]` to the article (again with an empty line above and below). This will bypass the rules of `exclude_list` and `processed_list` and force translation. Please refer to [测试文章\_force-mark.md](testdir/to-translate/测试文章_force-mark.md).

5. If a Markdown file contains Front Matter, it will be processed according to the rules defined in the program's `front_matter_translation_rules`:
   1. Automatic Translation: Translated by ChatGPT. Applicable to article titles or article description fields.
   2. Fixed Field Replacement: Applicable to categories or tags fields. For example, when the same Chinese tag name should not be translated into different English tags to avoid indexing errors.
   3. No Action: If a field does not appear in the above two rules, the original text will be retained, and no action will be taken. This is suitable for date, URL, and other fields.

## GitHub Actions Automation Guide

You can create a `.github/workflows/ci.yml` file in your project repository. This file enables automatic translation and commits to your repository when changes are detected in your GitHub repository.

You can refer to the template for the contents of `ci.yml` here: [ci_template.yml](ci_template.yml).

To set this up, you'll need to add two secrets in your repository under `Settings` - `Secrets and variables` - `Repository secrets`: `CHATGPT_API_BASE` and `CHATGPT_API_KEY`. Additionally, make sure to comment out the `import env` statement in the `auto-translater.py` program.

## Troubleshooting

1. If you want to verify the usability of your ChatGPT API key, you can use the program [verify-api-key.py](Archive/verify-api-key.py) for testing. Please note that if you are using the official API within China, you may need a local proxy.
2. If Front Matter in your Markdown cannot be recognized correctly, you can use the program [detect_front_matter.py](Archive/detect_front_matter.py) for testing.
3. When encountering issues with GitHub Actions, please ensure that your path references are correct (e.g., `dir_to_translate`, `dir_translated_en`, `dir_translated_es`, `dir_translated_ar`, `processed_list`).

## Outstanding Issues

1. In certain special cases, translation inaccuracies or unprocessed fields may occur. It is recommended to manually verify the translation before publishing the content.
2. (Resolved) ~~Front Matter in Markdown will retain its original content. The translation of parameters within the Front Matter is currently in development.~~

## Contribution

We welcome your contributions to this project! If you would like to contribute code, report issues, or provide suggestions, please check our [Contribution Guidelines](CONTRIBUTING.md).

## Copyright and License

This project is licensed under the [MIT License](LICENSE).

## Questions and Support

If you encounter any issues while using Auto-i18n or need technical support, please feel free to [submit an issue](https://github.com/linyuxuanlin/Auto-i18n/issues).

My blog utilizes Auto-i18n to achieve multilingual support. You can check out the demo at [Power's Wiki](https://wiki-power.com).

[![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202310222223670.png)](https://wiki-power.com)

## Acknowledgments

- Special thanks to [chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free) for providing the free ChatGPT API key.
- We appreciate [linweiyuan/go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) for offering the method to convert the web-based ChatGPT into an API.

[![Star History Chart](https://api.star-history.com/svg?repos=linyuxuanlin/Auto-i18n&type=Date)](https://star-history.com/#linyuxuanlin/Auto-i18n&Date)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.