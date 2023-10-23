# Homelab - Servidor de Hogar Inteligente Home Assistant

![Imagen](https://img.wiki-power.com/d/wiki-media/img/202306011647498.png)

**Home Assistant** es un servidor de hogar inteligente de código abierto que permite monitorear todos los dispositivos en tu hogar. Tiene funcionalidades similares a las de Mi Home, una interfaz amigable y atractiva, y su despliegue es relativamente sencillo.

## Despliegue (Docker Compose)

En primer lugar, crea un archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # Ruta personalizada para almacenar el proyecto, por ejemplo, ./homeassistant

# homeassistant
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores orquestados.

## Instrucciones de Configuración

Puedes utilizar la aplicación oficial de Home Assistant en tu dispositivo móvil.

## Referencias y Agradecimientos

- [Sitio web oficial](https://www.home-assistant.io/)
- [Documentación](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [Repositorio en GitHub](https://github.com/home-assistant)
- [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [Sitio de demostración](https://demo.home-assistant.io/#/lovelace/0)

[por_sustituir[1]]
[por_sustituir[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.