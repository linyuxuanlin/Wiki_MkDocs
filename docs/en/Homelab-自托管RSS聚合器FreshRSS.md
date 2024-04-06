# Homelab - Self-hosted RSS Aggregator with FreshRSS

![FreshRSS](https://media.wiki-power.com/img/202304102312005.png)

**FreshRSS** is a self-hosted RSS aggregator that supports subscribing to multiple RSS sources and automatically refreshing them. It provides web-based reading and an API for use with mobile apps.

## Deployment (Docker Compose)

To get started, create a `compose.yaml` file and paste the following content:

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

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` to customize your environment variables. If you prefer not to use environment variables, you can also directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `freshrss`).

```dotenv title=".env"
STACK_NAME=freshrss
STACK_DIR=xxx # Customize your project storage path, e.g., ./freshrss

# freshrss
APP_VERSION=latest
APP_PORT=xxxx # Customize your access port, choose an unoccupied one
```

Finally, run the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Notes

You can find recommended RSS sources in [**rss-list**](https://github.com/saveweb/rss-list), a list of Chinese blogs curated by saveweb.

For mobile apps, we recommend using FeedMe for Android and NetNewsWire for iOS.

For more RSS-related content, please refer to the article on [**RSS - A High-Efficiency Reading Method**](https://wiki-power.com/RSS-%E9%AB%98%E6%95%88%E7%8E%87%E7%9A%84%E9%98%85%E8%AF%BB%E6%96%B9%E5%BC%8F/).

## References and Acknowledgments

- [Official Website](https://freshrss.org)
- [Documentation](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [GitHub Repository](https://github.com/FreshRSS/FreshRSS)
- [Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [Demo Site](https://demo.freshrss.org/i/?rid=64342708bf322)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
