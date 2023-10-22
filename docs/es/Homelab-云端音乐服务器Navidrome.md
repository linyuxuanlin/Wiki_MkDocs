# Homelab - Servidor de música en la nube Navidrome

![](https://img.wiki-power.com/d/wiki-media/img/20230531212854.png)

**Navidrome** es un servidor de música y streaming basado en web de código abierto que te permite almacenar tu propia música y escucharla en varios clientes.

## Implementación (Docker Compose)

Primero, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  navidrome:
    container_name: ${STACK_NAME}_app
    image: deluan/navidrome:${APP_VERSION}
    user: 1000:1000 # Si tienes problemas de permisos, puedes intentar implementar como root (0:0)
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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `navidrome`).

```dotenv title=".env"
STACK_NAME=navidrome
STACK_DIR=xxx # Ruta de almacenamiento personalizada para tu proyecto, por ejemplo, ./navidrome
DATA_DIR=xxx # Ruta de almacenamiento personalizada para tu música, por ejemplo, ./music

# navidrome
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
```

Si tienes un NAS, también puedes montar el espacio de almacenamiento en tu NAS a través del protocolo NFS para guardar tu música en el NAS y ahorrar espacio en el servidor. Para obtener más detalles, consulta [**Montar un disco duro Synology NAS en Linux para ampliar el espacio (NFS)**](https://www.navidrome.org/docs/installation/docker/) (Reemplaza ](https://wiki-power.com/es/ por el enlace correcto).

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores que has definido.

## Instrucciones de configuración

Hay muchas opciones de aplicaciones móviles para elegir. En Android, la aplicación que mejor funciona en mi experiencia es substreamer. Para obtener más aplicaciones, consulta la lista oficial en [**Aplicaciones**](https://www.navidrome.org/docs/overview/#apps).

## Referencias y Agradecimientos

- [Sitio web oficial](https://www.navidrome.org/)
- [Documentación](https://www.navidrome.org/docs/installation/docker/)
- [Repositorio de GitHub](https://github.com/navidrome/navidrome/)
- [Docker Hub](https://hub.docker.com/r/deluan/navidrome)
- [Sitio de demostración](https://demo.navidrome.org/app/) (usuario y contraseña: demo)

[Por reemplazar[1]]
[Por reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.