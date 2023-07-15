---
id: Homelab-极简个人书签导航站Flare
title: Homelab - 极简个人书签导航站 Flare
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410170939.png)

**Flare** 是一个轻量、快速、美观的个人导航页面，无任何数据库依赖，应用数据完全开放透明，支持在线编辑，内置 Material Design Icons 6k+ 图标。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3.6"

services:
  flare:
    container_name: ${STACK_NAME}_app
    image: soulteary/flare:${APP_VERSION}
    # 更多启动参数请参考文档 https://github.com/soulteary/docker-flare/blob/main/docs/advanced-startup.md
    ports:
      - ${APP_PORT}:5005
    volumes:
      - ${STACK_DIR}:/app
    command: flare --nologin=0 # 开启用户登录模式，需要先设置 `nologin` 启动参数为 `0`
    environment:
      - FLARE_USER= ${APP_USER} # 如开启用户登录模式，且未设置 FLARE_USER，则默认用户为 `flare`
      - FLARE_PASS= ${APP_PASS} # 如开启用户登录模式，且未设置 FLARE_USER，则会默认生成密码并展示在应用启动日志中
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `flare`）。

```dotenv title=".env"
STACK_NAME=flare
STACK_DIR=xxx # 自定义项目储存路径，例如 ./flare

# flare
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
APP_USER=xxxx # 自定义用户名
APP_PASS=xxxx # 自定义密码
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

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
