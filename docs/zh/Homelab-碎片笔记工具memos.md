---
id: Homelab-碎片笔记工具memos
title: Homelab - 碎片笔记工具 memos
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111548420.png)

**memos** 是一个开源的自托管 memos 工具。支持 Markdown 语法、公开分享、iframe 嵌入、标签管理、日历视图、简单的数据迁移与备份功能。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3.0"
services:
  memos:
    container_name: ${STACK_NAME}_app
    image: neosmemo/memos:${APP_VERSION}
    ports:
      - ${APP_PORT}:5230
    volumes:
      - ${STACK_DIR}:/var/opt/memos
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `memos`）。

```dotenv title=".env"
STACK_NAME=memos
STACK_DIR=xxx # 自定义项目储存路径，例如 ./memos

# memos
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

移动端 iOS/Android App：[**Moe Memos**](https://memos.moe/)。还有更多第三方客户端（如微信小程序、浏览器扩展、Telegram Bot 等）请参考文档 [**contribution·memos**](https://github.com/usememos/memos#contribution)。

用户数据的导入导出，可使用 VS Code 插件 [**SQLite**](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)，下载并打开 `${DIR}` 下的 `memos_prod.db` 即可进行增删改查、导入导出备份等操作。注意，只有在 docker 容器关闭 / 重启的时候才会更新 `memos_prod.db` 文件。

## 参考与致谢

- [官网](https://usememos.com/)
- [文档](https://usememos.com/docs/install#docker-compose)
- [GitHub repo](https://github.com/usememos/memos)
- [Docker Hub](https://hub.docker.com/r/neosmemo/memos)
- [Demo site](https://demo.usememos.com/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
