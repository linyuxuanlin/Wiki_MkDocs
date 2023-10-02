# How to Run VS Code on iPad

Note: This tutorial is based on code-server v3.8.0 and CentOS 8.2.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20201221140748.jpg)

It is recommended to install code-server service using Docker compose.  
With just one command, you can deploy it without configuring background running and it comes with Git and other environments.  
See: [**Homelab - Online Code Editor code-server**](https://wiki-power.com/Homelab-%E5%9C%A8%E7%BA%BF%E4%BB%A3%E7%A0%81%E7%BC%96%E8%BE%91%E5%99%A8code-server)

If you don't want to deploy it using Docker compose, please continue reading.

## Configure the Server

First, you need a server that runs 24/7 (it is recommended to buy an Alibaba Cloud/Tencent Cloud student server for only ¥9.9/month)  
To ensure a good user experience, it is recommended that the server has the following configuration:

- 2 cores or more
- 1GB or more memory

Install Linux (here I use CentOS 8.2) and make sure ssh can be connected normally.

## Install code-server

In the new version (≥v3.8.0), you can directly use the script to install:

```shell
curl -fsSL https://code-server.dev/install.sh | sh
```

If you find that it cannot be downloaded for a long time, it is probably due to DNS pollution. Refer to [**GitHub Change Host**](https://wiki-power.com/GitHub改Host) to solve it.

## Run code-server

Use the command:

```shell
export PASSWORD="set an access password" && code-server --port 80 --host 0.0.0.0 --auth password
```

If there is no error, then open the browser, enter the server's IP address to access, and you can see an online VS Code.

## Configure Background Running

The code-server running in the foreground will end the process because ssh exits.  
To make it run in the background, we can use the screen program (you can think of it as a container).

### Install screen

```shell
yum install screen
```

### Create a screen job

```shell
screen -S VSCode-online # VSCode-online is a self-selected name
```

### Start the code-server service

```shell
export PASSWORD="set an access password" && code-server --port 80 --host 0.0.0.0 --auth password
```

If everything goes well, you can access it by entering the IP address in the browser.

## Extensions

### Add Desktop Shortcut

If you are using an iPad, you can open it with the Safari browser, click the `Share` icon in the upper right corner --> `Add to Home Screen`.  
You can pretend to use it as an app and hide the browser status bar.  
By the way, external keyboard and mouse are also supported.

### Other Operations of screen

- View the running job id: `screen -ls`
- Re-enter the running screen job: `screen -r job id # the job id needs to include the prefix digital identifier`
- End the running of a certain job: `screen -X -S job id quit`
- Exit the screen interface of the current job: `Ctrl + A + D`

### code-server Related Command Parameters

- Accessing through external network: By default, the code-server service only runs locally (`127.0.0.1`). To access it through an IP address, you can add the `--host 0.0.0.0` parameter.
- Specifying the running port: `--port xxxx`, where you can replace `xxxx` with `8888` or `80` (using HTTP protocol, directly accessing through IP address without adding a port number).
- Setting access password: Add `--auth password`. If not needed, do not add any parameters or add `--auth none`.

### Installing Git

VS Code can be used with Git to facilitate cloud development.  
You can use the following command to install Git:

```shell
yum install git
```

### Accessing through a domain name

Accessing through the server IP address may seem strange, so we can bind a custom domain name to access the code-server service through the domain name.  
Purchase a domain name and add the server IP address in DNS resolution using the A type.

### Current version bugs and solutions

- Unable to synchronize user settings through the built-in Settings Sync service in VS Code: You can solve this by installing the [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) plugin.
- Settings Sync jumps to GitHub login error: Configure it using a computer browser.
- Unable to scroll the page normally with a mouse wheel on iPad: Currently, you can only use direct touch scrolling or use keyboard arrow keys as a substitute.

## References and Acknowledgments

- [Running VSCode in the browser (old)](https://wiki-power.com/在浏览器上运行VSCode（旧）)
- [GitHub Host Modification](https://wiki-power.com/GitHub改Host)
- [Installation and Usage of screen](https://www.jianshu.com/p/420569381e74)
- [Setup Guide · cdr/code-server](https://github.com/cdr/code-server/blob/v3.8.0/doc/guide.md)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.