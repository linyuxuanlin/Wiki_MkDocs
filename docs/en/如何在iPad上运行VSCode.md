# How to Run VS Code on iPad

Note: This tutorial is based on code-server v3.8.0, CentOS 8.2.

![](https://media.wiki-power.com/img/20201221140748.jpg)

It is highly recommended to install the code-server service using Docker Compose.  
With just one command, you can deploy it without the need for background configuration and it comes with built-in Git and other environments.  
For more details, please refer to: [**Homelab - Online Code Editor code-server**](https://wiki-power.com/Homelab-%E5%9C%A8%E7%BA%BF%E4%BB%A3%E7%A0%81%E7%BC%96%E8%BE%91%E5%99%A8code-server)

If you do not want to deploy it using Docker Compose, please continue reading.

## Configure the Server

First, you need a server that runs 24/7 (it is recommended to buy an Alibaba Cloud / Tencent Cloud student server, which costs only ¥9.9/month).  
To ensure a good user experience, it is recommended to have the following server configuration:

- 2 cores or more
- 1GB of RAM or more

Install Linux (here I use CentOS 8.2) and make sure that SSH can be connected to it.

## Install code-server

In the latest version (≥v3.8.0), you can directly use the script to install it:

```shell
curl -fsSL https://code-server.dev/install.sh | sh
```

If you find that it takes a long time to download, it is probably due to DNS pollution. Refer to [**GitHub Host Modification**](https://wiki-power.com/GitHub%E6%94%B9Host) for a solution.

## Run code-server

Use the following command:

```shell
export PASSWORD="Set an access password" && code-server --port 80 --host 0.0.0.0 --auth password
```

If no errors occur, open a browser and enter the IP address of the server to access an online VS Code.

## Configure Background Running

The code-server running in the foreground will end the process when SSH exits.  
To run it in the background, we can use the screen program (which can be understood as a container).

### Install screen

```shell
yum install screen
```

### Create a screen job

```shell
screen -S VSCode-online # VSCode-online is a name of your choice
```

### Start the code-server service

```shell
export PASSWORD="Set an access password" && code-server --port 80 --host 0.0.0.0 --auth password
```

If everything goes smoothly, you can access it by entering the IP address in the browser.

## Extensions

### Add Desktop Shortcut

If you are using an iPad, you can open it in the Safari browser, click on the `Share` icon in the upper right corner, and then select `Add to Home Screen`.  
You can use it as if it were an app and hide the browser status bar.  
By the way, external keyboards and mice are also supported.

### Other Operations with screen

- View the running job ID: `screen -ls`
- Re-enter a running screen job: `screen -r job_id # The job ID needs to include the prefix number identifier`
- Terminate the execution of a specific job: `screen -X -S job_id quit`
- Exit the screen interface of the current job: `Ctrl + A + D`

### code-server Related Command Parameters

- Accessing via the Internet: By default, the code-server service only runs locally (`127.0.0.1`). To access it via IP, you can add the `--host 0.0.0.0` parameter.
- Specifying the running port: `--port xxxx`, you can replace `xxxx` with `8888`; or it can be `80` (using the HTTP protocol, directly access via IP without adding a port number).
- Setting an access password: Add `--auth password`; if not needed, do not add any parameters or add `--auth none`.

### Installing Git

Using VS Code with Git makes cloud development easier. You can install Git using the following command:

```shell
yum install git
```

### Accessing via a Domain Name

Accessing through the server IP may seem strange, so we can bind a custom domain name to access the code-server service.
Purchase a domain name and add the server IP in the DNS resolution using the A record type.

### Current Version Bugs and Solutions

- Unable to synchronize user settings through the built-in Settings Sync service in VS Code: You can solve this by installing the [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) plugin.
- Settings Sync encounters errors when redirecting to GitHub login: Configure it using a computer browser.
- Unable to scroll the page properly using a mouse wheel on an iPad: Currently, you can only use direct touch scrolling or use the keyboard arrow keys as alternatives.

## References and Acknowledgments

- [Running VSCode in a Browser (Old)](https://wiki-power.com/在浏览器上运行VSCode（旧）)
- [GitHub Host Modification](https://wiki-power.com/GitHub改Host)
- [Installation and Usage of Screen](https://www.jianshu.com/p/420569381e74)
- [Setup Guide · cdr/code-server](https://github.com/cdr/code-server/blob/v3.8.0/doc/guide.md)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
