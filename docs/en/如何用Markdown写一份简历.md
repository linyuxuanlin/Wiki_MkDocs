# How to Write a Resume Using Markdown

![](https://media.wiki-power.com/img/20210318220041.png)

Write a resume using Markdown that can be previewed online and exported as a PDF.

**Preview URL**: [**cv-template.wiki-power.com**](https://cv-template.wiki-power.com/)

**How to Export as PDF**: Use the shortcut `Ctrl` + `P` on the webpage to bring up the print interface, select `Microsoft Print to PDF` as the target printer, and export the resume as a PDF.

## Instructions

Open the project [**linyuxuanlin/Markdown-CV-Site**](https://github.com/linyuxuanlin/Markdown-CV-Site), click on the green button `Use this template` to initialize it as your own repository.

Open [**Vercel**](https://vercel.com/), click `New Project`, import the GitHub repository that was just initialized, and set the following parameters:

- `FRAMEWORK PRESET`: Select `Other`
- `BUILD COMMAND`: Enter `npm run build`
- `OUTPUT DIRECTORY`: Enter `dist`

Click next and wait for a few seconds, the website will be generated.

To modify the content of the resume, please edit the `_config.yml` and `markdown/resume-template.md` files in the root directory. After pushing them to the GitHub repository, Vercel will automatically trigger a build.

## References and Acknowledgements

This project is based on [**BigLiao/markCV**](https://github.com/BigLiao/markCV) with some UI simplifications and improvements. The resume template uses the default content from [**Cold Bear Resume**](https://cv.ftqq.com/).

- [How to Write a Resume?](https://mp.weixin.qq.com/s/P64bm-SBYXyQymfHAR1rqA)
- > Original: <https://wiki-power.com/>
- > This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
