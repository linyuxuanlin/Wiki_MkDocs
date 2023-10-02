# Hugo Minimalist Setup Guide

Hugo is a framework for building websites with extremely fast build and deployment speeds. As for installation and configuration on Windows, the official documentation does not provide detailed instructions, and third-party tutorials are also uneven, so I wrote this tutorial.

## Download and Installation

1. Open the [**Releases**](https://github.com/gohugoio/hugo/releases) page on Hugo's official GitHub.
2. Choose the latest version to download (select `hugo_xxx_Windows-64/32bit.zip`).
3. Extract the `hugo.exe` file from the compressed package to the `D:\hugo` folder directory.
4. Right-click on a blank space in `File Explorer` (i.e. `My Computer`) and open Properties.
5. Click `Advanced system settings` - `Environment Variables`, and double-click `Path` in the System Variables.
6. Double-click on a blank line in the Environment Variables interface, add `D:\hugo`, and click OK.

Open the command prompt and enter the statement:

```
hugo version
```

to confirm whether Hugo has been successfully installed (if it is installed successfully, you can see the version number).

## Create a Site

Switch to the corresponding directory and use the following statement:

```
hugo new site quickstart
```

This will create a new Hugo site in a folder called `quickstart`.

## Add a Theme

Themes can be selected from the official [**Theme Page**](https://themes.gohugo.io/).

Directly jump to GitHub to download the theme folder, and extract it to the `theme` directory of the site.

Execute the following command to add the theme to the site's configuration file:

```
echo 'theme = "theme folder name"' >> config.toml
```

## Create an Article

Use the following command to create an article:

```
hugo new posts/my-first-post.md
```

Then open the article and change `draft: true` in the `front matter` to `draft: false` to remove it from the draft area and display it normally.

## Start Hugo Server

Use the following command to start the Hugo local preview service:

```
hugo server -D
```

Open [**http://localhost:1313/**](http://localhost:1313/) to see the real-time preview of the site (any changes made locally will be updated instantly).

## Local Deployment

Use the following command:

```
Build static pages
```

to deploy the site locally (output to the `public` folder directory).

## References and Acknowledgements

- [Quick Start · Hugo](https://gohugo.io/getting-started/quick-start/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.