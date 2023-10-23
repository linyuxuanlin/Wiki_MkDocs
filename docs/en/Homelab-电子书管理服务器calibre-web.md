# Homelab - Ebook Management Server calibre-web

![](https://img.wiki-power.com/d/wiki-media/img/20210429125418.png)

**calibre-web** is an all-in-one ebook solution based on Calibre. It allows you to read ebooks on a web interface, integrates with the calibre-server service, and offers ebook format conversion.

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # Customize your project storage path, e.g., ./calibre-web
DATA_DIR=xxx # Customize your ebook storage path, e.g., ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # Customize the access port for the Web UI, choose an available port
APP_PORT_SERVER=xxxx # Customize the access port for calibre-server, choose an available port
```

If you have a NAS, you can also mount storage space on your NAS using the NFS protocol to save server space. For details, please refer to [**Mount Synology NAS Hard Drive for Space Expansion (NFS) on Linux**](to_be_replaced[3]).

Finally, in the directory where `compose.yaml` is located, execute the `docker compose up -d` command to start the orchestrated containers.

## Configuration Notes

The default username is `admin`, and the password is `admin123`.

### Book Upload Functionality

By default, the book upload feature is disabled. To enable book uploads, follow these steps: Click on "Management Permissions" in the upper right corner, then select "Edit Basic Configuration," and enable the "Upload" option.

### Mobile Usage

On Android, you can use Librera to connect to calibre-web via the OPDS protocol. Add the library's URL by appending `/opds` to the original URL, for example, `calibre.xxx.com/opds`.

### Forgot Password

If you forget your password, you can download the `app.db` database from `calibre-web` and use SQLite software to view it (or use online tools like [**Sqlite Viewer | Editor**](https://www.lzltool.com/sqlite-viewer)). Execute the following SQL query:

```sql
SELECT * FROM 'user' LIMIT 0,30 -- You can manually switch to the table named 'user'
```

```markdown
Update the `user` table with the new password for the user identified by the name 'xxx'. Ensure to replace 'xxx' with your current username.

```sql
UPDATE user SET password='pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' WHERE name='xxx';
```

Replace the existing `app.db` with the updated one, and then log in using the new password, which is 'hello'.

## References and Acknowledgments

- [GitHub repo](https://github.com/janeczku/calibre-web)
- [Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
```

This translation maintains the original markdown format and provides a professional and fluent rendition of the content while ensuring the clarity of the instructions.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.