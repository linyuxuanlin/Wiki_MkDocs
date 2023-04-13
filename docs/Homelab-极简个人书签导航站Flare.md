---
id: Homelab-极简个人书签导航站Flare
title: Homelab - 极简个人书签导航站 Flare
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410170939.png)

**Flare** 是一个轻量、快速、美观的个人导航页面，无任何数据库依赖，应用数据完全开放透明，支持在线编辑，内置 Material Design Icons 6k+ 图标。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）；自定义 `${USERNAME}` 与 `${PASSWORD}`：

```yml title="docker-compose.yml"
version: "3.6"
services:
  flare:
    image: soulteary/flare:latest
    restart: always
    # 更多启动参数文档 https://github.com/soulteary/docker-flare/blob/main/docs/advanced-startup.md
    command: flare --nologin=0 # 开启用户登录模式，需要先设置 `nologin` 启动参数为 `0`
    environment:
      - FLARE_USER=${USERNAME} # 如开启用户登录模式，且未设置 FLARE_USER，则默认用户为 `flare`
      - FLARE_PASS=${PASSWORD} # 如开启用户登录模式，且未设置 FLARE_USER，则会默认生成密码并展示在应用启动日志中
    ports:
      - ${PORT}:5005
    volumes:
      - ${DIR}/flare:/app
```

## 配置说明

可在修改 `${DIR}/flare` 内的 `apps.yml` 与 `bookmarks.yml` 配置应用和书签的地址。容器会实时更新。也可在 url 后面加上以下参数进行调试：

- 引导操作：`/guide`
- 设置页面：`/settings`
- 在线编辑：`/editor`
- 图标获取：`/icons`
- 帮助页面：`/help`

## 参考与致谢

- [官网](https://soulteary.com/2022/02/23/building-a-personal-bookmark-navigation-app-from-scratch-flare.html)
- [文档 / GitHub repo](https://github.com/soulteary/docker-flare)
- [Docker Hub](https://hub.docker.com/r/soulteary/flare/)
