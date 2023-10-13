# Homelab - calibre-web, an eBook Management Server

![](https://img.wiki-power.com/d/wiki-media/img/20210429125418.png)

**calibre-web** is an all-in-one eBook solution based on Calibre. It allows users to read eBooks on a web page, integrates calibre-server service, and also supports eBook format conversion.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  calibre-web:
    container_name: ${STACK_NAME}_app
    image: johngong/calibre-web:${APP_VERSION}
    ports:
      - ${APP_PORT_WEB}:8083
      - ${APP_PORT_SERVER}:8080
    volumes:
      - ${STACK_DIR}:/config
      - ${DATA_DIR}:/library
      - ${DATA_DIR}/autoaddbooks:/autoaddbooks
    restart: unless-stopped
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `audiobookshelf`).

````dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # Customize your project storage path, such as ./calibre-web
DATA_DIR=xxx # Customize your book storage path, such as ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # Customize the access port of the Web UI, choose one that is not occupied
APP_PORT_SERVER=xxxx # Customize the access port of calibre-server, choose one that is not occupied

If you have a NAS, you can also mount the storage space on the NAS through the NFS protocol, store music on the NAS to save server space, please refer to [**Expanding the Space of Synology NAS Hard Disk under Linux (NFS)**](https://wiki-power.com/en/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/) for details.

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration Instructions

The default account is `admin` and the password is `admin123`.

### Book Upload Function

The system does not have the book upload function by default. You need to click `Admin` - `Edit Basic Configuration` - `Enable Upload` in order to enable the book upload function.

### Mobile Usage

On Android, you can use Librera to connect to calibre-web via the OPDS protocol. The URL of the book library to be added is the original URL plus `/opds`, for example, `calibre.xxx.com/opds`.

### Forgot Password

If you forget your password, you can download the `app.db` database in `calibre-web` and use SQLite to view the software (or online tools such as [**SQLite Viewer | Modifier**](https://www.lzltool.com/sqlite-viewer)). Execute the following statement:

```sql
SELECT * FROM 'user' LIMIT 0,30 --You can also manually switch to the table named user
````

```sql
UPDATE user SET password='pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' WHERE name='xxx'; -- Replace xxx with your current username
```

Replace the modified `app.db` with the original one, and then log in with the new password `hello`.

## References and Acknowledgements

- [GitHub repo](https://github.com/janeczku/calibre-web)
- [Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
