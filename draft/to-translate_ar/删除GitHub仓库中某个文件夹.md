# Eliminar una carpeta de un repositorio de GitHub

## Origen del problema

Al subir un repositorio local a GitHub, se olvidó de ignorar una carpeta y se hizo push directamente al repositorio remoto. ¿Cómo se puede eliminar la carpeta del repositorio de GitHub sin eliminarla del repositorio local?

## Solución

```shell
git pull origin master        # Primero, se descarga el proyecto del repositorio remoto
dir                           # Se verifica qué carpetas hay
git rm -r --cached target     # Se elimina la carpeta llamada "target"
git commit -m 'Eliminado target'  # Se agrega una descripción de la operación y se confirma
```

## Referencias y agradecimientos

- [Eliminar una carpeta de GitHub](https://blog.csdn.net/wudinaniya/article/details/77508229)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.