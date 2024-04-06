# Homelab - Alternativa gratuita para la travesía de red local: Cloudflared

![](https://media.wiki-power.com/img/20230416143051.png)

**Cloudflared** es una solución gratuita para la travesía de red local que permite acceder a máquinas sin una dirección IP pública desde la red externa.

Requisitos:

- Aunque Cloudflared es gratuito, requiere la vinculación de una tarjeta VISA/PayPal.
- El servidor de nombres de dominio (NameServer) debe apuntar a Cloudflare.
- Es necesario habilitar la CDN de Cloudflare (la velocidad de acceso desde China puede ser lenta).

Ventajas:

- No se necesita una dirección IP pública para el servidor.
- No se requieren cortafuegos ni servidores proxy inversos.
- No es necesario registrar el servidor para usar los puertos 80 y 443.
- No se necesita solicitar un certificado SSL por cuenta propia.
- Es gratuito.

Desventajas:

- Velocidad de acceso lenta desde China.
- Dependencia relativa de la plataforma de Cloudflare.

## Implementación (Docker Compose)

En primer lugar, crea un archivo `compose.yaml` y pega el siguiente contenido:

```yaml title="compose.yaml"
version: "3"
services:
  cloudflared:
    container_name: ${STACK_NAME}_app
    image: cloudflare/cloudflared:${APP_VERSION}
    network_mode: host
    restart: unless-stopped
    command: tunnel run
    environment:
      - TUNNEL_TOKEN=${APP_TUNNEL_TOKEN}
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `cloudflared`).

```dotenv title=".env"
STACK_NAME=cloudflared

# cloudflared
APP_VERSION=latest
APP_TUNNEL_TOKEN=xxx # Reemplaza por tu token
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores que has definido.

## Instrucciones de Configuración

Accede al panel de [**Cloudflare Zero Trust**](https://one.dash.cloudflare.com/), selecciona `Access` en la barra lateral izquierda y luego `Tunnels`. Haz clic en "Create a tunnel" para crear un túnel. Ingresa un nombre para el túnel (para distinguir entre distintas máquinas físicas) y guárdalo. Toma nota del token y agrégalo en `compose.yaml`.

Luego, ve al túnel que has creado y en la pestaña "Public Hostname Page," agrega los puertos de los servicios que deseas que se actúen como proxies. Por ejemplo, si tu dominio en Cloudflare es `wiki-power.com` y deseas que el servicio local en el puerto `80` se exponga a través del protocolo `HTTP`, simplemente configúralo de esta manera:

![](https://media.wiki-power.com/img/20230416183438.png)

De esta manera, podrás acceder al puerto local a través de <https://dashboard.wiki-power.com> y Cloudflared se encargará automáticamente de solicitar un certificado SSL, permitiendo el acceso a través de https.

## Referencias y Agradecimientos

- [Sitio web / Documentación oficial](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
- [Repositorio en GitHub](https://github.com/cloudflare/cloudflared)
- [Docker Hub](https://hub.docker.com/r/cloudflare/cloudflared)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
