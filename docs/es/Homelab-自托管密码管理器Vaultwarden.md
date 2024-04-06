# Homelab - Gestor de contraseñas autoalojado Vaultwarden

![](https://media.wiki-power.com/img/20230304195414.jpg)

**Vaultwarden** es un servidor de Bitwarden autoalojado de terceros que protege y administra las contraseñas de varios sitios web con una contraseña maestra, y puede generar contraseñas aleatorias para diferentes sitios web.

## Implementación (Docker Compose)

Primero, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  vaultwarden:
    container_name: ${STACK_NAME}_app
    image: vaultwarden/server:${APP_VERSION}
    ports:
      - ${APP_PORT}:80
    volumes:
      - ${STACK_DIR}:/data/
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `vaultwarden`).

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # Ruta personalizada para almacenar el proyecto, por ejemplo, ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores orquestados.

## Instrucciones de configuración

Por defecto, Vaultwarden requiere iniciar sesión a través de https. Se recomienda utilizar un proxy inverso (puedes consultar el artículo [**Homelab - Nginx Proxy Manager, un panel de gestión de certificados de proxy inverso**](https://wiki-power.com/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/) para obtener información sobre cómo configurar un servidor proxy inverso).

Cuando uses la extensión del navegador, la aplicación de escritorio o la aplicación móvil, deberás hacer clic en Configuración en la página de inicio de sesión y configurar la URL del servidor para poder utilizar el servicio autoalojado correctamente.

Además, las versiones antiguas (anteriores a 1.27.0) de Vaultwarden no son compatibles con las extensiones del navegador de Bitwarden y pueden causar problemas al iniciar sesión. Consulta el problema: [**Client fails to connect or login**](https://github.com/dani-garcia/vaultwarden/issues/3082) para obtener más detalles.

Debido a que es un servicio autoalojado, debes tener en cuenta la seguridad de tus datos. Recuerda hacer copias de seguridad regulares de la base de datos de contraseñas.

## Referencias y agradecimientos

- [Sitio web oficial](https://github.com/dani-garcia/vaultwarden/wiki)
- [Documentación](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Repositorio de GitHub](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
