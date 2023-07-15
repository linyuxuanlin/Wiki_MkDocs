---
id: Homelab-支持多存储的文件列表程序Alist
title: Homelab - 支持多存储的文件列表程序 Alist
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304141808001.png)

**Alist** 是一个文件列表程序，支持多种储存方式如本地、阿里云盘、OneDrive、GoogleDrive、百度网盘、夸克网盘、蓝奏云、S3、FTP / SFTP 等等，带在线视频播放器与各类文件预览（兼容 Office、PDF、Markdown 等），还有离线下载功能。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3.3"
services:
  alist:
    container_name: ${STACK_NAME}_app
    image: "xhofe/alist:${APP_VERSION}"
    volumes:
      - ${STACK_DIR}:/opt/alist/data
    ports:
      - ${APP_PORT}:5244
    environment:
      - UMASK=022
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `alist`）。

```dotenv title=".env"
STACK_NAME=alist
STACK_DIR=xxx # 自定义项目储存路径，例如 ./alist

# alist
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

接入各类网盘的方法，官方的文档写得非常详细，一步步按着配置就可以了。

## 参考与致谢

- [官网](https://alist.nn.ci/)
- [文档](https://alist.nn.ci/guide/install/docker.html#release-version)
- [GitHub repo](https://github.com/alist-org/alist)
- [Docker Hub](https://hub.docker.com/r/xhofe/alist)
- [Demo site](https://al.nn.ci/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
