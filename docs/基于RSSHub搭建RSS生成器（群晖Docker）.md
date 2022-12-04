---
id: 基于RSSHub搭建RSS生成器（群晖Docker）
title: 基于 RSSHub 搭建 RSS 生成器（群晖 Docker）
---

在群晖 Docker 上搭建 RSSHub 服务，给各种奇奇怪怪的内容生成 RSS 订阅源。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504105215.png)

## 在群晖 Docker 上部署

打开群晖 Docker 套件，下载 `diygod/rsshub` 镜像，双击启动，勾选 `启用自动重新启动`，然后进入 `高级设置`。

在 `端口设置` 页面，手动设置容器端口 1200 所对应的本地端口（比如我设置为 `8004`）：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504085806.png)

随后完成配置，启动容器。输入群晖本地 IP:8004，如果能看到 RSSHub 的页面，就算安装成功了。

## 使用步骤

详细的使用方法请参考 [**RSSHub 官方文档**](https://docs.rsshub.app/)

举个简单的例子，在官方文档中查到，豆瓣 `正在上映的电影` 生成方法如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504104630.png)

那么，使用 `你的域名/douban/movie/playing` 就可以使用自己的服务器来生成 RSS 源了。

建议使用群晖系统自带的反向代理，实现 HTTPS 加密访问。具体教程可以跳转文章 [**用群晖自带反向代理实现 HTTPS 访问**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE)

## 使用 RSSHub Radar 自动检测路由

[**RSSHub Radar**](https://github.com/DIYgod/RSSHub-Radar) 是一个可以帮助你快速发现和订阅当前网站 RSS 和 RSSHub 的浏览器扩展。

在其设置页面填入自定义地址即可使用。

## 参考与致谢

- [RSSHub 官方文档](https://docs.rsshub.app/)
- [在群晖中使用 Docker 安装 RSSHub](https://immwind.com/use-docker-install-rsshub-in-synology)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

