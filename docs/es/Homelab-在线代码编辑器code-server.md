# Homelab - Editor de código en línea code-server

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304132214418.png)

**code-server** es un VS Code que se puede ejecutar en un navegador. En comparación con la versión de escritorio, la ventaja es que puedes escribir código en cualquier dispositivo en línea, incluyendo dispositivos como teléfonos móviles y tabletas que no pueden instalar directamente VS Code.

## Implementación (Docker Compose)

Primero, crea el archivo `compose.yaml` y pega el siguiente contenido:

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
    environment: # necesita ejecutarse con permisos de root, de lo contrario no podrá leer otros directorios de docker o el directorio raíz del host
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} #opcional
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} #opcional
      #- SUDO_PASSWORD_HASH= #opcional
      #- PROXY_DOMAIN=code.wiki-power.com #opcional
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `code-server`).

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # ruta personalizada de almacenamiento del proyecto, por ejemplo, ./code-server
DATA_DIR_LOCAL=xxx # directorio local montado personalizado, por ejemplo, /DATA

# code-server
APP_VERSION=latest
APP_PORT=xxxx # puerto de acceso personalizado, elige uno que no esté en uso
APP_PASSWORD=xxx # contraseña de inicio de sesión
APP_SUDO_PASSWORD=xxx # contraseña de permisos de superusuario

```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

### Configurar Git

Después de la instalación, si necesitas usar Git, configura tu nombre de usuario y correo electrónico. Consulta el artículo [**Notas de aprendizaje de Git**](https://wiki-power.com/es/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE) para obtener más información.

### Problemas de permisos de lectura y escritura

Si encuentras el error `Error: EACCES: permission denied` al trabajar con archivos, abre la terminal e ingresa el siguiente comando para otorgar la propiedad al usuario actual:

```shell
sudo chown -R username folder_path
```

Por ejemplo, el siguiente comando otorga la propiedad del directorio actual al usuario `abc`:

```shell
sudo chown -R abc .
```

### Configurar la contraseña de la cuenta root

Si necesitas usar la cuenta root, usa el siguiente comando para configurar su contraseña:

```shell
sudo passwd root
```

## Referencias y Agradecimientos

- [Sitio web oficial](https://coder.com/docs/code-server/latest)
- [Documentación / Repositorio de GitHub](https://github.com/linuxserver/docker-code-server)
- [Docker Hub](https://hub.docker.com/r/linuxserver/code-server)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
