# Homelab - Fragmentary Notes Tool memos

![Image](https://media.wiki-power.com/img/202304111548420.png)

**memos** is an open-source, self-hosted memos tool. It supports Markdown syntax, public sharing, iframe embedding, tag management, calendar view, simple data migration, and backup capabilities.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.0"
services:
  memos:
    container_name: ${STACK_NAME}_app
    image: neosmemo/memos:${APP_VERSION}
    ports:
      - ${APP_PORT}:5230
    volumes:
      - ${STACK_DIR}:/var/opt/memos
    restart: always
```

(Optional) It is recommended to create a `.env` file at the same level as `compose.yaml` and customize your environment variables. If you don't want to use environment variables, you can also customize your parameters directly within `compose.yaml` (e.g., replace `${STACK_NAME}` with `memos`).

```dotenv title=".env"
STACK_NAME=memos
STACK_DIR=xxx # Customize your project storage path, e.g., ./memos

# memos
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not already in use
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Details

For mobile iOS/Android app, you can use [**Moe Memos**](https://memos.moe/). There are also more third-party clients such as WeChat Mini Program, browser extensions, Telegram Bot, and others. Please refer to the [**contribution·memos**](https://github.com/usememos/memos#contribution) documentation for more information.

To import and export user data, you can use the VS Code plugin [**SQLite**](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite). Download and open the `memos_prod.db` file under `${DIR}` to perform various operations like adding, deleting, updating, importing, and exporting backups. Note that the `memos_prod.db` file is only updated when the Docker container is stopped or restarted.

## References and Acknowledgments

- [Official Website](https://usememos.com/)
- [Documentation](https://usememos.com/docs/install#docker-compose)
- [GitHub Repository](https://github.com/usememos/memos)
- [Docker Hub](https://hub.docker.com/r/neosmemo/memos)
- [Demo Site](https://demo.usememos.com/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
