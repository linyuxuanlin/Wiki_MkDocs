# Homelab - Software de memoria asistida por tarjetas Anki

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202306191745527.png)

**Anki** es una aplicación de tarjetas de memoria de código abierto que ayuda a los usuarios a memorizar fácil y eficientemente diversos puntos de conocimiento, generalmente utilizada para aprender vocabulario. Su característica principal es que utiliza la curva de olvido de la memoria, generando un plan de revisión adecuado según el progreso del aprendizaje, ayudando a los usuarios a aprovechar al máximo las leyes de la memoria del cerebro para lograr el mejor efecto de memoria. Anki es altamente personalizable, puedes crear tus propias tarjetas de estudio, incluyendo texto, imágenes e incluso audio y video. Anki también es compatible con múltiples plataformas.

Debido a que el servidor de sincronización está en el extranjero, a veces puede haber problemas de sincronización. Podemos usar **anki-sync-server** para construir nuestro propio servicio de sincronización. El siguiente tutorial utiliza la imagen `johngong/anki-sync-server`, que funciona correctamente, pero no se ha probado con otras versiones.

## Despliegue (Docker Compose)

Primero, crea el archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `anki-sync-server`).

```dotenv title=".env"
STACK_NAME=anki-sync-server
STACK_DIR=/DATA/AppData/anki-sync-server # Personaliza la ruta de almacenamiento del proyecto, por ejemplo, ./anki-sync-server

# anki-sync-server
APP_VERSION=latest
APP_PORT=xxxx # Personaliza el puerto de acceso, elige uno que no esté ocupado
APP_USERNAME=xxx@xx.com  # Personaliza el nombre de usuario, debe ser un correo electrónico
APP_PASSWORD=xxxxxx # Personaliza la contraseña
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

### Windows

En Windows, utilicé [**Anki 2.1.28**](https://github.com/ankitects/anki/releases/download/2.1.28/anki-2.1.28-windows.exe) (probé la versión 2.1.65 y no se pudo sincronizar).

Después de la instalación, haz clic en `Herramientas` - `Complementos` en la barra de herramientas, luego haz clic en `Obtener complementos`, ingresa el código del complemento `358444159` y haz clic en `OK`, luego haz clic en `Configuración` y cambia la dirección al servidor donde desplegaste `anki-sync-server` y su puerto, finalmente reinicia el software.

Después de reiniciar, haz clic en `Sincronizar` en la pantalla principal, ingresa el correo electrónico y la contraseña que ingresaste al desplegar el contenedor Docker, y podrás sincronizar tus tarjetas.

Si aún no puede sincronizar, consulte [**Configuración de Anki**](https://github.com/ankicommunity/anki-sync-server/blob/develop/README.md#setting-up-anki).

### Android

En Android, se utiliza AnkiDroid, que permite personalizar la dirección del servidor sin necesidad de instalar complementos, pero se requiere iniciar sesión con https. Se recomienda utilizar un proxy inverso (se puede consultar el artículo [**Homelab - Nginx Proxy Manager para la gestión de certificados de proxy inverso**](https://wiki-power.com/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/)).

Después de iniciar sesión con https, en la pantalla principal, seleccione `Advanced` - `Custom sync server` para configurar el servidor personalizado. Tenga en cuenta que en el campo `Media sync url`, debe agregar `/msync` después de la dirección original para sincronizar correctamente.

## Referencias y agradecimientos

- [Sitio web oficial](https://apps.ankiweb.net/)
- [Documentación](https://www.navidrome.org/docs/installation/docker/)
- [Repositorio de GitHub](https://github.com/ankicommunity/anki-sync-server)
- [Docker Hub](https://hub.docker.com/r/johngong/anki-sync-server)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.