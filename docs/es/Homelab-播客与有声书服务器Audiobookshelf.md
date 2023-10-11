# Homelab - Servidor de podcasts y audiolibros Audiobookshelf

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230531204505.png)

**Audiobookshelf** es un servidor de podcasts y audiolibros autohospedado que permite buscar fácilmente podcasts, detectar actualizaciones y descargarlos automáticamente, y organizarlos automáticamente.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3.7"
services:
  audiobookshelf:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/advplyr/audiobookshelf:${APP_VERSION}
    ports:
      - ${APP_PORT}:80
    volumes:
      - ${STACK_DIR}/audiobooks:/audiobooks
      - ${STACK_DIR}/config:/config
      - ${STACK_DIR}/metadata:/metadata
      - ${DATA_DIR}:/podcasts
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=audiobookshelf
STACK_DIR=xxx # Personalice la ruta de almacenamiento del proyecto, por ejemplo, ./audiobookshelf
DATA_DIR=xxx # Personalice la ruta de almacenamiento de podcasts, por ejemplo, ./podcast

# audiobookshelf
APP_VERSION=latest
APP_PORT=xxxx # Personalice el puerto de acceso, elija uno que no esté en uso
```

Si tiene un NAS, también puede montar el espacio de almacenamiento en el NAS a través del protocolo NFS, almacenar los podcasts en el NAS para ahorrar espacio en el servidor. Para obtener más detalles, consulte [**Cómo montar un disco duro de NAS Synology en Linux (NFS)**](https://wiki-power.com/es/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Aplicación móvil: hay una aplicación oficial disponible para iOS y Android que se puede utilizar directamente.

## Referencias y agradecimientos

- [Sitio web oficial](https://www.audiobookshelf.org/)
- [Documentación](https://www.audiobookshelf.org/docs#docker-compose-install)
- [Repositorio de GitHub](https://github.com/advplyr/audiobookshelf)
- [Docker Hub](https://hub.docker.com/r/advplyr/audiobookshelf)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
