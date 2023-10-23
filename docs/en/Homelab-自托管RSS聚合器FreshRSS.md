# Homelab - Self-Hosted RSS Aggregator with FreshRSS

![FreshRSS](https://img.wiki-power.com/d/wiki-media/img/202304102312005.png)

**FreshRSS** is a self-hosted RSS aggregator that allows you to subscribe to multiple RSS feeds and automatically refresh them. It provides web-based reading and an API for mobile apps.

## Deployment (Docker Compose)

Start by creating a `compose.yaml` file and paste the following content:

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
      CRON_MIN: "*/60" # Fetch article updates every 60 minutes
    restart: unless-stopped
```

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `freshrss`).

```dotenv title=".env"
STACK_NAME=freshrss
STACK_DIR=xxx # Customize your project storage path, e.g., ./freshrss

# FreshRSS
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose an unoccupied one
```

Finally, run the `docker compose up -d` command in the directory where `compose.yaml` is located to start the orchestrated containers.

## Configuration

You can find a recommended list of Chinese blogs on RSS feeds on saveweb's [**rss-list**](https://github.com/saveweb/rss-list).

For mobile apps, we recommend using FeedMe (Android) and NetNewsWire (iOS).

For more RSS-related content, you can refer to the article [**RSS - An Efficient Way to Read**]().

## References and Acknowledgments

- [Official Website](https://freshrss.org)
- [Documentation](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [GitHub Repository](https://github.com/FreshRSS/FreshRSS)
- [Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [Demo Site](https://demo.freshrss.org/i/?rid=64342708bf322)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
