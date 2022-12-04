---
id: Docker方式运行code-server
title: Docker 方式运行 code-server
---

## 准备

本方法需要使用 Docker. 其安装部署请参照：[**Docker 简易指南**](https://wiki-power.com/Docker%E7%AE%80%E6%98%93%E6%8C%87%E5%8D%97)

## 使用 Docker Compose 方式（推荐）

如果不熟悉 Docker Compose, 请详细阅读 [**Docker Compose - 更优雅的打开方式**](https://wiki-power.com/DockerCompose-%E6%9B%B4%E4%BC%98%E9%9B%85%E7%9A%84%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F) 这篇文章。

```yaml
---
version: "2.1"
services:
  code-server:
    image: ghcr.io/linuxserver/code-server
    container_name: code-server
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - PASSWORD=password #optional
      - SUDO_PASSWORD=password #optional
      - SUDO_PASSWORD_HASH= #optional
      - PROXY_DOMAIN=code-server.my.domain #optional
    volumes:
      - /path/to/appdata/config:/config
    ports:
      - 8443:8443
    restart: unless-stopped
```


## 使用 Docker Cli 方式

## 部署

一行命令部署：

```shell
docker run -d --name=[容器名] -e PASSWORD=[密码] -e SUDO_PASSWORD=[root密码] -p [外部端口]:8443 --restart unless-stopped ghcr.io/linuxserver/code-server
```

参数详情：
- `--name`：给容器取个名
- `-e PASSWORD`：访问密码
- `-e SUDO_PASSWORD`：root 密码
- `-p`：端口设置，如果外部端口设置为 80, 可通过服务器 IP 访问

例子：

```shell
docker run -d --name=VSConline -e PASSWORD=123 -e SUDO_PASSWORD=123 -p 8443:8443 --restart unless-stopped ghcr.io/linuxserver/code-server
```

## Git 配置

请参照 [**Git 学习笔记**](https://wiki-power.com/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE) 中对 Git 的用户名和邮箱配置。


## 参考与致谢

- [linuxserver/code-server](https://hub.docker.com/r/linuxserver/code-server)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

