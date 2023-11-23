# Installation and Uninstallation of Node.js and npm (MacOS)

## Installation

You can install Node.js and npm by following the steps below:

1. Visit the Node.js website at [http://nodejs.cn/download/](http://nodejs.cn/download/).

2. Download the appropriate installer for MacOS.

3. Follow the installation instructions provided on the website to complete the installation process.

## Uninstallation

If you have installed Node.js and npm using Homebrew, you can uninstall them using the following command:

```shell
brew uninstall node
```

If you have installed Node.js and npm using a `.pkg` installer package, you can uninstall them with the following command:

```shell
sudo rm -rf /usr/local/{bin/{node,npm},lib/node_modules/npm,lib/node,share/man/*/node.*}
```

## Troubleshooting

Q: After changing my MacOS username, I encounter a "permission denied" error, such as `EACCES: permission denied`. How can I resolve this?

A: You can run the following command in non-secure mode to address the permission issue:

```shell
sudo npm install -g appium --unsafe-perm=true --allow-root
```

[Additional troubleshooting information here]
[More troubleshooting tips here]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.