---
id: Homelab-多功能PDF工具箱Stirling-PDF
title: Homelab - 多功能 PDF 工具箱 Stirling-PDF
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410172939.png)

**Stirling-PDF** 是一个自托管 PDF 工具包，功能包括 PDF 的分割、合并、旋转、提取页面、图像互转、重新排序、添加 / 提取图像、添加删除密码、设置权限、添加水印、将其他文件转换为 PDF、OCR 文字识别、元数据编辑，支持暗黑模式。

## 部署（docker-compose）

```yml title="docker-compose.yml"
version: "3.3"
services:
  s-pdf:
    ports:
      - "${PORT}:8080"
    image: frooodle/s-pdf
```

## 参考与致谢

- [文档 / GitHub repo](https://github.com/Frooodle/Stirling-PDF)
- [Docker Hub](https://hub.docker.com/r/frooodle/s-pdf)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
