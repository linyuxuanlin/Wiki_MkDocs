# CSS Study Notes

## Invocation

To include an external stylesheet in your HTML, place the following code within the `<head>` section:

```html
<link rel="stylesheet" href="xxx.css">
```

Here, `xxx.css` refers to the CSS file in the same directory. Note: It is advisable to use **external style sheets** whenever possible (as shown above).

## Selectors

### Basic Syntax

```css
selector {
  property: value;
}
```

### Comparison of Various Selectors

| Selector       | Definition                             | Invocation                  | Specificity |
| :------------- | :------------------------------------- | :-------------------------- | :---------- |
| Tag Selector   | p {...}                                | &lt;p&gt; ... &lt;/p&gt;     | Low         |
| Class Selector | .carrot {...} / p.carrot {...}         | class = "carrot"             | Medium      |
| ID Selector    | \#first {...}                          | id = "first"                 | High        |

### Selector Groups

Define the same styles for different elements.

```css
h1,
h2,
h3 {
  color: navy;
}
```

## Colors

```css
/* Font Color */
color: #56a455;

/* Background Color */
background-color: blue;

/* Opacity */
/* Values between 0.0 and 1.0 */
opacity: 0.5;
```

## Text

### Font Size

| Style | Percentage | EM Value |
| :---  | :--------  | :------- |
| h1    | 200%      | 2em      |
| h2    | 150%      | 1.5em    |
| h3    | 133%      | 1.125em  |
| body  | 100%      | 1em      |

```css
/* Font Size */
font-size: 200%;
```

### Font Selection

Note: For font names with multiple words, use quotation marks, e.g., 'Courier New'.

```css
/* Font Selection */
/* Local Fonts */
font-family: "Courier New", Courier, monospace, External Font Name;
/* External Fonts */
@font-face {
  font-family: External Font Name;
  src: url("External Font URL");
}
```

### Text Formatting

The default value is `normal`.

```css
/* Bold */
font-weight: bold;

/* Italic */
font-style: italic;

/* Letter Case */
/* uppercase, lowercase, capitalize (first letter capitalized) */
text-transform: uppercase;

/* Underline */
text-decoration: underline;

/* Strikethrough */
text-decoration: line-through;

/* Line Height */
line-height: 1.4em;

/* Alignment */
/* left, right, center, justify (justified) */
text-align: left;
```

### Pseudo-Classes

```css
/* Unvisited Link */
a:link {
  color: #ff0000;
}

/* Visited Link */
a:visited {
  color: #00ff00;
}

/* Hovered Link */
a:hover {
  color: #ff00ff;
}

/* Active Link */
a:active {
  color: #0000ff;
}
```

## Boxes

## Lists, Tables, and Forms

To be added.

## Layout

To be added.

## Guidelines

### Order of Property Categories

- Display & Layout
- Positioning
- Box Model
  - Margin
  - Border
  - Padding
- Dimensions
- Text Styling
  - Font
  - Text
  - Text Color
- Background
- Outline
- Transparency & Shadows
- Animation
  - Transitions
  - Transformations
  - Keyframes
- Miscellaneous
  - Pseudo-classes & Pseudo-elements
  - Quotes
  - Media Queries

### Property Order List

Certainly, here is the translated content in colloquial yet professional English:

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

I hope this translation meets your requirements. If you have any further requests or questions, feel free to ask.

## References and Acknowledgments

- [CSS Beginner's Guide](https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Getting_started)
- [CSS3 Tutorial](https://waylau.gitbooks.io/css3-tutorial/content/)
- [CSS Property Declaration Order Guidelines](https://wiki.zthxxx.me/wiki/程序语言/CSS/CSS%20属性声明顺序规范/)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.