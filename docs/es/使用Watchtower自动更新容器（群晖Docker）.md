# Uso de Watchtower para Actualizar Automáticamente Contenedores en Docker de Synology

Aprende a utilizar Watchtower para automatizar la actualización de contenedores en Docker de Synology.

## Descarga la Imagen en la Aplicación Docker de Synology

Abre la suite de Docker en tu dispositivo Synology y descarga la imagen `containrrr/watchtower`.

## Configura Watchtower en el Programador de Tareas

Accede al panel de control de Synology, dirígete a `Tareas Programadas` y crea una nueva tarea programada. Selecciona la opción `Tarea programada de usuario definido` y configura la tarea siguiendo las imágenes a continuación:

![Imagen 1](https://media.wiki-power.com/img/202301092319956.png)

![Imagen 2](https://media.wiki-power.com/img/202301092321592.png)

El script que debes utilizar es el siguiente:

```shell
docker run --rm --name watchtower -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once calibre-web freshrss code-server
```

Ten en cuenta que la parte final del script, `calibre-web freshrss code-server`, representa los nombres de los contenedores que deseas actualizar. Reemplázalos con los nombres de los contenedores que quieras actualizar o déjalo en blanco para actualizar todos los contenedores.

Guarda la configuración y ejecuta el script para programar actualizaciones periódicas de los contenedores Docker.

## Referencias y Agradecimientos

- [Cómo actualizar de manera elegante los contenedores Docker de Synology con una sola orden - Tutorial de Watchtower](https://post.smzdm.com/p/awzggnqp/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
