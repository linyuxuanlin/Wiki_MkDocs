---
id: CSS学习笔记
title: CSS 学习笔记
---

## 调用

在 HTML 的 `<head>` 下添加外部样式表：

```
<link rel="stylesheet" href="xxx.css">
```

其中，`xxx.css` 为同目录下的 CSS 文件。  
注意：尽量使用 **链接式的外部样式表**（如上）

## 选择器

### 基本语法

```css
selector {
  prpperty: value;
}
```

### 几种选择器对比

| 选择器     | 定义                           | 调用                     | 优先级 |
| :--------- | :----------------------------- | :----------------------- | :----- |
| 标签选择器 | p {...}                        | &lt;p&gt; ... &lt;/p&gt; | 低     |
| 类选择器   | .carrot {...} / p.carrot {...} | class = "carrot"         | 中     |
| ID 选择器  | \#first {...}                  | id = "first"             | 高     |

### 选择器组

用相同样式定义不同元素。

```css
h1,
h2,
h3 {
  color: navy;
}
```

## 颜色

```css
/*字体颜色*/
color: #56a455;

/*背景色*/
background-color: blue;

/*透明度*/
/*取值 0.0 ~ 1.0*/
opacity: 0.5;
```

## 文本

### 字体大小

| 样式 | 百分比 | EM 值   |
| :--- | :----- | :------ |
| h1   | 200%   | 2em     |
| h2   | 150%   | 1.5em   |
| h3   | 133%   | 1.125em |
| body | 100%   | 1em     |

```css
/*字体大小*/
font-size: 200%;
```

### 字体选用

注：多单词组成的字体名称，要放引号，eg. 'Courier New'

```css
/*字体选用*/
/*本地*/
font-family: "Courier New", Courier, monospace, 外链字体名称；
/*外链*/
@font-face {
  font-family: 外链字体名称；
  src: url("外链地址");
}
```

### 文本格式化

默认值为 `normal`

```css
/*粗体*/
font-weight: bold;

/*斜体*/
font-style: italic;

/*大小写*/
/*uppercase，lowercase，capitalize（首字母大写）*/
text-transform: uppercase;

/*下划线*/
text-decoration: underline;

/*删除线*/
text-decoration: line-through;

/*行间距*/
line-height: 1.4em;

/*对齐*/
/*left,right,center,justify（两端对齐）*/
text-align: left;
```

### 伪类

```css
/* 未访问的链接 */
a:link {
  color: #ff0000;
}

/* 已访问的链接 */
a:visited {
  color: #00ff00;
}

/* 鼠标划过链接 */
a:hover {
  color: #ff00ff;
}

/* 已选中的链接 */
a:active {
  color: #0000ff;
}
```

## 盒子

## 列表，表格与表单

待补充

## 布局

待补充

## 规范

### 属性分类顺序

- 显示方法 & 布局
- 定位
- 盒模型框
  - 外边距
  - 边框
  - 内边距
- 尺寸
- 文本样式
  - 字体
  - 文本
  - 文字颜色
- 背景
- 轮廓
- 透明度 & 阴影
- 动效
  - 过渡
  - 转换变形
  - 动画
- 其他
  - 伪类 & 伪元素
  - 引用
  - 媒体查询

### 属性顺序列表

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

## 参考与致谢

- [CSS 入门教程](https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Getting_started)
- [CSS3 Tutorial 《CSS3 教程》](https://waylau.gitbooks.io/css3-tutorial/content/)
- [CSS 属性声明顺序规范](https://wiki.zthxxx.me/wiki/程序语言/CSS/CSS%20 属性声明顺序规范/)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

