# Homelab - Anki, the Card-Based Memory Aid Software

![Anki](https://img.wiki-power.com/d/wiki-media/img/202306191745527.png)

**Anki** is an open-source flashcard application designed to help users efficiently memorize a wide range of information, commonly used for vocabulary and terminology retention. What sets it apart is its utilization of a spaced repetition algorithm, tailoring review schedules based on your learning progress, and thus optimizing memory retention by adhering to the brain's natural memory patterns. Anki offers a high degree of customization, allowing you to create your own study cards incorporating text, images, and even audio and video elements. Anki is also compatible with multiple platforms.

As the synchronization server is located overseas, occasional syncing issues may arise. To address this, we can set up our own synchronization service using **anki-sync-server**. The tutorial below utilizes the `johngong/anki-sync-server` image, which has been tested and proven to work effectively.

## Deployment (Docker Compose)

Begin by creating a `compose.yaml` file and paste the following content:

```yaml
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

(Optional) It is recommended to create a `.env` file at the same directory level as `compose.yaml` and define your custom environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `anki-sync-server`).

```dotenv
STACK_NAME=anki-sync-server
STACK_DIR=/DATA/AppData/anki-sync-server # Customize the project storage path, e.g., ./anki-sync-server

# anki-sync-server
APP_VERSION=latest
APP_PORT=xxxx # Choose an available access port
APP_USERNAME=xxx@xx.com  # Customize your username, in email format
APP_PASSWORD=xxxxxx # Customize your password
```

Finally, execute the `docker compose up -d` command at the same directory level as `compose.yaml` to start the orchestrated container.

## Configuration Details

### Windows

For Windows, I used [**Anki 2.1.28**](https://github.com/ankitects/anki/releases/download/2.1.28/anki-2.1.28-windows.exe) (tested and working, as version 2.1.65 may have synchronization issues).

After installation, follow these steps: Click on 'Tools' in the top menu, then select 'Add-ons.' Click on 'Get Add-ons,' input the add-on code `358444159`, and click 'OK.' Next, click on 'Settings' and modify the address to match the server address and port where you've deployed `anki-sync-server`. Finally, restart the software.

After the restart, click 'Sync' on the main interface, enter the email and password you provided during Docker deployment, and you'll be able to synchronize.

If synchronization issues persist, please refer to [**Setting up Anki**](https://github.com/ankicommunity/anki-sync-server/blob/develop/README.md#setting-up-anki).

### Android

On the Android platform, AnkiDroid is utilized. You can customize the server address without the need for plugin installation, but it does require using HTTPS for login. It is recommended to utilize a reverse proxy setup (for instructions on setting up a reverse proxy server, refer to the article [**Homelab - Nginx Proxy Manager for Certificate Management**](https://wiki-power.com/en/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/).

Once you have logged in using HTTPS, you can configure your custom server by selecting `Advanced` on the main interface and choosing `Custom sync server`. Please note that in the `Media sync URL` field, you should append `/msync` to the original address to ensure proper synchronization.

## References and Acknowledgments

- [Official Website](https://apps.ankiweb.net/)
- [Documentation](https://www.navidrome.org/docs/installation/docker/)
- [GitHub Repository](https://github.com/ankicommunity/anki-sync-server)
- [Docker Hub](https://hub.docker.com/r/johngong/anki-sync-server)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.