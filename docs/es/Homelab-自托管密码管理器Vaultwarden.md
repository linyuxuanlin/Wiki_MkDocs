# Homelab - Gestor de contraseñas autohospedado Vaultwarden

![](https://img.wiki-power.com/d/wiki-media/img/20230304195414.jpg)

**Vaultwarden** es un servidor de Bitwarden autohospedado de terceros que protege y administra las contraseñas de varios sitios web mediante una contraseña maestra y puede generar contraseñas aleatorias para su uso en diferentes sitios.

## Implementación (Docker Compose)

Comienza creando un archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente dentro de `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `vaultwarden`).

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # Ruta personalizada para almacenar el proyecto, por ejemplo, ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores definidos.

## Instrucciones de configuración

Vaultwarden requiere https para iniciar sesión de forma predeterminada, se recomienda utilizar un proxy inverso (puedes consultar cómo configurar un servidor de proxy inverso en el artículo [**Homelab - Nginx Proxy Manager, un panel de gestión de certificados de proxy inverso**](https://wiki-power.com/es/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/).

Cuando uses la extensión del navegador, la aplicación de escritorio o móvil, debes hacer clic en Configuración en la página de inicio de sesión y configurar la URL del servidor para poder utilizar el servicio autohospedado.

Además, las versiones antiguas (anteriores a 1.27.0) de Vaultwarden no son compatibles con las extensiones del navegador de Bitwarden, lo que puede resultar en problemas de inicio de sesión. Consulta el problema en el siguiente enlace: [**Fallo de conexión o inicio de sesión del cliente**](https://github.com/dani-garcia/vaultwarden/issues/3082).

Dado que este es un servicio autohospedado, debes ser responsable de la seguridad de tus datos. No olvides realizar copias de seguridad regulares de tu base de datos de contraseñas.

## Referencias y Agradecimientos

- [Sitio web oficial](https://github.com/dani-garcia/vaultwarden/wiki)
- [Documentación](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Repositorio de GitHub](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.