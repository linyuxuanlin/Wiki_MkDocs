# Homelab - Multi-functional PDF Toolbox Stirling-PDF

![](https://f004.backblazeb2.com/file/wiki-media/img/20230410172939.png)

**Stirling-PDF** is a self-hosted PDF toolkit that includes functions such as PDF splitting, merging, rotating, page extraction, image conversion, reordering, adding/extracting images, adding/removing passwords, setting permissions, adding watermarks, converting other files to PDF, OCR text recognition, metadata editing, and supports dark mode.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.3"
services:
  s-pdf:
    container_name: ${STACK_NAME}_app
    image: frooodle/s-pdf:${APP_VERSION}
    ports:
      - ${APP_PORT}:8080
    restart: always
```

(Optional) It is recommended to create a `.env` file at the same level as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `s-pdf`).

```dotenv title=".env"
STACK_NAME=s-pdf
STACK_DIR=xxx # Customize the project storage path, such as ./s-pdf

# s-pdf
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated container.

## Reference and Acknowledgement

- [Documentation / GitHub repo](https://github.com/Frooodle/Stirling-PDF)
- [Docker Hub](https://hub.docker.com/r/frooodle/s-pdf)

Sorry, there is no Chinese article provided for translation. Please provide the article to be translated.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.