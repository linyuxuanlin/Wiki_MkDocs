# Homelab - File Listing Program Alist with Multi-Storage Support

![Alist](https://media.wiki-power.com/img/202304141808001.png)

**Alist** is a file listing program that supports various storage options such as local storage, Alibaba Cloud Drive, OneDrive, Google Drive, Baidu NetDisk, Kuake NetDisk, Lanzou Cloud, S3, FTP/SFTP, and more. It comes with an online video player, supports various file previews (including Office, PDF, Markdown, and others), and offers offline download functionality.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.3"
services:
  alist:
    container_name: ${STACK_NAME}_app
    image: "xhofe/alist:${APP_VERSION}"
    volumes:
      - ${STACK_DIR}:/opt/alist/data
    ports:
      - ${APP_PORT}:5244
    environment: # It needs to run with root privileges; otherwise, it cannot access other Docker directories or the host machine's root directory
      - PUID=0
      - PGID=0
      - UMASK=022
    restart: always
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters in `compose.yaml` (e.g., replace `${STACK_NAME}` with `alist`).

```dotenv title=".env"
STACK_NAME=alist
STACK_DIR=xxx # Customize your project storage path, e.g., ./alist

# Alist
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not already in use
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Details

The methods for connecting to various cloud storage services are well-documented on the official website. Simply follow the configuration steps as outlined in the official documentation.

## References and Acknowledgments

- [Official Website](https://alist.nn.ci/)
- [Documentation](https://alist.nn.ci/guide/install/docker.html#release-version)
- [GitHub Repository](https://github.com/alist-org/alist)
- [Docker Hub](https://hub.docker.com/r/xhofe/alist)
- [Demo Site](https://al.nn.ci/)

[1]  
[2]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
