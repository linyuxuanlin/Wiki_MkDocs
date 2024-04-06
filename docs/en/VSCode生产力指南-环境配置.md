# VS Code Productivity Guide - Environment Setup

—— How to create an efficient productivity tool with VS Code.

![](https://media.wiki-power.com/img/20200319135609.png)

## Background

> To do a good job, one must first sharpen one's tools. Creation is a wonderful thing, and with the right tools at hand, the process becomes more comfortable.

### Why Choose VS Code?

- Open-source and free, with an outstanding appearance
- Comprehensive editing features (auto-completion, syntax highlighting, etc.)
- Direct code debugging within the editor
- Git integration
- Rich plugin support and customization options

## Software Installation

You can download the latest version of VS Code from the official website: [https://code.visualstudio.com/](https://code.visualstudio.com/)

In general, we choose to download the **Stable** version. If you're not afraid of bugs and want to experience the latest features, you can also try the **Insiders** version.

After completing the installation, open the software, and the first thing you'll see is the startup page:

![](https://media.wiki-power.com/img/20200318224855.png)

## Plugin Installation

To keep the software lightweight, VS Code includes only a few essential features. However, if you want to boost your efficiency, these features are far from sufficient. Fortunately, VS Code offers a wide range of third-party plugins that you can use on-demand.

Below are some useful plugins (you can click the links to install them):

### Basics

- [**Chinese (Simplified) Language Pack**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans): Localizes VS Code to Simplified Chinese
- [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync): Back up settings and plugins for synchronization across multiple devices
  - **Configuration**: Set the corresponding `GitHub Gist ID` and `GitHub Access Token`
  - **Usage**: Upload with `Shift + Alt + U`, download with `Shift + Alt + D`
  - (The latest version of VS Code includes built-in synchronization, but this plugin can still be useful for version management.)

### Markdown

- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): Provides robust Markdown syntax support
- [**Markdown Paste Image**](https://marketplace.visualstudio.com/items?itemName=onesdev.vscode-paste-image-plus): Paste images into Markdown and copy them to the /res folder
- [**Pangu-Markdown**](https://marketplace.visualstudio.com/items?itemName=xlthu.Pangu-Markdown): Standardize Markdown format (add spaces between Chinese and English, replace standard punctuation, etc.)
  - **Configuration**: Enable automatic formatting on save
- [**vscode-pandoc**](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc): Enhance Pandoc support for exporting Markdown to PDF/Word/HTML, and other formats
  - **Configuration**: Ensure [Pandoc](https://pandoc.org/installing.html) is installed

### Beautification

- [**Indenticator**](https://marketplace.visualstudio.com/items?itemName=SirTori.indenticator): Highlights code indentation depth.
- [**vscode-icons**](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons): Adds attractive icons for different file formats.

### Programming Languages

- [**C/C++**](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Frontend

- [**Prettier - Code formatter**](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): An automatic formatting tool for frontend languages like HTML, CSS, and JavaScript.
  - **Usage**: `Ctrl + Shift + P`
- [**Color Manager**](https://marketplace.visualstudio.com/items?itemName=RoyAction.color-manager): Provides direct color previews for corresponding color values.
- [**Live Server**](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer): Runs local web pages within VS Code.

### Others

- [**Google Translate**](https://marketplace.visualstudio.com/items?itemName=hancel.google-translate): Offers translation within VS Code.
  - **Usage**: `Ctrl + Alt + T`
- [**Start git-bash**](https://marketplace.visualstudio.com/items?itemName=McCarter.start-git-bash): Adds `bash` to the terminal in VS Code.
- [**TinyPNG**](https://marketplace.visualstudio.com/items?itemName=andi1984.tinypng): Compresses images.
  - **Configuration**: Set the correct `TinyPNG API Key`.
  - **Usage**: Right-click on images in the file tree - `TinyPNG:Compress`
- [**Zhihu Daily**](https://marketplace.visualstudio.com/items?itemName=YRM.zhihu): A must-have for procrastination, allows you to browse Zhihu Daily within VS Code.
- [**坤坤鼓励师**](https://marketplace.visualstudio.com/items?itemName=sakura1357.cxk): Codes continuously for an hour, and you'll receive a special reminder with Cai Xukun's basketball dance to take a break.

## Themes

You can choose your preferred theme by going to `File - Preferences - Color Theme`. For example, I've chosen the `Monokai Dimmed` theme:

![Monokai Dimmed Theme](https://media.wiki-power.com/img/20200319132727.png)

If you find the default themes insufficient, you can also search and download your favorite themes in the plugin store using the keyword "theme."

## Common Settings

For a smoother experience, you can modify some common settings when using VS Code for the first time. You can access the settings page by going to `File - Preferences - Settings`.

### Auto Save

You can set `Files: Auto Save` to any option other than `off`. For everyday use, automatic saving is quite essential.

### Font

A monospaced font is a must-have for coding, and I personally recommend [**Microsoft YaHei Mono**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Microsoft-YaHei-Mono.ttf) font.

After downloading the .ttf font file, install it, restart VS Code, and add `'Microsoft YaHei Mono'` to the beginning of the list in the `Settings - Text Editor - Font - Font Family` option to enable the font.

## Common Shortcuts

|        Action        |          Shortcut          |
| :------------------: | :------------------------: |
|   Command Palette    | `F1` or `Ctrl + Shift + P` |
|       Terminal       | <code>Ctrl + &#96;</code>  |
|       Explorer       |     `Ctrl + Shift + E`     |
|    Global Search     |     `Ctrl + Shift + F`     |
|    Source Control    |     `Ctrl + Shift + G`     |
|         Run          |     `Ctrl + Shift + D`     |
| Extension Management |     `Ctrl + Shift + X`     |
| Quick File Switching |         `Ctrl + D`         |

## Source Control

Do you have to enter your username and password every time you commit to GitHub? Enter the following command:

```shell
git config --global credential.helper store
```

Restart VS Code to resolve this issue.

## Summary

The above information covers the basic environment configuration for VS Code. The next article will discuss Git, Jupyter Notebook, and user code snippets in detail. Stay tuned!

### Reference Links

- [Docs · Visual Studio Code](https://code.visualstudio.com/docs)
- [Why I Choose VS Code for Front-End Development](https://zhuanlan.zhihu.com/p/28631442)
- [VS Code Keeps Prompting for Username and Password When Committing](https://www.jianshu.com/p/8854713433c5)
- [Editing Markdown Code Blocks (Snippets) in Vscode](https://www.jianshu.com/p/a87e9ca2d208)
- [Adding Custom Code Snippets in Visual Studio Code](https://blog.walterlv.com/post/add-custom-code-snippet-for-vscode.html##%E5%85%B3%E4%BA%8E%E6%96%87%E4%BB%B6%E5%90%8D%E7%A7%B0)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
