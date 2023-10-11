# VS Code Productivity Guide - Environment Configuration

—— How to use VS Code to create an efficient productivity tool.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200319135609.png)

## Background

> To do a good job, one must first sharpen one's tools. Creation is a beautiful thing, and with the help of good tools, the process can become more comfortable.

### Why choose VS Code?

- Open source and free, with outstanding appearance
- Perfect editing functions (auto-completion, syntax highlighting, etc.)
- Direct code debugging in the editor
- Integrated Git
- Rich plug-in support and customization options

## Software Installation

You can download the latest version from the VS Code official website: <https://code.visualstudio.com/>

Generally, we choose to download the **Stable** version. If you are not afraid of bugs and want to experience the latest features, you can also try the **Insiders** version.

After downloading and installing the software, we open it and the first thing we see is the startup page:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200318224855.png)

## Plug-in Installation

To streamline the volume, VS Code only retains some of the most basic functions. However, if you want to improve efficiency, these functions are far from enough.  
Fortunately, VS Code has a variety of third-party plug-ins that can truly be used on demand.

Here are some useful plug-ins (click the link to install directly):

### Basic

- [**Chinese (Simplified) Language Pack**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans): Chinese localization for VS Code
- [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync): Backup settings and plug-ins, synchronize across multiple devices
  - **Configuration**: Configure the corresponding `GitHub Gist ID` and `GitHub Access Token`
  - **Usage**: `Shift + Alt + U` to upload, `Shift + Alt + D` to download
  - (The latest version of VS Code already has built-in synchronization function, but this plug-in can still be used for version management if needed)

### Markdown

- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): Provides more powerful Markdown syntax support
- [**Markdown Paste Image**](https://marketplace.visualstudio.com/items?itemName=onesdev.vscode-paste-image-plus): Paste images into Markdown and copy them to the /res folder
- [**Pangu-Markdown**](https://marketplace.visualstudio.com/items?itemName=xlthu.Pangu-Markdown): Standardize Markdown format (add spaces between Chinese and English, replace standard punctuation, etc.)
  - **Configuration**: Enable automatic formatting when saving
- [**vscode-pandoc**](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc): Adds Pandoc support to export Markdown to PDF/Word/HTML and other formats
  - **Configuration**: Make sure [Pandoc](https://pandoc.org/installing.html) is installed

### Beautification

- [**Indenticator**](https://marketplace.visualstudio.com/items?itemName=SirTori.indenticator): Highlights code indentation depth
- [**vscode-icons**](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons): Adds attractive icons for different file formats

### Programming Languages

- [**C/C++**](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Front-end

- [**Prettier - Code formatter**](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Automatic formatting tool for front-end languages such as HTML/CSS/JavaScript
  - **Usage**: `Ctrl + Shift + P`
- [**Color Manager**](https://marketplace.visualstudio.com/items?itemName=RoyAction.color-manager): Directly preview the color corresponding to the color value
- [**Live Server**](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer): Run local web pages within VS Code

### Others

- [**Google Translate**](https://marketplace.visualstudio.com/items?itemName=hancel.google-translate): Provides translation within VS Code
  - **Usage**: `Ctrl + Alt + T`
- [**Start git-bash**](https://marketplace.visualstudio.com/items?itemName=McCarter.start-git-bash): Adds `bash` to the VS Code terminal
- [**TinyPNG**](https://marketplace.visualstudio.com/items?itemName=andi1984.tinypng): Compress images
  - **Configuration**: Set the correct `TinyPNG API Key`
  - **Usage**: Right-click on the image in the file tree - `TinyPNG:Compress`
- [**Zhihu Daily**](https://marketplace.visualstudio.com/items?itemName=YRM.zhihu): A must-have for slacking off, read Zhihu Daily within VS Code
- [**Kunkun Encouragement**](https://marketplace.visualstudio.com/items?itemName=sakura1357.cxk): After coding for an hour, there will be a Cai Xukun exclusive basketball dance to remind you to take a break

## Themes

You can choose your favorite theme through `File - Preferences - Color Theme`, for example, I chose the `Monokai Dimmed` theme:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200319132727.png)

If you feel that the default themes are not enough, you can also search and download your favorite themes in the plugin store using the keyword `theme`.

## Common Settings

For first-time use, you can modify some common settings to make VS Code more user-friendly. You can open the settings page through `File - Preferences - Settings`.

### Auto Save

You can set `Files: Auto Save` to any of the three options besides `off`. Automatic saving is still necessary for daily use.

### Fonts

Monospaced fonts are essential for coding, and I personally recommend [**Microsoft YaHei Mono**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Microsoft-YaHei-Mono.ttf).

After downloading the .ttf font file, install it, restart VS Code, and add `'Microsoft YaHei Mono'` to the top of the `Settings - Text Editor - Font - Font Family` option to enable the font.

## Common Shortcuts

|     Operation     |          Shortcut          |
| :---------------: | :------------------------: |
|  Command Palette  | `F1` or `Ctrl + Shift + P` |
|     Terminal      | <code>Ctrl + &#96;</code>  |
|     Explorer      |     `Ctrl + Shift + E`     |
|   Global Search   |     `Ctrl + Shift + F`     |
|  Source Control   |     `Ctrl + Shift + G`     |
|        Run        |     `Ctrl + Shift + D`     |
|     Extension     |     `Ctrl + Shift + X`     |
| Quick File Switch |         `Ctrl + D`         |

## Source Control

Do you have to enter your username and password every time you commit to Github? Enter the command:

```shell
git config --global credential.helper store
```

and restart VS Code.

## Conclusion

The above is the basic environment configuration for VS Code. The next article will discuss in detail the methods of Git, Jupyter NoteBook, and user code snippets. Stay tuned.

### References

- [Docs · Visual Studio Code](https://code.visualstudio.com/docs)
- [Why I choose to use VS Code for front-end development?](https://zhuanlan.zhihu.com/p/28631442)
- [vscode git always prompts for username and password](https://www.jianshu.com/p/8854713433c5)
- [Editing Markdown Code Blocks (Snippets) in Vscode](https://www.jianshu.com/p/a87e9ca2d208)
- [Add Custom Code Snippets for Visual Studio Code](https://blog.walterlv.com/post/add-custom-code-snippet-for-vscode.html##%E5%85%B3%E4%BA%8E%E6%96%87%E4%BB%B6%E5%90%8D%E7%A7%B0)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
