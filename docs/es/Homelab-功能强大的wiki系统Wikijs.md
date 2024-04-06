# Homelab - Potente sistema de wiki Wiki.js

![](https://media.wiki-power.com/img/20230304195348.png)

**Wiki.js** es una herramienta de documentación de wiki con un editor y páginas de gestión en el backend, que incluye características como gestión de permisos de múltiples usuarios, Markdown y diversas opciones de sincronización y almacenamiento, como la sincronización con git.

## Implementación (Docker Compose)

Para comenzar, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  wikijs:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/requarks/wiki:${APP_VERSION}
    depends_on:
      - db
    environment:
      DB_TYPE: ${APP_DB_TYPE}
      DB_HOST: ${APP_DB_HOST}
      DB_PORT: ${APP_DB_PORT}
      DB_USER: ${APP_DB_USER}
      DB_PASS: ${APP_DB_PASS}
      DB_NAME: ${APP_DB_NAME}
    restart: unless-stopped
    ports:
      - "${APP_PORT}:3000"
  db:
    container_name: ${STACK_NAME}_db
    image: postgres:${DB_VERSION}
    environment:
      POSTGRES_DB: ${DB_POSTGRES_DB}
      POSTGRES_PASSWORD: ${DB_POSTGRES_PASSWORD}
      POSTGRES_USER: ${DB_POSTGRES_USER}
    logging:
      driver: "none"
    volumes:
      - ${STACK_DIR}/postgres/db-data:/var/lib/postgresql/data
    restart: unless-stopped
volumes:
  db-data:
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente dentro de `compose.yaml` (por ejemplo, sustituir `${STACK_NAME}` por `wikijs`).

```dotenv title=".env"
STACK_NAME=wikijs
STACK_DIR=xxx # Ruta de almacenamiento personalizada del proyecto, como ./wikijs

# wikijs
APP_VERSION=2
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
APP_DB_TYPE=postgres
APP_DB_HOST=db
APP_DB_PORT=5432 # Puerto interno predeterminado de la base de datos
APP_DB_USER=xxx # Nombre de usuario de la base de datos
APP_DB_PASS=xxx # Contraseña de la base de datos
APP_DB_NAME=wikijs # Nombre de la base de datos

# db
DB_VERSION=10-alpine
DB_POSTGRES_DB=wikijs # Nombre de la base de datos, igual que arriba
DB_POSTGRES_PASSWORD=xxx # Contraseña de la base de datos, igual que arriba
DB_POSTGRES_USER=xxx # Nombre de usuario de la base de datos, igual que arriba
```

Finalmente, ejecuta el comando `docker compose up -d` en el directorio del mismo nivel que `compose.yaml` para iniciar los contenedores orquestados.

## Instrucciones de configuración

Para obtener una guía detallada sobre la sincronización de repositorios git, visita: <https://docs.requarks.io/storage/git>

## Referencias y Agradecimientos

- [Página oficial](https://js.wiki)
- [Documentación](https://docs.requarks.io/install/docker)
- [Repositorio en GitHub](https://github.com/requarks/wiki)
- [Docker Hub](https://hub.docker.com/r/requarks/wiki)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
