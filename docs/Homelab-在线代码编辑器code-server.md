---
id: Homelab-在线代码编辑器code-server
title: Homelab - 在线代码编辑器 code-server
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304132214418.png)

**code-server** 是一个能在浏览器中运行的 VS Code。相比于桌面端的优势是，你可以用任意设备在线码字，包括手机与平板这一类无法直接安装 VS Code 的设备。

## 部署（Docker Compose）
首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "2.1"
services:
  code-server:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/linuxserver/code-server:${APP_VERSION}
    ports:
      - ${APP_PORT}:8443
    volumes:
      - ${STACK_DIR}/config:/config
      - ${DATA_DIR_LOCAL}:/DATA
    environment:
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} #optional
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} #optional
      #- SUDO_PASSWORD_HASH= #optional
      #- PROXY_DOMAIN=code.wiki-power.com #optional
    restart: unless-stopped
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `code-server`）。

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # 自定义项目储存路径，例如 ./code-server
DATA_DIR_LOCAL=xxx # 自定义挂载本地目录，例如 /DATA 

# code-server
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
APP_PASSWORD=xxx # 登录密码
APP_SUDO_PASSWORD=xxx # 超级用户权限密码

```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

### 配置 git

安装完成后，如果需要使用 Git，对用户名和邮箱初始化配置，请参考文章 [**Git 学习笔记**](https://wiki-power.com/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE)。

### 读写权限问题

如果在操作文件时遇到 `Error: EACCES: permission denied` 错误，可以打开终端，输入以下命令赋予当前用户所有权：

```shell
sudo chown -R 用户名 文件夹路径
```

例如，以下是给 `abc` 用户赋予当前目录的所有权的操作：

```shell
sudo chown -R abc .
```

### 设置 root 账户密码

如果需要用到 root 账户，可以使用以下命令初始化其密码：

```shell
sudo passwd root
```

## 参考与致谢

- [官网](https://coder.com/docs/code-server/latest)
- [文档 / GitHub repo](https://github.com/linuxserver/docker-code-server)
- [Docker Hub](https://hub.docker.com/r/linuxserver/code-server)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
