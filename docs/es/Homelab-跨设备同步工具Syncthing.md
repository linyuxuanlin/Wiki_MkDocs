# Homelab - Herramienta de sincronización multi-dispositivo Syncthing

![](https://img.wiki-power.com/d/wiki-media/img/202304111529987.png)

**Syncthing** es una aplicación de sincronización de archivos de código abierto y gratuita que permite sincronizar archivos y carpetas entre múltiples dispositivos, con soporte para sincronización incremental. Lo uso para hacer copias de seguridad de los datos del servidor en mi NAS y gestionarlos de manera centralizada.

## Implementación (Docker Compose)

Primero, cree un archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  syncthing:
    container_name: ${STACK_NAME}_app
    image: syncthing/syncthing:${APP_VERSION}
    hostname: my-syncthing
    environment: # Necesita ejecutarse con permisos de root, de lo contrario no podrá leer otros directorios de Docker o el directorio raíz del host
      - PUID=0
      - PGID=0
    volumes:
      - ${APP_SYNC_DIR}:/DATA
      - ${STACK_DIR}/config:/var/syncthing/config/
    ports:
      - ${APP_PORT}:8384 # Interfaz web
      - 22000:22000/tcp # Transferencias de archivos TCP
      - 22000:22000/udp # Transferencias de archivos QUIC
      - 21027:21027/udp # Recibir difusiones de descubrimiento local
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `syncthing`).

```dotenv title=".env"
STACK_NAME=syncthing
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo ./syncthing

# syncthing
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
APP_SYNC_DIR=xxxx # Ruta personalizada que desea sincronizar, por ejemplo /DATA
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Si recibe un mensaje de error de permisos insuficientes, intente cambiar los valores de `PUID` y `PGID` a `0` y ejecutarlo con permisos de root.

## Referencias y agradecimientos

- [Sitio web oficial](https://syncthing.net/)
- [Documentación](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)
- [Foro](https://forum.syncthing.net/)
- [Repositorio de GitHub](https://github.com/syncthing/syncthing)
- [Docker Hub](https://hub.docker.com/r/syncthing/syncthing/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
