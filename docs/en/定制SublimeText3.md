# Customizing SublimeText3

## Background

**Sublime Text** is a very powerful text editor. As I will be taking Python-related courses next semester, and tools like Pycharm have a somewhat unattractive UI, I want to try to turn Sublime Text into a Python development tool.

Customized effect picture:  
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/ST3效果.png)

## [Minimal Deployment](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB)

1. Download the `Consolas-with-Yahei` font and install it after extracting it.
2. Download [**Sublime Text 3**](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB) **customized by me** (not guaranteed to be updated).
3. Run the `.exe` file directly. For detailed parameter configuration, please see below.

## Detailed Configuration

### Software Download and Installation

Sublime Text 3 can be downloaded from the [official website](http://www.sublimetext.com/) (it is recommended to download the [**portable version**](https://download.sublimetext.com/Sublime%20Text%20Build%203176%20x64.zip)). The software can be used for free, but sometimes a payment prompt may pop up. As a reminder, the serial number has been removed from the article. Please contact me if needed.

### Package Manager and Plugin Installation

Install the package manager: `Preferences -> Install Package Control`. Afterwards, you can use the shortcut `Ctrl + Shift + P` to quickly bring up the package manager interface.

Install plugins: Bring up the `Package Control` interface, type in `Install Package`, press Enter, and wait patiently. In the interface that pops up later, search for the required plugins and click install. For unpublished plugins, you can directly select `Preference -> Browser packages`, open the folder where the plugins are stored, and put the plugins directly into it.

Uninstall plugins: Bring up the `Package Control` interface, type in `remove package`.

### Adapting to Chinese

1. Chinese localization: Use `Package Control` to search for `ChineseLocalizations` and click install.
2. Chinese input problem: Download [IMESupport](https://github.com/zcodes/IMESupport/archive/master.zip), extract it to the plugin installation directory, restart Sublime, and solve the problem of the input box not following when inputting Chinese.
3. Chinese font: Download `Consolas-with-Yahei`, extract and install it, and replace it with `"font_face": "Consolas-with-Yahei",` in the user settings.

   **Theme**

The dark theme I use: Use `Package Control` to search for `Spacegray` and `Afterglow`, and replace it with the following in the user settings:

```
"color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme",
"theme": "Afterglow-green.sublime-theme"
```

### Fine-tuning

The following code can be added to the user settings:

```
"word_wrap": "true", // Automatically wrap when obscured
"fold_buttons": true, // Enable code folding
"fade_fold_buttons": true, // Automatically hide the fold button
"tab_size": 4, // Tab indentation size
"margin": 4, // Indentation
"tabs_small": true, // Make the tab bar smaller
"trim_trailing_white_space_on_save": true, // Automatically remove trailing whitespace
"ensure_newline_at_eof_on_save": true, // Automatically keep an empty line at the end of the file, for use in C language
```

### Recommended Plugins

The following plugins can be installed directly through `Package Control`.

**StyleToken**: displays the color (RGB) represented by the code.

**FileHeader**: customizes file templates. Open `Preferences -> Package Settings -> FileHeader -> Settings - User`, copy the contents of `Default` to `User`, and modify personal information such as:

```
{
    "Default": {
        "author": "linyuxuanlin",
        "email": "824676271@qq.com",
        "website": "yxrct.com"
    }
}
```

Modify the template content in `Preferences -> Browse Packages... -> FileHeader -> template -> header or body`.

Effect:  
 ![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/ST3 模板效果。png)

### Running Python

Since the built-in compiler does not have user input, a plugin is needed: `SublimeREPL`. Install it directly using `Package Control`, and add a shortcut key in `Preferences -> Key Buildings -> User` to wake it up:

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

Afterwards, you can directly press `F5` to run Python code.

### Automatic Code Formatting

Install the `Python PEP8 Autoformat` plugin and add the following to `Key Buildings`:

```
{ "keys": ["alt+r"], "command": "pep8_autoformat" },
```

You can then use `Alt + R` to format Python code.

## Summary

Appearance is productivity. Sublime Text not only supports Python, but almost all file formats can be opened and edited with it. With proper tuning, it is quite romantic to code in a minimalist and powerful interface.

## References and Acknowledgements

- [Sublime Text 3 调教你的私人利器（上）](https://www.sheyilin.com/2015/05/sublime_text_3_tiao_jiao_ni_de_si_ren_li_qi_1/)
- [Sublime Text 自动生成文件头部注释（版权信息）：FileHeader 插件的使用](https://blog.csdn.net/afei__/article/details/82890493)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
