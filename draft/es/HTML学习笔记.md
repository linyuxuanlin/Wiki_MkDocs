# Notas de aprendizaje de HTML

## Estructura básica

```markup
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Título</title>
</head>
<body>

</body>
</html>
```

Puede abrir un archivo `.html` y escribir `html:5` para llamarlo.

## Declaraciones

Algunas convenciones:

1. Las etiquetas se escriben en minúsculas y los elementos deben cerrarse.
2. Los elementos vacíos deben cerrarse con una barra diagonal, por ejemplo `<br />`.
3. No se utiliza la semántica, todos los estilos se almacenan en CSS, separando el contenido de los estilos.

```markup
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Título</title>
</head>

<body>
    <h1>Título de nivel 1</h1>
    <h2>Título de nivel 2</h2>
    <p>Párrafo</p>

    <!--Salto de línea-->
    <br />
    <!--Línea divisoria-->
    <hr />

    <!--Listas, pueden ser anidadas-->
    <!--Lista ordenada-->
    <ol>
        <li>Primer elemento</li>
        <li>Segundo elemento</li>
    </ol>
    <!--Lista desordenada-->
    <ul>
        <li>Primer elemento</li>
        <li>Segundo elemento</li>
    </ul>

    <!--Enlaces-->
    <a href="https://www.google.com/">Texto del enlace</a>
    <!--Enlace a una ubicación específica de la página, utilizando el atributo ID-->
    <a href="#top">Volver arriba</a>
    <p id="top">Arriba</p>
    <!--Enlace a una ubicación específica en otra página-->
    <a href="http://wiki-power.com/#top">Saltar a una ubicación en otra página</a>

    <!--Imágenes-->
    <img src="/xx.png" alt="Texto alternativo cuando no se puede cargar la imagen" />

    <!--Tablas-->
    <table>
        <!--Primera fila-->
        <tr>
            <!--Primera columna-->
            <th></th>
            <!--Segunda columna-->
            <th scope="col">Sábado</th>
            <!--Tercera columna-->
            <th scope="col">Domingo</th>
        </tr>
        <!--Segunda fila-->
        <tr>
            <th scope="row">Cantidad</th>
            <td>120</td>
            <td>135</td>
        </tr>
        <!--Tercera fila-->
        <tr>
            <th scope="row">Ingresos</th>
            <!--Columna que abarca varias celdas, utilizando colspan y rowspan-->
            <td colspan="2">500</td>
        </tr>
    </table>

# Introducción a HTML

HTML (Lenguaje de Marcado de Hipertexto) es el lenguaje de marcado estándar utilizado para crear páginas web. Con HTML, se pueden crear documentos estructurados y enriquecidos con contenido multimedia, como imágenes, videos y audio.

## Estructura básica de un documento HTML

Un documento HTML comienza con una etiqueta `<!DOCTYPE html>` que indica al navegador que se está utilizando la última versión de HTML. Luego, la estructura básica de un documento HTML consta de dos partes principales: la sección `head` y la sección `body`.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Título de la página</title>
</head>
<body>
  Contenido de la página
</body>
</html>
```

La sección `head` contiene información sobre la página, como el título, la descripción y las palabras clave. La sección `body` contiene el contenido real de la página, como texto, imágenes y otros elementos multimedia.

## Etiquetas HTML comunes

Las etiquetas HTML se utilizan para estructurar y dar formato al contenido de la página. Algunas etiquetas comunes incluyen:

- `<h1>` a `<h6>`: encabezados de diferentes tamaños
- `<p>`: párrafos de texto
- `<a>`: enlaces a otras páginas o recursos
- `<img>`: imágenes
- `<ul>` y `<ol>`: listas sin ordenar y ordenadas, respectivamente
- `<table>`: tablas de datos
- `<form>`: formularios para recopilar información del usuario

## Añadiendo multimedia

HTML también permite la inclusión de contenido multimedia en una página web. Algunos elementos comunes incluyen:

- `<iframe>`: permite incrustar una página web dentro de otra página web
- `<video>`: permite la inclusión de videos
- `<audio>`: permite la inclusión de archivos de audio
- `<img>`: permite la inclusión de imágenes

## Referencias y agradecimientos

- [Tutorial de HTML | Tutorial de novatos](http://www.runoob.com/html/html-tutorial.html)
- [Tutorial de HTML en 30 minutos](http://deerchao.net/tutorials/html/html.htm)
- [HTML - Análisis superficial de la sección de encabezado](https://www.tielemao.com/831.html)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.