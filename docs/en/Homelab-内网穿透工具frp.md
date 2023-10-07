# Homelab - Internal Network Penetration Tool frp

![](https://f004.backblazeb2.com/file/wiki-media/img/20230304195137.png)

**frp** is a method of internal network penetration. You can expose the ports of internal hosts to the Internet through a server with a public IP address. frp supports multiple protocols such as TCP, UDP, HTTP, and HTTPS.

## Deployment of Server-side frps (Docker Compose)

First, create the `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  frps:
    container_name: ${STACK_NAME}_app
    image: snowdreamtech/frps:${APP_VERSION}
    network_mode: host
    volumes:
      - ${STACK_DIR}/frps.ini:/etc/frp/frps.ini
    restart: always
```

(Optional) It is recommended to create a `.env` file at the same level as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `frps`).

```dotenv title=".env"
STACK_NAME=frps
STACK_DIR=xxx # Custom project storage path, such as ./frps

# frps
APP_VERSION=latest
```

Add the configuration file `frps.ini` in your project storage path `${STACK_DIR}`:

```ini title="frps.ini"
[common]
bind_port = 7000 # The port for clients to connect to the server, which will be used when configuring the client later.
dashboard_port = 7500 # The port for the server dashboard.
token = ${TOKEN-FRPS} # The token for clients to connect to the server, please set it yourself.
dashboard_user = ${USERNAME-FRPS} # The username for the dashboard.
dashboard_pwd = ${PASSWORD-FRPS} # The password for the dashboard.
```

Finally, execute the command `docker compose up -d` in the directory where `compose.yaml` is located to start the orchestrated containers.

If you don't use the docker method, you can also refer to this article: [**Server Configuration·How to Implement External Network RDP Remote Control (frp)**](https://wiki-power.com/en/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#_2).

## Client frpc Deployment (Docker Compose)

First, create the `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.3"
services:
  frpc:
    container_name: ${STACK_NAME}_app
    image: stilleshan/frpc:${APP_VERSION}
    network_mode: "host"
    volumes:
      - ${STACK_DIR}/frpc.ini:/frp/frpc.ini
    restart: always
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you don't want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `replace`).

```dotenv title=".env"
STACK_NAME=replace
STACK_DIR=xxx # Custom project storage path, for example ./replace

# replace
APP_VERSION=latest
```

Add the configuration file `frps.ini` to your project storage path `${STACK_DIR}`:

```ini title="frpc.ini"
[common]
server_addr = xx.xx.xx.xx # Public IP of the server
server_port = 7000 # Keep consistent with the server-side port
tls_enable = true
token = ${TOKEN-FRPS} # Keep consistent with the token on the server-side

[xxx]
type = tcp
remote_port = xx # Public port number for access
local_ip = localhost
local_port = xx # Internal port number
```

Finally, execute the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated containers.

## References and Acknowledgments

- [GitHub repo · snowdreamtech/frps](https://github.com/snowdreamtech/frp)
- [GitHub repo · stilleshan/frpc](https://github.com/stilleshan/frpc)
- [Docker Hub · snowdreamtech/frps](https://hub.docker.com/r/snowdreamtech/frps)
- [Docker Hub · stilleshan/frpc](https://hub.docker.com/r/stilleshan/frpc)
- [How to implement external network RDP remote control (frp)](https://wiki-power.com/en/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [Access Synology NAS using frp](https://wiki-power.com/en/%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.