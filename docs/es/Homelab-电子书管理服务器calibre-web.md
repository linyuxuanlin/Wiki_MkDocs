# Homelab - Servidor de gestión de libros electrónicos calibre-web

![](https://img.wiki-power.com/d/wiki-media/img/20210429125418.png)

**calibre-web** es una solución integral de libros electrónicos basada en Calibre, que permite leer libros electrónicos en línea, integra el servicio calibre-server y también incluye la conversión de formatos de libros electrónicos.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./calibre-web
DATA_DIR=xxx # Ruta personalizada de almacenamiento de libros, por ejemplo, ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # Puerto de acceso personalizado de la interfaz de usuario web, simplemente elija uno que no esté ocupado
APP_PORT_SERVER=xxxx # Puerto de acceso personalizado de calibre-server, simplemente elija uno que no esté ocupado
```

Si tiene un NAS, también puede montar el espacio de almacenamiento en el NAS a través del protocolo NFS, almacenar libros en el NAS para ahorrar espacio en el servidor. Para obtener más detalles, consulte **Montar discos duros NAS Synology en Linux (NFS)**.

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

La cuenta predeterminada es `admin` y la contraseña es `admin123`.

### Función de carga de libros

El sistema no tiene la función de carga de libros habilitada de forma predeterminada. Para habilitar esta función, haga clic en "Permisos de administración" - "Editar configuración básica" - "Habilitar carga".

### Uso en dispositivos móviles

En Android, puede usar Librera para conectarse a calibre-web a través del protocolo OPDS. La URL de la biblioteca de libros es la URL original seguida de `/opds`, por ejemplo, `calibre.xxx.com/opds`.

### Olvidó su contraseña

Si olvida su contraseña, puede descargar la base de datos `app.db` de `calibre-web` y usar SQLite para ver el software (o herramientas en línea como **Visor | Editor de SQLite**), y luego ejecutar las siguientes instrucciones:

```sql
SELECT * FROM 'user' LIMIT 0,30 -- También se puede cambiar manualmente a la tabla llamada user
```

```sql
UPDATE user SET password='pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' WHERE name='xxx'; -- Reemplaza xxx con tu nombre de usuario actual
```

Reemplaza el archivo `app.db` modificado por el original y luego inicia sesión con la nueva contraseña `hello`.

## Referencias y agradecimientos

- [Repositorio de GitHub](https://github.com/janeczku/calibre-web)
- [Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
