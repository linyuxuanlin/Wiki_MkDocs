# Homelab - Self-hosted RSS Aggregator FreshRSS

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304102312005.png)

**FreshRSS** is a self-hosted RSS aggregator that supports subscribing to multiple RSS feeds and automatically refreshing them. It provides web-based reading and an API for mobile apps.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "2.4"
services:
  freshrss:
    container_name: ${STACK_NAME}_app
    image: freshrss/freshrss:${APP_VERSION}
    hostname: freshrss
    logging:
      options:
        max-size: 10m
    ports:
      - "${APP_PORT}:80"
    volumes:
      - ${STACK_DIR}/data:/var/www/FreshRSS/data
      - ${STACK_DIR}/extensions:/var/www/FreshRSS/extensions
    environment:
      TZ: Asia/Shanghai
      CRON_MIN: "*/60" # Pull article updates every 60 minutes
    restart: unless-stopped
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `freshrss`).

```dotenv title=".env"
STACK_NAME=freshrss
STACK_DIR=xxx # Customize the project storage path, such as ./freshrss

# freshrss
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not already in use

```

Finally, execute the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

Recommended RSS sources include saveweb's Chinese blog list [**rss-list**](https://github.com/saveweb/rss-list).

For mobile apps, we recommend using FeedMe (Android) and NetNewsWire (iOS).

For more RSS-related content, please refer to the article [**RSS - Efficient Reading Method**](https://wiki-power.com/en/RSS-%E9%AB%98%E6%95%88%E7%8E%87%E7%9A%84%E9%98%85%E8%AF%BB%E6%96%B9%E5%BC%8F/).

## References and Acknowledgements

- [Official Website](https://freshrss.org)
- [Documentation](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [GitHub repo](https://github.com/FreshRSS/FreshRSS)
- [Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [Demo site](https://demo.freshrss.org/i/?rid=64342708bf322)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
