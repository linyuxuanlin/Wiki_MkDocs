# Homelab - Sitio de marcadores personales minimalista Flare

![](https://media.wiki-power.com/img/20230410170939.png)

**Flare** es una página de navegación personal ligera, rápida y atractiva, sin dependencia de bases de datos, con datos de la aplicación completamente abiertos y transparentes, admite edición en línea e incluye más de 6,000 iconos Material Design.

## Implementación (Docker Compose)

Primero, cree un archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3.6"

services:
  flare:
    container_name: ${STACK_NAME}_app
    image: soulteary/flare:${APP_VERSION}
    # Para obtener más opciones de inicio, consulte la documentación en https://github.com/soulteary/docker-flare/blob/main/docs/advanced-startup.md
    ports:
      - ${APP_PORT}:5005
    volumes:
      - ${STACK_DIR}:/app
    command: flare --nologin=0 # Habilita el modo de inicio de sesión de usuario; debe configurar el parámetro de inicio 'nologin' en '0'
    environment:
      - FLARE_USER= ${APP_USER} # Si habilita el modo de inicio de sesión de usuario y no configura FLARE_USER, el usuario predeterminado será 'flare'
      - FLARE_PASS= ${APP_PASS} # Si habilita el modo de inicio de sesión de usuario y no configura FLARE_USER, se generará una contraseña predeterminada y se mostrará en el registro de inicio de la aplicación
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si prefiere no utilizar variables de entorno, también puede personalizar directamente sus parámetros en `compose.yaml` (por ejemplo, reemplace `${STACK_NAME}` con `flare`).

```dotenv title=".env"
STACK_NAME=flare
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./flare

# Flare
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
APP_USER=xxxx # Nombre de usuario personalizado
APP_PASS=xxxx # Contraseña personalizada
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores implementados.

## Instrucciones de configuración

Puede modificar las direcciones de las aplicaciones y marcadores en `${DIR}/flare/apps.yml` y `${DIR}/flare/bookmarks.yml`. Los contenedores se actualizarán en tiempo real. También puede depurar agregando los siguientes parámetros a la URL:

- Guía de uso: `/guide`
- Página de configuración: `/settings`
- Edición en línea: `/editor`
- Obtención de iconos: `/icons`
- Página de ayuda: `/help`

## Referencias y Agradecimientos

- [Sitio web oficial](https://soulteary.com/2022/02/23/building-a-personal-bookmark-navigation-app-from-scratch-flare.html)
- [Documentación / Repositorio de GitHub](https://github.com/soulteary/docker-flare)
- [Docker Hub](https://hub.docker.com/r/soulteary/flare/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
