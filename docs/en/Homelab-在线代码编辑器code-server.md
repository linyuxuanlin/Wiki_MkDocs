# Homelab - Online Code Editor code-server

![](https://img.wiki-power.com/d/wiki-media/img/202304132214418.png)

**code-server** is a browser-based version of VS Code. Its advantage over the desktop version is that you can code online with any device, including mobile phones and tablets, which cannot directly install VS Code.

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
    environment: # Needs to run with root permissions, otherwise it won't be able to access other Docker directories or the host machine's root directory
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} #optional
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} #optional
      #- SUDO_PASSWORD_HASH= #optional
      #- PROXY_DOMAIN=code.wiki-power.com #optional
    restart: unless-stopped
```

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you don't want to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `code-server`).

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # Customize your project storage path, e.g., ./code-server
DATA_DIR_LOCAL=xxx # Customize the local directory to be mounted, e.g., /DATA

# code-server
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that's not already in use
APP_PASSWORD=xxx # Login password
APP_SUDO_PASSWORD=xxx # Superuser password
```

Finally, in the same directory as `compose.yaml`, run the `docker compose up -d` command to start the orchestrated container.

## Configuration Notes

### Configuring Git

After installation, if you need to use Git and initialize your username and email, please refer to the article [**Git Study Notes**](https://wiki-power.com/en/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BDAE).

### Permissions Issues

If you encounter an `Error: EACCES: permission denied` error when working with files, you can open a terminal and use the following command to grant ownership to the current user:

```shell
sudo chown -R username folder_path
```

For example, the following command gives ownership of the current directory to the user `abc`:

```shell
sudo chown -R abc .
```

### Setting the Root Password

If you need to use the root account, you can initialize its password using the following command:

```shell
sudo passwd root
```

## References and Acknowledgments

- [Official Website](https://coder.com/docs/code-server/latest)
- [Documentation / GitHub Repository](https://github.com/linuxserver/docker-code-server)
- [Docker Hub](https://hub.docker.com/r/linuxserver/code-server)

[Link 1](https://coder.com/docs/code-server/latest)
[Link 2](https://github.com/linuxserver/docker-code-server)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.