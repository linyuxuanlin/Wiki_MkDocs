# Homelab - Powerful wiki system Wiki.js

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195348.png)

**Wiki.js** is a wiki documentation tool with a backend editor and management page, including multi-user permission management, Markdown, multiple synchronization and storage methods (such as git synchronization), and other functions.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (e.g. replace `${STACK_NAME}` with `wikijs`).

```dotenv title=".env"
STACK_NAME=wikijs
STACK_DIR=xxx # Custom project storage path, such as ./wikijs

# wikijs
APP_VERSION=2
APP_PORT=xxxx # Custom access port, choose one that is not occupied
APP_DB_TYPE=postgres
APP_DB_HOST=db
APP_DB_PORT=5432 # Default internal port of the database
APP_DB_USER=xxx # Database username
APP_DB_PASS=xxx # Database password
APP_DB_NAME=wikijs # Database name

# db
DB_VERSION=10-alpine
DB_POSTGRES_DB=wikijs # Database name, same as above
DB_POSTGRES_PASSWORD=xxx # Database password, same as above
DB_POSTGRES_USER=xxx # Database username, same as above
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

Detailed tutorial for configuring git repository synchronization: <https://docs.requarks.io/storage/git>

## References and Acknowledgements

- [Official Website](https://js.wiki)
- [Documentation](https://docs.requarks.io/install/docker)
- [GitHub repo](https://github.com/requarks/wiki)
- [Docker Hub](https://hub.docker.com/r/requarks/wiki)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.