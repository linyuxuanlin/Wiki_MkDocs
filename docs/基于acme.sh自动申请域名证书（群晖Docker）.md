---
id: 基于acme.sh自动申请域名证书（群晖Docker）
title: 基于 acme.sh 自动申请域名证书（群晖 Docker）
---

本文介绍如何使用 Docker 镜像 acme.sh，实现名证书自动申请和续签功能。

[**acme.sh**](https://github.com/acmesh-official/acme.sh) 可以从 letsencrypt 生成免费的证书，支持 Docker 部署，支持 http 和 DNS 两种域名验证方式，其中包括手动，自动 DNS 及 DNS alias 模式方便各种环境和需求。可同时申请合并多张单域名，泛域名证书，并自动续签证书和部署到项目。

## 准备 DNS API

本文以腾讯云为例申请 DNS API，其他解析平台请参考官方文档 [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi)。

首先，打开 [**DNSPOD**](https://console.dnspod.cn/)，点击右上角头像 - `密钥管理`

接着，创建一个新的密钥，并拷贝 **ID** 与 **Token**。

## 在群晖 Docker 上部署

本教程介绍的是 Docker 的 daemon 守护模式，一直挂着容器，实现证书到期自动续期的功能。

### 创建配置文件夹

我们先创建 `/docker/acme.sh` 文件夹，再手动创建 `account.conf` 文件：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210430212420.png)

接着，我们编辑这个文件，手动添加这几行：

```conf
export DP_Id="刚刚申请的 ID"
export DP_Key="刚刚申请的 TOKEN"
AUTO_UPGRADE='1'
```

随后保存并关闭文件。

### 下载镜像并配置容器

打开群晖 Docker 套件，下载 `neilpang/acme.sh` 镜像，双击启动并进入 `高级设置`

在 `卷` 页面配置挂载的文件夹，点击 `添加文件夹`，选择本地的 `docker/acme.sh` 路径，装载路径填 `/acme.sh`（默认不可变）：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210430214221.png)

在 `网络` 页面，勾选 `使用与 Docker Host 相同的网络`。

接着，切换到 `环境` 页面，在 `命令` 框里填入 `daemon` 命令：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210430215244.png)

随后创建并运行容器。双击已运行的容器，切换到 `终端机` 页面，点击 `通过命令启动`，输入 `sh` 后点确定。

输入以下命令实现自动更新：

```shell
acme.sh --upgrade --auto-upgrade
```

然后输入以下命令申请证书：

```shell
acme.sh --issue --dns dns_dp -d wiki-power.com -d *.wiki-power.com
```

其中，`dns_dp` 代表腾讯云 DNSPod，如果是阿里云请填写 `dns_ali`，CLoudflare 填写 `dns_cf`，其他请参考官方手册 [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi)。另外，其中 `*.wiki-power.com` 代表申请的是泛域名证书。如果需要同时申请多域名，可以按照以下的方式：

```shell
acme.sh --issue --dns dns_dp -d aaa.com -d *.aaa.com -d bbb.com -d *.bbb.com -d ccc.com -d *.ccc.com
```

在 daemon 守护模式下，acme.sh 会根据申请记录，每 60 天自动更新证书。

### 生成证书

如果一切顺利，你可以在 `docker/acme.sh/域名命名的文件夹` 内发现 `域名.cer` 和 `域名.key`，这就是证书和密钥文件，可以拷贝至需要用到的地方。

## 参考与致谢

- [群晖 NAS 高级服务 - docker 部署 acme.sh 自动申请域名证书](https://www.ioiox.com/archives/88.html)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

