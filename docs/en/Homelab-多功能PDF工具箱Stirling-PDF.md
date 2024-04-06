# Homelab - Multi-Purpose PDF Toolbox Stirling-PDF

![](https://media.wiki-power.com/img/20230410172939.png)

**Stirling-PDF** is a self-hosted PDF toolkit that offers a range of functionalities, including PDF splitting, merging, rotating, page extraction, image conversion, reordering, image insertion/extraction, password addition/removal, permission settings, watermarking, converting other files to PDF, OCR text recognition, metadata editing, and support for dark mode.

## Deployment (Docker Compose)

To get started, create a `compose.yaml` file and paste the following content:

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

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replacing `${STACK_NAME}` with `s-pdf`).

```dotenv title=".env"
STACK_NAME=s-pdf
STACK_DIR=xxx # Customize your project storage path, e.g., ./s-pdf

# s-pdf
APP_VERSION=latest
APP_PORT=xxxx # Customize your access port, choose an available one
```

Finally, run the `docker compose up -d` command in the directory where `compose.yaml` is located to start the orchestrated container.

## References and Acknowledgments

- [Documentation / GitHub repo](https://github.com/Frooodle/Stirling-PDF)
- [Docker Hub](https://hub.docker.com/r/frooodle/s-pdf)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
