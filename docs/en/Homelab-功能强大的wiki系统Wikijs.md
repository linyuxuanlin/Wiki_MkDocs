# Homelab - Powerful Wiki System Wiki.js

![Wiki.js](https://media.wiki-power.com/img/20230304195348.png)

**Wiki.js** is a wiki documentation tool with a backend editor and management pages, offering features like multi-user permission management, Markdown support, and various synchronization and storage methods, such as Git synchronization.

## Deployment (Docker Compose)

To get started, create a `compose.yaml` file and paste the following contents:

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` to customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `wikijs`).

```dotenv title=".env"
STACK_NAME=wikijs
STACK_DIR=xxx # Customize your project storage path, e.g., ./wikijs

# wikijs
APP_VERSION=2
APP_PORT=xxxx # Choose an available access port
APP_DB_TYPE=postgres
APP_DB_HOST=db
APP_DB_PORT=5432 # Default internal port for the database
APP_DB_USER=xxx # Database username
APP_DB_PASS=xxx # Database password
APP_DB_NAME=wikijs # Database name

# db
DB_VERSION=10-alpine
DB_POSTGRES_DB=wikijs # Database name, matching the one above
DB_POSTGRES_PASSWORD=xxx # Database password, matching the one above
DB_POSTGRES_USER=xxx # Database username, matching the one above
```

Finally, run the `docker compose up -d` command in the directory where `compose.yaml` is located to start the orchestrated containers.

## Configuration Details

For detailed instructions on configuring Git repository synchronization, please refer to [this link](https://docs.requarks.io/storage/git).

## References and Acknowledgments

- [Official Website](https://js.wiki)
- [Documentation](https://docs.requarks.io/install/docker)
- [GitHub Repository](https://github.com/requarks/wiki)
- [Docker Hub](https://hub.docker.com/r/requarks/wiki)

[Placeholder 1]  
[Placeholder 2]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
