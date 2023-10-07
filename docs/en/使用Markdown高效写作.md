# Efficient Writing with Markdown

If you are used to writing with tools like Word, you may often encounter the following situations:

- Where is the button for bolding text? Where is the button for creating lists? How can I insert images properly?
- What font size should I use for different headings? What font size is appropriate for the body text?
- When I open it with a different version of Word, the style is not what I want.

When the time spent on formatting exceeds the time spent on writing itself, it proves that this writing method is not efficient. Markdown, on the other hand, allows you to focus on writing itself without being interrupted by formatting.

## Tools

First, you need an editor that supports Markdown. I recommend using VS Code or Typora. 
For installation and configuration of the software, you can refer to my tutorial: [**VS Code Productivity Guide - Environment Configuration**](https://wiki-power.com/en/VSCode%E7%94%9F%E4%BA%A7%E5%8A%9B%E6%8C%87%E5%8D%97-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE)

## Common Syntax

Markdown has only a few commonly used syntax: **headings, text styles, quotes, code, links, images, lists, tables, and horizontal lines**, mastering these will allow you to write with ease.

### Headings

To create headings, add 1-6 `#` symbols before the heading text. The number of heading levels depends on the number of `#` symbols. Generally, the structure of an article should not exceed 4 levels.

```markdown
# Largest Heading

## Second Largest Heading

### Third Largest Heading

#### Fourth Largest Heading

……
```

### Text Styles

Add symbols on both sides of the characters to style the text:

|   Style   |    Keyboard Shortcut    | Syntax                   | Rendered Output             |
| :------: | :--------------: | ---------------------- | -------------------- |
|   Bold   | `Ctrl`/`⌘` + `B` | `**Bold Text**`         | **Bold Text**         |
|   Italic   | `Ctrl`/`⌘` + `I` | `*Italic Text*`           | _Italic Text_           |
| Bold and Italic |                  | `***Bold and Italic Text***` | **_Bold and Italic Text_** |
|  Strikethrough  |                  | `~~Strikethrough Text~~`         | ~~Strikethrough Text~~         |

Note: Italic text is designed for English, please do not use italics for Chinese for readability and standardization.

### Quoting Text

You can use the `>` symbol to quote a paragraph:

```markdown
As in the Christmas message from Pirate Bay:

> We believe that we have changed something. Not just us, but everyone. We no longer want to just run a website, but we want to find some meaning. This cannot be done without your help. Our history is still being written, so please don't draw any conclusions yet.
```

As in the Christmas message from Pirate Bay:

> We believe that we have changed something. Not just us, but everyone. We no longer want to just run a website, but we want to find some meaning. This cannot be done without your help. Our history is still being written, so please don't draw any conclusions yet.

### Quoting Code

#### Inline Code

You can use backticks <code>`</code> (located in the upper left corner of the keyboard) to quote code inline. For example:

```markdown
Extract the `hugo.exe` file from the compressed package to the `D:\hugo` folder directory.
```

Extract the `hugo.exe` file from the compressed package to the `D:\hugo` folder directory.

#### Multi-line Code

If you need multiple lines of code, you can use three backticks <code>```</code> to surround the code block:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210215164653.png)

```c
int fputc(int ch,FILE *f)
{
    HAL_UART_Transmit(&huart1,(uint8_t*)&ch,1,100);
    return ch;
}
```

Here, <code>```c</code> indicates that this code block is in C language, and will be rendered with syntax highlighting according to C syntax.

If you need to display the file where the code is located, you can add <code>```c title="stm32f4xx_it.c"</code>, the effect is as follows:

```c title="stm32f4xx_it.c"
int fputc(int ch,FILE *f)
{
    HAL_UART_Transmit(&huart1,(uint8_t*)&ch,1,100);
    return ch;
}
```

### Links

Create a link by enclosing the link text in square brackets `[ ]` and the URL in parentheses `( )`. For example:

```markdown
This site is built using [Docusaurus](https://v2.docusaurus.io/).
```

This site is built using [Docusaurus](https://v2.docusaurus.io/).

### Images

The format for images is just one more `!` symbol than for links. For example:

```markdown
![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-WildWolf/static/uploads/b944219198103ea09f0f02bcb830e9b.png)
```

![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-WildWolf/static/uploads/b944219198103ea09f0f02bcb830e9b.png)

Note: The image can be displayed without text, i.e. the `[ ]` can be left empty.

### Lists

#### Unordered Lists

Create an unordered list by adding `- ` or `* ` before the text (note: there should be a space after the symbol, otherwise it may not render correctly). For example:

```markdown
- List item
- List item
- List item
```

- List item
- List item
- List item

#### Ordered Lists

To create an ordered list, add the number before each line:

```markdown
1. List item one
2. List item two
3. List item three
```

1. List item one
2. List item two
3. List item three

#### TODO Lists

To create a TODO list, use the following format:

```markdown
- [x] Finish changes
- [ ] Push commits to GitHub
- [ ] Open a pull request
```

- [x] Finish changes
- [ ] Push commits to GitHub
- [ ] Open a pull request

#### Nested Lists

To nest a list, use the `Tab` key to indent and `Shift` + `Tab` to unindent:

```markdown
1. List item one
   1. Sublist item one
   2. Sublist item two
      - Sub-sublist item
      - Sub-sublist item
2. List item two
```

1. List item one
   1. Sublist item one
   2. Sublist item two
      - Sub-sublist item
      - Sub-sublist item
2. List item two

### Tables

Use the `|` symbol to separate cells and the `-` symbol to separate the header from other rows:

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

To align columns in a table, use the `:` symbol:

- `:---` or `---` for left alignment
- `:--:` for center alignment
- `---:` for right alignment

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

### Horizontal Rule

You can use the `---` symbol to generate a dividing line to separate different sections of text:

```markdown
---
```

![](https://f004.backblazeb2.com/file/wiki-media/img/20210216123630.png)

## Advanced Usage

### Paragraphs and Line Breaks

In Markdown, use a blank line before and after to distinguish different paragraphs.  
To create a line break within the same paragraph, simply add two spaces at the end of the line.

### Exporting to Other Formats

If you need to export to PDF, Word, images, and other formats, you can use Pandoc to achieve this.  
If you are using VS Code, you can directly use [**Markdown PDF**](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) to export PDF documents.

### Writing WeChat Official Account Articles with Markdown

WeChat Official Account uses a rich text editor. We can use the web tool [**MD2WeChat**](https://md2wechat.wiki-power.com/) to parse and render Markdown, and then paste it into the official account editor.

For more information, please refer to the article [**Efficient Writing with Markdown**](https://wiki-power.com/en/%E5%A6%82%E4%BD%95%E7%94%A8Markdown%E5%86%99%E5%85%AC%E4%BC%97%E5%8F%B7%E6%96%87%E7%AB%A0).

## References and Acknowledgments

- [Personal Markdown Editing Method](https://sinnammanyo.cn/About-Markdown/)
- [Efficient Writing with Markdown, Letting You Completely Get Rid of Typesetting Problems](https://zhuanlan.zhihu.com/p/41893875)
- [younghz/Markdown](https://github.com/younghz/Markdown)
- [Learning-Markdown (Markdown Beginner's Guide)](https://xianbai.me/learn-md/index.html)
- [Basic Writing and Formatting Syntax](https://docs.github.com/cn/github/writing-on-github/basic-writing-and-formatting-syntax)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.