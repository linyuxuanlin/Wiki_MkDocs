---
id: 使用Watchtower自动更新容器（群晖Docker）
title: 使用 Watchtower 自动更新容器（群晖 Docker）
---

使用 Watchtower 自动更新群晖 Docker 上的容器。

## 在群晖 Docker 应用中下载镜像

打开群晖 Docker 套件，下载 `containrrr/watchtower` 镜像即可。

## 在任务计划中配置 Watchtower

打开群晖的 `控制面板` - `任务计划` - `新增` - `计划的任务` - `用户定义的脚本`，随后按以下图片填写配置：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202301092319956.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202301092321592.png)

其中的脚本：

```shell
docker run --rm --name watchtower -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once calibre-web freshrss code-server
```

注意，脚本的最后 `calibre-web freshrss code-server` 是需要更新的容器名，请替换为你需要更新的；或者留空表示更新全部容器。

保存，运行脚本即可实现 Docker 容器批量定时更新。

## 参考与致谢

- [如何优雅地使用一条命令更新群晖 docker 容器 - Watchtower 教程](https://post.smzdm.com/p/awzggnqp/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
