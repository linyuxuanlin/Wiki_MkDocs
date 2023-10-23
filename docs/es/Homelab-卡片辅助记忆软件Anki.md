# Homelab - Software de Memoria Asistida por Tarjetas Anki

![](https://img.wiki-power.com/d/wiki-media/img/202306191745527.png)

**Anki** es una aplicación de tarjetas de memoria de código abierto que ayuda a los usuarios a recordar una variedad de conceptos de manera efectiva y sencilla, comúnmente utilizada para memorizar vocabulario. Su característica distintiva radica en el uso de la curva de olvido, generando un plan de revisión adaptado a las necesidades de aprendizaje, lo que ayuda a los usuarios a aprovechar al máximo los patrones de memoria del cerebro para lograr el mejor resultado en la retención de información. Anki es altamente personalizable, permitiendo a los usuarios crear sus propias tarjetas de estudio, que pueden incluir texto, imágenes, e incluso audio y video. Anki también es compatible con múltiples plataformas.

Dado que el servidor de sincronización se encuentra en el extranjero, a veces la sincronización puede no funcionar correctamente. En estos casos, se puede configurar su propio servicio de sincronización utilizando **anki-sync-server**. El siguiente tutorial utiliza la imagen `johngong/anki-sync-server`, que ha sido probada y se sabe que funciona correctamente, aunque otras versiones no han sido verificadas.

## Implementación (Docker Compose)

En primer lugar, cree un archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si prefiere no utilizar variables de entorno, puede personalizar directamente los parámetros en `compose.yaml` (por ejemplo, reemplace `${STACK_NAME}` con `anki-sync-server`).

```dotenv title=".env"
STACK_NAME=anki-sync-server
STACK_DIR=/DATA/AppData/anki-sync-server # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./anki-sync-server

# anki-sync-server
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
APP_USERNAME=xxx@xx.com  # Nombre de usuario personalizado en formato de correo electrónico
APP_PASSWORD=xxxxxx # Contraseña personalizada
```

Por último, ejecute el comando `docker-compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores programados.

## Instrucciones de Configuración

### Windows

En Windows, he utilizado [**Anki 2.1.28**](https://github.com/ankitects/anki/releases/download/2.1.28/anki-2.1.28-windows.exe) (he probado la versión 2.1.65 y la sincronización no funciona).

Después de instalarlo, vaya a "Herramientas" en la barra superior, seleccione "Complementos", haga clic en "Obtener complementos", ingrese el código del complemento `358444159` y haga clic en "Aceptar". Luego, vaya a "Configuración", cambie la dirección al servidor donde ha implementado `anki-sync-server` junto con el puerto y reinicie el software.

Después de reiniciar, haga clic en "Sincronizar" en la interfaz principal, ingrese el correo electrónico y la contraseña que ingresó durante la implementación de Docker y podrá realizar la sincronización.

Si aún tiene problemas con la sincronización, consulte [**Configuración de Anki**](https://github.com/ankicommunity/anki-sync-server/blob/develop/README.md#setting-up-anki).

### Android

En la plataforma Android, se utiliza AnkiDroid, que permite la personalización de la dirección del servidor sin necesidad de instalar complementos, aunque se requiere la autenticación a través de HTTPS. Se recomienda utilizar un servidor de proxy inverso para facilitar esta configuración. Puede encontrar información sobre cómo configurar un servidor de proxy inverso en el artículo [**Homelab - Panel de Gestión de Certificados para Proxy Nginx**](to_be_replace[3]).

Una vez autenticado mediante HTTPS, en la pantalla principal de AnkiDroid, seleccione `Avanzado` y luego `Servidor de Sincronización Personalizado` para configurar su propio servidor. Tenga en cuenta que en el campo `URL de Sincronización de Medios`, debe agregar `/msync` al final de la dirección original para que la sincronización funcione correctamente.

## Referencias y Agradecimientos

- [Sitio Oficial](https://apps.ankiweb.net/)
- [Documentación](https://www.navidrome.org/docs/installation/docker/)
- [Repositorio en GitHub](https://github.com/ankicommunity/anki-sync-server)
- [Docker Hub](https://hub.docker.com/r/johngong/anki-sync-server)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.