# Homelab - Herramienta de monitoreo de estado del sitio web Uptime Kuma

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410160253.jpg)

**Uptime Kuma** es una herramienta de monitoreo de estado que admite varios protocolos de red. Puede monitorear el estado en tiempo real, la duración de la respuesta, la validez del certificado, etc. de varios sitios web personalizados y proporciona varios métodos de notificación.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplace `${STACK_NAME}` con `uptime-kuma`).

```dotenv title=".env"
STACK_NAME=uptime-kuma
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./uptime-kuma

# uptime-kuma
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, simplemente elija uno que no esté en uso
```

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Nota: Si utiliza un proxy inverso, habilite la función "Soporte de Websockets".

## Referencias y agradecimientos

- [Sitio web oficial](https://uptime.kuma.pet/)
- [Documentación](https://github.com/louislam/uptime-kuma/wiki)
- [Repositorio de GitHub](https://github.com/louislam/uptime-kuma)
- [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.