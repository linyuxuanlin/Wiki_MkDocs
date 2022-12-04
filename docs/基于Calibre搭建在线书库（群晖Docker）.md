---
id: 基于Calibre搭建在线书库（群晖Docker）
title: 基于 Calibre 搭建在线书库（群晖 Docker）
---

如何在群晖 NAS 用 calibre-web（Docker）搭建一个在线书库。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429125418.png)

相比于传统用文件夹的方式，以开源的 Calibre 为代表的书库管理方式，能提供更丰富的功能诸如在线阅读、下载、格式转换、推送到邮箱、去除重复书籍等。calibre-web 是一个基于 Calibre 的 Docker 镜像，可以让我们很方便地将书库部署在像群晖这样的服务器上。

## 建立初始文件夹

首先，建立书库资源文件夹，这里我直接在磁盘根目录建立了一个名为 `book` 的共享文件夹：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429214028.png)

相应地，在 `docker` 文件夹内创建一个名为 `calibre-web` 文件夹，专门用于存放 Docker 镜像的配置文件。

## 创建容器

打开群晖的 Docker 套件，在注册表中搜索 `johngong/calibre-web`，双击下载后，初始化容器，点进高级设置。

在 `卷` 页面添加映射文件夹，装载路径分别是 `/library` 和 `/config`：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429214908.png)

在 `端口设置` 页面添加端口映射，主要将容器内部的 `8083` 端口映射出去，这里我选择 `5004`。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429215121.png)

随后，创建并启动容器。

## 运行测试

打开群晖内网 IP:5004 打开管理界面，默认的账号是 `admin`，密码是 `admin123`

需要注意的是，默认是没有书籍上传功能的，需要依次点击右上角 `管理权限` - `编辑基本配置` — `启用上传`，才能启用书籍上传功能。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429215628.png)

## 启用 HTTPS

### 使用群晖系统自带的反向代理（推荐）

具体教程可以跳转文章 [**用群晖自带反向代理实现 HTTPS 访问**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE)

### 直接添加证书方法

将申请到的证书和密钥文件复制一份到 `docker/calibre-web/` 目录下。

随后在 calibre-web 内依次点击 `管理权限` - `编辑基本配置` - `服务器配置`，配置 SSL 证书及密钥文件的路径（例如我是 `/config/wiki-power.com.cer` 和 `/config/wiki-power.com.key`），随后点击保存。

这样就可以开启 HTTPS 访问了。

## 参考与致谢

- [群晖 Docker 安装 calibre-web 图书管理系统](https://www.chrno.cn/index.php/docker/15.html)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

