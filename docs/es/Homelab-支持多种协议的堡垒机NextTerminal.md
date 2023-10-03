# Homelab - Next Terminal, un bastión de múltiples protocolos

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230312001443.png)

**Next Terminal** es un bastión (jump server) fácil de usar e integrado con Apache Guacamole, un gateway de escritorio remoto sin cliente, que admite múltiples protocolos como RDP, SSH, VNC, TELNET, Kubernetes, y puede acceder a recursos de la red interna directamente a través de la web, con una excelente compatibilidad multiplataforma. Admite autenticación multifactor (MFA), grabación de auditoría y otras funciones de registro.

## Implementación (Docker Compose)

Primero, cree un archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3.3"
services:
  guacd:
    container_name: ${STACK_NAME}_guacd
    image: dushixiang/guacd:${GUACD_VERSION}
    volumes:
      - ${STACK_DIR}/data:/usr/local/next-terminal/data
    restart: always
  next-terminal:
    container_name: ${STACK_NAME}_app
    image: dushixiang/next-terminal:${APP_VERSION}
    environment:
      DB: sqlite
      GUACD_HOSTNAME: ${APP_GUACD_HOSTNAME}
      GUACD_PORT: ${APP_GUACD_PORT}
    ports:
      - ${APP_PORT}:8088
    volumes:
      - /etc/localtime:/etc/localtime
      - ${STACK_DIR}/data:/usr/local/next-terminal/data
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar las variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `next-terminal`).

```dotenv title=".env"
STACK_NAME=next-terminal
STACK_DIR=xxx # Personalice la ruta de almacenamiento del proyecto, por ejemplo, ./next-terminal

# next-terminal
APP_VERSION=latest
APP_PORT=xxxx # Personalice el puerto de acceso, elija uno que no esté ocupado
APP_GUACD_HOSTNAME=guacd # Por defecto
APP_GUACD_PORT=4822 # Por defecto

# guacd
GUACD_VERSION=latest
```

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Cuenta / contraseña inicial: `admin`.

## Referencias y agradecimientos

- [Sitio web oficial](https://next-terminal.typesafe.cn/)
- [Documentación](https://next-terminal.typesafe.cn/docs/install/docker-install.html)
- [Repositorio de GitHub](https://github.com/dushixiang/next-terminal)
- [Docker Hub](https://hub.docker.com/r/dushixiang/next-terminal)
- [Sitio de demostración](https://next.typesafe.cn/) (nombre de usuario: test, contraseña: test)
- [Next Terminal | Fuente abierta, ligera y sencilla de bastión](https://blog.samliu.tech/2022/07/22/next-terminal-%E5%BC%80%E6%BA%90-%E8%BD%BB%E9%87%8F-%E7%AE%80%E5%8D%95%E7%9A%84%E5%A0%A1%E5%9E%92%E6%9C%BA/?utm_source=rss&utm_medium=rss&utm_campaign=next-terminal-%25e5%25bc%2580%25e6%25ba%2590-%25e8%25bd%25bb%25e9%2587%258f-%25e7%25ae%2580%25e5%258d%2595%25e7%259a%2584%25e5%25a0%25a1%25e5%259e%2592%25e6%259c%25ba)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.