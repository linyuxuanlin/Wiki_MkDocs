---
id: Homelab-电子书管理服务器calibre-web
title: Homelab - 电子书管理服务器 calibre-web
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429125418.png)

**calibre-web** 是一个一站式电子书解决方案，它基于 Calibre，可在网页上阅读电子书，集成了 calibre-server 服务，也带电子书格式转换。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  calibre-web:
    container_name: ${STACK_NAME}_app
    image: johngong/calibre-web:${APP_VERSION}
    ports:
      - ${APP_PORT_WEB}:8083
      - ${APP_PORT_SERVER}:8080
    volumes:
      - ${STACK_DIR}:/config
      - ${DATA_DIR}:/library
      - ${DATA_DIR}/autoaddbooks:/autoaddbooks
    restart: unless-stopped
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `audiobookshelf`）。

```dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # 自定义项目储存路径，例如 ./calibre-web
DATA_DIR=xxx # 自定义播客储存路径，例如 ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # 自定义 Web UI 的访问端口，选择不被占用的即可
APP_PORT_SERVER=xxxx # 自定义 calibre-server 的访问端口，选择不被占用的即可
```

如果你有个 NAS，也可以通过 NFS 协议挂载 NAS 上的储存空间，把音乐储存在 NAS 上以节省服务器空间，详情请参考 [**Linux 下挂载群晖 NAS 硬盘拓展空间（NFS）**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/)。

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

默认的账号是 `admin`，密码是 `admin123`。

### 书籍上传功能

系统默认是没有书籍上传功能的，需要依次点击右上角 `管理权限` - `编辑基本配置` — `启用上传`，这样才能启用书籍上传功能。

### 移动端使用

Android 上可使用 Librera，通过 OPDS 协议连接 calibre-web。添加书库的 url 是在原 url 最后加上`/opds`，例如`calibre.xxx.com/opds`。

### 忘记密码

如果忘记密码，可以将 `calibre-web` 中的 `app.db` 数据库下载下来，使用 SQLite 查看软件（或在线工具如 [**Sqlite 查看器 | 修改器**](https://www.lzltool.com/sqlite-viewer)），分别执行以下语句：

```sql
SELECT * FROM 'user' LIMIT 0,30 --也可也手动切换到名为 user 的表
```

```sql
UPDATE user SET password='pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' WHERE name='xxx'; -- 需要修改xxx为你当前的用户名
```

把修改的 `app.db` 替换掉原来的，随后使用新的密码 `hello` 登录即可。

## 参考与致谢

- [GitHub repo](https://github.com/janeczku/calibre-web)
- [Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
