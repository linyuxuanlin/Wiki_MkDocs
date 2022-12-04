---
id: CentOS配置OhMyZsh
title: CentOS 配置 Oh My Zsh
---

## 查看当前 Shell

```Shell
echo $SHELL
```

一般情况下会返回 `bin/bash`

## 安装 zsh

```shell
yum install -y zsh
```

## 切换默认 Shell 为 zsh

需要在 root 用户下运行此命令：

```shell
chsh -s /bin/zsh
```

## 安装 git

```shell
yum install -y git
```

## 安装 Oh My Zsh

### 自动

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
或
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

### 手动

如果无法通过上面的方式安装（可能因为墙），则可通过以下方式手动安装：

下载源码：

```shell
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

复制配置：

```shell
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

## 修改 Oh My Zsh 主题

列出所有主题：

```shell
ls ~/.oh-my-zsh/themes
```

修改主题：

```shell
vim ~/.zshrc
```

将默认主题是 `ZSH_THEME="robbyrussell"` 修改为自己喜欢的即可。

## 重启生效

```shell
reboot
```

## 参考与致谢

- [centos7 安装 zsh 配置 oh-my-zsh](https://www.jianshu.com/p/4ce7d511bc13)
- [CentOs 安装 oh my zsh](https://www.jianshu.com/p/556ff130fc65)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

