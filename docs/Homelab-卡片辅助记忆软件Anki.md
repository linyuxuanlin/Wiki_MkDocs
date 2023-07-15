---
id: Homelab-卡片辅助记忆软件Anki
title: Homelab - 卡片辅助记忆软件 Anki
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202306191745527.png)

**Anki** 一款开源的记忆卡片应用程序，可帮助用户轻松高效地记忆各种知识点，一般常用于背单词。它的特点在于采用记忆遗忘曲线，根据学习情况生成适当的复习计划，帮助用户充分利用大脑的记忆规律，达到最佳的记忆效果。Anki 具有极高的定制性，你可以制作自己的学习卡片，包括文字、图片甚至音频和视频。Anki 也支持多平台使用。

由于同步服务器在国外，有时候可能会无法正常同步，我们可以使用 **anki-sync-server** 自己搭建同步服务。以下教程使用的是 `johngong/anki-sync-server` 镜像，可正常使用，其他版本未经测试。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  anki-sync-server:
    container_name: ${STACK_NAME}_app
    image: johngong/anki-sync-server:${APP_VERSION}
    ports:
      - "${APP_PORT}:27701"
    volumes:
      - ${STACK_DIR}:/config
    environment:
      - ANKI_SYNC_SERVER_USER=${APP_USERNAME}
      - ANKI_SYNC_SERVER_PASSWORD=${APP_PASSWORD}
      - UID=1000
      - GID=1000
    restart: unless-stopped
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `anki-sync-server`）。

```dotenv title=".env"
STACK_NAME=anki-sync-server
STACK_DIR=/DATA/AppData/anki-sync-server # 自定义项目储存路径，例如 ./anki-sync-server

# anki-sync-server
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
APP_USERNAME=xxx@xx.com  # 自定义账户名，需要邮箱格式
APP_PASSWORD=xxxxxx # 自定义密码
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

### Windows

Windows 端我使用的是 [**Anki 2.1.28**](https://github.com/ankitects/anki/releases/download/2.1.28/anki-2.1.28-windows.exe)（测试过 2.1.65 无法同步）。

安装完成后，依次点击顶栏的 `工具` - `附加组件`，然后点击 `获取插件`，输入插件代码 `358444159` 后点击 `OK`，随后点击 `设置`，将地址改为你部署 `anki-sync-server` 的服务器的地址与端口，最后重启软件。

重启后，在主界面点击同步，输入 docker 部署时填写的邮箱和密码，即可进行同步。

如果仍然无法同步，请参考 [**Setting up Anki**](https://github.com/ankicommunity/anki-sync-server/blob/develop/README.md#setting-up-anki)。

### Android

Android 端使用的是 AnkiDroid，不用安装插件即可自定义服务器地址，但是需要使用 https 登录。推荐通过反向代理使用（反向代理服务器的搭建可参考文章 [**Homelab - 反代证书管理面板 Nginx Proxy Manager**](https://wiki-power.com/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/)。

可使用 https 登录后，在主界面选择 `Advanced` - `Custom sync server` 可配置自定义服务器。注意，在 `Media sync url` 一栏中，需要在原地址后加上 `/msync`，才可正常进行同步。

## 参考与致谢

- [官网](https://apps.ankiweb.net/)
- [文档](https://www.navidrome.org/docs/installation/docker/)
- [GitHub repo](https://github.com/ankicommunity/anki-sync-server)
- [Docker Hub](https://hub.docker.com/r/johngong/anki-sync-server)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
