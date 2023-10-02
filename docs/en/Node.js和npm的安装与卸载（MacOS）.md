# Installation and Uninstallation of Node.js and npm (MacOS)

## Installation

[http://nodejs.cn/download/](http://nodejs.cn/download/)

## Uninstallation

If installed through `homebrew`:

```shell
brew uninstall node
```

If installed through `.pkg` package:

```shell
sudo rm -rf /usr/local/{bin/{node,npm},lib/node_modules/npm,lib/node,share/man/*/node.*}
```

## Troubleshooting

Q: After changing the username on MacOS, it prompts "EACCES: permission denied". A: Run `sudo npm install -g appium --unsafe-perm=true --allow-root` in unsafe mode.

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.