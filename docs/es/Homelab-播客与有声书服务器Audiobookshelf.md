# Homelab - Servidor de Podcasts y Audiolibros Audiobookshelf

![](https://img.wiki-power.com/d/wiki-media/img/20230531204505.png)

**Audiobookshelf** es un servidor de podcasts y audiolibros autohospedado que facilita la búsqueda, la detección automática de actualizaciones y la descarga de podcasts, además de organizarlos automáticamente.

## Implementación (Docker Compose)

Comienza por crear un archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazando `${STACK_NAME}` por `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=audiobookshelf
STACK_DIR=xxx # Personaliza la ruta de almacenamiento de tu proyecto, por ejemplo, ./audiobookshelf
DATA_DIR=xxx # Personaliza la ruta de almacenamiento de tus podcasts, por ejemplo, ./podcast

# audiobookshelf
APP_VERSION=latest
APP_PORT=xxxx # Personaliza el puerto de acceso, elige uno que no esté en uso
```

Si tienes un NAS, también puedes montar el espacio de almacenamiento de tu NAS a través del protocolo NFS y guardar tus podcasts en el NAS para ahorrar espacio en tu servidor. Para obtener más detalles, consulta [**Cómo montar un disco duro de Synology NAS en Linux para ampliar el espacio (NFS)**](https://wiki-power.com/es/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9C%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/) (en inglés).

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores en el entorno de Docker.

## Configuración

Aplicación móvil: Hay aplicaciones oficiales disponibles para iOS y Android que puedes utilizar directamente.

## Referencias y Agradecimientos

- [Sitio web oficial](https://www.audiobookshelf.org/)
- [Documentación](https://www.audiobookshelf.org/docs#docker-compose-install)
- [Repositorio en GitHub](https://github.com/advplyr/audiobookshelf)
- [Docker Hub](https://hub.docker.com/r/advplyr/audiobookshelf)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.