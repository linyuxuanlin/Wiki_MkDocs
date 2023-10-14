# Homelab - Servidor de música en la nube Navidrome

![](https://img.wiki-power.com/d/wiki-media/img/20230531212854.png)

**Navidrome** es un servidor de música y streaming basado en web de código abierto, donde puedes almacenar tu propia música y escucharla en múltiples clientes.

## Despliegue (Docker Compose)

Primero, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  navidrome:
    container_name: ${STACK_NAME}_app
    image: deluan/navidrome:${APP_VERSION}
    user: 1000:1000 # Si hay problemas de permisos, intenta desplegar como root (0:0)
    ports:
      - "${APP_PORT}:4533"
    environment:
      # Opcional: personaliza tus opciones de configuración aquí. Ejemplos:
      ND_SCANSCHEDULE: 24h
      ND_LOGLEVEL: info
      ND_SESSIONTIMEOUT: 24h
      ND_BASEURL: ""
    volumes:
      - ${STACK_DIR}:/data
      - ${DATA_DIR}:/music:ro
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `navidrome`).

```dotenv title=".env"
STACK_NAME=navidrome
STACK_DIR=xxx # Personaliza la ruta de almacenamiento del proyecto, por ejemplo ./navidrome
DATA_DIR=xxx # Personaliza la ruta de almacenamiento de la música, por ejemplo ./music

# navidrome
APP_VERSION=latest
APP_PORT=xxxx # Personaliza el puerto de acceso, elige uno que no esté en uso
```

Si tienes un NAS, también puedes montar el espacio de almacenamiento del NAS a través del protocolo NFS, almacenar la música en el NAS para ahorrar espacio en el servidor. Para más detalles, consulta [**Montar un disco duro de expansión de espacio NAS Synology en Linux (NFS)**](https://wiki-power.com/es/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Por último, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Hay muchas opciones de aplicación móvil, en Android, la que mejor experiencia me ha dado es substreamer. Para más aplicaciones, consulta la lista oficial en [**Apps**](https://www.navidrome.org/docs/overview/#apps).

## Referencias y agradecimientos

- [Sitio web oficial](https://www.navidrome.org/)
- [Documentación](https://www.navidrome.org/docs/installation/docker/)
- [Repositorio de GitHub](https://github.com/navidrome/navidrome/)
- [Docker Hub](https://hub.docker.com/r/deluan/navidrome)
- [Sitio de demostración](https://demo.navidrome.org/app/) (nombre de usuario y contraseña son demo)

a_ser_reemplazado[1]
a_ser_reemplazado[2]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
