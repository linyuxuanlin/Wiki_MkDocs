---
id: 打造一个属于自己的HomeLab
title: 打造一个属于自己的 HomeLab
---

如果你有一个云服务器，觉得不跑点什么服务挺浪费的，那可以尝试部署以下的自托管应用，为生活增加点乐趣。以下服务大多基于 Docker，配合 CasaOS 图形化面板使用，便于折腾与管理。

注：下文出现的 `[local-dir]` 替换为本地的目录，比如我用的是 `/DATA/AppData/xxx`；`[local-port]` 替换为自定义的端口号（0~65535），比如 `1234`。

---

## CasaOS - 轻量级服务器面板

**主要功能**：管理面板、状态监测、文件管理、终端、Docker 容器管理、内置 Docker 应用商店。

**官网**：<https://casaos.io>  
**文档**：<https://wiki.casaos.io/en/home>

```shell
curl -fsSL https://get.casaos.io | sudo bash
```

**面板访问地址**：<http://127.0.0.1:80>

**备注**：

- 官方推荐系统是 Debian 11，更多支持的架构与系统详见文档。
- 登陆后把默认的 80 端口改掉，留给 Nginx Proxy Manager 用。

---

## Nginx Proxy Manager - 反代证书一站式管理面板

**主要功能**：图形化 nginx 管理、自动申请续签 SSL 证书。

**官网**：<https://nginxproxymanager.com>  
**文档**：<https://nginxproxymanager.com/guide>

```yml title="docker-compose.yml"
version: "3"
services:
  nginx-proxy-manager:
    image: "jc21/nginx-proxy-manager:latest"
    restart: unless-stopped
    ports:
      - "[local-port]:80"
      - "[local-port]:81"
      - "[local-port]:443"
    volumes:
      - [local-dir]/nginx-proxy-manager/data:/data
      - [local-dir]/nginx-proxy-manager/letsencrypt:/etc/letsencrypt
```

**面板访问地址**：<http://127.0.0.1:81>

**初始账户密码**：

- Email: `admin@example.com`
- Password: `changeme`

**获取 docker 本地地址**：

```shell
ip addr show docker0
```

注：对于自部署的服务，请通过反代走域名访问（80/443 端口），并在服务器管理控制台防火墙中关闭其他端口，以提高安全性。

---

## Watchtower - 自动更新 Docker 容器

**主要功能**：自动更新全部 / 部分 Docker 容器。

**文档**：<https://containrrr.dev/watchtower>

```yml title="docker-compose.yml"
version: "3"
services:
  watchtower:
    image: containrrr/watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

---

## frps - 内网穿透工具（服务端）

**主要功能**：通过有公网 IP 的服务器，将内网主机端口暴露到互联网。

**文档**：<https://hub.docker.com/r/snowdreamtech/frps>

在 `[local-dir]/frp/` 下新建 `frps.ini`：

```ini title="frps.ini"
[common]
bind_port = 7000
dashboard_port = 7500
token = 设置 token
dashboard_user = 设置用户名
dashboard_pwd = 设置面板密码
```

```yml title="docker-compose.yml"
version: "3"
services:
  frps:
    image: "snowdreamtech/frps:latest"
    restart: always
    ports:
      - [local-port]:7000
      - [local-port]:7500
    volumes:
      - [local-dir]/frp/frps.ini:/etc/frp/frps.ini
      manager/letsencrypt:/etc/letsencrypt
```

**面板访问地址**：<http://127.0.0.1:7500>

**参考文档**：

- [**如何实现外网 RDP 远控（frp）**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [**使用 frp 访问群晖 NAS**](https://wiki-power.com/%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/)

---

## iconserver - favicon 服务器

**主要功能**：抓取网站的 favicon。

**文档**：<https://github.com/mat/besticon#docker>

```yml title="docker-compose.yml"
version: "3"
services:
  iconserver:
    image: "matthiasluedtke/iconserver:latest"
    restart: always
    ports:
      - [local-port]:8080
```

**面板访问地址**：<http://127.0.0.1:8080>

---

## Focalboard - 项目管理工具

**主要功能**：开源的项目管理、TODO 工具

**文档**：<https://hub.docker.com/r/mattermost/focalboard>

```yml title="docker-compose.yml"
version: "3"
services:
  webdav:
    image: mattermost/focalboard
    restart: always
    ports:
      - "[local-port]:8000"
