# Escribir eficientemente con Markdown

Si estás acostumbrado a escribir con herramientas como Word, es posible que te encuentres con situaciones como estas con frecuencia:

- ¿Dónde está el botón para poner en negrita? ¿Y el de las listas? ¿Cómo puedo insertar imágenes correctamente?
- ¿Qué tamaño de fuente debo usar para los diferentes títulos? ¿Y para el cuerpo del texto?
- Cuando abro el documento con otra versión de Word, los estilos no son los que quiero.

Cuando el tiempo dedicado a la maquetación supera al de la escritura en sí misma, queda claro que este método de escritura no es eficiente. En cambio, el uso de Markdown permite centrarse en la escritura en sí misma, sin que el formato interrumpa el flujo de pensamiento.

## Herramientas

En primer lugar, necesitarás un editor que admita Markdown. Recomiendo usar VS Code o Typora. 
Para la instalación y configuración del software, puedes consultar el tutorial que he escrito: [**Guía de productividad de VS Code - Configuración del entorno**](https://wiki-power.com/VSCode生产力指南-环境配置)

## Sintaxis común

La sintaxis común de Markdown se compone de: **títulos, estilo de texto, citas, código, enlaces, imágenes, listas, tablas, líneas divisorias**, y una vez que las domines, podrás moverte con facilidad.

### Títulos

Para crear títulos, agrega de 1 a 6 símbolos `#` antes del texto del título. El número de niveles de título depende de la cantidad de `#`. En general, la estructura del artículo no debe tener más de 4 niveles.

```markdown
# Título principal

## Título de segundo nivel

### Título de tercer nivel

#### Título de cuarto nivel

……
```

### Estilo de texto

Agrega símbolos alrededor del texto para darle estilo:

|   Estilo   |    Atajo de teclado    | Sintaxis                   | Apariencia             |
| :------: | :--------------: | ---------------------- | -------------------- |
|   Negrita   | `Ctrl`/`⌘` + `B` | `**Texto en negrita**`         | **Texto en negrita**         |
|   Cursiva   | `Ctrl`/`⌘` + `I` | `*Texto en cursiva*`           | _Texto en cursiva_           |
| Negrita y cursiva |                  | `***Texto en negrita y cursiva***` | **_Texto en negrita y cursiva_** |
|  Tachado  |                  | `~~Texto tachado~~`         | ~~Texto tachado~~         |

Nota: El texto en cursiva está diseñado específicamente para el inglés. Para mayor legibilidad y coherencia, no uses cursiva en el texto en español.

### Citas

Puedes usar el símbolo `>` para citar un párrafo:

```markdown
Como dice el mensaje navideño de "The Pirate Bay":

> Creemos que hemos cambiado algo. No solo nosotros, sino todos. Ya no queremos simplemente ejecutar un sitio web, sino buscar un significado. No podemos hacerlo sin tu ayuda. Nuestra historia aún se está escribiendo, así que no saques conclusiones precipitadas.
```

Como dice el mensaje navideño de "The Pirate Bay":

> Creemos que hemos cambiado algo. No solo nosotros, sino todos. Ya no queremos simplemente ejecutar un sitio web, sino buscar un significado. No podemos hacerlo sin tu ayuda. Nuestra historia aún se está escribiendo, así que no saques conclusiones precipitadas.

### Código

#### Código en línea

Puedes usar las comillas invertidas <code>`</code> (en la esquina superior izquierda del teclado) para citar código en línea. Por ejemplo:

```markdown
Descomprime el archivo `hugo.exe` en la carpeta `D:\hugo`.
```

Descomprime el archivo `hugo.exe` en la carpeta `D:\hugo`.

#### Código de varias líneas

Si necesitas varias líneas de código, puedes usar tres comillas invertidas <code>```</code> para encerrar el bloque de código:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210215164653.png)

```c
int fputc(int ch,FILE *f)
{
    HAL_UART_Transmit(&huart1,(uint8_t*)&ch,1,100);
    return ch;
}
```

Donde <code>```c</code> indica que este fragmento de código es en lenguaje C, y se resaltará según la sintaxis de C.

Si desea mostrar el archivo en el que se encuentra el código, puede agregar <code>```c title="stm32f4xx_it.c"</code>, el efecto es el siguiente:

```c title="stm32f4xx_it.c"
int fputc(int ch,FILE *f)
{
    HAL_UART_Transmit(&huart1,(uint8_t*)&ch,1,100);
    return ch;
}
```

### Enlaces

Puede crear enlaces incluyendo el texto del enlace entre corchetes `[ ]` y la URL entre paréntesis `( )`. Por ejemplo:

```markdown
Este sitio web está construido con [Docusaurus](https://v2.docusaurus.io/).
```

