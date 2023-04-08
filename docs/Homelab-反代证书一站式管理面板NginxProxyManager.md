---
id: Homelab-反代证书一站式管理面板NginxProxyManager
title: Homelab - 反代证书一站式管理面板 Nginx Proxy Manager 🚧
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
      - "[local-port]:80"
      - "[local-port]:81"
      - "[local-port]:443"
    volumes:
      - [local-dir]/nginx-proxy-manager/data:/data
      - [local-dir]/nginx-proxy-manager/letsencrypt:/etc/letsencrypt
```

---

🚧

**默认面板访问地址**：<http://127.0.0.1:81>

**初始账户密码**：

- Email: `admin@example.com`
- Password: `changeme`

**获取 docker 本地地址**：

```shell
ip addr show docker0
```

注：对于自部署的服务，请通过反代走域名访问（80/443 端口），并在服务器管理控制台防火墙中关闭其他端口，以提高安全性。

## 参考与致谢

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

---
