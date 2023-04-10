---
id: 搭建属于自己的HomeLab
title: 搭建属于自己的 HomeLab
---

Homelab 是指可在家中搭建的实验（折腾）环境，用于进行实验和学习。通常指一系列硬件设备（家用服务器、小主机、旧电脑手机、树莓派等），上面运行着操作系统环境和软件（Linux、虚拟机、Docker 等）。Homelab 有很多种用途，比如作为软路由、远程主机，也可以部署一系列的自托管服务，如个人书库、影视库、密码管理器、个人网站、RSS 阅读器、播客服务器、备忘录等等。不仅实用，也可以作一门兴趣，为生活增添乐趣。

## 我的 Homelab 配置

我自己的 Homelab 配置是 **轻量云服务器** + **小主机** + **群晖 NAS**，它们的配置与用途各有千秋：

|              | 轻量云服务器（阿里云 1C2G） | 小主机（N100 CPU） | 群晖 NAS（DS220+） |
| ------------ | --------------------------- | ------------------ | ------------------ |
| 公网 IP      | 有                          | 无                 | 无                 |
| 储存空间     | 小                          | 中                 | 大                 |
| 性能         | 低                          | 高                 | 低                 |
| 应用服务偏向 | 网络访问型                  | 性能消耗型         | 储存需求型         |

基于这个铁三角，我在 **轻量云服务器** 上部署的应用包含 frp 服务器、反向代理服务器、堡垒机、服务器监控面板、小型网站服务、网站 uptime 监测等；在 **小主机** 上部署的有在线 VS Code 环境、内网浏览器、私有笔记库、RSS 阅读器、播客服务器、影视库；而在 **群晖 NAS** 上主要是资料备份、网盘同步、照片、书库等服务。

## 自托管的优势

相比于第三方托管，让别人替你保管数据，**自托管（Self-Hosted）** 具有十足的优势，表现在你对个人数据拥有完全的掌控权，可以根据自己的喜好去定制所需，能帮你获取到更多优质的信息源（个人书库、影视库、RSS 服务）。前提是要有一定的时间精力与资金投入，并且拥有一颗乐于折腾的心。

在接下来的一系列文章中，我将介绍一些基础的配置，还有许多有趣的服务。上面提到的铁三角组合，只是我个人的差异化配置，如果你只有一台机器，折腾起来也是完全没有问题的。我将介绍的内容大多是基于 Docker 与 Docker-compose 部署的，因为这种方式兼容性极佳，在不同配置的机器上都能做到开箱即用。但需要提及的一点是，机器的选择最好是 X86 架构的，因为有些许容器没有做 ARM 适配，需要自己编译安装。

---

以下内容有待逐步排版，将分散为多篇文章。

---

## frps - 内网穿透工具（服务端）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195137.png)

**主要功能**：通过有公网 IP 的服务器，将内网主机端口暴露到互联网。

**文档**：<https://hub.docker.com/r/snowdreamtech/frps>

在 `[custom-dir]/frp/` 下新建 `frps.ini`：

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
      - [custom-port]:7000 # bind_port
      - [custom-port]:7500 # dashboard_port
    volumes:
      - [custom-dir]/frp/frps.ini:/etc/frp/frps.ini
      manager/letsencrypt:/etc/letsencrypt
```

**默认面板访问地址**：<http://127.0.0.1:7500>

**参考文档**：

- [**如何实现外网 RDP 远控（frp）**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [**使用 frp 访问群晖 NAS**](https://wiki-power.com/%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/)

---

## iconserver - favicon 服务器

网站图标favicon抓取服务器iconserver

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195157.png)

**主要功能**：抓取网站的 favicon。

**文档**：<https://github.com/mat/besticon#docker>

https://hub.docker.com/r/matthiasluedtke/iconserver/

[Demo site](https://besticon-demo.herokuapp.com/)

```yml title="docker-compose.yml"
version: "3"
services:
  iconserver:
    image: "matthiasluedtke/iconserver:latest"
    restart: always
    ports:
      - [custom-port]:8080
