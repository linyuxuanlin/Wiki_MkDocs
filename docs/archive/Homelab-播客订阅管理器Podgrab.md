---
id: Homelab-播客订阅管理器Podgrab
title: Homelab - 播客订阅管理器 Podgrab
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230316131448.png)

**Podgrab** 是一个自托管的播客管理器 / 下载器 / 存档工具，可通过 RSS 或内置搜索引擎搜索订阅播客节目，可自动下载新上线节目，并且自带 web 播放器。

## 部署（Docker Compose）

首先创建 `compose.yaml` ，并将以下的 `${DIR}` 替换为本地的目录（例如 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

```yaml title="compose.yaml"
version: "2.1"
services:
  podgrab:
    image: akhilrex/podgrab:latest
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

## 参考与致谢

- [文档 / GitHub repo](https://github.com/akhilrex/podgrab)
- [Docker Hub](https://hub.docker.com/r/akhilrex/podgrab/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
