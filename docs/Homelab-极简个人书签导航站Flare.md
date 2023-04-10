---
id: Homelab-极简个人书签导航站Flare
title: Homelab-极简个人书签导航站Flare
---

## 参考与致谢

- []()

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230408182138.png)

**Nginx Proxy Manager** 是一个 Nginx 图形化面板，能让用户在 Web 界面上轻松配置反向代理、申请网站 SSL 证书，而无需了解过多 Nginx / Letsencrypt 的底层原理。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `[custom-dir]` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`[custom-port]` 替换为自定义的端口号（比如 `1234`）；自定义 `[custom-username]` 与 `[custom-password]`：

```yml title="docker-compose.yml"
version: "3.6"
services:
  flare:
    image: soulteary/flare:latest
    restart: always
    # 更多启动参数文档 https://github.com/soulteary/docker-flare/blob/main/docs/advanced-startup.md
    command: flare --nologin=0 # 开启用户登录模式，需要先设置 `nologin` 启动参数为 `0`
    environment:
      - FLARE_USER=[custom-username] # 如开启用户登录模式，且未设置 FLARE_USER，则默认用户为 `flare`
      - FLARE_PASS=[custom-password] # 如开启用户登录模式，且未设置 FLARE_USER，则会默认生成密码并展示在应用启动日志中
    ports:
      - [custom-port]:5005
    volumes:
      - [custom-dir]/flare:/app
```

## 配置说明

获取 Docker 的 IP 地址：

```shell
ip addr show docker0
```

注：自托管服务尽量通过反代，绑定二级域名访问（80/443 端口），并在公网服务器管理控制台防火墙中关闭其他端口，这样可以提高安全性。

## 参考与致谢

- [官网](https://nginxproxymanager.com)
- [文档](https://nginxproxymanager.com/guide)
- [GitHub repo](https://github.com/NginxProxyManager/nginx-proxy-manager)
- [Docker Hub](https://hub.docker.com/r/jlesage/nginx-proxy-manager)
