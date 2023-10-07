# Homelab - Online Code Editor code-server

![](https://f004.backblazeb2.com/file/wiki-media/img/202304132214418.png)

**code-server** is a VS Code that can run in a browser. Compared to the desktop version, the advantage is that you can code online with any device, including devices such as mobile phones and tablets that cannot directly install VS Code.

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
    environment: # needs to be run with root privileges, otherwise cannot read other docker directories or host root directories
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} #optional
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} #optional
      #- SUDO_PASSWORD_HASH= #optional
      #- PROXY_DOMAIN=code.wiki-power.com #optional
    restart: unless-stopped
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `code-server`).

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # Custom project storage path, such as ./code-server
DATA_DIR_LOCAL=xxx # Custom mount local directory, such as /DATA

# code-server
APP_VERSION=latest
APP_PORT=xxxx # Custom access port, choose one that is not occupied
APP_PASSWORD=xxx # Login password
APP_SUDO_PASSWORD=xxx # Superuser password

```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration Instructions

### Configure Git

After installation, if you need to use Git, please refer to the article [**Git Learning Notes**](https://wiki-power.com/en/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE) for initializing configuration of username and email.

### Read and Write Permission Issues

If you encounter the `Error: EACCES: permission denied` error when operating files, you can open the terminal and enter the following command to grant ownership to the current user:

```shell
sudo chown -R username folder_path
```

For example, the following is the operation of giving ownership of the current directory to the `abc` user:

```shell
sudo chown -R abc .
```

### Set Root Account Password

If you need to use the root account, you can use the following command to initialize its password:

```shell
sudo passwd root
```

## Reference and Acknowledgement

- [Official website](https://coder.com/docs/code-server/latest)
- [Documentation / GitHub repo](https://github.com/linuxserver/docker-code-server)
- [Docker Hub](https://hub.docker.com/r/linuxserver/code-server)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.