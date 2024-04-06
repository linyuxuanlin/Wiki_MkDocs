# Homelab - Editor de código en línea code-server

![](https://media.wiki-power.com/img/202304132214418.png)

**code-server** es una versión de VS Code que se puede ejecutar en un navegador web. La ventaja de esto es que puedes escribir código en cualquier dispositivo, incluyendo teléfonos móviles y tabletas, que no pueden instalar directamente VS Code en ellos.

## Implementación (Docker Compose)

Primero, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "2.1"
services:
  code-server:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/linuxserver/code-server:${APP_VERSION}
    ports:
      - ${APP_PORT}:8443
    volumes:
      - ${STACK_DIR}/config:/config
      - ${DATA_DIR_LOCAL}:/DATA
    environment: # Necesita ejecutarse con permisos de root, de lo contrario no podrá acceder a otros directorios de Docker o al directorio raíz del host
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} #opcional
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} #opcional
      #- SUDO_PASSWORD_HASH= #opcional
      #- PROXY_DOMAIN=code.wiki-power.com #opcional
      #- DOCKER_MODS=linuxserver/mods:code-server-python3 #opcional, si deseas agregar un entorno de Python
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `code-server`).

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # Ruta personalizada para almacenar el proyecto, por ejemplo, ./code-server
DATA_DIR_LOCAL=xxx # Directorio local montado personalizado, por ejemplo, /DATA

# code-server
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
APP_PASSWORD=xxx # Contraseña de inicio de sesión
APP_SUDO_PASSWORD=xxx # Contraseña de superusuario
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores orquestados.

## Instrucciones de configuración

### Configuración de Git

Después de la instalación, si deseas utilizar Git y configurar tu nombre de usuario y correo electrónico, consulta el artículo [**Git 学习笔记**](https://wiki-power.com/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE) (en chino).

### Problemas de permisos de lectura y escritura

Si encuentras el error `Error: EACCES: permission denied` al operar con archivos, puedes abrir una terminal e ingresar el siguiente comando para otorgar la propiedad al usuario actual:

```shell
sudo chown -R username folder_path
```

Por ejemplo, el siguiente comando otorga la propiedad del directorio actual al usuario `abc`:

```shell
sudo chown -R abc .
```

### Configuración de la contraseña de la cuenta root

Si necesita utilizar la cuenta root, puede utilizar el siguiente comando para inicializar su contraseña:

```shell
sudo passwd root
```

## Referencias y agradecimientos

- [Sitio web oficial](https://coder.com/docs/code-server/latest)
- [Documentación / Repositorio de GitHub](https://github.com/linuxserver/docker-code-server)
- [Docker Hub](https://hub.docker.com/r/linuxserver/code-server)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
