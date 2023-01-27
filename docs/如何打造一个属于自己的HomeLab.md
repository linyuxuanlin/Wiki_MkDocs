---
id: 如何打造一个属于自己的 HomeLab
title: 如何打造一个属于自己的 HomeLab
---

注：下文出现的 `[docker-dir]` 替换为本地的目录，比如我用的是 `/DATA/AppData`；`[port]` 替换为自定义的端口号（0~65535），比如 `1234`

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
      - "80:80"
      - "81:81"
      - "443:443"
    volumes:
      - [docker-dir]/nginx-proxy-manager/data:/data
      - [docker-dir]/nginx-proxy-manager/letsencrypt:/etc/letsencrypt
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

在 `[docker-dir]/frp/` 下新建 `frps.ini`：

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
      - 7000:7000
      - 7500:7500
    volumes:
      - [docker-dir]/frp/frps.ini:/etc/frp/frps.ini
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
      - 8081:8080
```

**面板访问地址**：<http://127.0.0.1:8081>

---

## WebDAV - 跨平台文件共享协议

**主要功能**：把数据备份到其他服务器上。

**文档**：<https://hub.docker.com/r/derkades/webdav>

```
version: '3'
services:
  webdav:
    image: derkades/webdav
    restart: always
    ports:
      - "[port]:80"
    environment:
      USERNAME: [username]
      PASSWORD: [password]
    volumes:
      - [syncing-dir]:/data
```

---

## （可一键安装）Vaultwarden

---

## 参考与致谢

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

---


https://icon.casaos.io/main/all/focalboard.png

docker run -it -p 8082:8000 mattermost/focalboard