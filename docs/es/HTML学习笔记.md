# Notas de Estudio sobre HTML

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

Puedes abrir un archivo `.html` y escribir `html:5` para generar esto.

## Etiquetas

Algunas pautas a seguir:

1. Utiliza letras minúsculas para las etiquetas, y asegúrate de que todos los elementos estén debidamente cerrados.
2. Para elementos vacíos, agrega una barra diagonal para cerrarlos, por ejemplo, `<br />`.
3. No utilices la semántica para estilizar; guarda todos los estilos en CSS para separar contenido y presentación.

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
    <h1>Título de Primer Nivel</h1>
    <h2>Título de Segundo Nivel</h2>
    <p>Párrafo</p>

    <!-- Salto de línea -->
    <br />
    <!-- Línea divisoria -->
    <hr />

    <!-- Listas, pueden anidarse -->
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
    <a href="https://www.google.com/">Texto a Mostrar en el Enlace</a>
    <!-- Enlace a una ubicación específica de la página utilizando el atributo ID -->
    <a href="#arriba">Volver Arriba</a>
    <p id="arriba">Arriba</p>
    <!-- Enlace a una ubicación específica en otra página -->
    <a href="http://wiki-power.com/#arriba">Saltar a una ubicación en una página externa</a>

    <!-- Imágenes -->
    <img src="/xx.png" alt="Descripción en caso de que la imagen no se cargue" />

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
            <th scope="row">Ganancia</th>
            <!-- Colspan para combinar celdas y rowspan para combinar filas -->
            <td colspan="2">500</td>
        </tr>
    </table>
```

```markdown
```html
<!-- Formulario - Pendiente de completar -->
<!-- IFrame - Pendiente de completar -->
<!-- Flash/Vídeo/Audio - Pendiente de completar -->

</body>

</html>
```

## Referencias y Agradecimientos

- [Tutorial de HTML | Tutorial de Cómo Hacerlo](http://www.runoob.com/html/html-tutorial.html)
- [Tutorial de HTML en 30 minutos](http://deerchao.net/tutorials/html/html.htm)
- [HTML - Análisis básico de la sección head](https://www.tielemao.com/831.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.