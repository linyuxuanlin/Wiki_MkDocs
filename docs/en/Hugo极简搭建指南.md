# Hugo Minimal Setup Guide

Hugo is a framework for building websites with exceptionally fast build and deployment speeds. When it comes to installation and configuration on Windows, the official documentation lacks detailed instructions, and third-party tutorials vary in quality. Therefore, I have crafted this tutorial to fill the gap.

## Download and Installation

1. Navigate to the [**Releases**](https://github.com/gohugoio/hugo/releases) page on Hugo's official GitHub.
2. Choose the latest version for download (select `hugo_xxx_Windows-64/32bit.zip`).
3. Extract the `hugo.exe` file from the downloaded zip archive to the `D:\hugo` directory.
4. In Windows File Explorer (commonly known as "My Computer"), right-click on an empty area and open "Properties."
5. Click on "Advanced system settings" and then "Environment Variables."
6. Under the System Variables section, double-click on "Path."
7. In the Environment Variables window, double-click on an empty row and add `D:\hugo`. Click "OK."

Open the Command Prompt and enter the following command:

```plaintext
hugo version
```

This will confirm whether Hugo has been successfully installed (the version number should be displayed if it is).

## Create a Site

Navigate to the desired directory and use the following command:

```plaintext
hugo new site quickstart
```

This will create a new Hugo site within a folder named `quickstart`.

## Add a Theme

You can explore and select themes from the official [**Themes page**](https://themes.gohugo.io/).

Download the theme folder directly from its GitHub repository and extract it into the `themes` directory of your site.

Run the following command to add the theme to your site's configuration file:

```plaintext
echo 'theme = "theme-folder-name"' >> config.toml
```

## Create Content

To create a new post, use the following command:

```plaintext
hugo new posts/my-first-post.md
```

Then, open the post and change `draft: true` to `draft: false` in the "front matter" to publish it and make it visible.

## Start the Hugo Server

Initiate Hugo's local preview server with the following command:

```plaintext
hugo server -D
```

Open [**http://localhost:1313/**](http://localhost:1313/) to view the real-time preview of your site (any changes made locally will be instantly updated).

## Local Deployment

Use the following command:

```plaintext
Build static pages
```

This will deploy your site locally, and the output will be stored in the `public` directory.

## References and Acknowledgments

- [Quick Start · Hugo](https://gohugo.io/getting-started/quick-start/)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.