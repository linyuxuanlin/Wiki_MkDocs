# Homelab - Cloudreve, a Public Cloud Image Hosting System Supporting Multiple Cloud Providers

![Cloudreve](https://media.wiki-power.com/img/20230304195423.png)

**Cloudreve** is a public cloud file system that supports multiple cloud storage providers, including local storage, remote hosts, Qiniu, Alibaba Cloud OSS, Tencent Cloud COS, UpYun, OneDrive, and S3-compatible protocols as storage endpoints. It can also be integrated with Aria2 for offline downloads, supports multiple users, drag-and-drop uploads/management, online preview/editing, WebDAV, and more. It is typically used for personal image hosting or web-based file management.

## Deployment (Docker Compose)

To begin, create the directory structure. Navigate to the directory where you want to store Cloudreve (e.g., `/DATA/AppData/cloudreve`) and execute the following commands:

```shell
mkdir -vp cloudreve/{uploads,avatar,data} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db \
&& mkdir -p aria2/config \
&& mkdir -p cloudreve/data/aria2 \
&& chmod -R 777 cloudreve/data/aria2 \
&& mkdir data
```

Next, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.8"
services:
  cloudreve:
    container_name: ${STACK_NAME}_app
    image: cloudreve/cloudreve:${APP_VERSION}
    ports:
      - "${APP_PORT}:5212"
    volumes:
      - temp_data:/data
      - ${STACK_DIR}/cloudreve/uploads:/cloudreve/uploads
      - ${STACK_DIR}/cloudreve/conf.ini:/cloudreve/conf.ini
      - ${STACK_DIR}/cloudreve/cloudreve.db:/cloudreve/cloudreve.db
      - ${STACK_DIR}/cloudreve/avatar:/cloudreve/avatar
    restart: unless-stopped
    depends_on:
      - aria2
  aria2:
    container_name: ${STACK_NAME}_aria2
    image: p3terx/aria2-pro:${ARIA2_VERSION}
    volumes:
      - ${STACK_DIR}/aria2/config:/config
      - ${STACK_DIR}/data:/var/lib/docker/volumes/cloudreve_temp_data/_data
    environment:
      - RPC_SECRET=${ARIA2_RPC_SECRET}
      - RPC_PORT=${ARIA2_RPC_PORT}
    restart: unless-stopped
volumes:
  temp_data:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/temp_data
      o: bind
```

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `cloudreve`).

```dotenv title=".env"
STACK_NAME=cloudreve
STACK_DIR=xxx # Custom project storage path, e.g., ./cloudreve

# cloudreve
APP_VERSION=latest
APP_PORT=xxxx # Custom access port, choose one that is not in use

# aria2
ARIA2_VERSION=latest
ARIA2_RPC_SECRET=xxx # ARIA2 password
ARIA2_RPC_PORT=6800
```

Finally, execute the `docker compose up -d` command in the same directory as the `compose.yaml` to start the orchestrated containers.

## Configuration Notes

Upon the initial launch, an initial admin account will be created automatically, and you can find it in the logs. If you miss it, delete the `cloudreve.db` in the directory and restart the main program to initialize a new admin account.

I adhere to the image naming convention: `{year}{month}{day}{hour}{minute}{second}{ext}`.

## References and Acknowledgments

- [Official Website](https://docs.cloudreve.org/)
- [Documentation](https://docs.cloudreve.org/getting-started/install#docker-compose)
- [Forum](https://forum.cloudreve.org/)
- [GitHub Repository](https://github.com/cloudreve/Cloudreve)
- [Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)
- [Demo Site](https://demo.cloudreve.org/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

```

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
```
