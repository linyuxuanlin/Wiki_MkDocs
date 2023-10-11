# Homelab - Alist, a file listing program that supports multiple storage options

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304141808001.png)

**Alist** is a file listing program that supports multiple storage options such as local, Alibaba Cloud, OneDrive, GoogleDrive, Baidu Cloud, Quark Cloud, Lanzou Cloud, S3, FTP/SFTP, etc. It comes with an online video player and various file preview options (compatible with Office, PDF, Markdown, etc.), as well as offline download functionality.

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
    environment: # Needs to be run with root permissions, otherwise it cannot read other docker directories or host root directories
      - PUID=0
      - PGID=0
      - UMASK=022
    restart: always
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (e.g., replace `${STACK_NAME}` with `alist`).

```dotenv title=".env"
STACK_NAME=alist
STACK_DIR=xxx # Customize your project storage path, e.g., ./alist

# alist
APP_VERSION=latest
APP_PORT=xxxx # Customize your access port, choose one that is not already in use
```

Finally, execute the command "docker compose up -d" in the same directory as the `compose.yaml` file to start the orchestrated containers.

## Configuration Instructions

The official documentation provides detailed instructions on how to configure various cloud storage services. Simply follow the steps provided in the documentation.

## References and Acknowledgments

- [Official Website](https://alist.nn.ci/)
- [Documentation](https://alist.nn.ci/guide/install/docker.html#release-version)
- [GitHub Repo](https://github.com/alist-org/alist)
- [Docker Hub](https://hub.docker.com/r/xhofe/alist)
- [Demo Site](https://al.nn.ci/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
