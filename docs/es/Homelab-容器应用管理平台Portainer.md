# Homelab - Plataforma de Gestión de Aplicaciones de Contenedores Portainer

![](https://media.wiki-power.com/img/202304111545899.png)

**Portainer** es una herramienta de gestión gráfica para aplicaciones de contenedores (incluyendo Docker, Docker Compose, Swarm y Kubernetes) que permite administrar entornos Docker a través de una interfaz web. También ofrece numerosas funcionalidades, como visualización de registros, inicio y detención de contenedores, gestión de imágenes, redes, y volúmenes, entre otras.

## Implementación (Docker Compose)

Para comenzar, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3.3"
services:
  portainer:
    container_name: ${STACK_NAME}_app
    image: portainer/portainer-ce:${APP_VERSION}
    ports:
      - ${APP_PORT_HTTP}:9000 # HTTP
    # - ${APP_PORT_HTTPS}:9443 # HTTPS (opcional)
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ${STACK_DIR}/portainer_data:/data
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si prefieres no utilizar variables de entorno, puedes personalizar directamente tus parámetros en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `portainer`).

```dotenv title=".env"
STACK_NAME=portainer
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./portainer

# portainer
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar la implementación de los contenedores.

## Notas de Configuración

Es importante tener en cuenta que la imagen de la versión comunitaria es `portainer/portainer-ce`, que se diferencia de la versión comercial (portainer-be).

## Referencias y Agradecimientos

- [Sitio web oficial](https://www.portainer.io/)
- [Documentación](https://docs.portainer.io/)
- [Repositorio en GitHub](https://github.com/portainer/portainer)
- [Docker Hub](https://hub.docker.com/r/portainer/portainer-ce)

[por_reemplazar[1]]
[por_reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
