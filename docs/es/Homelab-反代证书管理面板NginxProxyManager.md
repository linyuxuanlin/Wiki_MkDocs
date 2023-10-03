# Homelab - Panel de gestión de certificados de proxy inverso Nginx Proxy Manager

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230408182138.png)

**Nginx Proxy Manager** es un panel gráfico de Nginx que permite a los usuarios configurar fácilmente un proxy inverso y solicitar certificados SSL para sitios web a través de una interfaz web, sin necesidad de conocer los detalles técnicos de Nginx/Letsencrypt.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  nginx-proxy-manager:
    container_name: ${STACK_NAME}_app
    image: "jc21/nginx-proxy-manager:${APP_VERSION}"
    ports:
      - "${APP_PORT}:81" # Dirección del panel
      - "80:80"
      - "443:443"
    volumes:
      - ${STACK_DIR}/data:/data
      - ${STACK_DIR}/letsencrypt:/etc/letsencrypt
    restart: unless-stopped
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar las variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar los parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `nginx-proxy-manager`).

```dotenv title=".env"
STACK_NAME=nginx-proxy-manager
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./nginx-proxy-manager

# nginx-proxy-manager
APP_VERSION=latest
APP_PORT=81 # Por defecto es 81, consulte la documentación para cambiarlo
```

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Credenciales iniciales:

- Email: `admin@example.com`
- Contraseña: `changeme`

Obtenga la dirección IP de Docker:

```shell
ip addr show docker0
```

Nota: Para mejorar la seguridad, se recomienda acceder a los servicios de autohospedaje a través de un proxy inverso, utilizando un subdominio y los puertos 80/443, y cerrar todos los demás puertos en el firewall del servidor público.

## Referencias y agradecimientos

- [Sitio web oficial](https://nginxproxymanager.com)
- [Documentación](https://nginxproxymanager.com/guide)
- [Repositorio de GitHub](https://github.com/NginxProxyManager/nginx-proxy-manager)
- [Docker Hub](https://hub.docker.com/r/jlesage/nginx-proxy-manager)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.