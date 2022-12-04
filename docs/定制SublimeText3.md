---
id: 定制SublimeText3
title: 定制 SublimeText3
---

## 背景

**Sublime Text** 是一款非常强大的文本编辑器。由于下学期有 Python 相关课程，而 Pycharm 等工具的 UI 有些难看。我想尝试把 Sublime Text 打造为 Python 开发利器。

定制后的效果图：  
 ![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/ST3效果.png)

## [极简部署](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB)

1. 下载 `Consolas-with-Yahei` 字体，解压安装
2. 下载**由我定制**的 [**Sublime Text 3**](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB)（不保证更新）
3. 直接运行 `.exe` 文件，详细参数配置请见下文

## 详细配置

### 软件下载及安装

Sublime Text 3 可从 [官网](http://www.sublimetext.com/) 下载（推荐下载 [**免安装版本**](https://download.sublimetext.com/Sublime%20Text%20Build%203176%20x64.zip)） 软件可以免费使用，但有时候会弹出付费提示。经提醒，已将序列号从文章中删除。需要可以联系我。

### 包管理器及插件安装

安装包管理器：`Preferences -> Install Package Control`，之后可用快捷键 `Ctrl + Shift + P` 快速调出包管理器界面。

安装插件：调出 `Package Control` 界面，输入 `Install Package` ，回车，耐心等待，在稍后弹出的界面里搜索所需插件并点击安装。对于未发布插件，可直接选择 `Preference -> Browser packages` ，打开存放插件的文件夹，把插件直接放进去即可。

卸载插件：调出 `Package Control` 界面，输入 `remove package` .

### 适配中文

1. 汉化：用 `Package Control` 搜索 `ChineseLocalizations` ，点击安装。
2. 中文输入问题：下载 [IMESupport](https://github.com/zcodes/IMESupport/archive/master.zip)，解压到插件安装目录，重启 Sublime ，解决中文输入时输入框不跟随的问题。
3. 中文字体：下载 `Consolas-with-Yahei` ，解压安装，在用户设置里替换为 `"font_face": "Consolas-with-Yahei",` .

   **主题**

我使用的暗色主题：用 `Package Control` 搜索 `Spacegray` 和 `Afterglow` ，在用户设置里替换为：

```
"color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme",
"theme": "Afterglow-green.sublime-theme"
```

### 细节调整

在用户设置里可添加如下代码：

```
"word_wrap": "true", // 被遮挡自动换行
"fold_buttons": true, // 开启代码折叠
"fade_fold_buttons": true, // 折叠按钮自动隐藏
"tab_size": 4, // tab 缩进位数
"margin": 4, // 缩进
"tabs_small": true, // 使标签栏变小
"trim_trailing_white_space_on_save": true, // 自动移除行尾多余空格
"ensure_newline_at_eof_on_save": true, // 文件末尾自动保留一个空行，C 语言可用
```

### 推荐插件

以下插件可用 `Package Control` 直接安装。

**StyleToken**：显示代码所代表的颜色（RGB） **FileHeader**：自定义文件模板 打开 `Preferences -> Package Settings -> FileHeader -> Settings - User` ，把 `Default` 里的内容拷贝到 `User` , 并修改个人信息如：

```
{
    "Default": {
        "author": "linyuxuanlin",
        "email": "824676271@qq.com",
        "website": "yxrct.com"
    }
}
```

在 `Preferences -> Browse Packages... -> FileHeader -> template -> header 或 body` 中修改模板内容。 效果：  
 ![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/ST3 模板效果。png)

### 运行 Python

由于自带编译器没有用户输入，所以这里需要一个插件：`SublimeREPL`. 直接 用 `Package Control` 安装，并在 `Preferences —> Key Buildings -> User` 下添加快捷键唤醒：

```
[
    { "keys": ["f5"], "caption": "SublimeREPL:Python",
                      "command": "run_existing_window_command", "args":
                      {
                           "id": "repl_python_run",
                           "file": "config/Python/Main.sublime-menu"
                      }
    },
]
```

之后，在 Python 代码里可直接按 `F5` 运行。

### 自动格式化代码

安装 `Python PEP8 Autoformat` 插件，在 `Key Buildings` 中加入：

```
{ "keys": ["alt+r"], "command": "pep8_autoformat" },
```

便可用 `Alt + R` 格式化 Python 代码。

## 总结

颜值即生产力。Sublime Text 不止支持 Python，几乎所有的文件格式都可以用它打开编辑。调教得当的话，在一个极简、强大的界面下敲代码，想想也是挺浪漫的。

## 参考与致谢

- [Sublime Text 3 调教你的私人利器（上）](https://www.sheyilin.com/2015/05/sublime_text_3_tiao_jiao_ni_de_si_ren_li_qi_1/)
- [Sublime Text 自动生成文件头部注释（版权信息）：FileHeader 插件的使用](https://blog.csdn.net/afei__/article/details/82890493)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

