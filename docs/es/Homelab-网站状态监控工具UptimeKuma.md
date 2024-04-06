# Homelab - Herramienta de monitoreo de estado de sitios web Uptime Kuma

![](https://media.wiki-power.com/img/20230410160253.jpg)

**Uptime Kuma** es una herramienta de monitoreo de estado que admite múltiples protocolos de red. Puede supervisar el estado en tiempo real, la duración de respuesta y la validez del certificado de varios sitios web personalizados, y ofrece varias formas de notificación.

## Implementación (Docker Compose)

En primer lugar, cree un archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  uptime-kuma:
    container_name: ${STACK_NAME}_app
    image: louislam/uptime-kuma:${APP_VERSION}
    ports:
      - ${APP_PORT}:3001
    volumes:
      - ${STACK_DIR}:/app/data
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si prefiere no utilizar variables de entorno, también puede personalizar los parámetros directamente en `compose.yaml` (por ejemplo, reemplace `${STACK_NAME}` con `uptime-kuma`).

```dotenv title=".env"
STACK_NAME=uptime-kuma
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./uptime-kuma

# uptime-kuma
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
```

Finalmente, ejecute el comando `docker compose up -d` en el directorio donde se encuentra `compose.yaml` para iniciar los contenedores orquestados.

## Instrucciones de configuración

Nota: Si está utilizando un proxy inverso, asegúrese de habilitar la función de soporte de Websockets.

## Referencias y Agradecimientos

- [Sitio web oficial](https://uptime.kuma.pet/)
- [Documentación](https://github.com/louislam/uptime-kuma/wiki)
- [Repositorio en GitHub](https://github.com/louislam/uptime-kuma)
- [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma)

[por_reemplazar[1]]
[por_reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
