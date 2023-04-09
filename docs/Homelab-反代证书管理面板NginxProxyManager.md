---
id: Homelab-反代证书管理面板NginxProxyManager
title: Homelab - 反代证书管理面板 Nginx Proxy Manager
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230408182138.png)

**Nginx Proxy Manager** 是一个 Nginx 图形化面板，能让用户在 Web 界面上轻松配置反向代理、申请网站 SSL 证书，而无需了解过多 Nginx / Letsencrypt 的底层原理。

**功能**：Nginx 该有的功能都有、自动申请续签 SSL 证书。  
**官网**：<https://nginxproxymanager.com>  
**文档**：<https://nginxproxymanager.com/guide>

## 部署（docker-compose）

```yml title="docker-compose.yml"
version: "3"
services:
  nginx-proxy-manager:
    image: "jc21/nginx-proxy-manager:latest"
    restart: unless-stopped
    ports:
      - "[custom-port]:80"
      - "[custom-port]:81" # 默认面板地址
      - "[custom-port]:443"
    volumes:
      - [custom-dir]/nginx-proxy-manager/data:/data
      - [custom-dir]/nginx-proxy-manager/letsencrypt:/etc/letsencrypt
```

**初始账户密码**：

- Email: `admin@example.com`
- Password: `changeme`

## 配置说明

**获取 Docker 的 IP 地址**：

```shell
ip addr show docker0
```

注：自托管服务尽量通过反代，绑定二级域名访问（80/443 端口），并在公网服务器管理控制台防火墙中关闭其他端口，这样可以提高安全性。

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
