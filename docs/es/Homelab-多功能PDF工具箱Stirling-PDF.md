# Homelab - Caja de herramientas PDF multifuncional Stirling-PDF

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410172939.png)

**Stirling-PDF** es un paquete de herramientas PDF autoalojado que incluye funciones como la división, fusión, rotación, extracción de páginas, conversión de imágenes, reordenamiento, agregado/extracción de imágenes, agregado/eliminación de contraseñas, configuración de permisos, agregado de marcas de agua, conversión de otros archivos a PDF, reconocimiento de texto OCR, edición de metadatos y soporte para modo oscuro.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3.3"
services:
  s-pdf:
    container_name: ${STACK_NAME}_app
    image: frooodle/s-pdf:${APP_VERSION}
    ports:
      - ${APP_PORT}:8080
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` por `s-pdf`).

```dotenv title=".env"
STACK_NAME=s-pdf
STACK_DIR=xxx # Ruta personalizada para almacenar el proyecto, por ejemplo, ./s-pdf

# s-pdf
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Referencias y agradecimientos

- [Documentación / Repositorio de GitHub](https://github.com/Frooodle/Stirling-PDF)
- [Docker Hub](https://hub.docker.com/r/frooodle/s-pdf)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.