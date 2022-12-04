---
id: 如何用Markdown写公众号文章
title: 如何用 Markdown 写公众号文章
---


在 Markdown 介绍文章 [**使用 Markdown 进行高效写作**](https://wiki-power.com/%E4%BD%BF%E7%94%A8Markdown%E8%BF%9B%E8%A1%8C%E9%AB%98%E6%95%88%E5%86%99%E4%BD%9C) 中，我们得以见识 Markdown 用于排版的便捷性。假如我想用它来写微信公众号，该怎么操作呢？

我们都知道，微信公众号用的是富文本编辑器，是无法直接解析 Markdown 语法的。但我们可以自己先将 Markdown 解析为富文本，再粘贴进公众号文章的编辑界面。

## MD2WeChat

[**MD2WeChat**](https://md2wechat.wiki-power.com/) 是我根据开源项目 [lyricat/wechat-format](https://github.com/lyricat/wechat-format) 定制的一个网页工具，可以很方便地将 Markdown 语法解析为富文本：

[![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210216125752.png)](https://md2wechat.wiki-power.com/)

将 Markdown 语法的文章粘贴到左栏，并在右栏点击一键复制，粘贴进公众号的编辑器即可。

注：因公众号文章中不允许有外部链接，所以外链会被自动加脚注，并在底部附上。


## 参考与致谢 

- [lyricat/wechat-format](https://github.com/lyricat/wechat-format)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

