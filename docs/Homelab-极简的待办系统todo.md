---
id: Homelab-极简的待办系统todo
title: Homelab - 极简的待办系统 todo 🚧
---

![1](1)

**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：

```yml title="docker-compose.yml"
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

## 参考与致谢

- [文档 / Docker Hub](https://hub.docker.com/r/prologic/todo)
- [Demo site](https://todo.mills.io/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
