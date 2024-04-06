# Homelab - Stirling-PDF: una versátil caja de herramientas para archivos PDF

![Imagen](https://media.wiki-power.com/img/20230410172939.png)

**Stirling-PDF** es una herramienta para PDFs que puedes alojar tú mismo, con capacidades que incluyen dividir, unir, rotar, extraer páginas, convertir imágenes, reorganizar, agregar o extraer imágenes, establecer contraseñas, definir permisos, añadir marcas de agua, convertir otros archivos a PDF, reconocimiento óptico de caracteres (OCR), editar metadatos y es compatible con el modo oscuro.

## Implementación (Docker Compose)

Para comenzar, crea un archivo `compose.yaml` y pega el siguiente contenido:

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

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar tus variables de entorno. Si prefieres no utilizar variables de entorno, también puedes personalizar los parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `s-pdf`).

```dotenv title=".env"
STACK_NAME=s-pdf
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./s-pdf

# s-pdf
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elige uno que no esté en uso
```

Finalmente, ejecuta el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores orquestados.

## Referencias y Agradecimientos

- [Documentación / Repositorio en GitHub](https://github.com/Frooodle/Stirling-PDF)
- [Docker Hub](https://hub.docker.com/r/frooodle/s-pdf)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
