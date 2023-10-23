# Homelab - Servidor de gestión de libros electrónicos calibre-web

![](https://img.wiki-power.com/d/wiki-media/img/20210429125418.png)

**calibre-web** es una solución integral para libros electrónicos que se basa en Calibre. Permite la lectura de libros electrónicos en línea a través de una interfaz web, integra el servicio de calibre-server y ofrece funciones de conversión de formatos de libros electrónicos.

## Implementación (Docker Compose)

Primero, crea un archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar directamente tus parámetros en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # Ruta personalizada para el almacenamiento del proyecto, por ejemplo, ./calibre-web
DATA_DIR=xxx # Ruta personalizada para el almacenamiento de libros, por ejemplo, ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # Puerto personalizado para la interfaz web, elige un puerto disponible
APP_PORT_SERVER=xxxx # Puerto personalizado para calibre-server, elige un puerto disponible
```

Si tienes un NAS, también puedes montar el espacio de almacenamiento en el NAS a través del protocolo NFS para ahorrar espacio en el servidor. Consulta [**Linux下挂载群晖NAS硬盘拓展空间（NFS）**](https://wiki-power.com/es/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/) para obtener más detalles.

Finalmente, ejecuta el comando `docker compose up -d` en el directorio donde se encuentra `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

El nombre de usuario y contraseña predeterminados son `admin` y `admin123`, respectivamente.

### Función de carga de libros

Por defecto, la función de carga de libros está deshabilitada. Para habilitarla, sigue estos pasos: haz clic en "Gestión de permisos" en la esquina superior derecha, luego selecciona "Editar configuración básica" y habilita la opción de carga de libros.

### Uso en dispositivos móviles

En dispositivos Android, puedes utilizar Librera y conectarte a calibre-web a través del protocolo OPDS. El URL de la biblioteca se obtiene agregando "/opds" al URL original, por ejemplo, "calibre.xxx.com/opds".

### Olvidaste la contraseña

Si olvidaste tu contraseña, puedes descargar la base de datos "app.db" de calibre-web y usar una herramienta de SQLite, como [**Sqlite Viewer | Editor**](https://www.lzltool.com/sqlite-viewer), para ejecutar la siguiente consulta:

```sql
SELECT * FROM 'user' LIMIT 0,30 -- También puedes cambiar manualmente a la tabla llamada 'user'
```


```sql
-- Actualización de la contraseña del usuario en la base de datos
UPDATE user SET password='pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' WHERE name='xxx'; -- Reemplaza 'xxx' con tu nombre de usuario actual

-- Reemplaza el archivo 'app.db' original con el modificado y luego inicia sesión con la nueva contraseña 'hello'.

## Referencias y Agradecimientos

- [Repositorio en GitHub](https://github.com/janeczku/calibre-web)
- [Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```


> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.