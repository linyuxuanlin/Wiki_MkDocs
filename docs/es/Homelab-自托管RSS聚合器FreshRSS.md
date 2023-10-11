# Homelab - Agregador de RSS autohospedado FreshRSS

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304102312005.png)

**FreshRSS** es un agregador de RSS autohospedado que admite la suscripción a múltiples fuentes de RSS y se actualiza automáticamente. Proporciona lectura en línea a través de la web y una API para su uso en aplicaciones móviles.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

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
      CRON_MIN: "*/60" # Actualizar los artículos cada 60 minutos
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `freshrss`).

```dotenv title=".env"
STACK_NAME=freshrss
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./freshrss

# freshrss
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
```

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Se recomienda la lista de blogs en chino de saveweb [**rss-list**](https://github.com/saveweb/rss-list) para las fuentes de RSS.

Se recomienda la aplicación FeedMe (Android) y NetNewsWire (iOS) para dispositivos móviles.

Para obtener más información sobre RSS, consulte el artículo [**RSS - Una forma eficiente de leer**](https://wiki-power.com/es/RSS-%E9%AB%98%E6%95%88%E7%8E%87%E7%9A%84%E9%98%85%E8%AF%BB%E6%96%B9%E5%BC%8F/) (en chino).

## Referencias y agradecimientos

- [Sitio web oficial](https://freshrss.org)
- [Documentación](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [Repositorio de GitHub](https://github.com/FreshRSS/FreshRSS)
- [Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [Sitio de demostración](https://demo.freshrss.org/i/?rid=64342708bf322)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
