---
id: Homelab-在线代码编辑器code-server
title: Homelab - 在线代码编辑器 code-server
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304132214418.png)

**code-server** 是一个能在浏览器中运行的 VS Code。相比于桌面端的优势是，你可以用任意设备在线码字，包括手机与平板这一类无法直接安装 VS Code 的设备。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（例如 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）；将登陆密码 `${PASSWORD}` 也替换为你自己的：

```yml title="docker-compose.yml"
version: "2.1"
services:
  code-server:
    image: ghcr.io/linuxserver/code-server
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Shanghai
      - PASSWORD=${PASSWORD} #optional
    # - SUDO_PASSWORD=  #optional
    # - SUDO_PASSWORD_HASH=  #optional
    # - PROXY_DOMAIN= #optional
    volumes:
      - ${DIR}/code-server/config:/config
    ports:
      - ${PORT}:8443
    restart: unless-stopped
```

## 配置说明

### 配置 git

安装完成后，如果需要使用 Git，对用户名和邮箱初始化配置，请参考文章 [**Git 学习笔记**](https://wiki-power.com/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE)。

### 读写权限问题

如果在操作文件时遇到 `Error: EACCES: permission denied` 错误，可以用 `Ctrl` + `\`` 打开终端，输入以下命令赋予当前用户所有权：

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
