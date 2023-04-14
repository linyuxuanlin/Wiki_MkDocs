---
id: Homelab-支持多存储的文件列表程序Alist
title: Homelab - 支持多存储的文件列表程序 Alist
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304141808001.png)

**Alist** 是一个文件列表程序，支持多种储存方式如本地、阿里云盘、OneDrive、GoogleDrive、百度网盘、夸克网盘、蓝奏云、S3、FTP / SFTP 等等，带在线视频播放器与各类文件预览（兼容 Office、PDF、Markdown 等），还有离线下载功能。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

```yml title="docker-compose.yml"
version: "3.3"
services:
  alist:
    restart: always
    volumes:
      - ${DIR}/alist:/opt/alist/data
    ports:
      - ${PORT}:5244
    environment:
      - PUID=0
      - PGID=0
      - UMASK=022
    image: xhofe/alist:latest
```

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
