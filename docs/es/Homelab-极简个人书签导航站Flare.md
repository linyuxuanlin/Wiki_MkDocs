# Homelab - Flare, una página de marcadores personales minimalista

![](https://img.wiki-power.com/d/wiki-media/img/20230410170939.png)

**Flare** es una página de marcadores personales ligera, rápida y atractiva, sin dependencias de bases de datos, con datos de aplicaciones completamente abiertos y transparentes, admite edición en línea y tiene más de 6.000 iconos integrados de Material Design.

## Implementación (Docker Compose)

Primero, cree el archivo `compose.yaml` y pegue el siguiente contenido:

```yaml title="compose.yaml"
version: "3.6"

services:
  flare:
    container_name: ${STACK_NAME}_app
    image: soulteary/flare:${APP_VERSION}
    # Para obtener más parámetros de inicio, consulte la documentación en https://github.com/soulteary/docker-flare/blob/main/docs/advanced-startup.md
    ports:
      - ${APP_PORT}:5005
    volumes:
      - ${STACK_DIR}:/app
    command: flare --nologin=0 # Habilita el modo de inicio de sesión de usuario, primero debe establecer el parámetro de inicio `nologin` en `0`
    environment:
      - FLARE_USER= ${APP_USER} # Si se habilita el modo de inicio de sesión de usuario y FLARE_USER no está configurado, el usuario predeterminado es `flare`
      - FLARE_PASS= ${APP_PASS} # Si se habilita el modo de inicio de sesión de usuario y FLARE_USER no está configurado, se generará una contraseña predeterminada y se mostrará en los registros de inicio de la aplicación
    restart: always
```

(Opcional) Se recomienda crear un archivo `.env` en el mismo directorio que `compose.yaml` y personalizar sus variables de entorno. Si no desea utilizar variables de entorno, también puede personalizar sus parámetros directamente en `compose.yaml` (por ejemplo, reemplazar `${STACK_NAME}` con `flare`).

```dotenv title=".env"
STACK_NAME=flare
STACK_DIR=xxx # Ruta personalizada de almacenamiento del proyecto, por ejemplo, ./flare

# flare
APP_VERSION=latest
APP_PORT=xxxx # Puerto de acceso personalizado, elija uno que no esté en uso
APP_USER=xxxx # Nombre de usuario personalizado
APP_PASS=xxxx # Contraseña personalizada
```

Finalmente, ejecute el comando `docker compose up -d` en el mismo directorio que `compose.yaml` para iniciar los contenedores.

## Instrucciones de configuración

Puede modificar las direcciones de las aplicaciones y los marcadores en `apps.yml` y `bookmarks.yml` dentro de `${DIR}/flare`. El contenedor se actualizará en tiempo real. También puede agregar los siguientes parámetros a la URL para depurar:

- Operación de inicio: `/guide`
- Página de configuración: `/settings`
- Edición en línea: `/editor`
- Obtener iconos: `/icons`
- Página de ayuda: `/help`

## Referencias y agradecimientos

- [Sitio web oficial](https://soulteary.com/2022/02/23/building-a-personal-bookmark-navigation-app-from-scratch-flare.html)
- [Documentación / repositorio de GitHub](https://github.com/soulteary/docker-flare)
- [Docker Hub](https://hub.docker.com/r/soulteary/flare/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
