# Homelab - Autohospedaje del agregador RSS FreshRSS

![](https://media.wiki-power.com/img/202304102312005.png)

**FreshRSS** es un agregador RSS autohospedado que admite la suscripción a múltiples fuentes RSS y se actualiza automáticamente. Ofrece lectura en línea a través de la web y una API para su uso en aplicaciones móviles.

## Implementación (Docker Compose)

Primero, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "2.4"
services:
  freshrss:
    container_name: ${STACK_NAME}_app
    image: freshrss/freshrss:${APP_VERSION}
    hostname: freshrss
    logging:
      options:
        max-size: 10m
    ports:
      - "${APP_PORT}:80"
    volumes:
      - ${STACK_DIR}/data:/var/www/FreshRSS/data
      - ${STACK_DIR}/extensions:/var/www/FreshRSS/extensions
    environment:
      TZ: Asia/Shanghai
      CRON_MIN: "*/60" # Actualiza automáticamente los artículos cada 60 minutos
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `freshrss`).

```dotenv title=".env"
STACK_NAME=freshrss
STACK_DIR=xxx # Ruta de almacenamiento personalizada para el proyecto, por ejemplo, ./freshrss

# freshrss
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores orquestados.

## Configuración

Puedes encontrar una lista recomendada de fuentes RSS en chino en [**rss-list**](https://github.com/saveweb/rss-list) de saveweb.

Para aplicaciones móviles, se recomienda usar FeedMe (Android) y NetNewsWire (iOS).

Para obtener más información sobre RSS, puedes consultar el artículo [**RSS - Una forma eficiente de leer**](https://wiki-power.com/RSS-%E9%AB%98%E6%95%88%E7%8E%87%E7%9A%84%E9%98%85%E8%AF%BB%E6%96%B9%E5%BC%8F/).

## Referencias y Agradecimientos

- [Sitio web oficial](https://freshrss.org)
- [Documentación](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [Repositorio en GitHub](https://github.com/FreshRSS/FreshRSS)
- [Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [Sitio de demostración](https://demo.freshrss.org/i/?rid=64342708bf322)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
