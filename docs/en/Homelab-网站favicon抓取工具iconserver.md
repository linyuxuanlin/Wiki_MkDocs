# Homelab - Website Favicon Retrieval Tool: iconserver

![iconserver](https://media.wiki-power.com/img/20230304195157.png)

**iconserver** is a website favicon icon retrieval tool. It supports fetching `favicon.ico` and `apple-touch-icon.png` and offers a simple URL API and a web-based operation page. In case of retrieval failure, it will generate a favicon starting with the first letter of the website.

## Deployment (docker-compose)

First, create a `compose.yaml` file and paste the following content:

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

(Optional) It is recommended to create a `.env` file at the same level as the `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can also directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `iconserver`).

```dotenv title=".env"
STACK_NAME=iconserver

# iconserver
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port to one that is not in use
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## References and Acknowledgments

- [Documentation](https://github.com/mat/besticon#docker)
- [GitHub repo](https://github.com/mat/besticon)
- [Docker Hub](https://hub.docker.com/r/matthiasluedtke/iconserver)
- [Demo site](https://besticon-demo.herokuapp.com/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
