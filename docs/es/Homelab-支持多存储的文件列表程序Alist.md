# Homelab - Programa de listado de archivos Alist con soporte para múltiples sistemas de almacenamiento

![Imagen](https://media.wiki-power.com/img/202304141808001.png)

**Alist** es un programa de listado de archivos que admite varias opciones de almacenamiento, como local, Alibaba Cloud Drive, OneDrive, Google Drive, Baidu Cloud Drive, Kuake Cloud, Lanzou Cloud, S3, FTP/SFTP, entre otros. También cuenta con un reproductor de vídeo en línea y una variedad de funciones de vista previa de archivos (compatible con Office, PDF, Markdown, etc.), así como capacidades de descarga sin conexión.

## Implementación (Docker Compose)

En primer lugar, cree un archivo `compose.yaml` y pegue el siguiente contenido:

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
    environment: # Debe ejecutarse con permisos de root, de lo contrario no podrá acceder a otros directorios de Docker o al directorio raíz del host
      - PUID=0
      - PGID=0
      - UMASK=022
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar directamente los parámetros en `compose.yaml` (por ejemplo, sustituyendo `${STACK_NAME}` por `alist`).

```dotenv title=".env"
STACK_NAME=alist
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./alist

# alist
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores definidos en la configuración.

## Instrucciones de configuración

La documentación oficial proporciona instrucciones detalladas para integrar con varios servicios de almacenamiento. Simplemente siga los pasos de configuración que se describen en la documentación.

## Referencias y Agradecimientos

- [Sitio web oficial](https://alist.nn.ci/)
- [Documentación](https://alist.nn.ci/guide/install/docker.html#release-version)
- [Repositorio en GitHub](https://github.com/alist-org/alist)
- [Docker Hub](https://hub.docker.com/r/xhofe/alist)
- [Sitio de demostración](https://al.nn.ci/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
