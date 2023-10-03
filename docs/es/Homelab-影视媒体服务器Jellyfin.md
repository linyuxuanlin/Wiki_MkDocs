# Homelab - Servidor de medios de cine y televisión Jellyfin

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230531213856.png)

**Jellyfin** es un servidor de medios de cine y televisión de código abierto que se puede utilizar para administrar películas, programas de televisión, etc. y verlos en diferentes dispositivos. Puede ser utilizado como alternativa a los software propietarios Emby y Plex.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3.5"
services:
  jellyfin:
    container_name: ${STACK_NAME}_app
    image: jellyfin/jellyfin:${APP_VERSION}
    #user: uid:gid
    #network_mode: 'host'
    ports:
      - ${APP_PORT}:8096
    volumes:
      - ${STACK_DIR}/config:/config
      - ${STACK_DIR}/cache:/cache
      - ${DATA_DIR}:/media
    restart: "unless-stopped"
    # Optional - alternative address used for autodiscovery
    #environment:
    #  - JELLYFIN_PublishedServerUrl=http://example.com
    # Optional - may be necessary for docker healthcheck to pass if running in host network mode
    #extra_hosts:
    #  - "host.docker.internal:host-gateway"
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `jellyfin`).

```dotenv title=".env"
STACK_NAME=jellyfin
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./jellyfin
DATA_DIR=xxx # Ruta personalizada de almacenamiento de videos, por ejemplo, ./video

# jellyfin
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, simplemente elija uno que no esté en uso
```

Si tiene un NAS, también puede montar el espacio de almacenamiento en el NAS a través del protocolo NFS, almacenar la música en el NAS para ahorrar espacio en el servidor. Para obtener más detalles, consulte [**Montar el disco duro de expansión del NAS Synology en Linux (NFS)**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar el contenedor.

## Instrucciones de configuración

La aplicación móvil se puede descargar desde la tienda de aplicaciones oficial de Jellyfin.

## Referencias y agradecimientos

- [Sitio web oficial](https://jellyfin.org/)
- [Documentación](https://jellyfin.org/docs/general/installation/container#using-docker-compose)
- [Repositorio de GitHub](https://github.com/jellyfin/jellyfin)
- [Docker Hub](https://hub.docker.com/r/jellyfin/jellyfin)
- [Sitio de demostración](https://demo.jellyfin.org/stable)

a_ser_reemplazado[1]  
a_ser_reemplazado[2]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.