---
id: 用reveal.js制作幻灯片
title: 用 reveal.js 制作幻灯片
---

## 快捷键

- 下一张幻灯片：**空格**
- 方向选择幻灯片：**方向键**
- 总览视图：**Esc**
- 演讲者视图：**S**
- 暂停演讲 / 黑屏：**V/B/.**

## PDF 导出

在地址后加 `?print-pdf`，例如 `http://localhost:8000/?print-pdf`

## 参考语法

### 图片

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

### 文字

```html
<p style="white-space: pre-line;"><small> </small></p>
```

### 视频

```html
<section
  data-transition="slide"
  data-background="#EAB547"
  data-background-transition="zoom"
>
  <video data-src=""></video>
</section>
```

## 参考与致谢

- [reveal.js](https://revealjs.com/)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

