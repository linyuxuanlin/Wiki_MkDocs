# JavaScript Study Notes

## Calling External JS

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

## Output

### Displaying Alert Dialog

```javascript
window.alert("Hello");
```

### Manipulating HTML Elements

```markup
<!DOCTYPE html>
<html>
    <body>
        <h1>My First Web Page</h1>
        <p id="demo">My first paragraph</p>
        <script>
            document.getElementById("demo").innerHTML = "Paragraph has been modified.";
        </script>
    </body>
</html>
```

## Data Types

Creating Variables:

```javascript
var carname = "Volvo";
```

**Value Types (Primitive Types):** String, Number, Boolean, Null, Undefined, Symbol.

**Reference Data Types:** Object, Array, Function.

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.