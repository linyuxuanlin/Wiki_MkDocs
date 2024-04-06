# Homelab - E-book Management Server calibre-web

![](https://media.wiki-power.com/img/20210429125418.png)

**calibre-web** is an all-in-one e-book solution based on Calibre. It allows you to read e-books on a web interface and integrates the calibre-server service, along with e-book format conversion.

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can also directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # Customize your project storage path, e.g., ./calibre-web
DATA_DIR=xxx # Customize your e-book storage path, e.g., ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # Customize the access port for the Web UI, choose an available port
APP_PORT_SERVER=xxxx # Customize the access port for calibre-server, choose an available port
```

If you have a NAS, you can also mount storage space on your NAS using the NFS protocol to save server space. For more details, please refer to [**Mounting Synology NAS Hard Drive for Space Expansion on Linux (NFS)**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Finally, execute the `docker compose up -d` command in the directory where `compose.yaml` is located to start the orchestrated containers.

## Configuration Instructions

The default username is `admin`, and the password is `admin123`.

### Book Upload Function

The system does not have book upload functionality enabled by default. To enable book upload, go to `Management Permissions` in the upper right corner - `Edit Basic Configuration` - `Enable Upload`.

### Mobile Usage

On Android, you can use Librera to connect to calibre-web via the OPDS protocol. Add the library's URL by appending `/opds` to the original URL, for example, `calibre.xxx.com/opds`.

### Forgot Password

If you forget your password, you can download the `app.db` database from `calibre-web` and use SQLite software (or online tools like [**SQLite Viewer | Editor**](https://www.lzltool.com/sqlite-viewer)) to execute the following SQL query:

```sql
SELECT * FROM 'user' LIMIT 0,30 -- You can also manually switch to the table named 'user'.
```

````markdown
```sql
-- Please replace 'xxx' with your current username
UPDATE user SET password = 'pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' WHERE name = 'xxx';
```
````

Replace the modified `app.db` with the original one, and then log in with the new password 'hello'.

## References and Acknowledgments

- [GitHub Repository](https://github.com/janeczku/calibre-web)
- [Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

```


> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
```
