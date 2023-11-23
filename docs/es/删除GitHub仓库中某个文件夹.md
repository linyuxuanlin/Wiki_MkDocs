# Eliminar una carpeta específica de un repositorio en GitHub

## Origen del problema

Cuando subes un repositorio local a GitHub, a veces olvidas omitir una carpeta y la envías directamente al repositorio remoto. ¿Cómo puedes eliminar una carpeta en el repositorio de GitHub manteniendo la carpeta local?

## Solución

```shell
git pull origin master        # Primero, descarga el proyecto desde el repositorio remoto
dir                           # Verifica las carpetas disponibles
git rm -r --cached target     # Elimina la carpeta llamada "target"
git commit -m 'Eliminada la carpeta "target"'  # Agrega una explicación de la operación y realiza la confirmación
```

## Referencias y Agradecimientos

- [Eliminar una carpeta específica en GitHub](https://blog.csdn.net/wudinaniya/article/details/77508229)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.