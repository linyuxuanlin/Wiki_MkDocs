# Configuring Oh My Zsh on CentOS

## Check Current Shell

```Shell
echo $SHELL
```

In general, it will return `bin/bash`.

## Install zsh

```shell
yum install -y zsh
```

## Switch Default Shell to zsh

This command needs to be run under root user:

```shell
chsh -s /bin/zsh
```

## Install git

```shell
yum install -y git
```

## Install Oh My Zsh

### Automatic

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
or
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

### Manual

If you cannot install it automatically (probably due to the Great Firewall), you can install it manually by following these steps:

Download the source code:

```shell
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

Copy the configuration:

```shell
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

## Modify Oh My Zsh Theme

List all themes:

```shell
ls ~/.oh-my-zsh/themes
```

Modify the theme:

```shell
vim ~/.zshrc
```

Change the default theme `ZSH_THEME="robbyrussell"` to your favorite one.

## Restart to Take Effect

```shell
reboot
```

## Reference and Acknowledgement

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.