# Homelab - Servidor de domótica inteligente Home Assistant

![](https://media.wiki-power.com/img/202306011647498.png)

**Home Assistant** es un servidor de domótica inteligente de código abierto que puede monitorear todos los dispositivos de tu hogar. Tiene funciones similares a Mi Home y una interfaz amigable y atractiva, además de ser relativamente fácil de configurar.

## Configuración (Docker Compose)

Comienza creando el archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  homeassistant:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/home-assistant/home-assistant:${APP_VERSION}
    ports:
      - ${APP_PORT}:8123
    volumes:
      - ${STACK_DIR}:/config
      - /etc/localtime:/etc/localtime:ro
    privileged: true
    #network_mode: host
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar directamente tus parámetros dentro de `compose.yaml` (por ejemplo, reemplazando `${STACK_NAME}` con `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # Ruta personalizada para el almacenamiento del proyecto, por ejemplo, ./homeassistant

# homeassistant
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté ocupado
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Puedes utilizar la aplicación oficial de Home Assistant en tu dispositivo móvil.

Si al intentar acceder a Home Assistant desde una red externa obtienes el mensaje "400 Bad Request", puedes agregar las siguientes líneas al archivo de configuración `configuration.yaml`:

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 10.0.0.200 # Dirección IP del servidor proxy
    - 172.30.33.0/24 # También se pueden proporcionar direcciones IP con máscara
```

Si no conoces la dirección IP del servidor proxy, puedes intentar acceder a Home Assistant desde una red externa y buscar en los registros (logs) el mensaje de error correspondiente.

## Referencias y agradecimientos

- [Sitio web oficial](https://www.home-assistant.io/)
- [Documentación](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [Repositorio de GitHub](https://github.com/home-assistant)
- [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [Sitio de demostración](https://demo.home-assistant.io/#/lovelace/0)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
