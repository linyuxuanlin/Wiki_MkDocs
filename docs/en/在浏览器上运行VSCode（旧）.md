# Running VS Code on a Browser (Old Method)

Note: For deployments of code-server version ≥v3.8.0, please refer to [**How to Run VS Code on iPad**](https://wiki-power.com/如何在iPad上运行VSCode) for a more streamlined approach.

## Background

It's well-known that VS Code is an incredibly powerful code editor. If we could use VS Code on lightweight platforms like the iPad (given that iPadOS's support for keyboards and mice can rival desktop systems), we could work from anywhere at any time.

Fortunately, there's a service that allows you to run VS Code on a server: code-server. Once deployed, you can access it through a web browser. This means that as long as you have an internet connection, you can easily access VS Code from any device.

## Preparing the Environment

You'll need a server with Linux installed (I used the lowest-tier student instance on Alibaba Cloud).

The official system requirements are as follows:

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

Do not blindly copy this command. Go to the [**Release**](https://github.com/cdr/code-server/releases) page of code-server and copy the link for the latest version (select the one that matches your server's architecture; I used the `code-server-3.1.0-linux-x86_64.tar.gz` version). Download or transfer it to your server using `wget` or `SFTP`.

If the download speed is slow, you can copy the download link and use [**GitHub File Accelerator**](https://gh.api.99988866.xyz/) to obtain an accelerated download link for use in China.

```shell
tar -xvf code-server-3.1.0-linux-x86_64.tar.gz # Extract
```

### 2. Installation

```shell
cd code-server
export PASSWORD="yourpassword"
./code-server --port 8888 --host 0.0.0.0
```

- Change `yourpassword` to your desired password; otherwise, a random password will be generated.
- `--port 8888` specifies the running port. You can set it to `80` (HTTP protocol) so you don't need to add the port number when accessing it.
- `--host 0.0.0.0` allows the service to be accessed from the external network. The default `127.0.0.1` restricts it to local access.
- If you don't need password authentication, you can add `--auth none`.
- If the service doesn't start successfully, it may be due to choosing the wrong **processor architecture version**. Try a different version.

### 3. Configuring Background Operation

By default, when running it directly, the SSH connection will be lost if it disconnects. To make it run in the background, you can use `screen`:

```shell
yum install screen
or
apt-get install screen
```

```shell
screen -S VSCode-online # Choose your own name for VS Code-online
export PASSWORD="password" && ./code-server --port 8888 --host 0.0.0.0
```

To re-enter the running screen job:

```shell
screen -r JobName
```

If you need to stop the background screen process:

```shell
screen -ls # View the IDs of running services
screen -X -S id quit # Replace 'id' with the actual ID
```

To detach from a screen session: `Ctrl + A + D`

### 4. Easy Access

Simply enter `http://your_server_ip` in your web browser to enjoy cloud-based VS Code.

![VS Code in the Browser](https://media.wiki-power.com/img/20200413181001.jpg)

Configuring domain access: _To be explored..._

## Current Issues

- The number of directly downloadable plugins is limited. Manually installing plugins is cumbersome and lacks automatic synchronization of plugins/user settings. This is expected to be addressed in future versions.

## References and Acknowledgments

- [Running VS Code in the Browser - code-server on Alibaba Cloud](https://copyfuture.com/blogs-details/20200405045150018h4edt0f4q8486jq)
- [Running VS Code in the Browser - code-server](https://segmentfault.com/a/1190000022267386)
- [(Recommended) Installation and Usage of VS Code Online Tool - code-server on a Cloud Server with Common Problem Solving (Detailed Guide)](https://blog.csdn.net/Granery/article/details/90415636)
- [Setting up the Web Version of VS Code for iPad Programming Environment](https://blog.icodef.com/2019/11/17/1670)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
