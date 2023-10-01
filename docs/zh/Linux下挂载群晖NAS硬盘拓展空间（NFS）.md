---
id: Linux下挂载群晖NAS硬盘拓展空间（NFS）
title: Linux 下挂载群晖 NAS 硬盘拓展空间（NFS）
---

如果你的服务器储存空间有限，可以尝试挂载群晖 NAS 上的硬盘，作为拓展的储存空间。

## 在群晖 NAS 上配置

### 开启 NFS 服务

打开群晖的 `设置` - `文件服务` - `NFS`，把 NFS 服务勾选上，协议选最新即可。

### 配置文件夹的 NFS 权限

在 `设置` - `共享文件夹` 下，选择需要开启 NFS 的共享文件夹，点击 `编辑`，切换到 `NFS 权限` 的标签栏下，点击 `新增`，添加新的 NFS 规则。

`服务器或IP地址`，填写需要访问群晖的服务器的 IP（比如我的服务器和群晖在同一局域网下，那么填我的服务器的内网 IP 192.168.1.2 即可）。勾选 `允许来自非特杈端口的连接` 和 `允许用户访问已装载了文件夹`，其他设置保持默认即可。

## 在服务器上执行挂载

首先，安装 nfs 服务：

```bash
apt update
apt install nfs-common
```

随后，在服务器上创建挂载的路径，比如：

```bash
sudo mkdir /DATA/nfs/music
```

最后执行挂载命令：

```bash
mount -t nfs NAS的IP地址:共享文件夹的路径 /NFS客户端路径
```

比如：

```bash
sudo mount -t nfs 192.168.1.3:/volume1/music /DATA/nfs/music
```

如果没有报错，使用 `df` 命令即可查看挂载情况。

## 参考与致谢

- [
  Linux(Ubuntu)通过 NFS 服务挂载群晖 NAS 为虚拟磁盘](https://cloud.tencent.com/developer/article/2104277)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
