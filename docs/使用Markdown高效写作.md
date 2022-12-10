---
id: 使用Markdown高效写作
title: 使用 Markdown 高效写作
---


如果你习惯使用 Word 之类的工具写作，你可能会常常遇到以下的场景：

- 加粗的按钮在哪里？列表的按钮在哪里？怎样才能正常地插图？
- 不同标题要用几号字体？正文用几号字体才合适？
- 用别的版本的 Word 打开，样式不是我想要的

当用于排版的时间超过了写作本身，足以证明，这种写作方式并不高效。  
而 Markdown 这种写作方式，可以专注于写作本身，而不是总被格式打断思绪。

## 工具

首先，你需要一个支持 Markdown 的编辑器，我推荐使用 VS Code 或 Typora。  
软件的安装配置，可以参考我写过的教程：[**VS Code 生产力指南 - 环境配置**](https://wiki-power.com/VSCode生产力指南-环境配置)

## 常用语法

Markdown 常用语法也就这么几种：**标题、文本样式、引用、代码、链接、图片、列表、表格、分割线** ，掌握即可游刃有余了。

### 标题

要创建标题，请在标题文本前添加 1~6 个 `#` 符号。标题的层级数取决于 `#` 的数量。一般来说，文章的结构不应超出 4 个层级。

```markdown
# 最大标题

## 二级标题

### 三级标题

#### 四级标题

……
```

### 文本样式

在字符两侧添加符号，对文本进行样式化：

|   样式   |    键盘快捷键    | 语法                   | 呈现样式             |
| :------: | :--------------: | ---------------------- | -------------------- |
|   粗体   | `Ctrl`/`⌘` + `B` | `**粗体文本**`         | **粗体文本**         |
|   斜体   | `Ctrl`/`⌘` + `I` | `*斜体文本*`           | _斜体文本_           |
| 又粗又斜 |                  | `***又粗又斜的文本***` | **_又粗又斜的文本_** |
|  删除线  |                  | `~~错误文本~~`         | ~~错误文本~~         |

注意：斜体文本是专为英文设计的，为了易读性和规范性，请勿对中文使用斜体。

### 引用文本

你可以使用 `>` 符号来引用文段：

```markdown
正如「海盗湾」的圣诞祝词：

> 我们相信，我们已经改变了一些东西。不仅仅是我们，而是我们所有人。 我们不再想仅仅运行一个网站，而是想寻找一些意义。这离不开你的帮助。我们的历史还在书写中，请不要匆忙下结论。
```

正如「海盗湾」的圣诞祝词：

> 我们相信，我们已经改变了一些东西。不仅仅是我们，而是我们所有人。 我们不再想仅仅运行一个网站，而是想寻找一些意义。这离不开你的帮助。我们的历史还在书写中，请不要匆忙下结论。

### 引用代码

#### 行内引用

你可以使用反引号 <code>`</code>（在键盘左上角）在行内引用代码。例如：

```markdown
将压缩包内的 `hugo.exe` 文件解压至 `D:\hugo` 文件夹目录下。
```

将压缩包内的 `hugo.exe` 文件解压至 `D:\hugo` 文件夹目录下。

#### 多行代码

如果需要多行代码，可以使用三个反引号 <code>```</code> 前后包围代码区块：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210215164653.png)

```c
int fputc(int ch,FILE *f)
{
    HAL_UART_Transmit(&huart1,(uint8_t*)&ch,1,100);
    return ch;
}
```

其中，<code>```c</code> 表示这段代码是 C 语言，即会按照 C 的语法来渲染高亮。

如果需要显示代码所在的文件，可以加上 <code>```c title="stm32f4xx_it.c"</code>，效果如下：

```c title="stm32f4xx_it.c"
int fputc(int ch,FILE *f)
{
    HAL_UART_Transmit(&huart1,(uint8_t*)&ch,1,100);
    return ch;
}
```

### 链接

将链接文本包含在方括号 `[ ]` 内，然后将 URL 包含在括号 `( )` 内，可创建链接。例如：