```

**备注**：如需使用反向代理，请开启 `Websockets Support`。

---

## Syncthing - 跨设备同步工具

**主要功能**：把本地的文件同步至其他服务器上。

**文档**：<https://hub.docker.com/r/syncthing/syncthing/>

在 CasaOS 内可一键安装。

---

## WebDAV - 跨平台文件共享协议

**主要功能**：把数据备份到其他服务器上。

**文档**：<https://hub.docker.com/r/derkades/webdav>

```yml title="docker-compose.yml"
version: '3'
services:
  webdav:
    image: derkades/webdav
    restart: always
    ports:
      - "[local-port]:80"
    environment:
      USERNAME: [username]
      PASSWORD: [password]
    volumes:
      - [syncing-dir]:/data
```

---

## Uptime Kuma - 网站状态监控工具

**主要功能**：监控网站的可用状态、响应时长、证书有效期等。

**官网**：<https://uptime.kuma.pet/>  
**文档**：<https://github.com/louislam/uptime-kuma/wiki>

```yml title="docker-compose.yml"
version: '3'
services:
  uptime-kuma:
    image: louislam/uptime-kuma
    restart: always
    ports:
      - "[local-port]:3001"
    volumes:
      - [local-dir]:/app/data
```

**面板访问地址**：<http://127.0.0.1:3001>

**备注**：如需使用反向代理，请开启 `Websockets Support`。

---

## memos - 开源的自托管备忘录

**主要功能**：支持公开分享、Markdown 语法、iframe 嵌入、标签管理、日历视图、简单数据迁移与备份等。

**官网**：<https://usememos.com/>  
**文档**：<https://github.com/usememos/memos>

```yml title="docker-compose.yml"
version: "3.0"
services:
  memos:
    image: neosmemo/memos:latest
    container_name: memos
    volumes:
      - [local-dir]:/var/opt/memos
    ports:
      - [local-port]:5230
```

**面板访问地址**：<http://127.0.0.1:5230>  
**移动端 App**：[Moe Memos](https://memos.moe/)

**备注**：因用户数据以数据库格式储存，如需导入 / 导出数据，可使用 VS Code 插件 [**SQLite**](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)，下载并打开 `[local-dir]` 下的 `memos_prod.db` 即可进行增删改查、导入导出备份等操作。注意，只有在 docker 容器关闭 / 重启的时候才会更新 `memos_prod.db` 文件。

---

## （可一键安装）Vaultwarden

注：且 Bitwarden 官方浏览器拓展与旧版本（低于 1.27.0）不兼容导致无法登录，请不要使用一键安装的版本（版本是锁定在 1.24.0），可一键安装后导出 appjson，再重新导入，改版本号后安装。（详情：https://github.com/dani-garcia/vaultwarden/issues/3082）

---

pg_hba.conf

把最后的 md5 改为 password

加端口 5432

DB_HOST: 127.0.0.1

🚧 未完待续~

---

## 参考与致谢

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

version: '3'
services:
lsky:
image: halcyonazure/lsky-pro-docker:latest
restart: unless-stopped
ports: - "5011:80"
volumes: - /DATA/AppData/lsky:/var/www/html

sqlite3



---

wiki.js

https://docs.requarks.io/install/docker

```yml title="docker-compose.yml"
version: "3"
services:
  db:
    image: postgres:10-alpine
    container_name: postgres
    environment:
      POSTGRES_DB: wiki
      POSTGRES_PASSWORD: wikijsrocks
      POSTGRES_USER: wikijs
    logging:
      driver: "none"
    restart: unless-stopped
    volumes:
      - [docker-dir]/db-data:/var/lib/postgresql/data

  wiki:
    image: ghcr.io/requarks/wiki:2
    container_name: wikijs
    depends_on:
      - db
    environment:
      DB_TYPE: postgres
      DB_HOST: db
      DB_PORT: 5432
      DB_USER: wikijs
      DB_PASS: wikijsrocks
      DB_NAME: wiki
    restart: unless-stopped
    ports:
      - "[port]:3000"

volumes:
  db-data:
```

注：如果 wikijs 不上 postgres，可尝试将 postgres 版本改为 10。

https://docs.requarks.io/storage/git


---

picuploader

```yml title="docker-compose.yml"
version: "3.0"
services:
  picuploader:
    image: artxia/picuploader-docker
    container_name: picuploader
    environment:
      TZ: Asia/Shanghai
      USER: admin
      PASSWD: admin
    volumes:
      - [docker-dir]/config/config-local.php:/var/www/PicUploader/config/config-local.php
      - [docker-dir]/db/PicUploader.db:/var/www/PicUploader/db/PicUploader.db 
    ports:
      - [local-port]:80
```

