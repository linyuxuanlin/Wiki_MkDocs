---
id: 基于Bitwarden搭建密码管理器（群晖Docker）
title: 基于 Bitwarden 搭建密码管理器（群晖 Docker）
---

本文介绍如何在自己的群晖上使用 Docker 对全平台密码管理服务器 Bitwarden 进行私有部署。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503221838.png)

目前的密码管理器方案有 1Password，Lastpass，KeePass，Bitwarden 等，这几种方案各有优劣。在这里我的需求是可多端同步使用，开源可自部署，且有自动填充的功能，同时兼顾界面美观，所以我选择了在自己的群晖上部署 Bitwarden 服务。

## 在群晖 Docker 上部署

### 建立存放数据的文件夹

我们在 `docker` 目录下建立存放 Bitwarden 数据的文件夹（比如 `docker/bitwarden`）。

### 下载镜像并配置容器

打开群晖 Docker 套件，下载 `bitwardenrs/server` 镜像，双击启动，勾选 `启用自动重新启动`，然后进入 `高级设置`。

在 `卷` 页面配置挂载的文件夹，点击 `添加文件夹`，选择本地的 `docker/bitwarden` 路径，装载路径填 `/data`（默认不可变）：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503211711.png)

在 `端口设置` 页面，手动设置容器端口 80 所对应的本地端口（比如我设置为 `8003`）：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503211759.png)

随后完成配置，启动容器。输入群晖本地 IP:8003，我们就能看到 Bitwarden 的登陆页面了。但是当我们创建账户后登录时，会看到这样一条提示：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503212146.png)

这是因为，Docker 容器本身没有提供 https 端口配置，而 Bitwarden 又只能够通过 https 来进行登录（SSL 加密防止中间人攻击）。所以，在这里我们必须使用群晖自带的反向代理服务，通过 https 来访问内部 http 端口了。具体教程可以跳转文章 [**用群晖自带反向代理实现 HTTPS 访问**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE)

## 多设备使用

可以在 Bitwarden 官方的 [**下载页面**](https://bitwarden.com/download/)，下载各版本的客户端

### 桌面端

推荐直接使用浏览器扩展 [**Bitwarden - 免费密码管理器**](https://chrome.google.com/webstore/detail/bitwarden-free-password-m/nngceckbapebfimnlniiiahkandclblb)

在登录的时候，先点击左上角的小齿轮，进入设置：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503215149.png)

在 `自托管环境` 中的 `服务器 URL` 填入群晖 NAS 的 IP:外部端口，即可正常登录。

如果需要，也可以下载桌面客户端使用。

### 移动端

直接在 AppStore 或各应用商城下载 Bitwarden App，在登录页面也需要配置自托管环境，步骤与桌面端相同。

## 备份密码数据库

备份 Bitwarden 数据库的方法有两种：

1. 在网页端或客户端内选择 `导出密码库`
2. 直接备份 `data` 文件夹

## 参考与致谢

- [群晖 NAS 高级服务 - docker 部署 bitwarden 全平台密码管理器](https://www.ioiox.com/archives/70.html)
- [使用群晖搭建第三方 Bitwarden 密码服务器](https://ppgg.in/blog/10271.html#comment-8463)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

