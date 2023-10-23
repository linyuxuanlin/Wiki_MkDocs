# Auto-i18n: Automatic Multilingual Translation Tool using ChatGPT

Auto-i18n is a tool that uses ChatGPT to automatically translate Markdown files into multiple languages. It achieves full automation of blog article i18n (Internationalization). By simply pushing your blog posts to a GitHub repository, you can leverage GitHub Actions to automatically translate them into multiple languages. (Currently supports English, Spanish, and Arabic, with more language support to be added in the future)

Key features of Auto-i18n:

- **Batch Multilingual Translation**: Auto-i18n provides the functionality to translate multiple Markdown documents in a given path all at once, greatly improving the efficiency of multilingual projects.
- **Front Matter Compatibility**: Auto-i18n is compatible with Markdown Front Matter syntax, allowing you to customize translation or replacement rules for different fields.
- **Fixed Content Replacement**: Auto-i18n also supports fixed content replacement. If you want the translations of certain repetitive fields in the document to remain unchanged, this feature can help you achieve consistency in your documents.
- **Automated Workflow**: You can use GitHub Actions to implement an automated translation workflow without manual intervention. The translation process will be carried out automatically, updating the documents and allowing you to focus more on the content.

## Quick Start

1. Clone the repository to your local machine, rename `env_template.py` to `env.py`, and provide your ChatGPT API. If you don't have your own API, you can apply for a free one at [GPT_API_free](https://github.com/chatanywhere/GPT_API_free), or use [go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) to convert the web version of ChatGPT into an API.
2. Install the required modules: `pip install -r requirements.txt`.
3. Run the command `python auto-translater.py` to execute the program. It will automatically process all Markdown files in the test directory `testdir/to-translate` and translate them in batches into English, Spanish, and Arabic. (More language support will be added in the future)

## Detailed Description

The logic of the program `auto-translater.py` is as follows:

Translate into English:

1. The program will automatically process all Markdown files in the test directory `testdir/to-translate`. You can exclude files that do not need to be translated in the `exclude_list` variable.
2. The processed file names will be recorded in the automatically generated `processed_list.txt`. When the program is run again, the processed files will not be translated again.
3. For articles originally written in English, the program will not translate them back into English or translate them into Chinese. Instead, they will be translated into other languages. You need to add the field `> This post was originally written in English.` (leave a blank line above and below) in the article for the program to recognize. Please refer to [test article\_en.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/test%20article_en.md).
4. If you need to re-translate a specific article (e.g., if the translation result is inaccurate or the content of the article has changed), you can add the field `[translate]` in the article (also leaving a blank line above and below). This will override the rules of `exclude_list` and `processed_list` and force the translation process. Please refer to [test article\_force-mark.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/test%20article_force-mark.md).
5. If the Markdown file contains Front Matter, the following processing methods will be selected according to the rules in the program `front_matter_translation_rules`:
   1. Automatic translation: Translated by ChatGPT. Applicable to article titles or article description fields.
   2. Fixed field replacement: Applicable to category or tag fields. For example, for the same Chinese tag name, you do not want it to be translated into different English tags causing indexing errors.
   3. No processing: If the field does not appear in the above two rules, the original text will be retained without any processing. Applicable to dates, URLs, etc.

## GitHub Actions Automation Guide

You can create `.github/workflows/ci.yml` in your project repository to automatically translate and commit back to the original repository when a GitHub repository update is detected using GitHub Actions.

The content of `ci.yml` can refer to the template: [ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml)

You need to add two secrets in the repository's `Settings` - `Secrets and variables` - `Repository secrets`: `CHATGPT_API_BASE` and `CHATGPT_API_KEY`, and comment out the `import env` statement in the program `auto-translater.py`.

## Troubleshooting

1. If you need to verify the availability of the ChatGPT API key, you can use the program [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py) for testing. If you are using the official API in China, you need to have a local proxy.
2. If the Front Matter in Markdown cannot be recognized correctly, you can use the program [detect_front_matter.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/detect_front_matter.py) for testing.
3. When encountering issues with GitHub Actions, please check the path references first (e.g., `dir_to_translate`, `dir_translated_en`, `dir_translated_es`, `dir_translated_ar`, `processed_list`).

## Pending Issues

Translate into English:



1. In some special cases, there may be inaccuracies in translation or some fields may not be translated. It is recommended to manually verify the translation before publishing the article.
2. (Resolved) ~~If the Markdown contains Front Matter, the original content of the Front Matter will be preserved. The translation function for the parameters in the Front Matter is under development.~~

## Contribution

You are welcome to contribute to this project! If you would like to contribute code, report issues, or make suggestions, please refer to the [Contribution Guide](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md).

## Copyright and License

This project is licensed under the [MIT License](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE).

## Issues and Support

If you encounter any issues while using Auto-i18n or need technical support, please feel free to [submit an issue](https://github.com/linyuxuanlin/Auto-i18n/issues).

My blog uses Auto-i18n to implement multilingual support. You can check out the demo effect at [Power's Wiki](https://wiki-power.com).

[![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202310222223670.png)](https://wiki-power.com)

## Acknowledgements

- Thanks to [chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free) for providing the free ChatGPT API key.
- Thanks to [linweiyuan/go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) for providing the method to convert the web version of ChatGPT to an API.

[![Star History Chart](https://api.star-history.com/svg?repos=linyuxuanlin/Auto-i18n&type=Date)](https://star-history.com/#linyuxuanlin/Auto-i18n&Date)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.