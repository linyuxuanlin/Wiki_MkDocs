# Cómo actualizar automáticamente los contenedores en Docker de Synology utilizando Watchtower

Utilice Watchtower para actualizar automáticamente los contenedores en Docker de Synology.

## Descargar la imagen en la aplicación Docker de Synology

Abra el paquete Docker de Synology y descargue la imagen `containrrr/watchtower`.

## Configurar Watchtower en la tarea programada

Abra el `Panel de control` de Synology - `Tarea programada` - `Agregar` - `Tarea programada` - `Script definido por el usuario`, y luego complete la configuración según las siguientes imágenes:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202301092319956.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202301092321592.png)

El script es el siguiente:

```shell
docker run --rm --name watchtower -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once calibre-web freshrss code-server
```

Tenga en cuenta que `calibre-web freshrss code-server` al final del script son los nombres de los contenedores que se deben actualizar. Reemplácelos con los nombres de los contenedores que desea actualizar o déjelos en blanco para actualizar todos los contenedores.

Guarde y ejecute el script para actualizar los contenedores de Docker de forma programada.

## Referencias y agradecimientos

- [Cómo actualizar los contenedores de Docker de Synology de manera elegante con un solo comando - Tutorial de Watchtower](https://post.smzdm.com/p/awzggnqp/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
