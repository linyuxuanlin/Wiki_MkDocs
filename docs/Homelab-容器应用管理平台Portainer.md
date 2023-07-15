---
id: Homelab-容器应用管理平台Portainer
title: Homelab - 容器应用管理平台 Portainer
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111545899.png)

**Portainer** 是一个容器应用（包括 Docker / Docker compose / Swarm / Kubernetes）的图形化管理工具，可通过 web 界面管理 Docker 环境。它也提供了许多功能如日志查看、容器启动和停止、镜像管理、网络、卷管理等。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3.3"
services:
  portainer:
    container_name: ${STACK_NAME}_app
    image: portainer/portainer-ce:${APP_VERSION}
    ports:
      - ${APP_PORT_HTTP}:9000 # HTTP
    # - ${APP_PORT_HTTPS}:9443 # HTTPS（可选）
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ${STACK_DIR}/portainer_data:/data
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `portainer`）。

```dotenv title=".env"
STACK_NAME=portainer
STACK_DIR=xxx # 自定义项目储存路径，例如 ./portainer

# portainer
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。


## 配置说明

需注意社区版的镜像是 `portainer/portainer-ce`，与商业版（portainer-be）区分开。

## 参考与致谢

- [官网](https://www.portainer.io/)
- [文档](https://docs.portainer.io/)
- [GitHub repo](https://github.com/portainer/portainer)
- [Docker Hub](https://hub.docker.com/r/portainer/portainer-ce)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
