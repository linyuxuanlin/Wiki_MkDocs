# Creación de presentaciones con reveal.js

## Atajos de teclado

- Siguiente diapositiva: **Espacio**
- Selección de diapositiva: **Teclas de dirección**
- Vista general: **Esc**
- Vista del presentador: **S**
- Pausar presentación / Pantalla en negro: **V/B/.**

## Exportación a PDF

Añade `?print-pdf` al final de la dirección, por ejemplo `http://localhost:8000/?print-pdf`

## Sintaxis de referencia

### Imágenes

```html
<img
  data-src=""
  style="
              width: px;
              margin: 0 auto 1rem auto;
              background: transparent;
            "
/>
```

```html
align="left"
```

### Texto

```html
<p style="white-space: pre-line;"><small> </small></p>
```

### Vídeos

```html
<section
  data-transition="slide"
  data-background="#EAB547"
  data-background-transition="zoom"
>
  <video data-src=""></video>
</section>
```

## Referencias y agradecimientos

- [reveal.js](https://revealjs.com/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.