# Homelab - Software de pizarra WeKan con abundantes funciones

![](https://media.wiki-power.com/img/20230508175842.png)

**WeKan** es una destacada aplicación de pizarra de código abierto que es flexible, fácil de usar y altamente eficiente. Esta aplicación es ideal para la gestión colaborativa de tareas, proyectos y flujos de trabajo en equipos. WeKan proporciona una interfaz de usuario sencilla pero poderosa que permite a los usuarios crear múltiples pizarras, agregar listas y tarjetas a cada una, y asignar tareas a diferentes miembros del equipo, lo que facilita la gestión de proyectos y el seguimiento del progreso.

## Implementación (Docker Compose)

Para implementar WeKan, primero debe crear un archivo llamado `compose.yaml` y pegar el siguiente contenido:

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

Este archivo le permitirá desplegar WeKan utilizando Docker Compose de manera eficaz.

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar directamente los parámetros en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `wekan`).

```dotenv title=".env"
STACK_NAME=wekan
STACK_DIR=xxx # Ruta personalizada para el almacenamiento del proyecto, por ejemplo, ./wekan

# wekandb
DB_VERSION=6

# wekan
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
```

A continuación, inicializamos la estructura de directorios. Cambie al directorio personalizado `STACK_DIR` (por ejemplo, `./wekan`) y ejecute el comando para crear las carpetas:

```shell
mkdir -vp {wekan-files,wekan-db,wekan-db-dump}
```

Finalmente, en el directorio que contiene `compose.yaml`, ejecute el comando `docker compose up -d` para iniciar los contenedores orquestados.

## Descripción de la configuración

El `compose.yaml` anterior ha sido simplificado y modificado. Si desea ver la versión completa, consulte [**wekan/compose.yaml**](https://github.com/wekan/wekan/blob/master/compose.yaml).

Una vez que la implementación esté completa, la primera cuenta registrada se convertirá en la cuenta de administrador. Si está utilizando Wekan para uso personal, se recomienda desactivar la función de registro de usuarios en el panel de configuración.

## Referencias y Agradecimientos

- [Sitio oficial](https://wekan.github.io/)
- [Documentación](https://github.com/wekan/wekan/wiki/Docker#note-docker-composeyml-works)
- [Repositorio en GitHub](https://github.com/wekan/wekan)
- [Docker Hub](https://hub.docker.com/r/wekanteam/wekan)
- [Sitio de demostración](https://boards.wekan.team/b/D2SzJKZDS4Z48yeQH/wekan-open-source-kanban-board-with-mit-license)

[Reemplazar[1]]
[Reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
