# Notas de Estudio de HTML

## Estructura Básica

```markup
<!DOCTYPE html>
<html lang="es">
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

Puedes abrir un archivo `.html` y simplemente escribir `html:5` para obtener esto.

## Etiquetas

Algunas convenciones:

1. Las etiquetas se escriben en minúsculas y los elementos deben cerrarse.
2. Para elementos vacíos, añade una barra diagonal para cerrarlos, por ejemplo, `<br />`.
3. No uses semántica en HTML, todos los estilos deben definirse en CSS para separar contenido y presentación.

```markup
<!DOCTYPE html>
<html lang="es">

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

    <!-- Salto de línea -->
    <br />
    <!-- Línea horizontal -->
    <hr />

    <!-- Listas anidadas -->
    <!-- Lista ordenada -->
    <ol>
        <li>Primer ítem</li>
        <li>Segundo ítem</li>
    </ol>
    <!-- Lista desordenada -->
    <ul>
        <li>Primer ítem</li>
        <li>Segundo ítem</li>
    </ul>

    <!-- Enlaces -->
    <a href="https://www.google.com/">Texto del enlace</a>
    <!-- Enlace a una posición específica en la página usando el atributo ID -->
    <a href="#arriba">Volver arriba</a>
    <p id="arriba">Arriba</p>
    <!-- Enlace a una posición específica en otra página -->
    <a href="http://wiki-power.com/#arriba">Ir a una ubicación específica en una página externa</a>

    <!-- Imágenes -->
    <img src="/xx.png" alt="Texto alternativo en caso de que la imagen no se cargue" />

    <!-- Tablas -->
    <table>
        <!-- Primera fila -->
        <tr>
            <!-- Primera columna -->
            <th></th>
            <!-- Segunda columna -->
            <th scope="col">Sábado</th>
            <!-- Tercera columna -->
            <th scope="col">Domingo</th>
        </tr>
        <!-- Segunda fila -->
        <tr>
            <th scope="row">Cantidad</th>
            <td>120</td>
            <td>135</td>
        </tr>
        <!-- Tercera fila -->
        <tr>
            <th scope="row">Ingresos</th>
            <!-- Atraviesa columnas con "colspan" o filas con "rowspan" -->
            <td colspan="2">500</td>
        </tr>
    </table>


```html
<!-- Formulario, por completar -->
<!-- Marco (iframe), por completar -->
<!-- Contenido flash/vídeo/audio, por completar -->

</body>

</html>
```

## Referencias y Agradecimientos

- [Tutorial de HTML | Código del Novato](http://www.runoob.com/html/html-tutorial.html)
- [Tutorial de HTML en 30 minutos](http://deerchao.net/tutorials/html/html.htm)
- [HTML - Análisis breve de la sección head](https://www.tielemao.com/831.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.