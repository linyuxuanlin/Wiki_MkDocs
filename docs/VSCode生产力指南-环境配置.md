---
id: VSCode生产力指南-环境配置
title: VS Code 生产力指南 - 环境配置
---

—— 如何用 VS Code 打造高效率的生产力工具。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200319135609.png)

## 背景

> 工欲善其事，必先利其器。创造是一件美好的事情，如有利器相辅，这个过程将会变得更加舒适。



### 为什么选用 VS Code ?

- 开源免费，颜值出众
- 完善的编辑功能（自动补全、语法突出等）
- 可直接在编辑器内调试代码
- 集成 Git
- 丰富的插件支持与自定义项

## 软件安装

你可以在 VS Code 官网下载最新的版本：<https://code.visualstudio.com/>

一般我们选择下载 **Stable** 版本。如果你不惧 bug，想体验最新的特性，也可以试试 **Insiders** 版本。

下载安装完成后，我们打开软件，首先看到的是启动页面：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200318224855.png)

## 插件安装

为了精简体积，VS Code 仅保留一些最基础的功能。但如果想提高效率，这些功能是远远不够的。  
好在 VS Code 有各式各样的第三方插件加成，可以真正做到按需取用。

下面推荐一些好用的插件（可直接点击链接安装）：

### 基本

- [**Chinese (Simplified) Language Pack**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)：汉化 VS Code
- [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync)：备份设置项和插件，多设备同步
  - **配置项**：配置相应的 `GitHub Gist ID` 和 `GitHub Access Token`
  - **用法**：`Shift + Alt + U` 上传，`Shift + Alt + D` 下载
  - （最新版本 VS Code 已自带同步功能，但如果需要版本管理还是可以用这个插件）

### Markdown

- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)：提供更强大的 Markdown 语法支持
- [**Markdown Paste Image**](https://marketplace.visualstudio.com/items?itemName=onesdev.vscode-paste-image-plus)：将图片粘贴到 Markdown，并拷贝至 /res 文件夹内
- [**Pangu-Markdown**](https://marketplace.visualstudio.com/items?itemName=xlthu.Pangu-Markdown)：规范 Markdown 格式（中英文间加空格、替换规范标点等）
  - **配置项**：启用保存时自动格式化
- [**vscode-pandoc**](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc)：增加 Pandoc 支持，将 Markdown 导出为 PDF/Word/HTML 等格式
  - **配置项**：确保 [Pandoc](https://pandoc.org/installing.html) 已经安装

### 美化

- [**Indenticator**](https://marketplace.visualstudio.com/items?itemName=SirTori.indenticator)：高亮代码缩进深度
- [**vscode-icons**](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)：为不同的文件格式添加好看的图标

### 编程语言

- [**C/C++**](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### 前端

- [**Prettier - Code formatter**](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)：HTML/CSS/JavaScript 等前端语言自动格式化工具
  - **用法**：`Ctrl + Shift + P`
- [**Color Manager**](https://marketplace.visualstudio.com/items?itemName=RoyAction.color-manager)：直接预览色值对应的颜色
- [**Live Server**](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)：在 VS Code 内运行本地网页

### 其他

- [**Google Translate**](https://marketplace.visualstudio.com/items?itemName=hancel.google-translate)：在 VS Code 内提供翻译
  - **用法**：`Ctrl + Alt + T`
- [**Start git-bash**](https://marketplace.visualstudio.com/items?itemName=McCarter.start-git-bash)：将 `bash` 添加至 VS Code 的终端
- [**TinyPNG**](https://marketplace.visualstudio.com/items?itemName=andi1984.tinypng)：压缩图片
  - **配置项**：设置正确的 `TinyPNG API Key`
  - **用法**：右键文件树内的图片 - `TinyPNG:Compress`
- [**Zhihu Daily**](https://marketplace.visualstudio.com/items?itemName=YRM.zhihu)：摸鱼必备，在 VS Code 内刷知乎日报
- [**坤坤鼓励师**](https://marketplace.visualstudio.com/items?itemName=sakura1357.cxk)：连续打代码一小时，会有蔡徐坤专属篮球舞提醒你休息

## 主题

你可以通过 `文件 - 首选项 - 颜色主题` 来选择自己喜欢的主题，例如我选的是 `Monokai Dimmed` 主题：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200319132727.png)

如果你觉得默认提供的主题不够用，也可以在插件商店内，用关键词 `theme` 搜索并下载自己喜欢的主题。

## 常用设置

初次使用，可以修改一些常用的设置，使 VS Code 用起来更加顺手。
通过 `文件 - 首选项 - 设置` 即可打开设置页面。

### 自动保存

可将 `Files: Auto Save` 设置为除 `off` 外其他 3 个选项。日常使用，自动保存还是很有必要的。

### 字体

等宽字体是写代码的必备，我个人推荐 [**雅黑等宽 (Microsoft YaHei Mono)**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Microsoft-YaHei-Mono.ttf) 字体。

下载 .ttf 字体文件后安装，重启 VS Code，并在 `设置 - 文本编辑器 - 字体 - Font Family` 选项中将 `'Microsoft YaHei Mono'` 添加至头部，即可启用字体。

## 常用快捷键

|     操作     |           快捷键           |
| :----------: | :------------------------: |
|   命令面板   | `F1` 或 `Ctrl + Shift + P` |
|     终端     | <code>Ctrl + &#96;</code>  |
|  资源管理器  |     `Ctrl + Shift + E`     |
|   全局搜索   |     `Ctrl + Shift + F`     |
| 源代码管理器 |     `Ctrl + Shift + G`     |
|     运行     |     `Ctrl + Shift + D`     |
|   插件管理   |     `Ctrl + Shift + X`     |
| 快速切换文件 |         `Ctrl + D`         |

## 源代码控制

提交 Github 每次都需要输入用户名及密码？
输入命令：

```shell
git config --global credential.helper store
```

重启 VS Code 即可。

## 总结

以上为 VS Code 基本的环境配置，下一篇将详细讨论 Git，Jupyter NoteBook 及用户代码片段等操作方法，敬请期待。

### 参考链接

- [Docs · Visual Studio Code](https://code.visualstudio.com/docs)
- [为什么我选择使用 VS Code 进行前端开发？](https://zhuanlan.zhihu.com/p/28631442)
- [vscode git 提交总让输入用户名及密码](https://www.jianshu.com/p/8854713433c5)
- [Vscode 编辑 markdown 代码块（snippets）](https://www.jianshu.com/p/a87e9ca2d208)
- [在 Visual Studio Code 中添加自定义的代码片段](https://blog.walterlv.com/post/add-custom-code-snippet-for-vscode.html##%E5%85%B3%E4%BA%8E%E6%96%87%E4%BB%B6%E5%90%8D%E7%A7%B0)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

