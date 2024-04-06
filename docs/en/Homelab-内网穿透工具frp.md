# Homelab - Local Network Penetration Tool frp

![frp](https://media.wiki-power.com/img/20230304195137.png)

**frp** is a method for local network penetration. You can expose the ports of your internal network hosts to the internet through a server with a public IP address. frp supports various protocols, including TCP, UDP, HTTP, and HTTPS.

## Deploying the Server-side frps (Docker Compose)

Start by creating a `compose.yaml` file and paste the following content:

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `frps`).

```dotenv title=".env"
STACK_NAME=frps
STACK_DIR=xxx # Customize your project storage path, e.g., ./frps

# frps
APP_VERSION=latest
```

In your project storage path `${STACK_DIR}`, add the configuration file `frps.ini`:

```ini title="frps.ini"
[common]
bind_port = 7000 # Port for client and server connection, which will be used when configuring the client later.
dashboard_port = 7500 # Port for the server's dashboard
token = ${TOKEN-FRPS} # Token for client and server connection, please set it yourself.
dashboard_user = ${USERNAME-FRPS} # Username
dashboard_pwd = ${PASSWORD-FRPS} # Password
```

Finally, run the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

If you prefer not to use Docker, you can also refer to this article: [**Server Configuration: How to Achieve External Network RDP Remote Control (frp)**](https://example.com) for instructions.

## Deploying the Client-side frpc (Docker Compose)

Begin by creating a `compose.yaml` file and paste the following content:

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `replace`).

````dotenv title=".env"
STACK_NAME=replace
STACK_DIR=xxx # Customize your project storage path, e.g., ./replace


```markdown
# Replace
APP_VERSION=latest
````

To configure the `frps.ini` file in your project storage path `${STACK_DIR}`:

```ini title="frpc.ini"
[common]
server_addr = xx.xx.xx.xx  # Public IP of your server
server_port = 7000  # Keep it consistent with the server-side port
tls_enable = true
token = ${TOKEN-FRPS}  # Keep it consistent with the server-side token

[xxx]
type = tcp
remote_port = xx  # Public access port
local_ip = localhost
local_port = xx  # Internal port
```

Finally, execute the `docker compose up -d` command in the same directory as the `compose.yaml` to start the orchestrated containers.

## References and Acknowledgments

- [GitHub Repository · snowdreamtech/frps](https://github.com/snowdreamtech/frp)
- [GitHub Repository · stilleshan/frpc](https://github.com/stilleshan/frpc)
- [Docker Hub · snowdreamtech/frps](https://hub.docker.com/r/snowdreamtech/frps)
- [Docker Hub · stilleshan/frpc](https://hub.docker.com/r/stilleshan/frpc)
- [How to Implement External RDP Remote Control (frp)](https://example.com/link1)
- [Accessing Synology NAS using frp](https://example.com/link2)

[Link 1 Placeholder]  
[Link 2 Placeholder]

```

Note: I've retained the placeholders for the links labeled `> Original: <https://wiki-power.com/>` and `> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.`. Please replace them with the actual URLs as needed.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
```
