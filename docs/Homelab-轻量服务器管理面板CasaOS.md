---
id: Homelab-轻量服务器管理面板CasaOS
title: Homelab - 轻量服务器管理面板 CasaOS
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304192541.png)

**CasaOS** 是一个简单易用、优雅的开源个人面板，功能包含了文件管理器、服务器状态监测、终端、Docker 容器管理、内置 Docker 应用商店等。

## 部署（shell）

```shell
curl -fsSL https://get.casaos.io | sudo bash
```

默认面板访问地址：<http://localhost:80>

注：如果是部署在有分配反向代理的服务器上，最好在设置内更换面板访问端口，把 80 端口留给 Nginx。

## 参考与致谢

- [官网](https://casaos.io)
- [文档](https://wiki.casaos.io/en/home)
- [GitHub repo](https://github.com/IceWhaleTech/CasaOS)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
