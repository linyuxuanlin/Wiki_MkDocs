# Homelab - Servidor de gestión de libros electrónicos con calibre-web

![Imagen](https://media.wiki-power.com/img/20210429125418.png)

**calibre-web** es una solución integral para libros electrónicos que se basa en Calibre. Permite la lectura de libros electrónicos en línea y ofrece la integración de servicios de calibre-server, así como la conversión de formatos de libros electrónicos.

## Implementación (Docker Compose)

Para comenzar, crea un archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas usar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # Ruta de almacenamiento personalizada para el proyecto, por ejemplo, ./calibre-web
DATA_DIR=xxx # Ruta de almacenamiento personalizada para la biblioteca, por ejemplo, ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # Puerto personalizado para la interfaz web, elige uno que no esté en uso
APP_PORT_SERVER=xxxx # Puerto personalizado para calibre-server, elige uno que no esté en uso
```

Si tienes un NAS, también puedes montar el espacio de almacenamiento en el NAS utilizando el protocolo NFS para ahorrar espacio en el servidor. Para obtener más detalles, consulta [**Montar discos duros de NAS Synology en Linux para ampliar el espacio (NFS)**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores orquestados.

## Instrucciones de configuración

La cuenta predeterminada es `admin` y la contraseña es `admin123`.

### Función de carga de libros

El sistema no tiene habilitada la función de carga de libros de forma predeterminada. Para habilitarla, sigue estos pasos: haz clic en la esquina superior derecha en `Permisos de administración` - `Editar configuración básica` - `Habilitar carga`, de esta manera podrás usar la función de carga de libros.

### Uso en dispositivos móviles

En dispositivos Android, puedes utilizar Librera para conectarte a calibre-web a través del protocolo OPDS. La URL de la biblioteca que debes agregar es la URL original seguida de `/opds`, por ejemplo, `calibre.xxx.com/opds`.

### Olvido de la contraseña

Si olvidas la contraseña, puedes descargar la base de datos `app.db` de `calibre-web` y usar SQLite para verla (o utilizar herramientas en línea como [**Visor | Editor SQLite**](https://www.lzltool.com/sqlite-viewer)). Luego, ejecuta las siguientes consultas:

```sql
SELECT * FROM 'user' LIMIT 0,30 -- También puedes cambiar manualmente a la tabla llamada 'user'
```

```sql
-- Actualiza la contraseña del usuario a 'pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' donde el nombre sea 'xxx'; -- Reemplaza 'xxx' con tu nombre de usuario actual

Reemplaza el archivo `app.db` con el modificado y luego podrás iniciar sesión con la nueva contraseña 'hello'.

## Referencias y Agradecimientos

- [Repositorio de GitHub](https://github.com/janeczku/calibre-web)
- [Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
