# Homelab - Code Server, Editor de Código en Línea

![Code Server](https://img.wiki-power.com/d/wiki-media/img/202304132214418.png)

**Code Server** es una aplicación que te permite ejecutar Visual Studio Code en tu navegador web. Su principal ventaja con respecto a la versión de escritorio es que puedes programar en línea desde cualquier dispositivo, incluyendo teléfonos y tabletas que no admiten la instalación directa de Visual Studio Code.

## Implementación (Docker Compose)

Para comenzar, crea un archivo llamado `compose.yaml` y pega el siguiente contenido:

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
    environment: # Se necesita ejecutar con permisos de root, de lo contrario, no se podrán acceder a otros directorios de Docker o al directorio raíz del host.
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} #opcional
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} #opcional
      #- SUDO_PASSWORD_HASH= #opcional
      #- PROXY_DOMAIN=code.wiki-power.com #opcional
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si prefieres no utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `code-server`).

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # Ruta personalizada para almacenar el proyecto, por ejemplo, ./code-server
DATA_DIR_LOCAL=xxx # Directorio local para montar, por ejemplo, /DATA

# code-server
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
APP_PASSWORD=xxx # Contraseña de inicio de sesión
APP_SUDO_PASSWORD=xxx # Contraseña de superusuario

```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar el contenedor configurado.

## Configuración

### Configuración de Git

Después de la instalación, si deseas utilizar Git, puedes configurar tu nombre de usuario y correo electrónico siguiendo las instrucciones en el artículo [**Notas de Aprendizaje de Git**](https://wiki-power.com/es/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE).

### Problemas de Permisos de Lectura y Escritura

Si te encuentras con un error de "Error: EACCES: permission denied" al manipular archivos, puedes abrir una terminal y ejecutar el siguiente comando para otorgar permisos al usuario actual:

```shell
sudo chown -R nombre_de_usuario ruta_del_directorio
```

Por ejemplo, aquí se muestra cómo otorgar todos los permisos del directorio actual al usuario `abc`:

```shell
sudo chown -R abc .
```

### Configuración de la Contraseña de la Cuenta Root

Si necesitas usar la cuenta root, puedes inicializar su contraseña con el siguiente comando:

```shell
sudo passwd root
```

## Referencias y Agradecimientos

- [Official Website](https://coder.com/docs/code-server/latest)
- [Documentation / GitHub Repository](https://github.com/linuxserver/docker-code-server)
- [Docker Hub](https://hub.docker.com/r/linuxserver/code-server)

[Reemplazar[1]]
[Reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.