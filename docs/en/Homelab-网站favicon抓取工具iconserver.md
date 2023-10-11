# Homelab - Website Favicon Retrieval Tool iconserver

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195157.png)

**iconserver** is a website favicon icon retrieval tool. It supports retrieving `favicon.ico` and `apple-touch-icon.png`, and has a simple URL API and web operation page. If the retrieval fails, it will generate a favicon starting with the first letter.

## Deployment (docker-compose)

First, create the `compose.yaml` file and paste the following content:

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

(Optional) It is recommended to create a `.env` file at the same level as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `iconserver`).

```dotenv title=".env"
STACK_NAME=iconserver

# iconserver
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated container.

## Reference and Acknowledgement

- [Documentation](https://github.com/mat/besticon#docker)
- [GitHub repository](https://github.com/mat/besticon)
- [Docker Hub](https://hub.docker.com/r/matthiasluedtke/iconserver)
- [Demo website](https://besticon-demo.herokuapp.com/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
