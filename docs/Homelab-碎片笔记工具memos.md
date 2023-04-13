---
id: Homelab-碎片笔记工具memos
title: Homelab - 碎片笔记工具 memos
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111548420.png)

**memos** 是一个开源的自托管 memos 工具。支持 Markdown 语法、公开分享、iframe 嵌入、标签管理、日历视图、简单的数据迁移与备份功能。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

```yml title="docker-compose.yml"
version: "3.0"
services:
  memos:
    image: neosmemo/memos:latest
    volumes:
      - ${DIR}/memos:/var/opt/memos
    ports:
      - ${PORT}:5230
```

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
