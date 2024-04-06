# Homelab - Next Terminal, a Bastion Host Supporting Multiple Protocols

![](https://media.wiki-power.com/img/20230312001443.png)

**Next Terminal** is an easy-to-use bastion host that integrates Apache Guacamole, a clientless remote desktop gateway solution, supporting various protocols such as RDP, SSH, VNC, TELNET, and Kubernetes. It allows direct web access to internal network resources and offers excellent cross-platform compatibility. Next Terminal also supports Multi-Factor Authentication (MFA) for login, audit recording, and other features.

## Deployment (Docker Compose)

To begin, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.3"
services:
  guacd:
    container_name: ${STACK_NAME}_guacd
    image: dushixiang/guacd:${GUACD_VERSION}
    volumes:
      - ${STACK_DIR}/data:/usr/local/next-terminal/data
    restart: always
  next-terminal:
    container_name: ${STACK_NAME}_app
    image: dushixiang/next-terminal:${APP_VERSION}
    environment:
      DB: sqlite
      GUACD_HOSTNAME: ${APP_GUACD_HOSTNAME}
      GUACD_PORT: ${APP_GUACD_PORT}
    ports:
      - ${APP_PORT}:8088
    volumes:
      - /etc/localtime:/etc/localtime
      - ${STACK_DIR}/data:/usr/local/next-terminal/data
    restart: always
```

(Optional) It is recommended to create a `.env` file at the same level as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replacing `${STACK_NAME}` with `next-terminal`).

```dotenv title=".env"
STACK_NAME=next-terminal
STACK_DIR=xxx # Customize your project storage path, e.g., ./next-terminal

# next-terminal
APP_VERSION=latest
APP_PORT=xxxx # Choose an available access port
APP_GUACD_HOSTNAME=guacd # Default
APP_GUACD_PORT=4822 # Default

# guacd
GUACD_VERSION=latest
```

Finally, execute the `docker compose up -d` command in the directory where `compose.yaml` is located to start the orchestrated containers.

## Configuration Details

Initial account/password: `admin`.

## References and Acknowledgments

- [Official Website](https://next-terminal.typesafe.cn/)
- [Documentation](https://next-terminal.typesafe.cn/docs/install/docker-install.html)
- [GitHub Repository](https://github.com/dushixiang/next-terminal)
- [Docker Hub](https://hub.docker.com/r/dushixiang/next-terminal)
- [Demo Site](https://next.typesafe.cn/) (Username: test, Password: test)
- [Next Terminal | Open Source, Lightweight, and Simple Bastion Host](https://blog.samliu.tech/2022/07/22/next-terminal-%E5%BC%80%E6%BA%90-%E8%BD%BB%E9%87%8F-%E7%AE%80%E5%8D%95%E7%9A%84%E5%A0%A1%E5%9E%92%E6%9C%BA/?utm_source=rss&utm_medium=rss&utm_campaign=next-terminal-%25e5%25bc%2580%25e6%25ba%2590-%25e8%25bd%25bb%25e9%2587%258f-%25e7%25ae%2580%25e5%258d%2595%25e7%259a%2584%25e5%25a0%25a1%25e5%259e%9e%25e6%259c%25ba)

[Placeholder 1]
[Placeholder 2]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
