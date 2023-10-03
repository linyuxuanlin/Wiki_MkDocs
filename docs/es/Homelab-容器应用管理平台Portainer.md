# Homelab - Plataforma de gestión de aplicaciones de contenedores Portainer

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111545899.png)

**Portainer** es una herramienta de gestión gráfica de aplicaciones de contenedores (incluyendo Docker / Docker compose / Swarm / Kubernetes) que permite gestionar entornos Docker a través de una interfaz web. También ofrece muchas funciones como la visualización de registros, el inicio y detención de contenedores, la gestión de imágenes, redes, volúmenes, entre otros.

## Implementación (Docker Compose)

Primero, cree un archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `portainer`).

```dotenv title=".env"
STACK_NAME=portainer
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo ./portainer

# portainer
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Notas de configuración

Tenga en cuenta que la imagen de la versión comunitaria es `portainer/portainer-ce`, que se diferencia de la versión comercial (portainer-be).

## Referencias y agradecimientos

- [Sitio web oficial](https://www.portainer.io/)
- [Documentación](https://docs.portainer.io/)
- [Repositorio de GitHub](https://github.com/portainer/portainer)
- [Docker Hub](https://hub.docker.com/r/portainer/portainer-ce)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.