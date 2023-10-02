# How to Write a Resume Using Markdown

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210318220041.png)

Write a resume using Markdown that can be previewed online and exported as a PDF.

**Preview URL**: [**cv-template.wiki-power.com**](https://cv-template.wiki-power.com/)

**How to Export as PDF**: Use the shortcut `Ctrl` + `P` to bring up the print interface on the webpage, select `Microsoft Print to PDF` as the target printer, and export the PDF version of the resume.

## Usage

Open the project [**linyuxuanlin/Markdown-CV-Site**](https://github.com/linyuxuanlin/Markdown-CV-Site), click the green button `Use this template` to initialize it as your own repository.

Open [**Vercel**](https://vercel.com/), click `New Project`, import the GitHub repository that was just initialized, and set the following parameters:

- `FRAMEWORK PRESET`: Select `Other`
- `BUILD COMMAND`: Enter `npm run build`
- `OUTPUT DIRECTORY`: Enter `dist`

Click next and wait a few seconds for the website to be generated.

To modify the content of the resume, edit the `_config.yml` and `markdown/resume-template.md` files in the root directory. After pushing to the GitHub repository, Vercel will automatically trigger a build.

## References and Acknowledgments

This project is based on [**BigLiao/markCV**](https://github.com/BigLiao/markCV) and has made some UI simplifications and improvements. The resume template uses the default content of [**Cold Bear Resume**](https://cv.ftqq.com/).

- [How to Write a Resume?](https://mp.weixin.qq.com/s/P64bm-SBYXyQymfHAR1rqA)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.