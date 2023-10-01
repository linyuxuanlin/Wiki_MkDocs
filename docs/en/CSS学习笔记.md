# CSS Study Notes

## Calling

Add an external style sheet in the `<head>` of HTML:

```
<link rel="stylesheet" href="xxx.css">
```

Here, `xxx.css` is the CSS file in the same directory.  
Note: Use **link-style external style sheets** as much as possible (as above).

## Selectors

### Basic Syntax

```css
selector {
  property: value;
}
```

### Comparison of Several Selectors

| Selector      | Definition                     | Calling                   | Priority |
| :------------ | :----------------------------- | :------------------------| :------- |
| Tag Selector  | p {...}                        | &lt;p&gt; ... &lt;/p&gt; | Low      |
| Class Selector| .carrot {...} / p.carrot {...} | class = "carrot"         | Medium   |
| ID Selector   | \#first {...}                  | id = "first"             | High     |

### Selector Group

Define different elements with the same style.

```css
h1,
h2,
h3 {
  color: navy;
}
```

## Color

```css
/*Font color*/
color: #56a455;

/*Background color*/
background-color: blue;

/*Opacity*/
/*Value 0.0 ~ 1.0*/
opacity: 0.5;
```

## Text

### Font Size

| Style | Percentage | EM Value |
| :---- | :--------- | :-------|
| h1    | 200%       | 2em     |
| h2    | 150%       | 1.5em   |
| h3    | 133%       | 1.125em |
| body  | 100%       | 1em     |

```css
/*Font size*/
font-size: 200%;
```

### Font Selection

Note: Font names consisting of multiple words should be enclosed in quotation marks, e.g. 'Courier New'

```css
/*Font selection*/
/*Local*/
font-family: "Courier New", Courier, monospace, external font name;
/*External*/
@font-face {
  font-family: external font name;
  src: url("external address");
}
```

### Text Formatting

Default value is `normal`

```css
/*Bold*/
font-weight: bold;

/*Italic*/
font-style: italic;

/*Capitalization*/
/*uppercase, lowercase, capitalize (first letter capitalized)*/
text-transform: uppercase;

/*Underline*/
text-decoration: underline;

/*Strikethrough*/
text-decoration: line-through;

/*Line height*/
line-height: 1.4em;

/*Alignment*/
/*left, right, center, justify (justified)*/
text-align: left;
```

### Pseudo-classes

```css
/* Unvisited link */
a:link {
  color: #ff0000;
}

/* Visited link */
a:visited {
  color: #00ff00;
}

/* Mouse over link */
a:hover {
  color: #ff00ff;
}

/* Selected link */
a:active {
  color: #0000ff;
}
```

## Box

## Lists, Tables, and Forms

To be added

## Layout

To be added

## Standards

### Property Classification Order

- Display & Layout
- Positioning
- Box Model
  - Margin
  - Border
  - Padding
- Size
- Text Style
  - Font
  - Text
  - Text Color
- Background
- Outline
- Opacity & Shadows
- Animation
  - Transition
  - Transform
  - Animation
- Others
  - Pseudo-classes & Pseudo-elements
  - Quotes
  - Media Queries

### Ordered List of Properties

1. Color
2. Font-size
3. Line-height
4. Font-weight
5. Font-family
6. Text-align
7. Text-decoration
8. Text-transform
9. Background-color
10. Background-image
11. Background-repeat
12. Background-position
13. Border-width
14. Border-style
15. Border-color
16. Border-radius
17. Padding
18. Margin
19. Width
20. Height
21. Display
22. Position
23. Float
24. Clear
25. z-index
26. Overflow
27. Visibility
28. Cursor
29. Opacity
30. Transition
31. Animation

Note: This is a suggested order for CSS properties, but it may vary depending on the specific project or personal preference.

The following is a list of CSS properties grouped by category:

- **Display**: display, visibility, float, clear, overflow, overflow-x, overflow-y, clip, zoom
- **Table**: table-layout, empty-cells, caption-side, border-spacing, border-collapse, list-style, list-style-position, list-style-type, list-style-image
- **Positioning**: position, top, right, bottom, left, z-index
- **Box Model**: margin, margin-top, margin-right, margin-bottom, margin-left, box-sizing, border, border-width, border-style, border-color, border-top, border-top-width, border-top-style, border-top-color, border-right, border-right-width, border-right-style, border-right-color, border-bottom, border-bottom-width, border-bottom-style, border-bottom-color, border-left, border-left-width, border-left-style, border-left-color, border-radius, border-top-left-radius, border-top-right-radius, border-bottom-right-radius, border-bottom-left-radius, border-image, border-image-source, border-image-slice, border-image-width, border-image-outset, border-image-repeat, padding, padding-top, padding-right, padding-bottom, padding-left, width, min-width, max-width, height, min-height, max-height
- **Typography**: font, font-family, font-size, font-weight, font-style, font-variant, font-size-adjust, font-stretch, font-effect, font-emphasize, font-emphasize-position, font-emphasize-style, font-smooth, line-height, text-align, text-align-last, vertical-align, white-space, text-decoration, text-emphasis, text-emphasis-color, text-emphasis-style, text-emphasis-position, text-indent, text-justify, letter-spacing, word-spacing, text-outline, text-transform, text-wrap, text-overflow, text-overflow-ellipsis, text-overflow-mode, word-wrap, word-break
- **Background**: color, background, background-color, background-image, background-repeat, background-attachment, background-position, background-position-x, background-position-y, background-clip, background-origin, background-size
- **Miscellaneous**: outline, outline-width, outline-style, outline-color, outline-offset, opacity, box-shadow, text-shadow
- **Transitions and Animations**: transition, transition-delay, transition-timing-function, transition-duration, transition-property, transform, transform-origin, animation, animation-name, animation-duration, animation-play-state, animation-timing-function, animation-delay, animation-iteration-count, animation-direction
- **Other**: content, quotes, counter-reset, counter-increment, resize, cursor, user-select, nav-index, nav-up, nav-right, nav-down, nav-left, tab-size, hyphens, pointer-events

## References and Acknowledgments

- [CSS Beginner's Guide](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started)
- [CSS3 Tutorial](https://waylau.gitbooks.io/css3-tutorial/content/)
- [CSS Property Declaration Order Specification](https://wiki.zthxxx.me/wiki/Programming_Languages/CSS/CSS_Property_Declaration_Order_Specification/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.