---
id: 在浏览器上运行VSCode（旧）
title: 在浏览器上运行 VS Code（旧）
---

注：≥v3.8.0 版本 code-server 的部署请参考 [**如何在 iPad 上跑 VS Code**](https://wiki-power.com/如何在iPad上运行VSCode) ，有更简洁的方法。

## 背景

众所周知，VS Code 是一个功能十分强大的编辑器。如果能在 iPad 这类轻便的平台上使用 VS Code（iPadOS 对键鼠的支持已经能够媲美桌面系统），那我们就可以随时随地工作了。

恰好有一个让 VS Code 跑在服务器上的服务：code-server. 部署完成后，可通过浏览器访问。这样，只要有网络，任何设备都能够轻松用上 VS Code.

## 准备环境

一台安装有 Linux 的服务器（我用的是阿里云最低配的学生机）。

官方要求配置如下：

> - 64-bit host.
> - At least 1GB of RAM.
> - 2 cores or more are recommended (1 core works but not optimally).
> - Secure connection over HTTPS or localhost (required for service workers and clipboard support).
> - For Linux: GLIBC 2.17 or later and GLIBCXX 3.4.15 or later.

## 安装过程

### 1. 下载

```shell
wget https://github.com/cdr/code-server/releases/download/3.1.0/code-server-3.1.0-linux-x86_64.tar.gz # 下载 code-server
```

不要照搬命令，在 code-server 的 [**Release**](https://github.com/cdr/code-server/releases) 页面复制最新版本的链接（根据服务器的架构来选择，我使用的是 `code-server-3.1.0-linux-x86_64.tar.gz` 版本），用 `wget` 或 `SFTP` 下载 / 传输至服务器上。

如果下载速度很慢，可复制下载链接，使用 [**GitHub 文件加速**](https://gh.api.99988866.xyz/) 这个网站获取国内加速下载链接。

```shell
tar -xvf code-server-3.1.0-linux-x86_64.tar.gz # 解压
```

### 2. 安装

```shell
cd code-server
export PASSWORD="yourpassword"
./code-server --port 8888 --host 0.0.0.0
```

- 将 `yourpassword` 改为你设定的密码，否则会随机生成密码
- `--port 8888` 意为指定运行端口，你可以设置为 `80` 端口（Http 协议），这样访问的时候就不用加端口号了
- `--host 0.0.0.0` 让服务能通过外网访问。默认的 `127.0.0.1` 只能本地访问
- 如不需要密码验证，可以加上 `--auth none`
- 如启动服务不成功，可能为 **处理器架构版本** 选择错误，换一个版本即可

### 3. 配置后台运行

默认直接运行的情况下，ssh 连接一断就没了。为了使其能够后台运行，可以用 `screen` ：

```shell
yum install screen
或
apt-get install screen
```

```shell
screen -S VSCode-online # VS Code-online 为自取的名字
export PASSWORD="password" && ./code-server --port 8888 --host 0.0.0.0
```

再次进入运行中的 screen 作业：

```shell
screen -r 作业名
```

如果需要停止后台 screen 的运行：

```shell
screen -ls # 查看已运行服务的 id
screen -X -S id quit # 替换掉 id
```

退出 screen：`Ctrl + A + D`

### 4. 轻松使用

在浏览器直接输入 `http://你的服务器 ip` 即可享用云端 VS Code.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200413181001.jpg)

配置域名访问：`待探索……`

## 现阶段问题

- 可直接下载的插件数量，手动安装插件很麻烦，且没有自动同步插件 / 用户设置功能，之后的版本应该会更新解决

## 参考与致谢

- [在浏览器上运行 VS Code，code-server（阿里云服务器）](https://copyfuture.com/blogs-details/20200405045150018h4edt0f4q8486jq)
- [在浏览器上运行 VS Code，code-server](https://segmentfault.com/a/1190000022267386)
- [（推荐）VS code 在线工具——code-serve 在云服务器上的安装和使用 与常见的问题解决 （超详细）](https://blog.csdn.net/Granery/article/details/90415636)
- [iPad 编程学习环境---VS Code web 版本搭建](https://blog.icodef.com/2019/11/17/1670)

> 文章作者：**Power Lin**
> 原文地址：<https://wiki-power.com>
> 版权声明：文章采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议，转载请注明出处。
