# Customizing Sublime Text 3

## Background

**Sublime Text** is an incredibly powerful text editor. With Python-related courses coming up next semester, and considering the not-so-pleasing UI of tools like PyCharm, I'd like to transform Sublime Text into a Python development powerhouse.

Here's a screenshot of the customized result:
![Customized Sublime Text 3](https://media.wiki-power.com/img/ST3效果.png)

## [Minimal Deployment](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB)

1. Download the `Consolas-with-Yahei` font and install it after extracting.
2. Download the [**customized Sublime Text 3**](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB) by me (updates not guaranteed).
3. Run the `.exe` file directly. For detailed configuration parameters, please see below.

## Detailed Configuration

### Software Download and Installation

Sublime Text 3 can be downloaded from the [official website](http://www.sublimetext.com/), and it is recommended to download the [**portable version**](https://download.sublimetext.com/Sublime%20Text%20Build%203176%20x64.zip). The software can be used for free, but occasionally, it may prompt for payment. As a reminder, the serial number has been removed from this article. Feel free to contact me if needed.

### Package Manager and Plugin Installation

To install the package manager, navigate to `Preferences -> Install Package Control`. Afterward, you can quickly access the package manager interface with the keyboard shortcut `Ctrl + Shift + P`.

To install plugins, open the `Package Control` interface, type `Install Package`, hit Enter, and patiently wait. In the dialog that appears shortly, search for the desired plugins and click to install. For unpublished plugins, you can select `Preference -> Browse Packages`, open the folder where the plugins are stored, and place the plugins directly in there.

To uninstall plugins, bring up the `Package Control` interface and type `remove package`.

### Chinese Language Support

1. Chinese localization: Use `Package Control` to search for `ChineseLocalizations` and click to install.
2. Chinese input issue: Download [IMESupport](https://github.com/zcodes/IMESupport/archive/master.zip), extract it to the plugin installation directory, restart Sublime Text to resolve the issue of the input box not following when typing in Chinese.
3. Chinese font: Download `Consolas-with-Yahei`, install it after extracting, and replace it in the user settings with `"font_face": "Consolas-with-Yahei"`.

### Themes

The dark theme I use: Search for `Spacegray` and `Afterglow` using `Package Control` and replace the following in user settings:

```json
"color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme",
"theme": "Afterglow-green.sublime-theme"
```

### Fine-Tuning

You can add the following code to your user settings:

```json
"word_wrap": "true", // Automatically wrap long lines
"fold_buttons": true, // Enable code folding
"fade_fold_buttons": true, // Automatically hide folding buttons
"tab_size": 4, // Number of spaces for tab indentation
"margin": 4, // Indentation margin
"tabs_small": true, // Make the tab bar smaller
"trim_trailing_white_space_on_save": true, // Automatically remove trailing whitespace on save
"ensure_newline_at_eof_on_save": true, // Automatically add an empty line at the end of the file (useful for C language)
```

### Recommended Plugins

The following plugins can be directly installed via `Package Control`.

**StyleToken**: Displays the color (RGB) represented by the code.

**FileHeader**: Customizes file templates. Open `Preferences -> Package Settings -> FileHeader -> Settings - User`, copy the contents from `Default` to `User`, and modify your personal information as follows:

```json
{
  "Default": {
    "author": "Your Name",
    "email": "your@email.com",
    "website": "yourwebsite.com"
  }
}
```

Modify the template content in `Preferences -> Browse Packages... -> FileHeader -> template -> header or body`. Result:

![FileHeader Template Effect](https://media.wiki-power.com/img/ST3-Template-Effect.png)

### Running Python

Since the default Sublime Text compiler lacks user input, you'll need a plugin: `SublimeREPL`. Install it directly via `Package Control` and add a shortcut key in `Preferences -> Key Bindings -> User`:

```json
[
  {
    "keys": ["f5"],
    "caption": "SublimeREPL: Python",
    "command": "run_existing_window_command",
    "args": {
      "id": "repl_python_run",
      "file": "config/Python/Main.sublime-menu"
    }
  }
]
```

Afterward, you can run Python code directly by pressing `F5`.

### Automatic Code Formatting

Install the `Python PEP8 Autoformat` plugin and add the following to `Key Bindings`:

```json
{ "keys": ["alt+r"], "command": "pep8_autoformat" }
```

Now you can use `Alt + R` to format Python code.

## In Summary

Aesthetic appeal enhances productivity. Sublime Text supports more than just Python; it can open and edit files in almost any format. When customized correctly, it provides a minimalistic and powerful coding environment, which can be quite romantic.

## References and Acknowledgments

- [Customizing Sublime Text 3 for Productivity (Part 1)](https://www.sheyilin.com/2015/05/sublime_text_3_tiao_jiao_ni_de_si_ren_li_qi_1/)
- [Using the FileHeader Plugin to Generate File Header Comments (Copyright Information) in Sublime Text](https://blog.csdn.net/afei__/article/details/82890493)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
