# Homelab - Sistema de almacenamiento en la nube Cloudreve compatible con servicios de nube pública

![Cloudreve](https://media.wiki-power.com/img/20230304195423.png)

**Cloudreve** es un sistema de almacenamiento en la nube público que admite múltiples controladores de almacenamiento en la nube. Es compatible con almacenamiento local, remoto, Qiniu, Alibaba Cloud OSS, Tencent Cloud COS, UpYun, OneDrive, protocolos compatibles con S3 y permite la integración con Aria2 para descargas fuera de línea. También admite múltiples usuarios, carga y gestión de archivos mediante arrastrar y soltar, vista previa y edición en línea, WebDAV, entre otras características. Su uso típico incluye la creación de un repositorio de imágenes personales o la gestión de archivos en la nube.

## Implementación (Docker Compose)

Primero, es necesario crear una estructura de directorios. Cambie al directorio donde se encuentra Cloudreve (por ejemplo, `/DATA/AppData/cloudreve`) y ejecute el siguiente comando:

```shell
mkdir -vp cloudreve/{uploads,avatar,data} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db \
&& mkdir -p aria2/config \
&& mkdir -p cloudreve/data/aria2 \
&& chmod -R 777 cloudreve/data/aria2 \
&& mkdir data
```

Luego, cree un archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` para personalizar sus variables de entorno. Si no desea utilizar variables de entorno, puede personalizar directamente sus parámetros en `compose.yaml` (por ejemplo, sustituir `${STACK_NAME}` por `cloudreve`).

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

Finally, execute the `docker compose up -d` command in the same directory as the `compose.yaml` file to start the orchestrated containers.

## Configuration Instructions

Upon initial startup, an administrator account will be created automatically, and you can find the details in the log. If you miss it, please delete the `cloudreve.db` file in the directory and restart the main program to initialize a new administrator account.

I use the following image naming convention: `{year}{month}{day}{hour}{minute}{second}{ext}`.

## References and Acknowledgments

- [Official Website](https://docs.cloudreve.org/)
- [Documentation](https://docs.cloudreve.org/getting-started/install#docker-compose)
- [Forum](https://forum.cloudreve.org/)
- [GitHub Repository](https://github.com/cloudreve/Cloudreve)
- [Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)
- [Demo Site](https://demo.cloudreve.org/)

[Por reemplazar[1]]
[Por reemplazar[2]]

```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
