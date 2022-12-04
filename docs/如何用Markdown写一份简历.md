---
id: 如何用Markdown写一份简历
title: 如何用 Markdown 写一份简历
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210318220041.png)

用 Markdown 写一份可在线预览，也可导出 PDF 的简历。

**预览网址**：[**cv-template.wiki-power.com**](https://cv-template.wiki-power.com/)

**如何导出 PDF**：在网页上使用快捷键 `Ctrl` + `P` 唤出打印界面，目标打印机选择 `Microsoft Print to PDF`，即可导出 PDF 版本的简历。

## 使用方法

打开项目 [**linyuxuanlin/Markdown-CV-Site**](https://github.com/linyuxuanlin/Markdown-CV-Site)，点击绿色的按钮 `Use this template` 初始化为自己的仓库。

打开 [**Vercel**](https://vercel.com/)，点击 `New Project`，导入刚刚初始化的 GitHub 仓库，设置下列参数：

- `FRAMEWORK PRESET`：选择 `Other`
- `BUILD COMMAND`：填入 `npm run build`
- `OUTPUT DIRECTORY`：填入 `dist`


点击下一步，等待几十秒，网站就生成了。

如需修改简历的内容，请编辑根目录下的 `_config.yml` 和 `markdown/resume-template.md` 文件，推送到 GitHub 仓库后，可自动触发 Vercel 构建。

## 参考与致谢

本项目基于 [**BigLiao/markCV**](https://github.com/BigLiao/markCV)，做了一些 UI 的简化和改善。简历模板使用的是 [**冷熊简历**](https://cv.ftqq.com/) 的默认内容。

- [聊聊简历怎么写？](https://mp.weixin.qq.com/s/P64bm-SBYXyQymfHAR1rqA)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。


