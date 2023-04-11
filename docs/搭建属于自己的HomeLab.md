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

以下内容将会被拆分为多篇文章，正在编辑中。

---

## frps - 内网穿透工具（服务端）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195137.png)

**主要功能**：通过有公网 IP 的服务器，将内网主机端口暴露到互联网。

**文档**：<https://hub.docker.com/r/snowdreamtech/frps>

在 `${DIR}/frp/` 下新建 `frps.ini`：

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
      - ${PORT}:7000 # bind_port
      - ${PORT}:7500 # dashboard_port
    volumes:
      - ${DIR}/frp/frps.ini:/etc/frp/frps.ini
      manager/letsencrypt:/etc/letsencrypt
```

**默认面板访问地址**：<http://127.0.0.1:7500>

**参考文档**：

- [**如何实现外网 RDP 远控（frp）**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [**使用 frp 访问群晖 NAS**](https://wiki-power.com/%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/)

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
      - "${PORT}:8000"
```

**备注**：如需使用反向代理，请开启 `Websockets Support`。

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
      - "${PORT}:80"
    environment:
      USERNAME: [username]
      PASSWORD: [password]
    volumes:
      - [syncing-dir]:/data
```

---

## lsky-pro

```yml title="docker-compose.yml"
version: "3"
services:
  lsky:
    image: halcyonazure/lsky-pro-docker:latest
    restart: unless-stopped
    ports:
      - "${PORT}:80"
    volumes:
      - ${DIR}:/var/www/html
```

---

---



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
      - ${DIR}/homebox:/data/
    ports:
      - ${PORT}:7745
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
      - ${PORT}:8000
    volumes:
      - ${DIR}:/config
      - /var/run/docker.sock:/var/run/docker.sock
    image: selfhostedpro/yacht
```

**初始账户密码**：

- Email: `admin@yacht.local`
- Password: `pass`

[用 Yacht 管理 docker 容器](https://laosu.ml/2022/06/01/%E7%94%A8Yacht%E7%AE%A1%E7%90%86docker%E5%AE%B9%E5%99%A8/)

---

## audiobookshelf

```yml title="docker-compose.yml"
version: "3.7"
services:
  audiobookshelf:
    image: ghcr.io/advplyr/audiobookshelf:latest
    ports:
      - ${PORT}:80
    volumes:
      - ${DIR}/audiobooks:/audiobooks
      - ${DIR}/podcasts:/podcasts
      - ${DIR}/config:/config
      - ${DIR}/metadata:/metadata
```

---

一键启动多个 docker-compose 配置容器:https://juejin.cn/post/7082842557482270734

---
