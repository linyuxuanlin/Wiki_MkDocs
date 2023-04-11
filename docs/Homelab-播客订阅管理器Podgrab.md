---
id: Homelab-播客订阅管理器Podgrab
title: Homelab - 播客订阅管理器 Podgrab 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230316131448.png)

**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：

```yml title="docker-compose.yml"
version: "2.1"
services:
  podgrab:
    image: akhilrex/podgrab
    environment:
      - CHECK_FREQUENCY=240
    # - PASSWORD=${PASSWORD} # 加访问密码，username = podgrab
    volumes:
      - ${DIR}/podgrab/config:/config
      - ${DIR}/podgrab/assets:/assets
    ports:
      - ${PORT}:8080
    restart: unless-stopped
```

## 配置说明

## 参考与致谢

- [文档 / GitHub repo](https://github.com/akhilrex/podgrab)
- [Docker Hub](https://hub.docker.com/r/akhilrex/podgrab/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
