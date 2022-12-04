---
id: Hugo极简搭建指南
title: Hugo 极简搭建指南
---


Hugo 是一个搭建网页的框架，有极高的构建和部署速度。至于在 Windows 下的安装配置，官方文档并未详细说明，第三方教程也参差不齐，所以我写了这一篇教程。


## 下载安装

1. 打开 Hugo 官方 GitHub 的 [** Releases**](https://github.com/gohugoio/hugo/releases) 页面
2. 选择最新的版本下载（选择 `hugo_xxx_Windows-64/32bit.zip`）
3. 将压缩包内的 `hugo.exe` 文件解压至 `D:\hugo` 文件夹目录下
4. 在 `文件资源管理器`（即 `我的电脑`）中空白处点击鼠标右键，打开属性
5. 依次点击 `高级系统设置` - `环境变量` ，双击打开系统变量中的 `Path`
6. 在环境变量界面中双击空白行，添加 `D:\hugo`，点击确定

打开命令提示符，输入语句：

```
hugo version
```

以确认 Hugo 是否安装成功（如果安装成功就能看到版本号）

## 创建站点

切换至相应目录下，使用如下语句：

```
hugo new site quickstart
```

这将在一个叫 `quickstart` 的文件夹内创建一个新的 Hugo 站点。

## 添加主题

主题的挑选可以到官方的 [**主题页面**](https://themes.gohugo.io/) 

直接跳转至 GitHub 下载主题文件夹，解压至站点的 `theme` 目录下即可。

执行如下命令，将主题添加至站点的配置文件中：

```
echo 'theme = "主题文件夹的名字"' >> config.toml
```

## 创建文章

使用如下命令，创建一篇文章：

```
hugo new posts/my-first-post.md
```

然后打开文章，将 `front matter` 中的 `draft: true` 改为 `draft: false`，以移出草稿区，正常呈现出来。

## 启动 Hugo 服务

使用以下命名启动 Hugo 本地预览服务：

```
hugo server -D
```

打开 [**http://localhost:1313/**](http://localhost:1313/) ，即可看到实时预览的站点（在本地的任何修改，将即时更新）。

## 本地部署

使用如下命令：

```
Build static pages
```

将站点部署进行本地部署（输出于 `public` 文件夹目录下）。

## 参考与致谢 

* [Quick Start · Hugo](https://gohugo.io/getting-started/quick-start/)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

