---
id: Homelab-支持公有云的图床系统Cloudreve
title: Homelab - 支持公有云的图床系统 Cloudreve
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195423.png)

**Cloudreve** 是一个支持多家云存储驱动的公有云文件系统，支持用本地、从机、七牛、阿里云 OSS、腾讯云 COS、又拍云、OneDrive、S3 兼容协议作为储存端，可对接 Aria2 离线下载，多用户，拖拽上传 / 管理，在线预览 / 编辑，WebDAV 等。典型的使用场景是个人图床或网盘文件管理。

## 部署（Docker Compose）

我们首先需要创建目录结构。切换到存放 Cloudreve 的目录下（例如 `/DATA/AppData/cloudreve`）并执行：

```shell
mkdir -vp cloudreve/{uploads,avatar,data} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db \
&& mkdir -p aria2/config \
&& mkdir -p cloudreve/data/aria2 \
&& chmod -R 777 cloudreve/data/aria2 \
&& mkdir data
```

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3.8"
services:
  cloudreve:
    container_name: ${STACK_NAME}_app
    image: cloudreve/cloudreve:${APP_VERSION}
    ports:
      - "${APP_PORT}:5212"
    volumes:
      - temp_data:/data
      - ${STACK_DIR}/cloudreve/uploads:/cloudreve/uploads
      - ${STACK_DIR}/cloudreve/conf.ini:/cloudreve/conf.ini
      - ${STACK_DIR}/cloudreve/cloudreve.db:/cloudreve/cloudreve.db
      - ${STACK_DIR}/cloudreve/avatar:/cloudreve/avatar
    restart: unless-stopped
    depends_on:
      - aria2
  aria2:
    container_name: ${STACK_NAME}_aria2
    image: p3terx/aria2-pro:${ARIA2_VERSION}
    volumes:
      - ${STACK_DIR}/aria2/config:/config
      - ${STACK_DIR}/data:/var/lib/docker/volumes/cloudreve_temp_data/_data
    environment:
      - RPC_SECRET=${ARIA2_RPC_SECRET}
      - RPC_PORT=${ARIA2_RPC_PORT}
    restart: unless-stopped
volumes:
  temp_data:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/temp_data
      o: bind
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `cloudreve`）。

```dotenv title=".env"
STACK_NAME=cloudreve
STACK_DIR=xxx # 自定义项目储存路径，例如 ./cloudreve

# cloudreve
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可

# aria2
ARIA2_VERSION=latest
ARIA2_RPC_SECRET=xxx # ARIA2 密码
ARIA2_RPC_PORT=6800
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器

## 配置说明

首次启动时，会自动创建初始的管理员账号，可以在 log 中找到。如果错过了，请删除目录下的 cloudreve.db，重新启动主程序以初始化新的管理员账户。

我采用的图像命名规则：`{year}{month}{day}{hour}{minute}{second}{ext}`。

## 参考与致谢

- [官网](https://docs.cloudreve.org/)
- [文档](https://docs.cloudreve.org/getting-started/install#docker-compose)
- [论坛](https://forum.cloudreve.org/)
- [GitHub repo](https://github.com/cloudreve/Cloudreve)
- [Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)
- [Demo site](https://demo.cloudreve.org/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
