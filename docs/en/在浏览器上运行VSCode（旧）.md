# Running VS Code on a Browser (Old Version)

Note: For deploying code-server version ≥v3.8.0, please refer to [**How to Run VS Code on iPad**](https://wiki-power.com/如何在iPad上运行VSCode) for a simpler method.

## Background

As we all know, VS Code is a powerful editor. If we can use VS Code on lightweight platforms like iPad (where iPadOS's support for keyboard and mouse is comparable to desktop systems), we can work anytime and anywhere.

Fortunately, there is a service that allows us to run VS Code on a server: code-server. After deployment, it can be accessed through a browser. This way, as long as there is a network, any device can easily use VS Code.

## Preparation

A server with Linux installed (I used the lowest configuration student machine from Alibaba Cloud).

The official requirements are as follows:

> - 64-bit host.
> - At least 1GB of RAM.
> - 2 cores or more are recommended (1 core works but not optimally).
> - Secure connection over HTTPS or localhost (required for service workers and clipboard support).
> - For Linux: GLIBC 2.17 or later and GLIBCXX 3.4.15 or later.

## Installation Process

### 1. Download

```shell
wget https://github.com/cdr/code-server/releases/download/3.1.0/code-server-3.1.0-linux-x86_64.tar.gz # Download code-server
```

Do not copy the command directly. Instead, copy the link to the latest version from the code-server [**Release**](https://github.com/cdr/code-server/releases) page (select according to the server architecture; I used version `code-server-3.1.0-linux-x86_64.tar.gz`) and download/transfer it to the server using `wget` or SFTP.

If the download speed is slow, you can copy the download link and use the [**GitHub File Acceleration**](https://gh.api.99988866.xyz/) website to obtain a domestically accelerated download link.

```shell
tar -xvf code-server-3.1.0-linux-x86_64.tar.gz # Unzip
```

### 2. Installation

```shell
cd code-server
export PASSWORD="yourpassword"
./code-server --port 8888 --host 0.0.0.0
```

- Change `yourpassword` to the password you set, otherwise a random password will be generated.
- `--port 8888` specifies the running port. You can set it to port `80` (HTTP protocol) so that you don't need to add a port number when accessing it.
- `--host 0.0.0.0` allows the service to be accessed through the Internet. The default `127.0.0.1` can only be accessed locally.
- If you don't need password verification, you can add `--auth none`.
- If the service fails to start, it may be due to selecting the wrong **processor architecture version**. Try another version.

### 3. Configure Background Running

By default, when running directly, the connection will be lost once the SSH connection is disconnected. To make it run in the background, you can use `screen`:

```shell
yum install screen
or
apt-get install screen
```

```shell
screen -S VSCode-online # VS Code-online is a self-selected name
export PASSWORD="password" && ./code-server --port 8888 --host 0.0.0.0
```

To re-enter the running screen job:

```shell
screen -r job name
```

If you need to stop the background screen from running:

```shell
screen -ls # View the ID of the running service
screen -X -S id quit # Replace id with the actual ID
```

Exit screen: `Ctrl + A + D`

### 4. Easy to use

Simply enter `http://your server IP` in your browser to enjoy cloud-based VS Code.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200413181001.jpg)

Configuring domain name access: `To be explored...`

## Current issues

- The number of directly downloadable plugins is limited, manual installation of plugins is cumbersome, and there is no automatic synchronization of plugins/user settings. This will be addressed in future versions.

## References and Acknowledgements

- [Running VS Code in the browser, code-server (Alibaba Cloud Server)](https://copyfuture.com/blogs-details/20200405045150018h4edt0f4q8486jq)
- [Running VS Code in the browser, code-server](https://segmentfault.com/a/1190000022267386)
- [(Recommended) VS Code Online Tool - Installation and Use of Code-Serve on Cloud Server and Common Problems (Super Detailed)](https://blog.csdn.net/Granery/article/details/90415636)
- [iPad Programming Learning Environment - VS Code Web Version Setup](https://blog.icodef.com/2019/11/17/1670)

> Article author: **Power Lin**
> Original address: <https://wiki-power.com>
> Copyright statement: This article is licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/) license. 
> Please indicate the source when reprinting.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.