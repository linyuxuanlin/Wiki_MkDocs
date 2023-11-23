# Notas de Estudio de JavaScript

## Llamando a JavaScript Externo

```markup
<!DOCTYPE html>
<html>
    <head>
        <script src="xx1.js"></script>
    </head>
    <body>
        <script src="xx2.js"></script>
    </body>
</html>
```

## Salida

### Mostrar una Alerta

```javascript
window.alert("Hola");
```

### Manipulación de Elementos HTML

```markup
<!DOCTYPE html>
<html>
    <body>
        <h1> Mi Primera Página Web </h1>
        <p id="demo"> Mi primer párrafo </p>
        <script>
            document.getElementById ("demo").innerHTML = "El párrafo ha sido modificado.";
        </script>
    </body>
</html>
```

## Tipos de Datos

Creación de Variables:

```javascript
var nombreCoche = "Volvo";
```

**Tipos de Valor (Tipos Primitivos)**: Cadena (String), Número (Number), Booleano (Boolean), Nulo (Null), Indefinido (Undefined), Símbolo (Symbol).

**Tipos de Datos por Referencia**: Objeto (Object), Arreglo (Array), Función (Function).

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.