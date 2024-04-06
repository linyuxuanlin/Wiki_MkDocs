# Homelab - Software de memorización asistida con tarjetas Anki

![](https://media.wiki-power.com/img/202306191745527.png)

**Anki** es una aplicación de tarjetas de memoria de código abierto que ayuda a los usuarios a recordar varios tipos de información de manera efectiva, comúnmente utilizada para aprender vocabulario. Su característica distintiva es la utilización de la curva de olvido, que genera un plan de revisión adaptado según el progreso de estudio, permitiendo a los usuarios aprovechar al máximo los patrones de memoria del cerebro para lograr un óptimo rendimiento en la memorización. Anki es altamente personalizable, permitiendo a los usuarios crear sus propias tarjetas de estudio con texto, imágenes e incluso audio y video. Además, Anki es compatible con múltiples plataformas.

Debido a que el servidor de sincronización se encuentra en el extranjero, a veces puede haber problemas de sincronización. Sin embargo, podemos configurar nuestro propio servicio de sincronización utilizando **anki-sync-server**. El siguiente tutorial utiliza la imagen de Docker `johngong/anki-sync-server`, que ha sido probada y es funcional.

## Implementación (Docker Compose)

En primer lugar, cree un archivo `compose.yaml` y copie el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si prefiere no usar variables de entorno, puede personalizar directamente los parámetros en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `anki-sync-server`).

```dotenv title=".env"
STACK_NAME=anki-sync-server
STACK_DIR=/DATA/AppData/anki-sync-server # Ruta de almacenamiento personalizada para el proyecto, como ./anki-sync-server

# anki-sync-server
APP_VERSION=latest
APP_PORT=xxxx # Puerto personalizado para acceder, elija uno que no esté en uso
APP_USERNAME=xxx@xx.com  # Nombre de usuario personalizado en formato de correo electrónico
APP_PASSWORD=xxxxxx # Contraseña personalizada
```

Finalmente, en el mismo directorio que `compose.yaml`, ejecute el comando `docker compose up -d` para iniciar los contenedores.

## Instrucciones de configuración

### Windows

En la versión de Windows, he utilizado [**Anki 2.1.28**](https://github.com/ankitects/anki/releases/download/2.1.28/anki-2.1.28-windows.exe) (he comprobado que la versión 2.1.65 no es compatible con la sincronización).

Después de la instalación, vaya a `Herramientas` en la barra de menú superior, luego seleccione `Complementos` y haga clic en `Obtener complementos`. Ingrese el código del complemento `358444159` y haga clic en `OK`. A continuación, vaya a `Configuración` y cambie la dirección al servidor en el que ha implementado `anki-sync-server`. Finalmente, reinicie el software.

Después de reiniciar, haga clic en "Sincronizar" en la pantalla principal, ingrese el correo electrónico y la contraseña que configuró al desplegar Docker y podrá iniciar la sincronización.

Si sigue experimentando problemas de sincronización, consulte [**Setting up Anki**](https://github.com/ankicommunity/anki-sync-server/blob/develop/README.md#setting-up-anki).

### Android

En el lado de Android, se utiliza AnkiDroid, que permite personalizar la dirección del servidor sin necesidad de instalar complementos, pero requiere la autenticación a través de HTTPS. Se recomienda su uso a través de un servidor de proxy inverso (puedes encontrar una guía para configurar un servidor de proxy inverso en [**Homelab - Panel de Gestión de Certificados para Proxy Nginx**](https://wiki-power.com/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/)).

Una vez que hayas iniciado sesión a través de HTTPS, puedes personalizar el servidor de sincronización en la pantalla principal seleccionando `Avanzado` - `Servidor de Sincronización Personalizado`. Ten en cuenta que en el campo `URL de Sincronización Multimedia`, debes agregar `/msync` al final de la dirección original para que la sincronización funcione correctamente.

## Referencias y Agradecimientos

- [Sitio Oficial](https://apps.ankiweb.net/)
- [Documentación](https://www.navidrome.org/docs/installation/docker/)
- [Repositorio en GitHub](https://github.com/ankicommunity/anki-sync-server)
- [Docker Hub](https://hub.docker.com/r/johngong/anki-sync-server)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
