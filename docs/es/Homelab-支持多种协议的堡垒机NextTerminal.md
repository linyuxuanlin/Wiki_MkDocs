# Homelab - Next Terminal, un Bastión que soporta múltiples protocolos

![Imagen](https://media.wiki-power.com/img/20230312001443.png)

**Next Terminal** es una sencilla y práctica pasarela (bastión) que integra una solución de bastión de puerta de enlace de escritorio remoto sin cliente basada en Apache Guacamole. Soporta varios protocolos, como RDP, SSH, VNC, TELNET y Kubernetes, y permite acceder a recursos de la red interna directamente a través de la web con una excelente compatibilidad multiplataforma. También ofrece autenticación de múltiples factores (MFA), funciones de grabación de auditoría y otras capacidades.

## Implementación (Docker Compose)

Primero, crea un archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, sustituir `${STACK_NAME}` por `next-terminal`).

```dotenv title=".env"
STACK_NAME=next-terminal
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./next-terminal

# next-terminal
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
APP_GUACD_HOSTNAME=guacd # Predeterminado
APP_GUACD_PORT=4822 # Predeterminado

# guacd
GUACD_VERSION=latest
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores programados.

## Instrucciones de Configuración

Usuario / Contraseña inicial: `admin`.

## Referencias y Agradecimientos

- [Official Website](https://next-terminal.typesafe.cn/)
- [Documentation](https://next-terminal.typesafe.cn/docs/install/docker-install.html)
- [GitHub Repository](https://github.com/dushixiang/next-terminal)
- [Docker Hub](https://hub.docker.com/r/dushixiang/next-terminal)
- [Demo Site](https://next.typesafe.cn/) (Username: test, Password: test)
- [Next Terminal | Bastión de código abierto, ligero y sencillo](https://blog.samliu.tech/2022/07/22/next-terminal-%E5%BC%80%E6%BA%90-%E8%BD%BB%E9%87%8F-%E7%AE%80%E5%8D%95%E7%9A%84%E5%A0%A1%E5%9E%92%E6%9C%BA/?utm_source=rss&utm_medium=rss&utm_campaign=next-terminal-%25e5%25bc%2580%25e6%25ba%2590-%25e8%25bd%25bb%25e9%2587%258f-%25e7%25ae%2580%25e5%258d%2595%25e7%259a%2584%25e5%25a0%25a1%25e5%259e%2592%25e6%259c%25ba)

[por_reemplazar[1]]
[por_reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
