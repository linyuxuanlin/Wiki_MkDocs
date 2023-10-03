# Homelab - Herramienta de notas fragmentadas memos

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111548420.png)

**memos** es una herramienta de notas de autohospedaje de código abierto. Admite sintaxis Markdown, uso compartido público, incrustación de iframes, gestión de etiquetas, vista de calendario, migración de datos simple y funciones de copia de seguridad.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3.0"
services:
  memos:
    container_name: ${STACK_NAME}_app
    image: neosmemo/memos:${APP_VERSION}
    ports:
      - ${APP_PORT}:5230
    volumes:
      - ${STACK_DIR}:/var/opt/memos
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `memos`).

```dotenv title=".env"
STACK_NAME=memos
STACK_DIR=xxx # Ruta de almacenamiento personalizada del proyecto, por ejemplo, ./memos

# memos
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, simplemente elija uno que no esté en uso
```

Por último, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Aplicación móvil iOS/Android: [**Moe Memos**](https://memos.moe/). Para obtener más clientes de terceros (como mini programas de WeChat, extensiones de navegador, bots de Telegram, etc.), consulte la documentación [**contribution·memos**](https://github.com/usememos/memos#contribution).

Para importar y exportar datos de usuario, puede utilizar la extensión de VS Code [**SQLite**](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite), descargar y abrir `memos_prod.db` en `${DIR}` para realizar operaciones de agregar, eliminar, modificar y consultar, así como para realizar copias de seguridad de importación y exportación. Tenga en cuenta que el archivo `memos_prod.db` solo se actualizará cuando el contenedor de Docker se cierre o reinicie.

## Referencias y agradecimientos

- [Sitio web oficial](https://usememos.com/)
- [Documentación](https://usememos.com/docs/install#docker-compose)
- [Repositorio de GitHub](https://github.com/usememos/memos)
- [Docker Hub](https://hub.docker.com/r/neosmemo/memos)
- [Sitio de demostración](https://demo.usememos.com/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.