# Homelab - memos, a Fragmented Note-taking Tool

![](https://f004.backblazeb2.com/file/wiki-media/img/202304111548420.png)

**memos** is an open-source self-hosted memos tool. It supports Markdown syntax, public sharing, iframe embedding, tag management, calendar view, simple data migration, and backup functions.

## Deployment (Docker Compose)

First, create the `compose.yaml` file and paste the following content:

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `memos`).

```dotenv title=".env"
STACK_NAME=memos
STACK_DIR=xxx # Customize the project storage path, for example, ./memos

# memos
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied
```

Finally, execute the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration Instructions

Mobile iOS/Android App: [Moe Memos](https://memos.moe/). For more third-party clients (such as WeChat mini programs, browser extensions, Telegram Bots, etc.), please refer to the [contribution·memos](https://github.com/usememos/memos#contribution) documentation.

To import and export user data, you can use the VS Code plugin [SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite). Download and open the `memos_prod.db` file in `${DIR}` to perform operations such as adding, deleting, modifying, querying, importing, and exporting backups. Note that the `memos_prod.db` file will only be updated when the docker container is closed/restarted.

## References and Acknowledgments

- [Official website](https://usememos.com/)
- [Documentation](https://usememos.com/docs/install#docker-compose)
- [GitHub repo](https://github.com/usememos/memos)
- [Docker Hub](https://hub.docker.com/r/neosmemo/memos)
- [Demo site](https://demo.usememos.com/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.