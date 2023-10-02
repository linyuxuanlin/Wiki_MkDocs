# Homelab - Alternativa gratuita a la conexión a través de la red interna: Cloudflared

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416143051.png)

**Cloudflared** es una solución gratuita para la conexión a través de la red interna, utilizada para acceder a máquinas sin dirección IP pública desde la red externa.

Requisitos:

- Aunque Cloudflared es gratuito, se requiere una cuenta VISA/PayPal.
- El servidor de nombres de dominio (DNS) debe apuntar a Cloudflare.
- Se debe habilitar el CDN de Cloudflare (la velocidad de acceso desde China es lenta).

Ventajas:

- No se requiere una dirección IP pública para el servidor.
- No se requiere un firewall ni un servidor proxy inverso.
- Se pueden utilizar los puertos 80 y 443 sin necesidad de registro.
- No se requiere una solicitud de certificado SSL.
- Es gratuito.

Desventajas:

- La velocidad de acceso desde China es lenta.
- Depende en cierta medida de la plataforma de Cloudflare.

## Implementación (Docker Compose)

Primero, cree un archivo `compose.yaml` y pegue el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `cloudflared`).

```dotenv title=".env"
STACK_NAME=cloudflared

# cloudflared
APP_VERSION=latest
APP_TUNNEL_TOKEN=xxx # Reemplace con su token
```

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Acceda al panel [**Cloudflare Zero Trust**](https://one.dash.cloudflare.com/), seleccione `Access` - `Tunnels` en la barra lateral izquierda y haga clic en `Create a tunnel` para crear un túnel. Escriba un nombre para el túnel (para distinguir entre diferentes máquinas físicas) y guarde. Anote el token y escríbalo en `compose.yaml`.

A continuación, haga clic en el túnel que ha creado y, en la pestaña `Public Hostname Page`, agregue el puerto que desea utilizar como proxy. Por ejemplo, si su dominio está vinculado a Cloudflare y es `wiki-power.com`, y desea utilizar el puerto `80` y el protocolo `HTTP` en su máquina local, simplemente escriba lo siguiente:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416183438.png)

De esta manera, podrá acceder al puerto local a través de <https://dashboard.wiki-power.com>, y automáticamente se solicitará un certificado SSL para el acceso a través de https desde la red externa.

## Referencias y agradecimientos

- [Sitio web / Documentación oficial](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
- [Repositorio de GitHub](https://github.com/cloudflare/cloudflared)
- [Docker Hub](https://hub.docker.com/r/cloudflare/cloudflared)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.