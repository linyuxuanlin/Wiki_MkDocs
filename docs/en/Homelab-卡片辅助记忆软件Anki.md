# Homelab - Anki Card-based Memory Aid Software

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202306191745527.png)

**Anki** is an open-source flashcard application that helps users easily and efficiently memorize various knowledge points, commonly used for vocabulary memorization. Its feature is the use of a memory retention curve, generating appropriate review plans based on learning progress, helping users fully utilize the brain's memory patterns to achieve optimal memory effects. Anki has high customization, allowing users to create their own study cards, including text, images, and even audio and video. Anki also supports multi-platform use.

Due to the synchronization server being overseas, it may sometimes fail to synchronize properly. We can use **anki-sync-server** to set up our own synchronization service. The following tutorial uses the `johngong/anki-sync-server` image, which can be used normally. Other versions have not been tested.

## Deployment (Docker Compose)

First, create the `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  anki-sync-server:
    container_name: ${STACK_NAME}_app
    image: johngong/anki-sync-server:${APP_VERSION}
    ports:
      - "${APP_PORT}:27701"
    volumes:
      - ${STACK_DIR}:/config
    environment:
      - ANKI_SYNC_SERVER_USER=${APP_USERNAME}
      - ANKI_SYNC_SERVER_PASSWORD=${APP_PASSWORD}
      - UID=1000
      - GID=1000
    restart: unless-stopped
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `anki-sync-server`).

```dotenv title=".env"
STACK_NAME=anki-sync-server
STACK_DIR=/DATA/AppData/anki-sync-server # Customize the project storage path, for example, ./anki-sync-server

# anki-sync-server
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied
APP_USERNAME=xxx@xx.com  # Customize the account name, which needs to be in email format
APP_PASSWORD=xxxxxx # Customize the password
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

### Windows

For Windows, I used [**Anki 2.1.28**](https://github.com/ankitects/anki/releases/download/2.1.28/anki-2.1.28-windows.exe) (tested and found that 2.1.65 cannot synchronize).

After installation, click `Tools` - `Add-ons` in the top bar, then click `Get Add-ons`, enter the add-on code `358444159`, and click `OK`. Then click `Settings` and change the address to the address and port of the server where you deployed `anki-sync-server`, and finally restart the software.

After restarting, click Sync on the main interface, enter the email and password you filled in when deploying docker, and you can synchronize.

If synchronization still fails, please refer to [**Setting up Anki**](https://github.com/ankicommunity/anki-sync-server/blob/develop/README.md#setting-up-anki).

### Android

The AnkiDroid app is used on the Android platform, which allows users to customize the server address without installing any plugins, but requires logging in using https. It is recommended to use reverse proxy (the setup of a reverse proxy server can refer to the article "**Homelab - Reverse Proxy Certificate Management Panel Nginx Proxy Manager**").

After logging in using https, users can select "Advanced" - "Custom sync server" on the main interface to configure their own server. Note that in the "Media sync url" column, users need to add "/msync" after the original address to synchronize properly.

## References and Acknowledgments

- [Official website](https://apps.ankiweb.net/)
- [Documentation](https://www.navidrome.org/docs/installation/docker/)
- [GitHub repo](https://github.com/ankicommunity/anki-sync-server)
- [Docker Hub](https://hub.docker.com/r/johngong/anki-sync-server)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.