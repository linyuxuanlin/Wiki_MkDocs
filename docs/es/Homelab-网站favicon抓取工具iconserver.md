# Homelab - Herramienta de extracción de favicon de sitios web iconserver

![](https://media.wiki-power.com/img/20230304195157.png)

**iconserver** es una herramienta que permite la extracción de iconos favicon de sitios web. Admite la extracción de `favicon.ico` y `apple-touch-icon.png`, y cuenta con una sencilla API de URL y una página de operación web. En caso de que la extracción falle, generará un favicon que comienza con la primera letra.

## Implementación (docker-compose)

Primero, cree un archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar directamente sus parámetros en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `iconserver`).

```dotenv title=".env"
STACK_NAME=iconserver

# iconserver
APP_VERSION=latest
APP_PORT=xxxx # Personalice el puerto de acceso, elija uno que no esté en uso
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores orquestados.

## Referencias y Agradecimientos

- [Documentación](https://github.com/mat/besticon#docker)
- [Repositorio en GitHub](https://github.com/mat/besticon)
- [Docker Hub](https://hub.docker.com/r/matthiasluedtke/iconserver)
- [Sitio de demostración](https://besticon-demo.herokuapp.com/)

[por_reemplazar[1]]
[por_reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
