---
id: 如何用Markdown写学术论文
title: 如何用 Markdown 写学术论文
---

## 环境安装

我们需要安装以下几样东西：

- [**Python 环境**](https://www.python.org/downloads/)
- [**Pandoc 环境**](https://github.com/jgm/pandoc/releases/)
  - pandoc-fignos 插件：`pip install pandoc-fignos`

## 语法

```shell
pandoc demo-math.md -o demo-math.docx
```

### 数学公式

可直接编辑 LaTeX 语法，具体参考 [LaTeX 希腊字母对照表](https://wiki-power.com/LaTeX%E5%B8%8C%E8%85%8A%E5%AD%97%E6%AF%8D%E5%AF%B9%E7%85%A7%E8%A1%A8)

### 脚注

```
学术文稿最小化示例[^1]

[^1]: 通讯作者: XXX，ORCID：XXXX-XXXX-XXXX-XXXX.
*本文受XXXX基金资助。
```

### 文献引用

将复制的 BibTeX 信息粘贴进 `myref.bib` 文件，在文章中使用 `[@article]` 引用。

```shell
pandoc --filter pandoc-citeproc --bibliography=myref.bib --csl=chinese-gb7714-2005-numeric.csl demo-citation.md -o demo-citation.docx
```

### 图片引用

在文章中插入 font-matter：

```
---
fignos-cleveref: On
fignos-plus-name: 图
---
```

在文章中的语法：

```markdown
![标题](链接){#fig:图注}
```

```shell
pandoc --filter pandoc-fignos --filter pandoc-citeproc --bibliography=myref.bib --csl=chinese-gb7714-2005-numeric.csl demo-figref.md -o demo-figref.docx
```

【更新中】

## 参考与致谢

- [如何用 Markdown 写论文？](https://www.jianshu.com/p/b0ac7ae98100)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

