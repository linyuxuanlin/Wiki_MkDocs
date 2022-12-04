---
id: Node.js和npm的安装与卸载（MacOS）
title: Node.js 和 npm 的安装与卸载（MacOS）
---

## 安装

[http://nodejs.cn/download/](http://nodejs.cn/download/)

## 卸载

通过 `homebrew` 安装的：

```shell
brew uninstall node
```

通过 `.pkg` 安装包安装的：

```shell
sudo rm -rf /usr/local/{bin/{node,npm},lib/node_modules/npm,lib/node,share/man/*/node.*}
```

## 疑难解答

Q：MacOS 修改用户名后，提示权限不足：`EACCES: permission denied` A：`sudo npm install -g appium --unsafe-perm=true --allow-root` ，以非安全模式运行。



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

