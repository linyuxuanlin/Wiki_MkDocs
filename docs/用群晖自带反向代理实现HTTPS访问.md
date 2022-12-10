---
id: 用群晖自带反向代理实现HTTPS访问
title: 用群晖自带反向代理实现 HTTPS 访问
---

首先，你需要一个外部访问群晖的 IP 或域名，并且已经申请了 SSL 证书。详细说明可跳转文章 [**基于 acme.sh 自动申请域名证书（群晖 Docker）**](https://wiki-power.com/%E5%9F%BA%E4%BA%8Eacme.sh%E8%87%AA%E5%8A%A8%E7%94%B3%E8%AF%B7%E5%9F%9F%E5%90%8D%E8%AF%81%E4%B9%A6%EF%BC%88%E7%BE%A4%E6%99%96Docker%EF%BC%89)

## 配置反向代理

依次打开 `控制面板` - `登录门户` - `高级` - `反向代理服务器`。

以 [**基于 Bitwarden 搭建密码管理器（群晖 Docker）**](https://wiki-power.com/%E5%9F%BA%E4%BA%8EBitwarden%E6%90%AD%E5%BB%BA%E5%AF%86%E7%A0%81%E7%AE%A1%E7%90%86%E5%99%A8%EF%BC%88%E7%BE%A4%E6%99%96Docker%EF%BC%89)
我们新增名称为 `bitwarden` 的反代服务。按照下图填写配置：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210503213004.png)

- `来源`
  - `协议`：选择 `HTTPS`
  - `主机名`：填写外部访问的域名
  - `端口`：填写外部访问的端口
  - 勾选 `启用 HSTS`（强制跳转 HTTPS）
- `目的地`
  - `协议`：选择 `HTTP`
  - `主机名`：填写 `localhost`
  - `端口`：填写内部访问的端口（对于 bitwarden 来说，就是刚刚容器 `80` 端口映射的端口，比如 `8003`）

## 配置证书

依次打开 `控制面板` - `安全性` - `证书`，选中正在使用的证书，点击 `设置`，确保 `bitwarden` 的反代服务所对应的域名的证书为当前证书即可。

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

