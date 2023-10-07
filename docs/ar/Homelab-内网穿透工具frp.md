# Homelab - Herramienta de penetración de red interna frp

![](https://f004.backblazeb2.com/file/wiki-media/img/20230304195137.png)

**frp** es un método de penetración de red interna. Puede exponer los puertos del host de la red interna a Internet a través de un servidor con una dirección IP pública. frp admite varios protocolos como TCP, UDP, HTTP, HTTPS, etc.

## Implementación del servidor frps (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `frps`).

```dotenv title=".env"
STACK_NAME=frps
STACK_DIR=xxx # Ruta de almacenamiento del proyecto personalizada, por ejemplo, ./frps

# frps
APP_VERSION=latest
```

Agregue el archivo de configuración `frps.ini` en la ruta de almacenamiento de su proyecto `${STACK_DIR}`:

```ini title="frps.ini"
[common]
bind_port = 7000 # Puerto al que se conectan el cliente y el servidor, se utilizará al configurar el cliente más adelante.
dashboard_port = 7500 # Puerto del panel de control del servidor
token = ${TOKEN-FRPS} # Contraseña para la conexión entre el cliente y el servidor, establezca la suya.
dashboard_user = ${USERNAME-FRPS} # Nombre de usuario
dashboard_pwd = ${PASSWORD-FRPS} # Contraseña
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores de la implementación.

Si no desea utilizar Docker, también puede consultar este artículo: [**Configuración del servidor · Cómo implementar el control remoto RDP en Internet (frp)**](https://wiki-power.com/es/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#_2).

## Implementación del cliente frpc (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `replace`).

```dotenv
STACK_NAME=replace
STACK_DIR=xxx # Ruta de almacenamiento del proyecto personalizada, por ejemplo, ./frpc

# frpc
APP_VERSION=latest
```

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator

```dotenv title=".env"
STACK_NAME=reemplazar
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo ./reemplazar

# reemplazar
APP_VERSION=latest
```

Agregue el archivo de configuración `frps.ini` en la ruta de almacenamiento de su proyecto `${STACK_DIR}`:

```ini title="frpc.ini"
[común]
server_addr = xx.xx.xx.xx # IP pública del servidor
server_port = 7000 # Mantener el mismo puerto que el servidor
tls_enable = true
token = ${TOKEN-FRPS} # Mantener el mismo token que el servidor

[xxx]
type = tcp
remote_port = xx # Número de puerto de acceso público
local_ip = localhost
local_port = xx # Número de puerto interno
```

Finalmente, ejecute el comando `docker compose up -d` en el directorio del mismo nivel que `compose.yaml` para iniciar los contenedores de orquestación.

## Referencias y agradecimientos

- [GitHub repo · snowdreamtech/frps](https://github.com/snowdreamtech/frp)
- [GitHub repo · stilleshan/frpc
  ](https://github.com/stilleshan/frpc)
- [Docker Hub · snowdreamtech/frps](https://hub.docker.com/r/snowdreamtech/frps)
- [Docker Hub · stilleshan/frpc](https://hub.docker.com/r/stilleshan/frpc)
- [Cómo implementar el control remoto RDP de Internet (frp)](https://wiki-power.com/es/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [Acceso a Synology NAS con frp](https://wiki-power.com/es/%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/) 

a_reemplazar[1]  
a_reemplazar[2]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.