```markdown
本站点是使用 [Docusaurus](https://v2.docusaurus.io/) 构建的。
```

本站点是使用 [Docusaurus](https://v2.docusaurus.io/) 构建的。

### 图片

图片的格式仅仅比链接多加了个 `!` 符号，例如：

```markdown
![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-WildWolf/static/uploads/b944219198103ea09f0f02bcb830e9b.png)
```

![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-WildWolf/static/uploads/b944219198103ea09f0f02bcb830e9b.png)

注：图片可不加显示文字，即 `[ ]` 内可留空。

### 列表

#### 无序列表

在文本前面添加 `- ` 或 `* `，可创建无序列表（注意：符号后应该带一个空格，否则可能渲染失败）。例如：

```markdown
- 列表子项
- 列表子项
- 列表子项
```

- 列表子项
- 列表子项
- 列表子项

#### 有序列表

若想创建有序列表，请在每行前添加编号：

```markdown
1. 列表项一
2. 列表项二
3. 列表项三
```

1. 列表项一
2. 列表项二
3. 列表项三

#### TODO 列表

若要创建 TODO 列表，则按照以下的格式：

```markdown
- [x] 完成更改
- [ ] 推送提交到 GitHub
- [ ] 打开拉取请求
```

- [x] 完成更改
- [ ] 推送提交到 GitHub
- [ ] 打开拉取请求

#### 列表嵌套

若想在列表内进行嵌套，可直接使用快捷键 `Tab` 缩进，`Shift` + `Tab` 取消缩进：

```markdown
1. 列表项一
   1. 列表子项一
   2. 列表子项二
      - 子子项
      - 子子项
2. 列表项二
```

1. 列表项一
   1. 列表子项一
   2. 列表子项二
      - 子子项
      - 子子项
2. 列表项二

### 表格

使用 `|` 符号来分隔不同的单元格，使用 `-` 符号来分隔表头和其他行：

```markdown
| name       | age |
| ---------- | --- |
| LearnShare | 12  |
| Mike       | 32  |
```

| name       | age |
| ---------- | --- |
| LearnShare | 12  |
| Mike       | 32  |

若想对齐表格中的列，可以使用 `:` 符号：

- `:---` 或 `---` 代表左对齐
- `:--:` 代表居中对齐
- `---:` 代表右对齐

```markdown
|    name    | age |
| :--------: | --: |
| LearnShare |  12 |
|    Mike    |  32 |
```

|    name    | age |
| :--------: | --: |
| LearnShare |  12 |
|    Mike    |  32 |

### 分割线

你可以用 `---` 符号生成分割线，以分隔不同内容的文段：

```markdown
---
```

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210216123630.png)

## 高级用法

### 段落与分行

在 Markdown 中，请以前后各空一行，来区分不同的段落。  
同一段落内的换行，只需在句末加两个空格即可。

### 导出其他格式

如需要导出 PDF，Word，图片等格式，可以使用 Pandoc 来实现。  
如果你使用的是 VS Code，可以直接使用 [**Markdown PDF**](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) 以导出 PDF 文档。

### 用 Markdown 写公众号文章

微信公众号用的是富文本编辑器，我们可以使用网页工具 [**MD2WeChat**](https://md2wechat.wiki-power.com/) 对 Markdown 进行解析渲染，并粘贴至公众号编辑器内。

详情请参考 [**使用 Markdown 进行高效写作**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E7%94%A8Markdown%E5%86%99%E5%85%AC%E4%BC%97%E5%8F%B7%E6%96%87%E7%AB%A0) 这篇文章。

## 参考与致谢

- [个人 Markdown 编辑方法](https://sinnammanyo.cn/About-Markdown/)
- [高效写作方式 Markdown，让你彻底摆脱排版的困扰](https://zhuanlan.zhihu.com/p/41893875)
- [younghz/Markdown](https://github.com/younghz/Markdown)
- [Learning-Markdown (Markdown 入门参考)](https://xianbai.me/learn-md/index.html)
- [基本撰写和格式语法](https://docs.github.com/cn/github/writing-on-github/basic-writing-and-formatting-syntax)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