```

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
      - "[custom-port]:8000"
```

**备注**：如需使用反向代理，请开启 `Websockets Support`。

---

## Syncthing - 跨设备同步工具

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195228.png)

**主要功能**：把本地的文件同步至其他服务器上。

**文档**：<https://hub.docker.com/r/syncthing/syncthing/>

在 CasaOS 内可一键安装。

```yml title="docker-compose.yml"
version: "3"
services:
  syncthing:
    image: syncthing/syncthing
    container_name: syncthing
    hostname: my-syncthing
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      - [DATA]:/DATA
      - [custom-dir]/config:/config
    ports:
      - [custom-port]:8384 # Web UI
      - 22000:22000/tcp # TCP file transfers
      - 22000:22000/udp # QUIC file transfers
      - 21027:21027/udp # Receive local discovery broadcasts
    restart: unless-stopped
```

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
      - "[custom-port]:80"
    environment:
      USERNAME: [username]
      PASSWORD: [password]
    volumes:
      - [syncing-dir]:/data
```

---

## memos - 开源的自托管备忘录

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195311.png)

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
      - [custom-dir]:/var/opt/memos
    ports:
      - [custom-port]:5230
```

**移动端 App**：[Moe Memos](https://memos.moe/)

**备注**：因用户数据以数据库格式储存，如需导入 / 导出数据，可使用 VS Code 插件 [**SQLite**](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)，下载并打开 `[custom-dir]` 下的 `memos_prod.db` 即可进行增删改查、导入导出备份等操作。注意，只有在 docker 容器关闭 / 重启的时候才会更新 `memos_prod.db` 文件。

---

## Wiki.js - 功能强大的 wiki 文档工具

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195348.png)

**主要功能**：带后台编辑器和管理页面的 wiki 文档工具，包括多用户权限管理、Markdown、多种储存方式（含 git）等功能。

**官网**：<https://js.wiki>  
**文档**：<https://docs.requarks.io/install/docker>

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
      - [custom-dir]/db-data:/var/lib/postgresql/data

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
      - "[custom-port]:3000"

volumes:
  db-data:
```

**备注**：如果 wikijs 不上 postgres，可尝试将 postgres 版本改为 10。  
**配置 git 仓库同步的详细教程**：<https://docs.requarks.io/storage/git>

---

## Vaultwarden - 密码管理器（可在 CasaOS 内一键安装）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195414.jpg)

**备注**：因 Bitwarden 官方浏览器拓展与旧版本（低于 1.27.0）不兼容导致无法登录，请勿直接使用一键安装的版本（版本默认为 1.24.0）。需要一键安装后手动导出 appjson，再重新导入、改版本号后安装。（issue 详见：https://github.com/dani-garcia/vaultwarden/issues/3082）

---

## lsky-pro

```yml title="docker-compose.yml"
version: '3'
services:
  lsky:
    image: halcyonazure/lsky-pro-docker:latest
    restart: unless-stopped
    ports:
      - "[custom-port]:80"
    volumes:
      - [custom-dir]:/var/www/html

