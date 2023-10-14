# Homelab - Software de tablero rico en funciones WeKan

![](https://img.wiki-power.com/d/wiki-media/img/20230508175842.png)

**WeKan** es un software de tablero de código abierto flexible, fácil de usar y eficiente que puede ayudar a los equipos a colaborar en la gestión de tareas, proyectos y flujos de trabajo. Proporciona una interfaz de usuario simple pero potente que permite a los usuarios crear fácilmente múltiples tableros, agregar listas y tarjetas a cada uno y asignar tareas a diferentes miembros para una mejor gestión del proyecto y seguimiento del progreso.

## Implementación (Docker Compose)

Primero, cree un archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "2"
services:
  wekandb:
    container_name: ${STACK_NAME}_db
    image: mongo:${DB_VERSION}
    command: mongod --logpath /dev/null --oplogSize 128 --quiet
    networks:
      - wekan-tier
    expose:
      - 27017
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
      - wekan-db:/data/db
      - wekan-db-dump:/dump
    restart: no
  wekan:
    container_name: ${STACK_NAME}_app
    image: quay.io/wekan/wekan:${APP_VERSION}
    user: 0:0
    networks:
      - wekan-tier
    ports:
      - ${APP_PORT}:8080
    environment:
      - WRITABLE_PATH=/data
      - MONGO_URL=mongodb://wekandb:27017/wekan
      - ROOT_URL=http://localhost
      - MAIL_URL=smtp://<mail_url>:25/?ignoreTLS=true&tls={rejectUnauthorized:false}
      - MAIL_FROM=Wekan Notifications <noreply.wekan@mydomain.com>
      - WITH_API=true
      - RICHER_CARD_COMMENT_EDITOR=false
      - CARD_OPENED_WEBHOOK_ENABLED=false
    depends_on:
      - wekandb
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - wekan-files:/data:rw
    restart: no
volumes:
  wekan-files:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/wekan-files
      o: bind
  wekan-db:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/wekan-db
      o: bind
  wekan-db-dump:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/wekan-db-dump
      o: bind
networks:
  wekan-tier:
    driver: bridge
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar directamente sus parámetros en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `wekan`).

```dotenv title=".env"
STACK_NAME=wekan
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo ./wekan

# wekandb
DB_VERSION=6
```

# wekan

APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté ocupado

````

Luego, inicializamos la estructura de directorios. Cambiamos al directorio personalizado `STACK_DIR` (por ejemplo, `./wekan`) y ejecutamos el comando para crear las carpetas:

```shell
mkdir -vp {wekan-files,wekan-db,wekan-db-dump}
````

Finalmente, en el directorio al mismo nivel que `compose.yaml`, ejecutamos el comando `docker compose up -d` para iniciar los contenedores de la orquestación.

## Instrucciones de configuración

El archivo `compose.yaml` anterior ha sido simplificado y modificado. Si desea ver la versión completa, consulte [**wekan/compose.yaml**](https://github.com/wekan/wekan/blob/master/compose.yaml).

Después de la implementación, la primera cuenta registrada será la cuenta de administrador. Si lo está utilizando para usted mismo, se recomienda desactivar la función de registro de usuarios en el panel de configuración.

## Referencias y agradecimientos

- [Sitio web oficial](https://wekan.github.io/)
- [Documentación](https://github.com/wekan/wekan/wiki/Docker#note-docker-composeyml-works)
- [Repositorio de GitHub](https://github.com/wekan/wekan)
- [Docker Hub](https://hub.docker.com/r/wekanteam/wekan)
- [Sitio de demostración](https://boards.wekan.team/b/D2SzJKZDS4Z48yeQH/wekan-open-source-kanban-board-with-mit-license)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
