# How to Achieve Remote Desktop Control over the Internet (frp)

Use frp to achieve remote desktop control in any network.

## Why Use RDP

RDP is a built-in protocol in Windows. Compared to other remote desktop software on the market, such as Todesk, Anydesk, and Sunflower, it has the following advantages:

- Better compatibility, adapts to device resolution based on the device, and allows connection with keyboard and mouse.
- Higher flexibility, no limit on the number of devices and no membership system.
- Connection speed depends on computer network speed and server configuration.

## Why Use frp

RDP only supports use within the same IP range. In order to achieve remote control over the Internet, we need to use the frp method to penetrate the internal network.

frp is a lightweight but powerful reverse proxy software that allows devices behind an internal network or firewall to provide services to the outside world. It supports various protocols such as HTTP, TCP, and UDP.  
The principle of using frp to achieve remote desktop control over the Internet is to connect the controlled end to the server, and we indirectly connect to the controlled end through the server to achieve remote control.

## Preparation

- Server (can be a cloud server or a physical machine with a public IP)
- Controlled end (Windows must be a professional version or above)
- Remote control end (applicable to all platforms)

## Server Configuration

First, check the server architecture:

```shell
arch
```

Refer to the [**Releases**](https://github.com/fatedier/frp/releases) page of frp, and choose the version that matches your architecture (for example, I have an `X86_64` architecture, so I choose `amd64`):

```shell
wget https://github.com/fatedier/frp/releases/download/v0.36.2/frp_0.36.2_linux_amd64.tar.gz
```

After downloading, extract and rename it:

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

Among them, `frps` and `frps.ini` are the server programs and configuration files (s stands for server), while `frpc` and `frpc.ini` are related to the client (c stands for client), which we don't need for now and can be deleted:

```shell
rm -f frpc frpc.ini
```

Next, let's modify the `frps.ini` file:

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

- **bind_port**: The port for the client to connect to the server, which will be used when configuring the client later, and the default value is generally fine.
- **dashboard_port**: The port for the server dashboard, which is generally fine with the default value. If it is set to the default value of `7500`, you can access the dashboard through port `7500` (for example, `Server IP:7500`) to check the frp status.
- **token**: The token for the client to connect to the server, please set it yourself.
- **dashboard_user** / **dashboard_pwd**: The username and password for the dashboard, please set them yourself.

After editing, press `Esc` and then enter `:wq` to save and exit.

To run the frp service in the background, we can use the `nohup` command:

```shell
nohup ./frps -c frps.ini &
```

If you see the following output:

```shell
nohup: ignoring input and appending output to 'nohup.out'
```

it means that the service is running normally. We can also use the `jobs` command to view the running services.

To test whether the server-side configuration is successful, you can access `x.x.x.x:7500` and try to log in to the dashboard using the username and password configured above. If you cannot access the dashboard, it is possible that the relevant ports are blocked by the server's firewall.

## Configuration on the controlled side

Refer to the [**Releases**](https://github.com/fatedier/frp/releases) page of frp and download the version that matches your architecture. After downloading, extract and rename the files. You can delete the `frps` and `frps.ini` files. Open the `frpc.ini` file:

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

- **server_addr**: Server IP address, please modify it accordingly.
- **server_port**: Keep the same value as the `bind_port` on the server side, the default is `7000`.
- **token**: Connection token, keep it the same as the `token` configured on the server side.

Next, we configure custom rules:

- **[rdp]**: [xxx] represents the rule name, you can customize it.
- **type**: Protocol type for forwarding, TCP/UDP are optional.
- **local_port**: Local port number, here we fill in the port number for the RDP protocol (3389).
- **remote_port**: The port number opened on the server side, you can customize it.

> The default port number for RDP (Remote Desktop Protocol) on Windows is 3389, TCP protocol.
> The default port number for SMB (Windows File Sharing Protocol) is 445, TCP protocol.

To run frpc in the background, we create a script `frpc.vbs` and paste the following content into it:

```vbscript title="frpc.vbs"
set ws=WScript.CreateObject("WScript.Shell")
ws.Run "c:\frp\frpc.exe -c c:\frp\frpc.ini",0
```

Note that you may need to modify the path.

Put `frpc.vbs` into the `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp` directory to achieve automatic startup when the computer starts.

If you want to test it, you can run the script directly or restart for automatic execution.

## Configuration on the remote control side

### Control from a mobile device

If you want to remotely control a computer from a smartphone or iPad, you need to install the "Microsoft Remote Desktop" app first, and then follow these steps:

1. In the app, click the `+` button in the upper right corner - `Add PC`.
2. Enter the `Computer Name` as `IP:remote_port`, for example, `x.x.x.x:7001`, and click back.
3. Enter the account password of the controlled computer in the `User Account` field, and click back.

If everything is configured correctly, you should be able to successfully remote control the computer.

### Control from Windows

Simply search and open "Remote Desktop Connection" in the Start menu, enter `IP:remote_port`, for example, `x.x.x.x:7001`, and follow the prompts to enter the username and password to achieve remote control.

## References and Acknowledgements

- [Using frp for intranet penetration](https://sspai.com/post/52523)
- [Usage of the nohup command in Linux](https://ehlxr.me/2017/01/18/Linux-%E7%9A%84-nohup-%E5%91%BD%E4%BB%A4%E7%9A%84%E7%94%A8%E6%B3%95/)
- [Tutorial: Build remote desktop with frp](https://pa.ci/77.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.