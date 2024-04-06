# Homelab - Herramienta de sincronización multiplataforma Syncthing

![Imagen](https://media.wiki-power.com/img/202304111529987.png)

**Syncthing** es una aplicación de sincronización de archivos de código abierto y gratuita que permite sincronizar archivos y carpetas entre múltiples dispositivos con soporte para sincronización incremental. Lo utilizo para respaldar los datos de mi servidor en un NAS y gestionarlos de manera centralizada.

## Implementación (Docker Compose)

En primer lugar, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  syncthing:
    container_name: ${STACK_NAME}_app
    image: syncthing/syncthing:${APP_VERSION}
    hostname: my-syncthing
    environment: # Debe ejecutarse con permisos de root para acceder a otros directorios de Docker o al directorio raíz del host
      - PUID=0
      - PGID=0
    volumes:
      - ${APP_SYNC_DIR}:/DATA
      - ${STACK_DIR}/config:/var/syncthing/config/
    ports:
      - ${APP_PORT}:8384 # Interfaz web
      - 22000:22000/tcp # Transferencia de archivos TCP
      - 22000:22000/udp # Transferencia de archivos QUIC
      - 21027:21027/udp # Recepción de transmisiones de descubrimiento local
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `syncthing`).

```dotenv title=".env"
STACK_NAME=syncthing
STACK_DIR=xxx # Ruta personalizada para almacenar el proyecto, por ejemplo, ./syncthing

# Syncthing
APP_VERSION=latest
APP_PORT=xxxx # Puerto personalizado para acceder, elige uno que no esté en uso
APP_SYNC_DIR=xxxx # Ruta personalizada que deseas sincronizar, por ejemplo, /DATA
```

Finalmente, ejecuta el comando `docker compose up -d` en el directorio que contiene `compose.yaml` para iniciar los contenedores definidos.

## Instrucciones de configuración

Si experimentas problemas de permisos, intenta cambiar los valores de `PUID` y `PGID` a `0` para ejecutarlo con permisos de root.

## Referencias y Agradecimientos

- [Sitio web oficial](https://syncthing.net/)
- [Documentación](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)
- [Foro](https://forum.syncthing.net/)
- [Repositorio de GitHub](https://github.com/syncthing/syncthing)
- [Docker Hub](https://hub.docker.com/r/syncthing/syncthing/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
