# Homelab - Herramienta Watchtower para Actualizar Automáticamente Contenedores Docker

![Imagen](https://media.wiki-power.com/img/202304092337531.png)

**Watchtower** es una herramienta que automatiza la actualización de todos o algunos de los contenedores Docker que elijas.

## Implementación (Docker Compose)

Para empezar, crea un archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si prefieres no utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `watchtower`).

```dotenv title=".env"
STACK_NAME=watchtower

# watchtower
APP_VERSION=latest
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar la orquestación de contenedores.

## Referencias y Agradecimientos

- [Sitio web / Documentación](https://containrrr.dev/watchtower)
- [Repositorio en GitHub](https://github.com/containrrr/watchtower/)
- [Docker Hub](https://hub.docker.com/r/containrrr/watchtower)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
