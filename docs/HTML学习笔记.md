---
id: HTML学习笔记
title: HTML 学习笔记
---

## 基本框架

```markup
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>标题</title>
</head>
<body>

</body>
</html>
```

可打开 `.html` 文件，直接输入 `html:5` 调出

## 语句

一些规范：

1. 标签使用小写，元素必须闭合
2. 空元素要加斜杠以闭合 eg. `<br />`
3. 不使用语义化，所有样式都存放于 CSS 中，内容与样式分离

```markup
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>标题</title>
</head>

<body>
    <h1>一级标题</h1>
    <h2>二级标题</h2>
    <p>段落</p>

    <!--换行符-->
    <br />
    <!--分割线-->
    <hr />

    <!--列表，可嵌套-->
    <!--有序列表-->
    <ol>
        <li>第一项</li>
        <li>第二项</li>
    </ol>
    <!--无序列表-->
    <ul>
        <li>第一项</li>
        <li>第二项</li>
    </ul>

    <!--链接-->
    <a href="https://www.google.com/">链接显示的文本</a>
    <!--链接到页面特定位置，使用 ID 特性-->
    <a href="#top">回到顶部</a>
    <p id="top">顶部</p>
    <!--链接到其他页面的特定位置-->
    <a href="http://wiki-power.com/#top">跳转到站外页面的某个位置</a>

    <!--图像-->
    <img src="/xx.png" alt="无法加载时的文字说明" />

    <!--表格-->
    <table>
        <!--第一行-->
        <tr>
            <!--第一列-->
            <th></th>
            <!--第二列-->
            <th scope="col">周六</th>
            <!--第三列-->
            <th scope="col">周日</th>
        </tr>
        <!--第二行-->
        <tr>
            <th scope="row">数量</th>
            <td>120</td>
            <td>135</td>
        </tr>
        <!--第三行-->
        <tr>
            <th scope="row">收益</th>
            <!--跨列 colspan，跨行 rowspan-->
            <td colspan="2">500</td>
        </tr>
    </table>

    <!--表单，待补充-->
    <!--iframe，待补充-->
    <!--flash/视频/音频，待补充-->

</body>

</html>
```

## 参考与致谢

- [HTML 教程 | 菜鸟教程](http://www.runoob.com/html/html-tutorial.html)
- [HTML 30 分钟入门教程](http://deerchao.net/tutorials/html/html.htm)
- [HTML - head 头部浅析](https://www.tielemao.com/831.html)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

