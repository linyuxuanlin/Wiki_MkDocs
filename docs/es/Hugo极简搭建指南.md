# Guía de Configuración Mínima de Hugo

Hugo es un marco para crear sitios web que se destaca por su velocidad de construcción y despliegue. En cuanto a la instalación y configuración en Windows, la documentación oficial no proporciona detalles exhaustivos y los tutoriales de terceros varían en calidad. Por esta razón, he preparado esta guía.

## Descarga e Instalación

1. Visita la página de [**Releases**](https://github.com/gohugoio/hugo/releases) en el GitHub oficial de Hugo.
2. Elige la versión más reciente para descargar (selecciona `hugo_xxx_Windows-64/32bit.zip`).
3. Descomprime el archivo `hugo.exe` en la carpeta `D:\hugo`.
4. Abre el "Explorador de archivos" (conocido como "Mi PC") y haz clic con el botón derecho en un área vacía para abrir las propiedades.
5. Luego, selecciona `Configuración avanzada del sistema` y después `Variables de entorno`. Haz doble clic en `Path` dentro de las variables del sistema.
6. En la interfaz de variables de entorno, haz doble clic en una línea vacía y agrega `D:\hugo`. Luego, haz clic en "Aceptar".

Abre la línea de comandos y escribe:

```plaintext
hugo version
```

Esto te permitirá confirmar si Hugo se ha instalado con éxito (verás el número de versión si la instalación ha sido exitosa).

## Creación del Sitio

Navega hasta el directorio apropiado y utiliza el siguiente comando:

```plaintext
hugo new site quickstart
```

Esto creará un nuevo sitio Hugo dentro de una carpeta llamada `quickstart`.

## Agregar Temas

Puedes seleccionar temas en la [**página de temas oficial**](https://themes.gohugo.io/).

Descarga la carpeta del tema directamente desde GitHub y descomprímela en la carpeta `theme` de tu sitio.

Luego, ejecuta el siguiente comando para añadir el tema al archivo de configuración del sitio:

```plaintext
echo 'theme = "nombre_de_la_carpeta_del_tema"' >> config.toml
```

## Creación de Artículos

Utiliza el siguiente comando para crear un nuevo artículo:

```plaintext
hugo new posts/mi-primer-articulo.md
```

Después, abre el artículo y cambia `draft: true` a `draft: false` en el "front matter" para sacarlo del estado de borrador y mostrarlo normalmente.

## Iniciar el Servicio de Hugo

Inicia el servicio de vista previa local de Hugo con el siguiente comando:

```plaintext
hugo server -D
```

Abre [**http://localhost:1313/**](http://localhost:1313/) para ver una vista previa en tiempo real del sitio (cualquier modificación local se actualizará de inmediato).

## Despliegue Local

Utiliza el siguiente comando:

```plaintext
Build static pages
```

Esto generará las páginas estáticas del sitio en la carpeta `public` para su despliegue local.

## Referencias y Agradecimientos

- [Quick Start · Hugo](https://gohugo.io/getting-started/quick-start/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.