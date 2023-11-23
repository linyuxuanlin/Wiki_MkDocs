# HTML Study Notes

## Basic Framework

```markup
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Title</title>
</head>
<body>

</body>
</html>
```

You can open an `.html` file and simply type `html:5` to generate this structure.

## Statements

Some conventions to follow:

1. Use lowercase for tags, and elements must be properly closed.
2. Add a slash to close empty elements, e.g., `<br />`.
3. Avoid semantic attributes; keep styles in CSS to maintain a clear separation of content and style.

```markup
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Title</title>
</head>
<body>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <p>Paragraph</p>

    <!-- Line break -->
    <br />
    <!-- Horizontal rule -->
    <hr />

    <!-- Lists, can be nested -->
    <!-- Ordered list -->
    <ol>
        <li>Item 1</li>
        <li>Item 2</li>
    </ol>
    <!-- Unordered list -->
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>

    <!-- Links -->
    <a href="https://www.google.com/">Text to Display</a>
    <!-- Link to a specific location on the page using the ID attribute -->
    <a href="#top">Back to Top</a>
    <p id="top">Top</p>
    <!-- Link to a specific location on an external page -->
    <a href="http://wiki-power.com/#top">Jump to a specific location on an external page</a>

    <!-- Images -->
    <img src="/xx.png" alt="Text description when the image cannot be loaded" />

    <!-- Tables -->
    <table>
        <!-- First row -->
        <tr>
            <!-- First column -->
            <th></th>
            <!-- Second column -->
            <th scope="col">Saturday</th>
            <!-- Third column -->
            <th scope="col">Sunday</th>
        </tr>
        <!-- Second row -->
        <tr>
            <th scope="row">Quantity</th>
            <td>120</td>
            <td>135</td>
        </tr>
        <!-- Third row -->
        <tr>
            <th scope="row">Earnings</th>
            <!-- Spanning columns using colspan and rowspan -->
            <td colspan="2">500</td>
        </tr>
    </table>
```

```markdown
```html
<!-- Form, to be completed -->
<!-- Iframe, to be completed -->
<!-- Flash/Video/Audio, to be completed -->

</body>

</html>
```

## References and Acknowledgments

- [HTML Tutorial | Runoob Tutorial](http://www.runoob.com/html/html-tutorial.html)
- [HTML in 30 Minutes](http://deerchao.net/tutorials/html/html.htm)
- [HTML - A Brief Analysis of the Head Section](https://www.tielemao.com/831.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
```

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.