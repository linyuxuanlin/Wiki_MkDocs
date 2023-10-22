# Configuring Oh My Zsh on CentOS

## Checking the Current Shell

```Shell
echo $SHELL
```

In most cases, this will return `bin/bash`.

## Installing Zsh

```shell
yum install -y zsh
```

## Changing the Default Shell to Zsh

You need to run this command as the root user:

```shell
chsh -s /bin/zsh
```

## Installing Git

```shell
yum install -y git
```

## Installing Oh My Zsh

### Automated Installation

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
or
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

### Manual Installation

If you cannot install using the methods above (possibly due to restrictions), you can manually install Oh My Zsh with the following steps:

Download the source code:

```shell
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

Copy the configuration:

```shell
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

## Changing the Oh My Zsh Theme

List all available themes:

```shell
ls ~/.oh-my-zsh/themes
```

Modify the theme:

```shell
vim ~/.zshrc
```

Change the default theme, which is `ZSH_THEME="robbyrussell," to your preferred one.

## Reboot to Apply Changes

```shell
reboot
```

## References and Acknowledgments

- [CentOS 7: Install Zsh and Configure Oh My Zsh](https://www.jianshu.com/p/4ce7d511bc13)
- [Install Oh My Zsh on CentOS](https://www.jianshu.com/p/556ff130fc65)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.