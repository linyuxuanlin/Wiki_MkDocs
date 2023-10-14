# Homelab - Cloudreve, a Public Cloud Image Hosting System that Supports Multiple Cloud Storage Providers

![](https://img.wiki-power.com/d/wiki-media/img/20230304195423.png)

**Cloudreve** is a public cloud file system that supports multiple cloud storage drivers. It supports local, secondary, Qiniu, Alibaba Cloud OSS, Tencent Cloud COS, Upyun, OneDrive, S3 compatible protocols as storage endpoints, and can be integrated with Aria2 offline download, multi-user, drag-and-drop upload/management, online preview/editing, WebDAV, etc. The typical use case is personal image hosting or cloud file management.

## Deployment (Docker Compose)

First, we need to create the directory structure. Switch to the directory where Cloudreve is stored (e.g. `/DATA/AppData/cloudreve`) and execute:

```shell
mkdir -vp cloudreve/{uploads,avatar,data} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db \
&& mkdir -p aria2/config \
&& mkdir -p cloudreve/data/aria2 \
&& chmod -R 777 cloudreve/data/aria2 \
&& mkdir data
```

First, create the `compose.yaml` file and paste the following content:

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

The above code is a YAML file for a Docker Compose configuration. It defines two services, `cloudreve` and `aria2`, which are containers that run the Cloudreve and Aria2 applications respectively. The `cloudreve` service is dependent on the `aria2` service.

The `cloudreve` service is configured to use the `cloudreve/cloudreve` Docker image with the version specified by the `APP_VERSION` environment variable. It exposes port `5212` on the host machine and mounts several volumes for data storage and configuration. The `restart` policy is set to `unless-stopped`.

The `aria2` service is configured to use the `p3terx/aria2-pro` Docker image with the version specified by the `ARIA2_VERSION` environment variable. It mounts volumes for configuration and data storage, and sets environment variables for the RPC secret and port. The `restart` policy is also set to `unless-stopped`.

Finally, a volume named `temp_data` is defined with a local driver and mounted to the `cloudreve` service for temporary data storage.

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `cloudreve`).

```dotenv title=".env"
STACK_NAME=cloudreve
STACK_DIR=xxx # Customize the project storage path, such as ./cloudreve

# cloudreve
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied

# aria2
ARIA2_VERSION=latest
ARIA2_RPC_SECRET=xxx # ARIA2 password
ARIA2_RPC_PORT=6800
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

When starting for the first time, an initial administrator account will be created automatically, which can be found in the log. If you miss it, please delete the `cloudreve.db` file in the directory and restart the main program to initialize a new administrator account.

I use the image naming convention: `{year}{month}{day}{hour}{minute}{second}{ext}`.

## References and Acknowledgments

- [Official Website](https://docs.cloudreve.org/)
- [Documentation](https://docs.cloudreve.org/getting-started/install#docker-compose)
- [Forum](https://forum.cloudreve.org/)
- [GitHub repo](https://github.com/cloudreve/Cloudreve)
- [Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)
- [Demo site](https://demo.cloudreve.org/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