Este sitio web está construido con [Docusaurus](https://v2.docusaurus.io/).

### Imágenes

El formato de las imágenes es simplemente agregar un signo `!` más que los enlaces. Por ejemplo:

```markdown
![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-WildWolf/static/uploads/b944219198103ea09f0f02bcb830e9b.png)
```

![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-WildWolf/static/uploads/b944219198103ea09f0f02bcb830e9b.png)

Nota: las imágenes pueden no tener texto de visualización, es decir, `[ ]` puede dejarse en blanco.

### Listas

#### Lista sin orden

Agregar `- ` o `* ` antes del texto crea una lista sin orden (nota: el símbolo debe ir seguido de un espacio, de lo contrario, la representación puede fallar). Por ejemplo:

```markdown
- Elemento de lista
- Elemento de lista
- Elemento de lista
```

- Elemento de lista
- Elemento de lista
- Elemento de lista

#### Lista ordenada

Para crear una lista ordenada, agregue un número a cada línea:

```markdown
1. Elemento de lista uno
2. Elemento de lista dos
3. Elemento de lista tres
```

1. Elemento de lista uno
2. Elemento de lista dos
3. Elemento de lista tres

#### Lista TODO

Para crear una lista TODO, siga el siguiente formato:

```markdown
- [x] Completar cambios
- [ ] Empujar confirmación a GitHub
- [ ] Abrir solicitud de extracción
```

- [x] Completar cambios
- [ ] Empujar confirmación a GitHub
- [ ] Abrir solicitud de extracción

#### Lista anidada

Para anidar listas, simplemente use la tecla Tab para indentar y Shift + Tab para cancelar la indentación:

```markdown
1. Elemento de lista uno
   1. Subelemento de lista uno
   2. Subelemento de lista dos
      - Subsubelemento
      - Subsubelemento
2. Elemento de lista dos
```

1. Elemento de lista uno
   1. Subelemento de lista uno
   2. Subelemento de lista dos
      - Subsubelemento
      - Subsubelemento
2. Elemento de lista dos

### Tablas

Use el símbolo `|` para separar las celdas y el símbolo `-` para separar las filas de la tabla:

```markdown
| nombre     | edad |
| ---------- | --- |
| LearnShare | 12  |
| Mike       | 32  |
```

| nombre     | edad |
| ---------- | --- |
| LearnShare | 12  |
| Mike       | 32  |

Si desea alinear las columnas de la tabla, puede usar el símbolo `:`:

- `:---` o `---` representa alineación a la izquierda
- `:--:` representa alineación centrada
- `---:` representa alineación a la derecha

```markdown
|    nombre    | edad |
| :--------: | --: |
| LearnShare |  12 |
|    Mike    |  32 |
```

|    nombre    | edad |
| :--------: | --: |
| LearnShare |  12 |
|    Mike    |  32 |

### Línea divisoria

Puedes usar el símbolo `---` para generar una línea divisoria y separar diferentes secciones de texto:

```markdown
---
```

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210216123630.png)

## Funciones avanzadas

### Párrafos y saltos de línea

En Markdown, utiliza una línea en blanco antes y después de cada párrafo para separarlos.  
Para hacer un salto de línea dentro del mismo párrafo, simplemente agrega dos espacios al final de la línea.

### Exportar a otros formatos

Si necesitas exportar a PDF, Word, imágenes u otros formatos, puedes usar Pandoc.  
Si estás usando VS Code, puedes usar [**Markdown PDF**](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) para exportar a PDF directamente.

### Escribir artículos de WeChat con Markdown

WeChat utiliza un editor de texto enriquecido, pero puedes usar la herramienta web [**MD2WeChat**](https://md2wechat.wiki-power.com/) para convertir y renderizar tu Markdown y luego pegarlo en el editor de WeChat.

Para más detalles, consulta el artículo [**Cómo escribir de manera eficiente con Markdown**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E7%94%A8Markdown%E5%86%99%E5%85%AC%E4%BC%97%E5%8F%B7%E6%96%87%E7%AB%A0) (en chino).

## Referencias y agradecimientos

- [Métodos personales de edición de Markdown](https://sinnammanyo.cn/About-Markdown/) (en chino)
- [Escribir de manera eficiente con Markdown, para liberarte de los problemas de formato](https://zhuanlan.zhihu.com/p/41893875) (en chino)
- [younghz/Markdown](https://github.com/younghz/Markdown) (en inglés)
- [Learning-Markdown (Introducción a Markdown)](https://xianbai.me/learn-md/index.html) (en inglés)
- [Sintaxis básica de escritura y formato](https://docs.github.com/cn/github/writing-on-github/basic-writing-and-formatting-syntax) (en inglés)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.