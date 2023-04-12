---
id: Homelab-支持公有云的图床系统Cloudreve
title: Homelab - 支持公有云的图床系统 Cloudreve
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195423.png)

**Cloudreve** 是一个支持多家云存储驱动的公有云文件系统，支持用本地、从机、七牛、阿里云 OSS、腾讯云 COS、又拍云、OneDrive、S3 兼容协议作为储存端，可对接 Aria2 离线下载，多用户，拖拽上传 / 管理，在线预览 / 编辑，WebDAV 等。典型的使用场景是个人图床或网盘文件管理。

## 部署（docker-compose）

首先创建目录结构，切换到存放 Cloudreve 的目录下（我的是 `/DATA/AppData/cloudreve`）并执行：

```shell
mkdir -vp cloudreve/{uploads,avatar,data} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db \
&& mkdir -p aria2/config \
&& mkdir -p cloudreve/data/aria2 \
&& chmod -R 777 cloudreve/data/aria2 \
&& mkdir data
```

随后创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）；最后自定义 `${PASSWORD-ARIA2}`：

```yml title="docker-compose.yml"
version: "3.8"
services:
  cloudreve:
    image: cloudreve/cloudreve:latest
    restart: unless-stopped
    ports:
      - "${PORT}:5212"
    volumes:
      - temp_data:/data
      - ${DIR}/cloudreve/cloudreve/uploads:/cloudreve/uploads
      - ${DIR}/cloudreve/cloudreve/conf.ini:/cloudreve/conf.ini
      - ${DIR}/cloudreve/cloudreve/cloudreve.db:/cloudreve/cloudreve.db
      - ${DIR}/cloudreve/cloudreve/avatar:/cloudreve/avatar
    depends_on:
      - aria2
  aria2:
    image: p3terx/aria2-pro
    restart: unless-stopped
    environment:
      - RPC_SECRET=${PASSWORD-ARIA2}
      - RPC_PORT=6800
    volumes:
      - ${DIR}/cloudreve/aria2/config:/config
      - ${DIR}/cloudreve/data:/var/lib/docker/volumes/cloudreve_temp_data/_data
volumes:
  temp_data:
    driver: local
    driver_opts:
      type: none
      device: ${DIR}/cloudreve/temp_data
      o: bind
```

## 配置说明

首次启动时，会自动创建初始的管理员账号，可以在 log 中找到。如果错过了，请删除目录下的 cloudreve.db，重新启动主程序以初始化新的管理员账户。

我采用的图像命名规则：`{year}{month}{day}{hour}{minute}{second}{ext}`。

## 参考与致谢

- [官网](https://docs.cloudreve.org/)
- [文档](https://docs.cloudreve.org/getting-started/install#docker-compose)
- [GitHub repo](https://github.com/cloudreve/Cloudreve)
- [Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)
- [Demo site](https://demo.cloudreve.org/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
