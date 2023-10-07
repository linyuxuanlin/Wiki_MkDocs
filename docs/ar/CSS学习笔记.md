# Notas de aprendizaje de CSS

## Llamado

Agregar una hoja de estilo externa en la sección `<head>` de HTML:

```
<link rel="stylesheet" href="xxx.css">
```

Donde `xxx.css` es el archivo CSS en el mismo directorio.  
Nota: Se recomienda usar **hojas de estilo externas vinculadas** (como se muestra arriba).

## Selectores

### Sintaxis básica

```css
selector {
  propiedad: valor;
}
```

### Comparación de varios selectores

| Selector       | Definición                     | Llamado                   | Prioridad |
| :------------- | :----------------------------- | :------------------------| :--------|
| Selector de etiqueta | p {...}                        | &lt;p&gt; ... &lt;/p&gt; | Baja     |
| Selector de clase   | .carrot {...} / p.carrot {...} | class = "carrot"         | Media    |
| Selector de ID      | \#first {...}                  | id = "first"             | Alta     |

### Grupo de selectores

Definir diferentes elementos con el mismo estilo.

```css
h1,
h2,
h3 {
  color: navy;
}
```

## Color

```css
/*Color de fuente*/
color: #56a455;

/*Color de fondo*/
background-color: blue;

/*Transparencia*/
/*Valores de 0.0 a 1.0*/
opacity: 0.5;
```

## Texto

### Tamaño de fuente

| Estilo | Porcentaje | Valor EM |
| :----- | :--------- | :------- |
| h1     | 200%       | 2em      |
| h2     | 150%       | 1.5em    |
| h3     | 133%       | 1.125em  |
| body   | 100%       | 1em      |

```css
/*Tamaño de fuente*/
font-size: 200%;
```

### Selección de fuente

Nota: Los nombres de fuentes compuestos por varias palabras deben ir entre comillas, por ejemplo, 'Courier New'

```css
/*Selección de fuente*/
/*Local*/
font-family: "Courier New", Courier, monospace, nombre_fuente_externa;
/*Externa*/
@font-face {
  font-family: nombre_fuente_externa;
  src: url("dirección_externa");
}
```

### Formato de texto

El valor predeterminado es `normal`

```css
/*Negrita*/
font-weight: bold;

/*Cursiva*/
font-style: italic;

/*Mayúsculas y minúsculas*/
/*uppercase, lowercase, capitalize (primera letra en mayúscula)*/
text-transform: uppercase;

/*Subrayado*/
text-decoration: underline;

/*Tachado*/
text-decoration: line-through;

/*Espacio entre líneas*/
line-height: 1.4em;

/*Alineación*/
/*left, right, center, justify (justificado)*/
text-align: left;
```

### Pseudo-clases

```css
/* Enlace no visitado */
a:link {
  color: #ff0000;
}

/* Enlace visitado */
a:visited {
  color: #00ff00;
}

/* Pase el cursor sobre el enlace */
a:hover {
  color: #ff00ff;
}

/* Enlace seleccionado */
a:active {
  color: #0000ff;
}
```

## Cajas

## Listas, tablas y formularios

Por completar

## Diseño

Por completar

## Normas

### Orden de clasificación de propiedades

- Métodos de visualización y diseño
- Posicionamiento
- Cajas de modelo de caja
  - Margen externo
  - Borde
  - Relleno
- Tamaño
- Estilo de texto
  - Fuente
  - Texto
  - Color de texto
- Fondo
- Contorno
- Opacidad y sombras
- Efectos de animación
  - Transición
  - Transformación
  - Animación
- Otros
  - Pseudo-clases y pseudo-elementos
  - Referencia
  - Consultas de medios

### Lista de orden de propiedades

```css
[
  [
    "display",
    "visibility",
    "float",
    "clear",
    "overflow",
    "overflow-x",
    "overflow-y",
    "clip",
    "zoom"
  ],
  [
    "table-layout",
    "empty-cells",
    "caption-side",
    "border-spacing",
    "border-collapse",
    "list-style",
    "list-style-position",
    "list-style-type",
    "list-style-image"
  ],
  [
    "position",
    "top",
    "right",
    "bottom",
    "left",
    "z-index"
  ],
  [
    "margin",
    "margin-top",
    "margin-right",
    "margin-bottom",
    "margin-left",
    "box-sizing",
    "border",
    "border-width",
    "border-style",
    "border-color",
    "border-top",
    "border-top-width",
    "border-top-style",
    "border-top-color",
    "border-right",
    "border-right-width",
    "border-right-style",
    "border-right-color",
    "border-bottom",
    "border-bottom-width",
    "border-bottom-style",
    "border-bottom-color",
    "border-left",
    "border-left-width",
    "border-left-style",
    "border-left-color",
    "border-radius",
    "border-top-left-radius",
    "border-top-right-radius",
    "border-bottom-right-radius",
    "border-bottom-left-radius",
    "border-image",
    "border-image-source",
    "border-image-slice",
    "border-image-width",
    "border-image-outset",
    "border-image-repeat",
    "padding",
    "padding-top",
    "padding-right",
    "padding-bottom",
    "padding-left",
    "width",
    "min-width",
    "max-width",
    "height",
    "min-height",
    "max-height"
  ],
  [
    "font",
    "font-family",
    "font-size",
    "font-weight",
    "font-style",
    "font-variant",
    "font-size-adjust",
    "font-stretch",
    "font-effect",
    "font-emphasize",
    "font-emphasize-position",
    "font-emphasize-style",
    "font-smooth",
    "line-height",
    "text-align",
    "text-align-last",
    "vertical-align",
    "white-space",
    "text-decoration",
    "text-emphasis",
    "text-emphasis-color",
    "text-emphasis-style",
    "text-emphasis-position",
    "text-indent",
    "text-justify",
    "letter-spacing",
    "word-spacing",
    "text-outline",
    "text-transform",
    "text-wrap",
    "text-overflow",
    "text-overflow-ellipsis",
    "text-overflow-mode",
    "word-wrap",
    "word-break"
  ],
  [
    "color",
    "background",
    "background-color",
    "background-image",
    "background-repeat",
    "background-attachment",
    "background-position",
    "background-position-x",
    "background-position-y",
    "background-clip",
    "background-origin",
    "background-size"
  ],
  [
    "outline",
    "outline-width",
    "outline-style",
    "outline-color",
    "outline-offset",
    "opacity",
    "box-shadow",
    "text-shadow"
  ],
  [
    "transition",
    "transition-delay",
    "transition-timing-function",
    "transition-duration",
    "transition-property",
    "transform",
    "transform-origin",
    "animation",
    "animation-name",
    "animation-duration",
    "animation-play-state",
    "animation-timing-function",
    "animation-delay",
    "animation-iteration-count",
    "animation-direction"
  ],
  [
    "content",
    "quotes",
    "counter-reset",
    "counter-increment",
    "resize",
    "cursor",
    "user-select",
    "nav-index",
    "nav-up",
    "nav-right",
    "nav-down",
    "nav-left",
    "tab-size",
    "hyphens",
    "pointer-events"
  ]
]
```

## Referencias y Agradecimientos

- [Tutorial de introducción a CSS](https://developer.mozilla.org/es/docs/Learn/CSS/First_steps)
- [Tutorial de CSS3](https://waylau.gitbooks.io/css3-tutorial/content/)
- [Especificación de orden de declaración de propiedades CSS](https://wiki.zthxxx.me/wiki/程序语言/CSS/CSS%20 属性声明顺序规范/)

por_reemplazar[1]  
por_reemplazar[2]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.