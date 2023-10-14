# Homelab - Herramienta Watchtower para actualizar automáticamente contenedores Docker

![](https://img.wiki-power.com/d/wiki-media/img/202304092337531.png)

**Watchtower** es una herramienta para actualizar automáticamente todos o algunos contenedores Docker.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  watchtower:
    container_name: ${STACK_NAME}_app
    image: containrrr/watchtower:${APP_VERSION}
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `watchtower`).

```dotenv title=".env"
STACK_NAME=watchtower

# watchtower
APP_VERSION=latest
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Referencias y agradecimientos

- [Sitio web / Documentación oficial](https://containrrr.dev/watchtower)
- [Repositorio de GitHub](https://github.com/containrrr/watchtower/)
- [Docker Hub](https://hub.docker.com/r/containrrr/watchtower)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
