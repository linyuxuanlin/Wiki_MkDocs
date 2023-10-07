# Homelab - Sistema de almacenamiento en la nube Cloudreve compatible con la nube pública

![](https://f004.backblazeb2.com/file/wiki-media/img/20230304195423.png)

**Cloudreve** es un sistema de archivos en la nube compatible con múltiples controladores de almacenamiento en la nube pública. Admite el almacenamiento local, secundario, Qiniu, Aliyun OSS, Tencent Cloud COS, Upyun, OneDrive, S3 y protocolos compatibles para la conexión con Aria2 para descargas sin conexión, múltiples usuarios, carga / gestión de arrastrar y soltar, vista / edición en línea, WebDAV, entre otros. El uso típico es como un servicio de almacenamiento de imágenes personal o gestión de archivos en la nube.

## Implementación (Docker Compose)

En primer lugar, debemos crear una estructura de directorios. Cambie al directorio donde se encuentra Cloudreve (por ejemplo, `/DATA/AppData/cloudreve`) y ejecute:

```shell
mkdir -vp cloudreve/{uploads,avatar,data} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db \
&& mkdir -p aria2/config \
&& mkdir -p cloudreve/data/aria2 \
&& chmod -R 777 cloudreve/data/aria2 \
&& mkdir data
```

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3.8"
services:
  cloudreve:
    container_name: ${STACK_NAME}_app
    image: cloudreve/cloudreve:${APP_VERSION}
    ports:
      - "${APP_PORT}:5212"
    volumes:
      - temp_data:/data
      - ${STACK_DIR}/cloudreve/uploads:/cloudreve/uploads
      - ${STACK_DIR}/cloudreve/conf.ini:/cloudreve/conf.ini
      - ${STACK_DIR}/cloudreve/cloudreve.db:/cloudreve/cloudreve.db
      - ${STACK_DIR}/cloudreve/avatar:/cloudreve/avatar
    restart: unless-stopped
    depends_on:
      - aria2
  aria2:
    container_name: ${STACK_NAME}_aria2
    image: p3terx/aria2-pro:${ARIA2_VERSION}
    volumes:
      - ${STACK_DIR}/aria2/config:/config
      - ${STACK_DIR}/data:/var/lib/docker/volumes/cloudreve_temp_data/_data
    environment:
      - RPC_SECRET=${ARIA2_RPC_SECRET}
      - RPC_PORT=${ARIA2_RPC_PORT}
    restart: unless-stopped
volumes:
  temp_data:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/temp_data
      o: bind
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `cloudreve`).

```dotenv title=".env"
STACK_NAME=cloudreve
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo ./cloudreve

# cloudreve
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté ocupado

# aria2
ARIA2_VERSION=latest
ARIA2_RPC_SECRET=xxx # Contraseña de ARIA2
ARIA2_RPC_PORT=6800
```

Finalmente, ejecuta el comando `docker compose up -d` en el directorio raíz de `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Al iniciar por primera vez, se creará automáticamente una cuenta de administrador inicial, que se puede encontrar en los registros. Si se pierde, elimina el archivo cloudreve.db en el directorio y reinicia el programa principal para inicializar una nueva cuenta de administrador.

Utilizo la convención de nomenclatura de imágenes: `{año}{mes}{día}{hora}{minuto}{segundo}{ext}`.

## Referencias y agradecimientos

- [Sitio web oficial](https://docs.cloudreve.org/)
- [Documentación](https://docs.cloudreve.org/getting-started/install#docker-compose)
- [Foro](https://forum.cloudreve.org/)
- [Repositorio de GitHub](https://github.com/cloudreve/Cloudreve)
- [Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)
- [Sitio de demostración](https://demo.cloudreve.org/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.