# Homelab - Servidor de hogar inteligente Home Assistant

![](https://f004.backblazeb2.com/file/wiki-media/img/202306011647498.png)

**Home Assistant** es un servidor de hogar inteligente de código abierto que puede monitorear todos los dispositivos de su hogar. Tiene funciones similares a Mi Home y una interfaz amigable y atractiva, y su implementación es relativamente sencilla.

## Implementación (Docker Compose)

Primero, cree un archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  homeassistant:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/home-assistant/home-assistant:${APP_VERSION}
    ports:
      - ${APP_PORT}:8123
    volumes:
      - ${STACK_DIR}:/config
      - /etc/localtime:/etc/localtime:ro
    privileged: true
    #network_mode: host
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplace `${STACK_NAME}` con `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # Personalice la ruta de almacenamiento del proyecto, por ejemplo, ./homeassistant

# homeassistant
APP_VERSION=latest
APP_PORT=xxxx # Personalice el puerto de acceso, simplemente elija uno que no esté ocupado
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

La aplicación móvil se puede utilizar directamente con la aplicación oficial de Home Assistant.

## Referencias y agradecimientos

- [Sitio web oficial](https://www.home-assistant.io/)
- [Documentación](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [Repositorio de GitHub](https://github.com/home-assistant)
- [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [Sitio de demostración](https://demo.home-assistant.io/#/lovelace/0)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.