---
id: Homelab-容器应用管理平台Portainer
title: Homelab - 容器应用管理平台 Portainer
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111545899.png)

**Portainer** 是一个容器应用（包括 Docker / Docker compose / Swarm / Kubernetes）的图形化管理工具，可通过 web 界面管理 Docker 环境。它也提供了许多功能如日志查看、容器启动和停止、镜像管理、网络、卷管理等。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

```yml title="docker-compose.yml"
version: "3.3"
services:
  portainer:
    ports:
      - ${PORT}:9000 # HTTP
      # - ${PORT}:9443 # HTTPS（可选）
    restart: always
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ${PORT}/portainer/portainer_data:/data
    image: portainer/portainer-ce:latest
```

## 配置说明

需注意社区版的镜像是 `portainer/portainer-ce`，与商业版（portainer-be）区分开。

## 参考与致谢

- [官网](https://www.portainer.io/)
- [文档](https://docs.portainer.io/)
- [GitHub repo](https://github.com/portainer/portainer)
- [Docker Hub](https://hub.docker.com/r/portainer/portainer-ce)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