```

---

## Cloudreve - 支持多家云存储驱动的公有云文件系统

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195423.png)

**主要功能**：支持本地、从机、七牛、阿里云 OSS、腾讯云 COS、又拍云、OneDrive、S3 兼容协议作为储存端，可对接 Aria2 离线下载，多用户，拖拽上传 / 管理，在线预览 / 编辑，WebDAV 等。经典的实例是用作个人图床 / 网盘文件管理。

**官网**：<https://docs.cloudreve.org/>  
**文档**：<https://docs.cloudreve.org/getting-started/install#docker-compose>

首先创建目录结构，切换到你的 [custom-dir] 下并执行：

```shell
mkdir -vp cloudreve/{uploads,avatar,data} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db \
&& mkdir -p aria2/config \
&& mkdir -p cloudreve/data/aria2 \
&& chmod -R 777 cloudreve/data/aria2 \
&& mkdir data
```

```yml title="docker-compose.yml"
version: "3.8"
services:
  cloudreve:
    container_name: cloudreve
    image: cloudreve/cloudreve:latest
    restart: unless-stopped
    ports:
      - "[custom-port]:5212"
    volumes:
      - temp_data:/data
      - [custom-dir]/uploads:/cloudreve/uploads
      - [custom-dir]/conf.ini:/cloudreve/conf.ini
      - [custom-dir]/cloudreve.db:/cloudreve/cloudreve.db
      - [custom-dir]/avatar:/cloudreve/avatar
    depends_on:
      - aria2
  aria2:
    container_name: aria2
    image: p3terx/aria2-pro
    restart: unless-stopped
    environment:
      - RPC_SECRET=[your_aria_rpc_token]
      - RPC_PORT=6800
    volumes:
      - [custom-dir]/config:/config
      - temp_data:/data
volumes:
  temp_data:
    driver: local
    driver_opts:
      type: none
      device: $PWD/data
      o: bind
```

**备注**：首次启动时，会创建初始管理员账号，可以在 log 中找到。如果错过了，请删除目录下的 cloudreve.db，重新启动主程序以初始化新的管理员账户。  
**推荐的文件命名规则**：`{year}{month}{day}{hour}{minute}{second}{ext}`

---

## FreshRSS - 自托管 RSS 聚合器

**官网**：<https://freshrss.org>  
**文档**：<https://github.com/FreshRSS/FreshRSS/tree/edge/Docker>

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230310205330.png)

**主要功能**：自带网页阅读，导入 OPML 订阅源，API 移动端阅读，插件生态齐全。

```yml title="docker-compose.yml"
version: "2.4"
services:
  freshrss:
    image: freshrss/freshrss
    container_name: freshrss
    hostname: freshrss
    restart: unless-stopped
    logging:
      options:
        max-size: 10m
    ports:
      - "[custom-port]:80"
    volumes:
      - [custom-dir]/data:/var/www/FreshRSS/data
      - [custom-dir]/extensions:/var/www/FreshRSS/extensions
    environment:
      TZ: Asia/Shanghai
      CRON_MIN: '*/5'
```

**移动端 App**：FeedMe (Android), NetNewsWire (iOS)

---

## Next Terminal - 堡垒机

Next Terminal 是集成了 Apache Guacamole 无客户端的远程桌面网关的堡垒机（也称跳板机）方案，能直接通过 web 访问内网资源，跨平台兼容性佳，协议支持 RDP、SSH、VNC、Telnet、Kubernetes。支持 MFA 多因子认证登录，也有审计录像功能和其他记录。

**官网**：<https://next-terminal.typesafe.cn/>  
**文档**：<https://next-terminal.typesafe.cn/docs/install/docker-install.html>

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230312001443.png)

```yml title="docker-compose.yml"
version: '3.3'
services:
  guacd:
    image: dushixiang/guacd:latest
    volumes:
      - [custom-dir]/data:/usr/local/next-terminal/data
    restart:
          always
  next-terminal:
    image: dushixiang/next-terminal:latest
    environment:
      DB: sqlite
      GUACD_HOSTNAME: guacd
      GUACD_PORT: 4822
    ports:
      - "[custom-port]:8088"
    volumes:
      - /etc/localtime:/etc/localtime
      - [custom-dir]/data:/usr/local/next-terminal/data
    restart:
      always
