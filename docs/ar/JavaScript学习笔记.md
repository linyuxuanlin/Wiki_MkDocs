# Notas de estudio de JavaScript

## Llamando a JS externo

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

### Alerta emergente

```javascript
window.alert("Hola");
```

### Manipulación de elementos HTML

```markup
<!DOCTYPE html>
<html>
    <body>
        <h1> Mi primera página web </h1>
        <p id="demo"> Mi primer párrafo </p>
        <script>
            document.getElementById ("demo").innerHTML = "El párrafo ha sido modificado.";
        </script>
    </body>
</html>
```

## Tipos de datos

Creando variables:

```javascript
var carname = "Volvo";
```

**Tipos de valores \ (tipos básicos)**: cadena (String), número (Number), booleano (Boolean), nulo (Null), indefinido (Undefined), símbolo.

**Tipos de datos de referencia**: objeto (Object), matriz (Array), función (Function).

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.