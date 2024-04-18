# Homelab - Tool for Intranet Penetration frp

![](https://media.wiki-power.com/img/20230304195137.png)

**frp** is a method for intranet penetration. You can expose the ports of your intranet hosts to the internet through a server with a public IP. frp supports various protocols such as TCP, UDP, HTTP, and HTTPS.

## Deploying the server-side frps (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  frps:
    container_name: ${STACK_NAME}_app
    image: fatedier/frps:${APP_VERSION}
    network_mode: host
    volumes:
      - ${STACK_DIR}/frps.toml:/etc/frp/frps.toml
    command: "-c /etc/frp/frps.toml"
    restart: always
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can also directly customize your parameters in `compose.yaml` (for example, replace `${STACK_NAME}` with `frps`).

```dotenv title=".env"
STACK_NAME=frps
STACK_DIR=/DATA/AppData/frps # Customize the project storage path, for example, ./frps

# frps
APP_VERSION=v0.56.0
```

Add a configuration file `frps.ini` in your project storage path `${STACK_DIR}`:

```toml title="frpc.toml"
bindAddr = "0.0.0.0"
bindPort = 7000 # The frp port open on the server, which must match the settings of frpc later

kcpBindPort = 7000

transport.maxPoolCount = 5

webServer.addr = "0.0.0.0" # Address of the panel, must be 0.0.0.0 for external access
webServer.port = 7500 # Port of the frps panel
webServer.user = "xxxxxx" # Panel username
webServer.password = "xxxxxx" # Password

auth.method = "token"
auth.token = "xxxxxx" # Custom token, which must match frpc

allowPorts = [
  { start = 2000, end = 3000 },
  { single = 3001 },
  { single = 3003 },
  { start = 4000, end = 50000 }
]
```

Finally, run the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated container.

If you prefer not to use Docker, you can also refer to this article: [**Server Configuration·How to achieve external RDP remote control (frp)**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#_2).

## Deploying the client-side frpc (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  frpc:
    container_name: ${STACK_NAME}_app
    image: fatedier/frpc:${APP_VERSION}
    network_mode: host
    volumes:
      - ${STACK_DIR}/frpc.toml:/etc/frp/frpc.toml
    command: "-c /etc/frp/frpc.toml"
    restart: always
```

（Optional）It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters in `compose.yaml` (e.g., replace `${STACK_NAME}` with `frpc`).

```dotenv title=".env"
STACK_NAME=frpc
STACK_DIR=/DATA/AppData/frpc # Customize your project storage path, e.g., ./frpc

# frpc
APP_VERSION=v0.56.0
```

Add a configuration file `frps.toml` in your project storage path `${STACK_DIR}`:

```toml title="frpc.toml"
user = "client-device-1" # Current device name

serverAddr = xx.xx.xx.xx # Public IP of the server
serverPort = 7000 # frp port opened by the server, should match the settings in frps

auth.method = "token"
auth.token = "xxxxxx" # Should match the settings in frps

transport.poolCount = 5

[[proxies]]
name = "app-name" # Application name
type = "tcp"
remotePort = xx # Public access port number
localIP = "127.0.0.1"
localPort = xx # Local port number
```

Finally, run the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Notes

Please make sure that the Toml files are correctly formatted, otherwise the services cannot be started properly. You can use an online Toml editor and validator to check.

## References and Acknowledgements

- [GitHub repo · fatedier/frp](https://github.com/fatedier/frp)
- [GitHub repo · snowdreamtech/frps](https://github.com/snowdreamtech/frp)
- [GitHub repo · stilleshan/frpc](https://github.com/stilleshan/frpc)
- [Docker Hub · snowdreamtech/frps](https://hub.docker.com/r/snowdreamtech/frps)
- [Docker Hub · stilleshan/frpc](https://hub.docker.com/r/stilleshan/frpc)
- [How to implement external RDP remote control (frp)](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [Access Synology NAS using frp](https://wiki-power.com/%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.