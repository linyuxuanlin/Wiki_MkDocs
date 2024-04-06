# Homelab - Panel de Gestión de Certificados de Proxy Inverso Nginx Proxy Manager

![Nginx Proxy Manager](https://media.wiki-power.com/img/20230408182138.png)

**Nginx Proxy Manager** es un panel gráfico de Nginx que permite a los usuarios configurar fácilmente proxy inversos y solicitar certificados SSL para sitios web a través de una interfaz web, sin necesidad de conocer en detalle los principios subyacentes de Nginx / Letsencrypt.

## Implementación (Docker Compose)

Primero, cree un archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar directamente los parámetros en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `nginx-proxy-manager`).

```dotenv title=".env"
STACK_NAME=nginx-proxy-manager
STACK_DIR=xxx # Ruta personalizada para el almacenamiento del proyecto, por ejemplo, ./nginx-proxy-manager

# nginx-proxy-manager
APP_VERSION=latest
APP_PORT=81 # Por defecto es 81, cambie según la documentación
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores según la configuración.

## Instrucciones de Configuración

Credenciales iniciales:

- Correo Electrónico: `admin@example.com`
- Contraseña: `changeme`

Obtención de la dirección IP de Docker:

```shell
ip addr show docker0
```

Nota: Para servicios de autohospedaje, se recomienda utilizar proxies inversos y acceder a través de subdominios de segundo nivel (puertos 80/443) y desactivar otros puertos en el firewall de la consola de administración del servidor público para mejorar la seguridad.

## Referencias y Agradecimientos

- [Sitio web oficial](https://nginxproxymanager.com)
- [Documentación](https://nginxproxymanager.com/guide)
- [Repositorio en GitHub](https://github.com/NginxProxyManager/nginx-proxy-manager)
- [Docker Hub](https://hub.docker.com/r/jlesage/nginx-proxy-manager)

[reemplazar[1]]  
[reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
