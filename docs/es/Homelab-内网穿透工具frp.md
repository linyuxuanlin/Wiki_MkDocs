# Homelab - Herramienta de Penetración de Red Local frp

![](https://img.wiki-power.com/d/wiki-media/img/20230304195137.png)

**frp** es un método de penetración de red local que te permite exponer los puertos de tus hosts de red local en Internet a través de un servidor con una dirección IP pública. frp admite varios protocolos, como TCP, UDP, HTTP, HTTPS, y más.

## Implementación del servidor frps (Docker Compose)

En primer lugar, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  frps:
    container_name: ${STACK_NAME}_app
    image: snowdreamtech/frps:${APP_VERSION}
    network_mode: host
    volumes:
      - ${STACK_DIR}/frps.ini:/etc/frp/frps.ini
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente dentro de `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `frps`).

```dotenv title=".env"
STACK_NAME=frps
STACK_DIR=xxx # Ruta de almacenamiento del proyecto personalizada, por ejemplo, ./frps

# frps
APP_VERSION=latest
```

En la ruta de almacenamiento de tu proyecto `${STACK_DIR}`, agrega el archivo de configuración `frps.ini`:

```ini title="frps.ini"
[common]
bind_port = 7000 # Puerto de conexión entre el cliente y el servidor, se utilizará al configurar el cliente más adelante.
dashboard_port = 7500 # Puerto del panel de control del servidor
token = ${TOKEN-FRPS} # Contraseña para la conexión entre el cliente y el servidor, personalízala.
dashboard_user = ${USERNAME-FRPS} # Nombre de usuario
dashboard_pwd = ${PASSWORD-FRPS} # Contraseña
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores según la configuración.

Si no deseas utilizar Docker, también puedes consultar este artículo: [**Configuración del servidor·Cómo habilitar el control remoto RDP desde Internet (frp)**](https://wiki-power.com/es/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#_2).

## Implementación del cliente frpc (Docker Compose)

En primer lugar, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3.3"
services:
  frpc:
    container_name: ${STACK_NAME}_app
    image: stilleshan/frpc:${APP_VERSION}
    network_mode: "host"
    volumes:
      - ${STACK_DIR}/frpc.ini:/frp/frpc.ini
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente dentro de `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `replace`).

```dotenv title=".env"
STACK_NAME=replace
STACK_DIR=xxx # Ruta de almacenamiento del proyecto personalizada, por ejemplo, ./replace


```markdown
# Reemplazar
APP_VERSION=última
```

En la ruta de almacenamiento de tu proyecto `${STACK_DIR}`, agrega el archivo de configuración `frps.ini`:

```ini title="frpc.ini"
[común]
server_addr = xx.xx.xx.xx # IP pública del servidor
server_port = 7000 # Mantener el puerto coincidente con el servidor
tls_enable = true
token = ${TOKEN-FRPS} # Mantener el token coincidente con el servidor

[xxx]
type = tcp
remote_port = xx # Número de puerto de acceso público
local_ip = localhost
local_port = xx # Número de puerto interno
```

Finalmente, ejecuta el comando `docker compose up -d` en el directorio de nivel similar a `compose.yaml` para iniciar los contenedores orquestados.

## Referencias y Agradecimientos

- [Repositorio de GitHub · snowdreamtech/frps](https://github.com/snowdreamtech/frp)
- [Repositorio de GitHub · stilleshan/frpc](https://github.com/stilleshan/frpc)
- [Docker Hub · snowdreamtech/frps](https://hub.docker.com/r/snowdreamtech/frps)
- [Docker Hub · stilleshan/frpc](https://hub.docker.com/r/stilleshan/frpc)
- [Cómo realizar control remoto RDP en Internet (frp) [para_ser_reemplazado[3]]% Cómo realizar control remoto RDP en Internet (frp))
- [Acceso a NAS Synology utilizando frp [para_ser_reemplazado[3]]% Acceso a NAS Synology utilizando frp)

[para_ser_reemplazado[1]]
[para_ser_reemplazado[2]]
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.