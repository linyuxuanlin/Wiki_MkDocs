---
id: 如何实现外网RDP远控（frp）
title: 如何实现外网 RDP 远控（frp）
---

使用 frp 在任意网络下实现远程桌面控制。

## 为什么使用 RDP

RDP 是 Windows 自带的协议。相比市面上的远程桌面软件，如 Todesk、Anydesk、向日葵等，有以下优势：

- 兼容性更佳，根据设备自适应分辨率，可连接键鼠使用
- 自由度高，不限制设备数量，也没有会员体系
- 连接速度取决于电脑网速和服务器配置

## 为什么使用 frp

RDP 仅支持同 IP 段使用，为了在外网下实现远控，我们需要用 frp 方法给内网做穿透。

frp 是一个反向代理软件，体积轻量但功能强大，可以使处于内网或防火墙后的设备对外界提供服务，它支持 HTTP、TCP、UDP 等众多协议。  
用 frp 实现外网 RDP 远控的原理，就是让被控端与服务器相连，我们通过服务器来间接连接被控端，从而实现远控。

## 准备

- 服务端（可以是云服务器，也可以是有公网 IP 的实体机）
- 被控端（Windows 必须是专业版以上）
- 远控端（全平台都适用）

## 服务端配置

首先，查看服务器架构：

```shell
arch
```

参考 frp 的 [**Releases**](https://github.com/fatedier/frp/releases) 页面，选择符合自己架构的版本下载（比如我是 `X86_64` 架构，即选择 `amd64`）:

```shell
wget https://github.com/fatedier/frp/releases/download/v0.36.2/frp_0.36.2_linux_amd64.tar.gz
```

下载后，解压并改名：

```shell
tar -zxvf frp_0.36.2_linux_amd64.tar.gz && mv frp_0.36.2_linux_amd64 frp
```

我们看一下 frp 文件夹内的文件：

```shell
cd frp && ls
```

- frps
- frps.ini
- frpc
- frpc.ini

其中，`frps` 与 `frps.ini` 是服务端的程序与配置文件（s 结尾代表 server），而 `frpc` 与 `frpc.ini` 是客户端相关的（c 结尾代表 client），我们现在暂时不用，可以删除：

```shell
rm -f frpc frpc.ini
```

接下来，我们修改 `frps.ini` 文件：

```shell
vim frps.ini
```

```ini title="frps.ini"
[common]
bind_port = 7000
dashboard_port = 7500
token = 12345678
dashboard_user = admin
dashboard_pwd = admin
```

- **bind_port**：客户端和服务端连接的端口，在之后配置客户端时会用上，一般默认即可。
- **dashboard_port**：服务端仪表板的端口，一般默认即可。如果按默认设置为 `7500`，则可通过 `7500` 端口访问仪表盘（例如 `服务器 IP:7500`），查看 frp 状态。
- **token**：客户端和服务端连接的口令，请自行设置。
- **dashboard_user** / **dashboard_pwd**：仪表盘用户名和密码，请自行设置。

编辑完成后，按 `Esc` 后输入 `:wq` 保存退出。

为了在后台运行 frp 服务，我们可以使用 nohup 命令：

```shell
nohup ./frps -c frps.ini &
```

如果看到以下输出：

```shell
nohup: ignoring input and appending output to 'nohup.out'
```

即表示服务正常运行。我们也可以用 `jobs` 命令，查看正在运行的服务。

为了测试服务端是否配置成功，我们可以访问 `x.x.x.x:7500`，使用上面配置的用户名和密码，看看能否顺利进入仪表盘。如果访问不了仪表盘，也有可能在服务器的防火墙处放开相关端口。

## 被控端配置

还是参考 frp 的 [**Releases**](https://github.com/fatedier/frp/releases) 页面，选择符合自己架构的版本下载。下载后解压重命名，可删除 `frps` 和 `frps.ini` 文件。打开 `frpc.ini` 文件：

```ini title="frpc.ini"
[common]
server_addr = x.x.x.x
server_port = 7000
token = 12345678
[rdp]
type = tcp
local_ip = 127.0.0.1
local_port = 3389
remote_port = 7001
[smb]
type = tcp
local_ip = 127.0.0.1
local_port = 445
remote_port = 7002
```

- **server_addr**：服务器 IP 地址，请自行修改。
- **server_port**：保持与服务端 `bind_port` 的值相同即可，默认是 `7000`。
- **token**：连接口令，保持与服务端配置的 `token` 相同。

接下来，我们配置自定义的规则：

- **[rdp]**：[xxx] 表示规则名称，可自定义。
- **type**：转发的协议类型，可选 TCP/UDP
- **local_port**：本地端口号，这里填写的是 RDP 协议的端口（3389）
- **remote_port**：在服务端开放的端口号，可自定义。

> RDP（Remote Desktop 协议）在 Windows 上默认的端口号为 3389，协议 TCP。
> SMB（Windows 文件共享协议）默认端口号为 445，协议 TCP。

为了在后台运行 frpc，我们创建脚本 `frpc.vbs`，将以下内容粘贴进去：

```vb title="frpc.vbs"
set ws=WScript.CreateObject("WScript.Shell")
ws.Run "c:\frp\frpc.exe -c c:\frp\frpc.ini",0
```

注意可能需要修改路径。

将 `frpc.vbs` 放入 `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp` 目录内，即可实现开机自启动。

如果想测试使用，可以直接运行脚本，或重启自动运行。

## 远控端配置

### 控制端是移动设备

如果需要在手机、iPad 上远控电脑，则需要先安装 `Microsoft 远程桌面` App，然后执行以下步骤：

1. 在 App 内右上角点击 `+` - `添加电脑`
2. `电脑名称` 填入 `IP:remote_port`，例如 `x.x.x.x:7001`，点击返回
3. `账户名称` 填入被控端电脑的账户密码，点击返回

如果一切配置正常，这时候应该可以成功远程控制了。

### 控制端是 Windows

直接在开始菜单搜索打开 `远程桌面连接`，填入 `IP:remote_port` 例如 `x.x.x.x:7001`，按提示输入用户名密码，即可实现远程控制。

## 参考与致谢

- [使用 frp 进行内网穿透](https://sspai.com/post/52523)
- [Linux 的 nohup 命令的用法](https://ehlxr.me/2017/01/18/Linux-%E7%9A%84-nohup-%E5%91%BD%E4%BB%A4%E7%9A%84%E7%94%A8%E6%B3%95/)
- [【教程】通过 frp 实现自建远程桌面](https://pa.ci/77.html)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

