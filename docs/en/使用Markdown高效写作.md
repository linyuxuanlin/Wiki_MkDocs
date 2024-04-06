# Efficient Writing with Markdown

If you're accustomed to using tools like Microsoft Word for writing, you might frequently encounter the following situations:

- Where's the button to bold text? Where's the button for creating lists? How do I insert images properly?
- What font size should different headings be? What's the right font size for the body text?
- When I open it with a different version of Word, the styles are not what I want.

When the time spent on formatting surpasses the time spent on actual writing, it's clear that this writing approach isn't efficient. Markdown, on the other hand, lets you focus on the writing itself without constant interruptions for formatting.

## Tools

First and foremost, you need an editor that supports Markdown. I recommend using VS Code or Typora. For software installation and setup, you can refer to the tutorial I've written: [**VS Code Productivity Guide - Environment Configuration**](https://wiki-power.com/VSCode生产力指南-环境配置).

## Common Markdown Syntax

Markdown primarily revolves around a handful of syntax elements: **headings, text styling, quotes, code, links, images, lists, tables, horizontal rules**. Once you've mastered these, you'll be well-equipped.

### Headings

To create headings, simply prefix your heading text with 1 to 6 `#` symbols. The level of the heading is determined by the number of `#` symbols. In general, a document's structure shouldn't have more than 4 levels.

```markdown
# Top-level Heading

## Second-level Heading

### Third-level Heading

#### Fourth-level Heading

……
```

### Text Styling

Style text by enclosing it with appropriate symbols:

|      Style      | Keyboard Shortcut | Syntax                       | Result                     |
| :-------------: | :---------------: | ---------------------------- | -------------------------- |
|      Bold       | `Ctrl`/`⌘` + `B`  | `**Bold Text**`              | **Bold Text**              |
|     Italic      | `Ctrl`/`⌘` + `I`  | `*Italic Text*`              | _Italic Text_              |
| Bold and Italic |                   | `***Bold and Italic Text***` | **_Bold and Italic Text_** |
|  Strikethrough  |                   | `~~Struck Text~~`            | ~~Struck Text~~            |

Note: Italics are designed primarily for English text. For readability and convention, avoid using italics with Chinese text.

### Quoting Text

You can use the `>` symbol to quote a paragraph:

```markdown
As stated in the Christmas message from "Pirate Bay":

> We believe we've changed something. Not just us, but all of us. We no longer want to run just a website; we want to find some meaning. This wouldn't be possible without your help. Our history is still being written; please don't rush to conclusions.
```

As stated in the Christmas message from "Pirate Bay":

> We believe we've changed something. Not just us, but all of us. We no longer want to run just a website; we want to find some meaning. This wouldn't be possible without your help. Our history is still being written; please don't rush to conclusions.

### Code Quoting

#### Inline Code

You can use backticks <code>`</code> (located in the upper left corner of the keyboard) to quote inline code. For example:

```markdown
Extract the `hugo.exe` file from the compressed archive to the `D:\hugo` directory.
```

Extract the `hugo.exe` file from the compressed archive to the `D:\hugo` directory.

#### Multi-line Code

For multi-line code, enclose the code block with triple backticks <code>```</code>:

![Code Block](https://media.wiki-power.com/img/20210215164653.png)

```c
int fputc(int ch,FILE *f)
{
    HAL_UART_Transmit(&huart1,(uint8_t*)&ch,1,100);
    return ch;
}
```

Here, <code>```c</code> indicates that this code block is in the C programming language, and it will be rendered with proper syntax highlighting.

If you need to display the file where the code is located, you can add <code>```c title="stm32f4xx_it.c"</code>, and the result will be as follows:

```c title="stm32f4xx_it.c"
int fputc(int ch, FILE *f)
{
    HAL_UART_Transmit(&huart1, (uint8_t *)&ch, 1, 100);
    return ch;
}
```

### Links

To create a link, enclose the link text in square brackets `[ ]` and then enclose the URL in parentheses `( )`. For example:

```markdown
This site is built using [Docusaurus](https://v2.docusaurus.io/).
```

This site is built using [Docusaurus](https://v2.docusaurus.io/).

### Images

The format for images is the same as for links, but with an additional `!` symbol, for example:

```markdown
![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-WildWolf/static/uploads/b944219198103ea09f0f02bcb830e9b.png)
```

![](https://cdn.jsdelivr.net/gh/linyuxuanlin/Wiki-WildWolf/static/uploads/b944219198103ea09f0f02bcb830e9b.png)

Note: Images can be left with empty text, i.e., the `[ ]` can remain blank.

### Lists

#### Unordered Lists

To create an unordered list, add `- ` or `* ` before the text (note: there should be a space after the symbol, or it may not render properly). For example:

```markdown
- List item
- List item
- List item
```

- List item
- List item
- List item

#### Ordered Lists

To create an ordered list, add a number before each line:

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
- [x] Complete the changes
- [ ] Push the changes to GitHub
- [ ] Open a pull request
```

- [x] Complete the changes
- [ ] Push the changes to GitHub
- [ ] Open a pull request

#### Nested Lists

To nest lists, use the `Tab` key to indent and `Shift` + `Tab` to unindent:

```markdown
1. List item one
   1. Subitem one
   2. Subitem two
      - Subsubitem
      - Subsubitem
2. List item two
```

1. List item one
   1. Subitem one
   2. Subitem two
      - Subsubitem
      - Subsubitem
2. List item two

### Tables

Use `|` to separate different cells and `-` to separate the header and other rows:

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

To align columns in the table, you can use `:`:

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

You can use the `---` symbol to create a horizontal rule, which separates different sections of text:

```markdown
---
```

![Image](https://media.wiki-power.com/img/20210216123630.png)

## Advanced Usage

### Paragraphs and Line Breaks

In Markdown, separate different paragraphs by leaving a blank line before and after them.
For line breaks within the same paragraph, simply add two spaces at the end of a line.

### Exporting to Other Formats

If you need to export to formats like PDF, Word, images, and more, you can use Pandoc for this purpose.
If you're using VS Code, you can directly use [**Markdown PDF**](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) for exporting PDF documents.

### Writing Public Articles in Markdown

WeChat Official Accounts use a rich text editor. You can use the web tool [**MD2WeChat**](https://md2wechat.wiki-power.com/) to parse and render your Markdown content and then paste it into the Official Account editor.

For more details, please refer to the article [**Efficient Writing with Markdown**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E7%94%A8Markdown%E5%86%99%E5%85%AC%E4%BC%97%E5%8F%B7%E6%96%87%E7%AB%A0).

## References and Acknowledgments

- [Personal Markdown Editing Methods](https://sinnammanyo.cn/About-Markdown/)
- [Efficient Writing with Markdown - Free Yourself from Formatting Woes](https://zhuanlan.zhihu.com/p/41893875)
- [younghz/Markdown](https://github.com/younghz/Markdown)
- [Learning-Markdown (Markdown Beginner's Reference)](https://xianbai.me/learn-md/index.html)
- [Basic Writing and Formatting Syntax](https://docs.github.com/cn/github/writing-on-github/basic-writing-and-formatting-syntax)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
