# Guía de construcción mínima de Hugo

Hugo es un marco para construir sitios web con una velocidad de construcción y implementación extremadamente alta. En cuanto a la instalación y configuración en Windows, la documentación oficial no lo explica detalladamente y los tutoriales de terceros son inconsistentes, por lo que he escrito este tutorial.

## Descarga e instalación

1. Abre la página de [**Releases**](https://github.com/gohugoio/hugo/releases) en GitHub oficial de Hugo.
2. Descarga la última versión (elige `hugo_xxx_Windows-64/32bit.zip`).
3. Descomprime el archivo `hugo.exe` en la carpeta `D:\hugo`.
4. Haz clic con el botón derecho del ratón en un espacio en blanco en el `Explorador de archivos` (es decir, `Mi PC`) y abre las propiedades.
5. Haz clic en `Configuración avanzada del sistema` - `Variables de entorno`, y haz doble clic en `Path` en las variables del sistema.
6. Haz doble clic en una línea en blanco en la interfaz de variables de entorno, agrega `D:\hugo` y haz clic en Aceptar.

Abre la línea de comandos e ingresa la siguiente declaración:

```
hugo version
```

para confirmar si Hugo se ha instalado correctamente (si se ha instalado correctamente, podrás ver el número de versión).

## Crear un sitio

Cambia al directorio correspondiente y usa la siguiente declaración:

```
hugo new site quickstart
```

Esto creará un nuevo sitio de Hugo en una carpeta llamada `quickstart`.

## Agregar un tema

Puedes elegir un tema en la página oficial de [**temas**](https://themes.gohugo.io/).

Simplemente ve a GitHub para descargar la carpeta del tema y descomprimirlo en el directorio `theme` del sitio.

Ejecuta el siguiente comando para agregar el tema al archivo de configuración del sitio:

```
echo 'theme = "nombre de la carpeta del tema"' >> config.toml
```

## Crear un artículo

Usa el siguiente comando para crear un artículo:

```
hugo new posts/my-first-post.md
```

Luego abre el artículo y cambia `draft: true` en `front matter` a `draft: false` para sacarlo del borrador y mostrarlo normalmente.

## Iniciar el servicio de Hugo

Usa el siguiente comando para iniciar el servicio de vista previa local de Hugo:

```
hugo server -D
```

Abre [**http://localhost:1313/**](http://localhost:1313/) para ver la vista previa en tiempo real del sitio (cualquier modificación local se actualizará inmediatamente).

## Implementación local

Usa el siguiente comando:

```
Build static pages
```

para implementar el sitio localmente (se mostrará en la carpeta `public`).

## Referencias y agradecimientos

- [Quick Start · Hugo](https://gohugo.io/getting-started/quick-start/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.