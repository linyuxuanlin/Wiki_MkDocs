---
id: Homelab-反代证书管理面板NginxProxyManager
title: Homelab - 反代证书管理面板 Nginx Proxy Manager
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230408182138.png)

**Nginx Proxy Manager** 是一个 Nginx 图形化面板，能让用户在 Web 界面上轻松配置反向代理、申请网站 SSL 证书，而无需了解过多 Nginx / Letsencrypt 的底层原理。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  nginx-proxy-manager:
    container_name: ${STACK_NAME}_app
    image: "jc21/nginx-proxy-manager:${APP_VERSION}"
    ports:
      - "${APP_PORT}:81" # 面板地址
      - "80:80"
      - "443:443"
    volumes:
      - ${STACK_DIR}/data:/data
      - ${STACK_DIR}/letsencrypt:/etc/letsencrypt
    restart: unless-stopped
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `nginx-proxy-manager`）。

```dotenv title=".env"
STACK_NAME=nginx-proxy-manager
STACK_DIR=xxx # 自定义项目储存路径，例如 ./nginx-proxy-manager

# nginx-proxy-manager
APP_VERSION=latest
APP_PORT=81 # 默认为 81，更改请参考文档
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

初始账户密码：

- Email: `admin@example.com`
- Password: `changeme`

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

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
