# Auto-i18n: Automatic Multilingual Translation Tool Using ChatGPT

Auto-i18n is a tool that leverages ChatGPT to automatically translate Markdown files into multiple languages. It achieves complete automation of blog article internationalization (i18n). Simply push your blog posts to a GitHub repository, and with the help of GitHub Actions, they can be automatically translated into various languages. (Currently supporting English, Spanish, and Arabic, with more language support to come in the future)

Key Features of Auto-i18n:

- **Batch Multilingual Translation**: Auto-i18n offers a batch translation feature, allowing you to translate all Markdown documents in an entire directory in multiple languages in one go, greatly enhancing the efficiency of multilingual projects.
- **Front Matter Compatibility**: Auto-i18n is compatible with Markdown Front Matter syntax, enabling you to customize translation or replacement rules for different fields.
- **Fixed Content Replacement**: Auto-i18n also supports fixed content replacement. If you wish to keep the translations of certain repetitive fields in your documents consistent, this feature can help you maintain document consistency.
- **Automation Workflow**: You can use GitHub Actions to implement an automated translation process without manual intervention. Translation work will be carried out automatically, allowing you to focus more on content.

## Getting Started

1. Clone the repository to your local machine, rename `env_template.py` to `env.py`, and provide your ChatGPT API key. If you don't have your own API key, you can obtain a free one from [GPT_API_free](https://github.com/chatanywhere/GPT_API_free) or utilize [go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) to turn the web-based ChatGPT into an API.
2. Install the necessary modules: `pip install -r requirements.txt`.
3. Execute the command `python auto-translator.py` to run the program. It will automatically process all Markdown files in the test directory `testdir/to-translate`, translating them into English, Spanish, and Arabic. (More language support will be added in the future)

## Detailed Description

The logic behind the operation of the `auto-translator.py` program is as follows:

1. The program will automatically process all Markdown files in the `testdir/to-translate` test directory. You can exclude files that do not need translation in the `exclude_list` variable.
2. The processed file names will be recorded in the automatically generated `processed_list.txt`. When you run the program again, files that have already been processed will not be translated again.
3. For articles originally written in English, the program will not retranslate them into English or back into Chinese but will translate them into other languages. You need to add the following field to the article: `> This post was originally written in English.` (please leave a blank line above and below). Please refer to [Test Article\_en.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md).
4. If you need to retranslate a specific article (for example, if the translation result is inaccurate or the article content has changed), you can add the `[translate]` field to the article (again, please leave a blank line above and below). This will override the rules of `exclude_list` and `processed_list` and force translation. Please refer to [Test Article\_force-mark.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md).
5. If a Markdown file contains Front Matter, the program will handle it according to the rules specified internally as follows:
   1. Automatic Translation: Translated by ChatGPT. Applicable to article titles or article description fields.
   2. Fixed Field Replacement: Applicable to categories or tags fields. For example, if you have the same Chinese tag name and do not want it to be translated into different English tags causing indexing errors.
   3. No Processing: If the field does not appear in the above two rules, it will be retained as is, without any changes. This is suitable for dates, URLs, etc.

## GitHub Actions Automation Guide

You can create a `.github/workflows/ci.yml` in your own project repository. When changes are detected in your GitHub repository, GitHub Actions can automatically handle the translation and commit the changes back to the original repository.

You can refer to the contents of `ci.yml` using this template: [ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml).

You need to add two secrets in your repository's `Settings` - `Secrets and variables` - `Repository secrets`: `CHATGPT_API_BASE` and `CHATGPT_API_KEY`. Then, comment out the `import env` statement in the `auto-translater.py` program.

## Troubleshooting

1. If you need to verify the availability of the ChatGPT API key, you can use the program [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py) for testing. If you are using the official API in China, you will need a local proxy.
2. If Front Matter in Markdown cannot be recognized correctly, you can use the program [detect_front_matter.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/detect_front_matter.py) for testing.
3. When encountering issues with GitHub Actions, please check the correctness of path references, such as `dir_to_translate`, `dir_translated_en`, `dir_translated_es`, `dir_translated_ar`, and `processed_list`.

1. In certain special circumstances, translation inaccuracies or untranslating some fields may occur. We recommend manually verifying the translation and then proceeding with article publication.

2. (Resolved) ~~If Markdown contains Front Matter, the original content of Front Matter will be retained. The translation functionality for parameters within the Front Matter section is currently under development.~~

## Contribution

You are welcome to contribute to this project! If you wish to contribute code, report issues, or provide suggestions, please refer to the [Contribution Guidelines](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md).

## Copyright and License

This project is licensed under the [MIT License](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE).

## Issues and Support

If you encounter any issues while using Auto-i18n or require technical support, please feel free to [submit an issue](https://github.com/linyuxuanlin/Auto-i18n/issues).

My blog utilizes Auto-i18n to implement multi-language support. You can check out the demo at [Power's Wiki](https://wiki-power.com).

[![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202310222223670.png)](https://wiki-power.com)

## Acknowledgments

- Special thanks to [chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free) for providing a free ChatGPT API key.
- Gratitude to [linweiyuan/go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) for providing the method to convert the web-based ChatGPT to an API.

[![Star History Chart](https://api.star-history.com/svg?repos=linyuxuanlin/Auto-i18n&type=Date)](https://star-history.com/#linyuxuanlin/Auto-i18n&Date)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.