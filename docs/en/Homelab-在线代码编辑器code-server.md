# Homelab - Online Code Editor code-server

![](https://media.wiki-power.com/img/202304132214418.png)

**code-server** is a browser-based version of VS Code. The advantage over the desktop version is that you can code online with any device, including devices like smartphones and tablets that cannot directly install VS Code.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "2.1"
services:
  code-server:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/linuxserver/code-server:${APP_VERSION}
    ports:
      - ${APP_PORT}:8443
    volumes:
      - ${STACK_DIR}/config:/config
      - ${DATA_DIR_LOCAL}:/DATA
    environment: # Need to run as root to read other docker directories or host root directory
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} #optional
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} #optional
      #- SUDO_PASSWORD_HASH= #optional
      #- PROXY_DOMAIN=code.wiki-power.com #optional
      #- DOCKER_MODS=linuxserver/mods:code-server-python3 #optional, if you want to add a python environment
    restart: unless-stopped
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you don't want to use environment variables, you can directly customize your parameters in `compose.yaml` (e.g., replace `${STACK_NAME}` with `code-server`).

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # Custom project storage path, e.g., ./code-server
DATA_DIR_LOCAL=xxx # Custom mount local directory, e.g., /DATA

# code-server
APP_VERSION=latest
APP_PORT=xxxx # Custom access port, choose one that is not occupied
APP_PASSWORD=xxx # Login password
APP_SUDO_PASSWORD=xxx # Superuser password
```

Finally, execute the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration Instructions

### Configure git

After installation, if you need to use Git and initialize the configuration for username and email, please refer to the article [**Git Learning Notes**](https://wiki-power.com/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE).

### Read and write permission issues

If you encounter an `Error: EACCES: permission denied` error when operating files, you can open the terminal and enter the following command to grant ownership to the current user:

```shell
sudo chown -R username folder_path
```

For example, the following command grants ownership of the current directory to the user `abc`:

```shell
sudo chown -R abc .
```

### Setting the root account password

If you need to use the root account, you can initialize its password using the following command:

```shell
sudo passwd root
```

## References and Acknowledgements

- [Official Website](https://coder.com/docs/code-server/latest)
- [Documentation / GitHub repo](https://github.com/linuxserver/docker-code-server)
- [Docker Hub](https://hub.docker.com/r/linuxserver/code-server)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
