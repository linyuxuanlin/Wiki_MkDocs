# Homelab - Programa de lista de archivos con soporte para múltiples almacenamientos: Alist

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304141808001.png)

**Alist** es un programa de lista de archivos que admite varios métodos de almacenamiento, como local, Alibaba Cloud Drive, OneDrive, GoogleDrive, Baidu Netdisk, KuaiPan, Lanzou Cloud, S3, FTP / SFTP, etc., con un reproductor de video en línea y varios tipos de vista previa de archivos (compatible con Office, PDF, Markdown, etc.), y también tiene funciones de descarga sin conexión.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

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
    environment: # necesita ejecutarse con permisos de root, de lo contrario no podrá leer otros directorios de docker o el directorio raíz del host
      - PUID=0
      - PGID=0
      - UMASK=022
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `alist`).

```dotenv title=".env"
STACK_NAME=alist
STACK_DIR=xxx # ruta de almacenamiento personalizada del proyecto, por ejemplo, ./alist

# alist
APP_VERSION=latest
APP_PORT=xxxx # puerto de acceso personalizado, simplemente elija uno que no esté ocupado
```

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

La documentación oficial explica muy detalladamente cómo conectarse a varios tipos de almacenamiento. Solo siga la configuración paso a paso.

## Referencias y agradecimientos

- [Sitio web oficial](https://alist.nn.ci/)
- [Documentación](https://alist.nn.ci/guide/install/docker.html#release-version)
- [Repositorio de GitHub](https://github.com/alist-org/alist)
- [Docker Hub](https://hub.docker.com/r/xhofe/alist)
- [Sitio de demostración](https://al.nn.ci/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.