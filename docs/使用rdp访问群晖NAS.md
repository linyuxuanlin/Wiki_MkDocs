---
id: 使用rdp访问群晖NAS
title: 使用 rdp 访问群晖 NAS
---

使用 frp 在任意网络下访问群晖 NAS。

## 为什么要通过 frp 访问群晖

- 无公网 IP
- QuickConnect 服务太慢
- 花生壳等服务需要单独买流量

## 服务端配置

跳转文章 [**如何实现外网 RDP 远控（frp）· 服务端配置**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%85%8D%E7%BD%AE)。需要注意的是，`frps.ini` 配置文件中的 `vhost_http_port` / `vhost_https_port` 参数必须保留。

### 绑定域名

- 在域名解析处以服务器 IP 添加 A 记录
- 在云服务器处配置域名绑定

## 群晖 NAS 配置

### 编辑配置文件

在任意位置新建 `frps.ini` 文件，填入以下内容：

```ini title="frps.ini"
[common]
server_addr = 服务器 IP
server_port = 服务端 frp 端口，默认为 7000
token = 密钥，需与服务端配置的相同

[dsm-http]
type = tcp
local_ip = localhost
local_port = 群晖 DSM http 端口，默认为 5000
custom_domains = 绑定的域名
remote_port = 自定义远程端口

[dsm-https]
type = tcp
local_ip = localhost
local_port = 群晖 DSM https 端口，默认为 5001
custom_domains = 绑定的域名
remote_port = 自定义远程端口

[ssh]
type = tcp
local_ip = localhost
local_port = 默认为 22
custom_domains = 绑定的域名
remote_port = 自定义远程端口
```

### 使用 Docker 方法

在群晖的 Docker 内安装 `stilleshan/frpc` 映像，使用以下参数初始化容器：

- 勾选 `使用高权限执行容器`
- 勾选 `启用自动重新启动`
- 在 `卷` 标签页添加文件，选择本地的 `frps.ini` 文件，对应装载路径为 `/frp/frpc.ini`
- 勾选 `使用与 Docker Host 相同的网络`

启动容器，稍等片刻，就可以通过域名 + http 端口号的形式访问群晖 DSM 了。

## 参考与致谢

- [群晖 NAS 使用 Docker 安装配置 frpc 内网穿透教程](https://www.ioiox.com/archives/26.html)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

