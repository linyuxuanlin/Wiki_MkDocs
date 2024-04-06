# Homelab - Herramienta de notas fragmentadas memos

![Imagen](https://media.wiki-power.com/img/202304111548420.png)

**memos** es una herramienta de notas de código abierto que puedes alojar por ti mismo. Admite la sintaxis Markdown, permite compartir públicamente, insertar en iframes, gestionar etiquetas, ver en formato de calendario y cuenta con funciones sencillas de migración y respaldo de datos.

## Implementación (Docker Compose)

Primero, crea un archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si no deseas utilizar variables de entorno, también puedes personalizar tus parámetros directamente en `compose.yaml` (por ejemplo, sustituir `${STACK_NAME}` por `memos`).

```dotenv title=".env"
STACK_NAME=memos
STACK_DIR=xxx # Personaliza la ruta de almacenamiento de tu proyecto, por ejemplo, ./memos

# memos
APP_VERSION=latest
APP_PORT=xxxx # Personaliza el puerto de acceso, elige uno que no esté en uso
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar el contenedor configurado.

## Instrucciones de configuración

Para dispositivos móviles iOS/Android, existe la aplicación [**Moe Memos**](https://memos.moe/). También hay clientes de terceros adicionales (como extensiones para navegadores, un bot de Telegram, etc.). Puedes consultar la documentación en [**contribution·memos**](https://github.com/usememos/memos#contribution).

Para importar y exportar datos de usuarios, puedes utilizar la extensión de VS Code llamada [**SQLite**](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite). Descarga y abre el archivo `memos_prod.db` en la carpeta `${DIR}` para realizar operaciones de lectura, escritura, importación y exportación, entre otras. Ten en cuenta que el archivo `memos_prod.db` solo se actualiza cuando se detiene o reinicia el contenedor Docker.

## Referencias y Agradecimientos

- [Sitio web oficial](https://usememos.com/)
- [Documentación](https://usememos.com/docs/install#docker-compose)
- [Repositorio en GitHub](https://github.com/usememos/memos)
- [Docker Hub](https://hub.docker.com/r/neosmemo/memos)
- [Sitio de demostración](https://demo.usememos.com/)

[para_reemplazar[1]]  
[para_reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
