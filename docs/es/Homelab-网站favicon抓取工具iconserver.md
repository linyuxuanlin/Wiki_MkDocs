# Homelab - Herramienta de captura de favicon del sitio web iconserver

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195157.png)

**iconserver** es una herramienta de captura de iconos favicon de sitios web. Admite la captura de `favicon.ico` y `apple-touch-icon.png`, tiene una API de URL simple y una página de operación web. Si la captura falla, se generará un favicon que comienza con la primera letra.

## Implementación (docker-compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  iconserver:
    container_name: ${STACK_NAME}_app
    image: matthiasluedtke/iconserver:${APP_VERSION}
    ports:
      - ${APP_PORT}:8080
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `iconserver`).

```dotenv title=".env"
STACK_NAME=iconserver

# iconserver
APP_VERSION=latest
APP_PORT=xxxx # Personalice el puerto de acceso, simplemente elija uno que no esté ocupado
```

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores de la implementación.

## Referencias y agradecimientos

- [Documentación](https://github.com/mat/besticon#docker)
- [Repositorio de GitHub](https://github.com/mat/besticon)
- [Docker Hub](https://hub.docker.com/r/matthiasluedtke/iconserver)
- [Sitio de demostración](https://besticon-demo.herokuapp.com/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
