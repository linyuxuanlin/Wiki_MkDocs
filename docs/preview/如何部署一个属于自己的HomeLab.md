id: 如何部署一个属于自己的 HomeLab
title: 如何部署一个属于自己的 HomeLab

---

## 参考与致谢

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

`[docker-dir]` 替换为本地的目录，比如我的是 `/DATA/AppData`

## CasaOS - 轻量级服务器面板

**官网**：<https://casaos.io>  
**文档**：<https://wiki.casaos.io/en/home>

```bash
curl -fsSL https://get.casaos.io | sudo bash
```

**备注**：官方推荐系统是 Debian 11，更多支持的架构与系统详见文档。

## Nginx Proxy Manager - 反代证书一站式管理工具

**官网**<：https://nginxproxymanager.com>  
**文档**<：https://nginxproxymanager.com/guide>

```yml title="docker-compose.yml"
version: "3"
services:
  app:
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

访问入口：http://127.0.0.1:81

初始账户密码：

- Email: `admin@example.com`
- Password: `changeme`

查看 docker 本地地址：

```bash
ip addr show docker0
```
