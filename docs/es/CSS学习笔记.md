# Notas de Estudio de CSS

## Llamado

Para agregar una hoja de estilos externa en el `<head>` de HTML, utiliza el siguiente código:

```html
<link rel="stylesheet" href="xxx.css">
```

Donde `xxx.css` es el nombre del archivo CSS en el mismo directorio.
Ten en cuenta: se recomienda utilizar **hojas de estilos externas vinculadas** (como se muestra arriba).

## Selectores

### Sintaxis Básica

```css
selector {
  propiedad: valor;
}
```

### Comparación de Diferentes Selectores

| Selector         | Definición                     | Uso                        | Prioridad |
| :--------------- | :----------------------------- | :------------------------- | :-------  |
| Selector de Etiqueta | p {...}                 | &lt;p&gt; ... &lt;/p&gt; | Baja     |
| Selector de Clase   | .zanahoria {...} / p.zanahoria {...} | class = "zanahoria"     | Media    |
| Selector de ID      | \#primero {...}                | id = "primero"           | Alta     |

### Grupos de Selectores

Define el mismo estilo para diferentes elementos.

```css
h1,
h2,
h3 {
  color: azul marino;
}
```

## Colores

```css
/* Color del texto */
color: #56a455;

/* Color de fondo */
background-color: azul;

/* Opacidad */
/* Valores entre 0.0 y 1.0 */
opacity: 0.5;
```

## Texto

### Tamaños de Fuente

| Estilo | Porcentaje | Valor EM   |
| :---   | :-----     | :------     |
| h1     | 200%       | 2em         |
| h2     | 150%       | 1.5em       |
| h3     | 133%       | 1.125em     |
| body   | 100%       | 1em         |

```css
/* Tamaño de fuente */
font-size: 200%;
```

### Selección de Fuentes

Nota: Para nombres de fuentes compuestas por múltiples palabras, se deben usar comillas, por ejemplo, 'Courier New'.

```css
/* Selección de fuentes */
/* Fuentes locales */
font-family: "Courier New", Courier, monospace, nombre-de-fuente-externa;

/* Fuentes externas */
@font-face {
  font-family: nombre-de-fuente-externa;
  src: url("dirección-de-fuente-externa");
}
```

### Formateo de Texto

El valor predeterminado es `normal`.

```css
/* Negritas */
font-weight: bold;

/* Cursivas */
font-style: italic;

/* Mayúsculas y minúsculas */
/* uppercase, lowercase, capitalize (con mayúscula inicial) */
text-transform: uppercase;

/* Subrayado */
text-decoration: underline;

/* Tachado */
text-decoration: line-through;

/* Espaciado entre líneas */
line-height: 1.4em;

/* Alineación de texto */
/* left, right, center, justify (justificación) */
text-align: left;
```

### Pseudo-Clases

```css
/* Enlace no visitado */
a:link {
  color: #ff0000;
}

/* Enlace visitado */
a:visited {
  color: #00ff00;
}

/* Desplazarse sobre el enlace */
a:hover {
  color: #ff00ff;
}

/* Enlace activo */
a:active {
  color: #0000ff;
}
```

## Cajas

## Listas, Tablas y Formularios

Por completar.

## Diseño

Por completar.

## Normas

### Orden de Clasificación de Propiedades

- Visualización y Diseño
- Posicionamiento
- Modelo de Caja
  - Márgenes Externos
  - Bordes
  - Relleno
- Dimensiones
- Estilo de Texto
  - Fuente
  - Texto
  - Color de Texto
- Fondo
- Contorno
- Opacidad y Sombras
- Animaciones
  - Transiciones
  - Transformaciones
  - Animaciones
- Otros
  - Pseudo-clases y Pseudo-elementos
  - Citas
  - Consultas de Medios

### Lista de Orden de Propiedades

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

- [Tutorial de Introducción a CSS](https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Getting_started)
- [Tutorial de CSS3 "CSS3 Tutorial"](https://waylau.gitbooks.io/css3-tutorial/content/)
- [Normativa de Orden de Declaración de Propiedades CSS](https://wiki.zthxxx.me/wiki/程序语言/CSS/CSS%20 属性声明顺序规范/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.