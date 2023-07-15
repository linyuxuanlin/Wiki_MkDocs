---
id: Homelab-自托管密码管理器Vaultwarden
title: Homelab - 自托管密码管理器 Vaultwarden
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195414.jpg)

**Vaultwarden** 是一个第三方自托管的 Bitwarden 服务器，通过一个主密码保护并管理各个网站的密码，可生成随机的密码供不同网站使用。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  vaultwarden:
    container_name: ${STACK_NAME}_app
    image: vaultwarden/server:${APP_VERSION}
    ports:
      - ${APP_PORT}:80
    volumes:
      - ${STACK_DIR}:/data/
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `vaultwarden`）。

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # 自定义项目储存路径，例如 ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

Vaultwarden 默认需要使用 https 登录，推荐通过反向代理使用（反向代理服务器的搭建可参考文章 [**Homelab - 反代证书管理面板 Nginx Proxy Manager**](https://wiki-power.com/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/)。

使用浏览器扩展、桌面与移动端 App 时，需要在登录页面点击设置，并配置服务器的 URL，才能正常使用自托管的服务。

另外，旧版本（低于 1.27.0）的 Vaultwarden 与 Bitwarden 的浏览器拓展不兼容，会导致无法登录。详见 issue：[**Client fails to connect or login**](https://github.com/dani-garcia/vaultwarden/issues/3082)。

因为是自托管的服务，所以需要自己留意数据安全。记得定期备份密码数据库。

## 参考与致谢

- [官网](https://github.com/dani-garcia/vaultwarden/wiki)
- [文档](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [GitHub repo](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