```

**默认账户密码**： `admin`  
**参考文章**：[Next Terminal | 开源 轻量 简单的堡垒机](https://blog.samliu.tech/2022/07/22/next-terminal-%E5%BC%80%E6%BA%90-%E8%BD%BB%E9%87%8F-%E7%AE%80%E5%8D%95%E7%9A%84%E5%A0%A1%E5%9E%92%E6%9C%BA/?utm_source=rss&utm_medium=rss&utm_campaign=next-terminal-%25e5%25bc%2580%25e6%25ba%2590-%25e8%25bd%25bb%25e9%2587%258f-%25e7%25ae%2580%25e5%258d%2595%25e7%259a%2584%25e5%25a0%25a1%25e5%259e%2592%25e6%259c%25ba)

---

## Podgrab - 自托管播客管理器

Podgrab 是一个自托管的播客管理器 / 下载器 / 存档工具，可通过 RSS 或内置搜索订阅播客，在播客节目上线后立即下载，web 带内置的播放器。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230316131448.png)

**官网**：<https://github.com/akhilrex/podgrab>  
**文档**：<https://hub.docker.com/r/akhilrex/podgrab/>

A self-hosted podcast manager/downloader/archiver tool to download podcast episodes as soon as they become live with an integrated player.

一个自我托管的/下载器/存档工具，可在播客节目上线后立即下载，并带有一个集成播放器。

```yml title="docker-compose.yml"
version: "2.1"
services:
  podgrab:
    image: akhilrex/podgrab
    container_name: podgrab
    environment:
      - CHECK_FREQUENCY=240
      # - PASSWORD=password     ## Uncomment to enable basic authentication, username = podgrab
    volumes:
      - /path/to/config:/config
      - /path/to/data:/assets
    ports:
      - 8080:8080
    restart: unless-stopped
```

---

🚧 未完待续~

---

## Todo - 简单的待办事项

```yml title="docker-compose.yml"
version: "3"

services:
  todo:
    image: prologic/todo
    container_name: todo
    restart: always
    ports:
      - [custom-port]:8000
    volumes:
      - [custom-dir]/todo/todo_db:/usr/local/go/src/todo/todo.db
    environment:
      - THEME=dracula
```

---

## Homebox - 家庭库存管理系统

doc: https://hay-kot.github.io/homebox/quick-start/

```yml title="docker-compose.yml"
version: "3.4"

services:
  homebox:
    image: ghcr.io/hay-kot/homebox:latest
    container_name: homebox
    restart: always
    environment:
      - HBOX_LOG_LEVEL=info
      - HBOX_LOG_FORMAT=text
      - HBOX_WEB_MAX_UPLOAD_SIZE=10
    volumes:
      - [custom-dir]/homebox:/data/
    ports:
      - [custom-port]:7745
```

---

## 参考与致谢

- [Docker Proxy](https://dockerproxy.com/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

---

## Yacht

```yml title="docker-compose.yml"
version: "3"
services:
  yacht:
    container_name: yacht
    restart: unless-stopped
    ports:
      - [custom-port]:8000
    volumes:
      - [custom-dir]:/config
      - /var/run/docker.sock:/var/run/docker.sock
    image: selfhostedpro/yacht
```

**初始账户密码**：

- Email: `admin@yacht.local`
- Password: `pass`

[用 Yacht 管理 docker 容器](https://laosu.ml/2022/06/01/%E7%94%A8Yacht%E7%AE%A1%E7%90%86docker%E5%AE%B9%E5%99%A8/)

---

## Portainer

```yml title="docker-compose.yml"
version: '3.3'
services:
    portainer:
        ports:
            - [custom-dir]:9000 #HTTP
            - [custom-dir]:9443 #HTTPS
        restart: always
        volumes:
            - /var/run/docker.sock:/var/run/docker.sock
            - [custom-dir]/portainer_data:/data
        image: portainer/portainer-ce:latest
```

---

## audiobookshelf

```yml title="docker-compose.yml"
version: "3.7"
services:
  audiobookshelf:
    image: ghcr.io/advplyr/audiobookshelf:latest
    ports:
      - [custom-port]:80
    volumes:
      - [custom-dir]/audiobooks:/audiobooks
      - [custom-dir]/podcasts:/podcasts
      - [custom-dir]/config:/config
      - [custom-dir]/metadata:/metadata
```

---

一键启动多个 docker-compose 配置容器:https://juejin.cn/post/7082842557482270734

---
