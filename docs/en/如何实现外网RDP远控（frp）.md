# How to Implement Remote Desktop Control (RDP) via External Network (frp)

Use frp to achieve remote desktop control in any network.

## Why Use RDP

RDP is a protocol built into Windows. Compared to remote desktop software on the market, such as Todesk, Anydesk, and Sunflower, it has the following advantages:

- Better compatibility, adapts to device resolution, and can connect to keyboard and mouse
- High degree of freedom, no limit on the number of devices, and no membership system
- Connection speed depends on computer network speed and server configuration

## Why Use frp

RDP only supports use within the same IP range. In order to achieve remote control in an external network, we need to use the frp method to penetrate the internal network.

frp is a reverse proxy software that is lightweight but powerful. It can enable devices behind a firewall or on an internal network to provide services to the outside world. It supports many protocols such as HTTP, TCP, and UDP.  
The principle of using frp to achieve external network RDP remote control is to connect the controlled end to the server, and we indirectly connect to the controlled end through the server, thereby achieving remote control.

## Preparation

- Server (can be a cloud server or a physical machine with a public IP)
- Controlled end (Windows must be Professional or above)
- Remote control end (applicable to all platforms)

## Server Configuration

First, check the server architecture:

```shell
arch
```

Refer to the [**Releases**](https://github.com/fatedier/frp/releases) page of frp, and choose the version that matches your own architecture (for example, I am using the `X86_64` architecture, so I choose `amd64`):

```shell
wget https://github.com/fatedier/frp/releases/download/v0.36.2/frp_0.36.2_linux_amd64.tar.gz
```

After downloading, unzip and rename:

```shell
tar -zxvf frp_0.36.2_linux_amd64.tar.gz && mv frp_0.36.2_linux_amd64 frp
```

Let's take a look at the files in the frp folder:

```shell
cd frp && ls
```

- frps
- frps.ini
- frpc
- frpc.ini

Among them, `frps` and `frps.ini` are the server program and configuration file (s suffix stands for server), while `frpc` and `frpc.ini` are related to the client (c suffix stands for client), which we don’t need for now and can be deleted:

```shell
rm -f frpc frpc.ini
```

Next, we modify the `frps.ini` file:

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

- **bind_port**: the port that the client and server connect to, which will be used when configuring the client later, and the default value is generally sufficient.
- **dashboard_port**: the port of the server dashboard, which is generally set to the default value. If set to `7500` according to the default settings, the dashboard (for example, `server IP:7500`) can be accessed to view the frp status.
- **token**: the password for the client and server connection, please set it yourself.
- **dashboard_user** / **dashboard_pwd**: the username and password of the dashboard, please set it yourself.

After editing, press `Esc` and enter `:wq` to save and exit.

In order to run the frp service in the background, we can use the nohup command:

```shell
nohup ./frps -c frps.ini &
```

If you see the following output:

```shell
nohup: ignoring input and appending output to 'nohup.out'
```

it means that the service is running normally. We can also use the `jobs` command to view the running services.

To test whether the server-side configuration is successful, we can access `x.x.x.x:7500` and use the username and password configured above to see if we can enter the dashboard smoothly. If the dashboard cannot be accessed, it may also be necessary to open the relevant ports in the server's firewall.

## Configuration of the controlled end

Still refer to the [**Releases**](https://github.com/fatedier/frp/releases) page of frp, and choose the version that matches your own architecture to download. After downloading, unzip and rename it, and you can delete the `frps` and `frps.ini` files. Open the `frpc.ini` file:

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

- **server_addr**: Server IP address, please modify it yourself.
- **server_port**: Keep the same value as the `bind_port` of the server-side, which is `7000` by default.
- **token**: Connection password, keep the same as the `token` configured on the server-side.

Next, we configure custom rules:

- **[rdp]**: [xxx] represents the rule name, which can be customized.
- **type**: The protocol type of the forwarding, TCP/UDP can be selected
- **local_port**: The local port number, which is the port number of the RDP protocol (3389) filled in here.
- **remote_port**: The port number opened on the server-side, which can be customized.

> The default port number for RDP (Remote Desktop Protocol) on Windows is 3389, and the protocol is TCP.
> The default port number for SMB (Windows file sharing protocol) is 445, and the protocol is TCP.

In order to run frpc in the background, we create a script `frpc.vbs` and paste the following content into it:

```vbscript title="frpc.vbs"
set ws=WScript.CreateObject("WScript.Shell")
ws.Run "c:\frp\frpc.exe -c c:\frp\frpc.ini",0
```

Note that the path may need to be modified.

Put `frpc.vbs` into the `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp` directory to achieve automatic startup.

If you want to test it, you can run the script directly or restart it to run automatically.

## Remote control configuration

### The control end is a mobile device

If you need to remotely control the computer on your phone or iPad, you need to install the `Microsoft Remote Desktop` App first, and then follow these steps:

1. Click `+` - `Add Computer` in the upper right corner of the App
2. Fill in the `Computer Name` with `IP:remote_port`, for example, `x.x.x.x:7001`, and click `Return`
3. Fill in the account password of the controlled computer in the `Account Name`, and click `Return`

If everything is configured properly, you should be able to remote control successfully at this time.

### The control end is Windows

Just search and open `Remote Desktop Connection` in the start menu, fill in `IP:remote_port` such as `x.x.x.x:7001`, and enter the username and password as prompted to achieve remote control.

## Reference and Acknowledgement

- [Using frp for intranet penetration](https://sspai.com/post/52523)
- [Usage of nohup command in Linux](https://ehlxr.me/2017/01/18/Linux-%E7%9A%84-nohup-%E5%91%BD%E4%BB%A4%E7%9A%84%E7%94%A8%E6%B3%95/)
- [【Tutorial】Realize self-built remote desktop through frp](https://pa.ci/77.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.