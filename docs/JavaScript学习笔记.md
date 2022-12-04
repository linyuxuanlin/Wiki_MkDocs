---
id: JavaScript学习笔记
title: JavaScript 学习笔记
---

## 调用外部 JS

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

## 输出

### 弹出警告框

```javascript
window.alert("Hello");
```

### 操作 HTML 元素

```markup
<!DOCTYPE html>
<html>
    <body>
        <h1> 我的第一个 Web 页面 </h1>
        <p id="demo"> 我的第一个段落 </p>
        <script>
            document.getElementById ("demo").innerHTML = "段落已修改。";
        </script>
    </body>
</html>
```

## 数据类型

创建变量：

```javascript
var carname = "Volvo";
```

**值类型 \（基本类型、)**：字符串（String）、数字 \(Number\)、布尔 \(Boolean\)、对空（Null）、未定义（Undefined）、Symbol。

**引用数据类型**：对象 \(Object\)、数组 \(Array\)、函数 \(Function\)。



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

