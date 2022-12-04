---
id: 如何在iPad上运行VSCode
title: 如何在 iPad 上运行 VS Code
---

注：本教程基于 code-server v3.8.0，CentOS 8.2.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20201221140748.jpg)

## 补充更新

更推荐以 Docker 方式安装 code-server 服务。  
仅需一行命令部署，且无需配置后台运行，自带 Git 等环境。  
详见：[**Docker 方式运行 code-server**](https://wiki-power.com/unlist/Docker%E6%96%B9%E5%BC%8F%E8%BF%90%E8%A1%8Ccode-server)

如果你不想用 Docker 的方式部署，请继续阅读下文。

## 一、配置服务器

首先，你需要有一台 24h 不停机的服务器（推荐买阿里云 / 腾讯云学生机，只需 ¥9.9/月）  
为保证使用体验，这里推荐服务器的配置：

- 2 核以上
- 1GB 以上内存

刷 Linux（这里我使用 CentOS 8.2），确保 ssh 能正常连上即可。



## 二、安装 code-server



在新的版本下（≥v3.8.0），可以直接使用脚本安装：

```shell
curl -fsSL https://code-server.dev/install.sh | sh
```

如果发现半天下载不下来，多半是因为 DNS 污染，参考 [**GitHub 改 Host**](https://wiki-power.com/GitHub改Host) 解决。

## 三、运行 code-server

使用命令：

```shell
export PASSWORD="设置一个访问密码" && code-server --port 80 --host 0.0.0.0 --auth password
```

如果没有出现错误，那么打开浏览器，输入服务器的 IP 地址访问，就可以看到一个在线的 VS Code 了。

## 四、配置后台运行

运行在前台的 code-server ，会因为 ssh 退出而结束进程。  
为了使其能在后台运行，我们可以使用 screen 程序（可以把它理解为一个容器）。

### 1. 安装 screen

```shell
yum install screen
```

### 2. 创建 screen 作业

```shell
screen -S VSCode-online # VSCode-online 为自取的名字
```

### 3. 开启 code-server 服务

```shell
export PASSWORD="设置一个访问密码" && code-server --port 80 --host 0.0.0.0 --auth password
```

如果顺利的话，就可以在浏览器输入 IP 地址访问了。

## 拓展

### 添加桌面快捷方式

如果在 iPad 上使用，可以用 Safari 浏览器打开，点击右上角 `分享` 图标 --> `添加到主屏幕` 。  
可以将其假装为一个 App 使用，并隐去浏览器状态栏。  
顺带说一句，外接键鼠也都支持。

### screen 的其他操作

- 查看正在运行的作业 id：`screen -ls`
- 重新进入运行中的 screen 作业：`screen -r 作业id # 作业 id 需要包含前缀的数字标识`
- 结束某作业的运行：`screen -X -S 作业id quit`
- 退出当前作业的 screen 界面：`Ctrl + A + D`

### code-server 相关命令参数

- 通过外网访问：code-server 服务默认只运行在本地（`127.0.0.1`）。为了能通过 IP 访问，可以添加 `--host 0.0.0.0` 参数
- 指定运行端口：`--port xxxx`，你可以将 `xxxx` 替换为 `8888` ；也可以是 `80` （走 Http 协议，直接用 IP 访问，不用加端口号）
- 设置访问密码：加上`--auth password` ；如不需要，则不加任何参数，或加上 `--auth none`

### 安装 Git

VS Code 配合 Git 使用，方便进行云开发。  
可以使用如下命令安装 Git：

```shell
yum install git
```

### 使用域名访问

通过服务器 IP 访问也许会有些奇怪，我们可以绑定一个自定义的域名，通过域名来访问 code-server 服务。  
购买一个域名，在 DNS 解析处添加服务器 IP 的，使用 A 类型即可。

### https

【施工中】

### 当前版本 bugs 及解决

- 无法通过 VS Code 内置的 Settings Sync 服务同步用户设置：可以通过额外安装 [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) 插件解决
- Settings Sync 跳转 GitHub 登录出错：使用电脑浏览器进行配置
- iPad 上用鼠标滚轮无法正常滚动页面：目前只能使用直接触摸滚动，或用键盘方向键替代

## 参考与致谢

- [在浏览器上运行 VSCode（旧）](https://wiki-power.com/在浏览器上运行VSCode（旧）)
- [GitHub 改 Host](https://wiki-power.com/GitHub改Host)
- [screen 的安装和使用](https://www.jianshu.com/p/420569381e74)
- [Setup Guide · cdr/code-server](https://github.com/cdr/code-server/blob/v3.8.0/doc/guide.md)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

