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

Open the `.html` file and type `html:5` to call it out.

## Statements

Some conventions:

1. Use lowercase for tags and elements must be closed.
2. Add a slash to close empty elements, e.g. `<br />`.
3. Do not use semantic tags. All styles should be stored in CSS, and content should be separated from style.

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

    <!--Line break-->
    <br />
    <!--Horizontal rule-->
    <hr />

    <!--List, can be nested-->
    <!--Ordered list-->
    <ol>
        <li>First item</li>
        <li>Second item</li>
    </ol>
    <!--Unordered list-->
    <ul>
        <li>First item</li>
        <li>Second item</li>
    </ul>

<!--Links-->
<a href="https://www.google.com/">Link Text</a>
<!--Link to a specific location on the page using the ID attribute-->
<a href="#top">Back to Top</a>
<p id="top">Top</p>
<!--Link to a specific location on another page-->
<a href="http://wiki-power.com/#top">Jump to a specific location on an external page</a>

<!--Images-->
<img src="/xx.png" alt="Text description when image cannot be loaded" />

<!--Tables-->
<table>
    <!--First row-->
    <tr>
        <!--First column-->
        <th></th>
        <!--Second column-->
        <th scope="col">Saturday</th>
        <!--Third column-->
        <th scope="col">Sunday</th>
    </tr>
    <!--Second row-->
    <tr>
        <th scope="row">Quantity</th>
        <td>120</td>
        <td>135</td>
    </tr>
    <!--Third row-->
    <tr>
        <th scope="row">Earnings</th>
        <!--Spanning columns using colspan and rowspan-->
        <td colspan="2">500</td>
    </tr>
</table>

<!--Forms - to be added-->
<!--Iframes - to be added-->
<!--Flash/Video/Audio - to be added-->

</body>

</html> 

## References and Acknowledgements

- [HTML Tutorial | Runoob Tutorial](http://www.runoob.com/html/html-tutorial.html)
- [HTML 30-Minute Quick Start Tutorial](http://deerchao.net/tutorials/html/html.htm)
- [Analysis of HTML Head](https://www.tielemao.com/831.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.