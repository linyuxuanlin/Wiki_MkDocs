# Homelab - Solución de escritorio remoto de código abierto RustDesk

![](https://media.wiki-power.com/img/20230531212854.png)

**RustDesk** es una solución de escritorio remoto de código abierto que permite el acceso remoto a través de clientes en múltiples plataformas en redes internas. En este artículo, se explicará cómo configurar tu propio servidor en una red pública.

## Implementación (Docker Compose)

Primero, crea el archivo `compose.yaml` y copia el siguiente contenido:

```yaml title="compose.yaml"
version: "3"

networks:
  rustdesk-net:
    external: false

services:
  hbbs:
    container_name: ${STACK_NAME}_hbbs
    ports:
      - 21115:21115
      - 21116:21116
      - 21116:21116/udp
      - 21118:21118
    image: rustdesk/rustdesk-server:${APP_VERSION}
    command: hbbs -r ${STACK_DOMAIN}:21117 -k _
    volumes:
      - ${STACK_DIR}/data:/root
    networks:
      - rustdesk-net
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: ${STACK_NAME}_hbbr
    ports:
      - 21117:21117
      - 21119:21119
    image: rustdesk/rustdesk-server:${APP_VERSION}
    command: hbbr -k _
    volumes:
      - ${STACK_DIR}/data:/root
    networks:
      - rustdesk-net
    restart: unless-stopped
```

En este docker compose, se han organizado dos servicios:

- hbbs: Servidor de registro de ID de RustDesk
- hbbr: Servidor de retransmisión de RustDesk

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si prefieres no usar variables de entorno, también puedes personalizar directamente tus parámetros dentro de `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `rustdesk-server`).

```dotenv title=".env"
STACK_NAME=rustdesk-server
STACK_DIR=xxx # Ruta de almacenamiento personalizada para el proyecto, por ejemplo, ./rustdesk-server
STACK_DOMAIN=xxx # Dominio o IP donde se desplegará el servidor RustDesk

# rustdesk-server
APP_VERSION=latest
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores configurados.

## Instrucciones de configuración

Si te encuentras con el error "Registered email required (-m option). Please pay and register on https://rustdesk.com/server...", podría ser porque no has descargado la versión más reciente del paquete. Para solucionarlo:

1. En <https://hub.docker.com/r/rustdesk/rustdesk-server/tags>, busca el número de identificación DIGEST de la versión más reciente (por ejemplo, `83e259792b50`).
2. En tu computadora local, utiliza el comando `docker image pull rustdesk/rustdesk-server:latest@sha256:83e259792b50` para descargar la última versión, asegúrate de reemplazar los últimos caracteres con los correspondientes a tu versión.

## Referencias y Agradecimientos

- [Sitio web oficial](https://rustdesk.com/)
- [Documentación](https://rustdesk.com/docs/en/self-host/)
- [Repositorio en GitHub](https://github.com/rustdesk/rustdesk)
- [Docker Hub](https://hub.docker.com/r/rustdesk/rustdesk-server)
- [Cómo autohospedar un servidor de RustDesk utilizando Docker](https://developer.aliyun.com/article/1299504)
- [Autohospedaje](https://rustdesk.com/docs/zh-cn/self-host/rustdesk-server-oss/install/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.