# Homelab - Servidor de medios de cine y televisión Jellyfin

![Jellyfin](https://media.wiki-power.com/img/20230531213856.png)

**Jellyfin** es un servidor de medios de cine y televisión de código abierto que se utiliza para gestionar películas, programas de televisión y más. Permite la visualización y navegación en diferentes dispositivos, y se presenta como una alternativa de código abierto a software propietario como Emby y Plex.

## Implementación (Docker Compose)

En primer lugar, crea un archivo `compose.yaml` y pega el siguiente contenido:

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
    # Opcional - dirección alternativa utilizada para la autodescubrimiento
    #environment:
    #  - JELLYFIN_PublishedServerUrl=http://example.com
    # Opcional - puede ser necesario para que el chequeo de salud de Docker pase si se ejecuta en modo de red de host
    #extra_hosts:
    #  - "host.docker.internal:host-gateway"
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar directamente tus parámetros en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `jellyfin`).

```dotenv title=".env"
STACK_NAME=jellyfin
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./jellyfin
DATA_DIR=xxx # Ruta de almacenamiento de medios personalizada, por ejemplo, ./video

# jellyfin
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
```

Si tienes un NAS, también puedes montar el espacio de almacenamiento del NAS a través del protocolo NFS. Esto te permite almacenar tus medios en el NAS y ahorrar espacio en el servidor. Para obtener más detalles, consulta [**Linux: Montar un disco duro de Synology NAS para ampliar el espacio (NFS)**[por_reemplazar[3]]Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9C%BC%E6%89%A9%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/) .

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores según la configuración.

## Instrucciones de configuración

Puedes optar por utilizar la aplicación oficial de Jellyfin en dispositivos móviles.

## Referencias y Agradecimientos

- [Sitio web oficial](https://jellyfin.org/)
- [Documentación](https://jellyfin.org/docs/general/installation/container#using-docker-compose)
- [Repositorio en GitHub](https://github.com/jellyfin/jellyfin)
- [Docker Hub](https://hub.docker.com/r/jellyfin/jellyfin)
- [Sitio de demostración](https://demo.jellyfin.org/stable)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
