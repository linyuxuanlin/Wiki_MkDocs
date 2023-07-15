---
id: Homelab-多功能PDF工具箱Stirling-PDF
title: Homelab - 多功能 PDF 工具箱 Stirling-PDF
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410172939.png)

**Stirling-PDF** 是一个自托管 PDF 工具包，功能包括 PDF 的分割、合并、旋转、提取页面、图像互转、重新排序、添加 / 提取图像、添加删除密码、设置权限、添加水印、将其他文件转换为 PDF、OCR 文字识别、元数据编辑，支持暗黑模式。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3.3"
services:
  s-pdf:
    container_name: ${STACK_NAME}_app
    image: frooodle/s-pdf:${APP_VERSION}
    ports:
      - ${APP_PORT}:8080
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `s-pdf`）。

```dotenv title=".env"
STACK_NAME=s-pdf
STACK_DIR=xxx # 自定义项目储存路径，例如 ./s-pdf

# s-pdf
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。


## 参考与致谢

- [文档 / GitHub repo](https://github.com/Frooodle/Stirling-PDF)
- [Docker Hub](https://hub.docker.com/r/frooodle/s-pdf)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
