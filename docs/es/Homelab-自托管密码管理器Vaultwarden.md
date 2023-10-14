# Homelab - Gestor de contraseñas autohospedado Vaultwarden

![](https://img.wiki-power.com/d/wiki-media/img/20230304195414.jpg)

**Vaultwarden** es un servidor de Bitwarden autohospedado de terceros que protege y administra las contraseñas de diferentes sitios web con una contraseña maestra, y puede generar contraseñas aleatorias para diferentes sitios web.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `vaultwarden`).

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # Personalice la ruta de almacenamiento del proyecto, por ejemplo, ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # Personalice el puerto de acceso, elija uno que no esté en uso
```

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Vaultwarden requiere https para iniciar sesión de forma predeterminada, se recomienda utilizar un proxy inverso (consulte el artículo [**Homelab - Panel de gestión de certificados de proxy inverso Nginx Proxy Manager**](https://wiki-power.com/es/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/) para obtener información sobre cómo configurar un servidor de proxy inverso).

Cuando se utiliza la extensión del navegador, la aplicación de escritorio o la aplicación móvil, es necesario hacer clic en Configuración en la página de inicio de sesión y configurar la URL del servidor para utilizar el servicio autohospedado correctamente.

Además, las versiones antiguas (inferiores a 1.27.0) de Vaultwarden no son compatibles con la extensión del navegador de Bitwarden, lo que puede impedir el inicio de sesión. Consulte el problema: [**Client fails to connect or login**](https://github.com/dani-garcia/vaultwarden/issues/3082).

Debido a que es un servicio autohospedado, es importante prestar atención a la seguridad de los datos. Recuerde hacer copias de seguridad regulares de la base de datos de contraseñas.

## Referencias y agradecimientos

- [Sitio web oficial](https://github.com/dani-garcia/vaultwarden/wiki)
- [Documentación](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Repositorio de GitHub](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
