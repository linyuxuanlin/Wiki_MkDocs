---
id: Homelab-极简的待办系统todo
title: Homelab - 极简的待办系统 todo
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111520508.png)

**todo** 是一个极简的待办系统工具。

## 部署（Docker Compose）

首先创建 `compose.yaml` ，并将以下的 `${DIR}` 替换为本地的目录（例如 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

```yaml title="compose.yaml"
version: "3"

services:
  todo:
    image: prologic/todo
    restart: always
    ports:
      - ${PORT}:8000
    volumes:
      - ${DIR}/todo/todo_db:/usr/local/go/src/todo/todo.db
    environment:
      - THEME=ayu
```

## 配置说明

配置主题的变量 `THEME` 可根据需要替换为以下值：`ayu, dracula, gruvbox-dark, gruvbox-light, lucario, monokai, nord, solarized-dark, solarized-light, tomorrow, tomorrow-night, zenburn`。

如果不满足需求，也可以自定义主题，请参考官方文档 `Custom Color Themes` 部分的内容。

## 参考与致谢

- [文档 / Docker Hub](https://hub.docker.com/r/prologic/todo)
- [Demo site](https://todo.mills.io/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
