# Remote Development with VS Code

- Use VS Code as an SSH tool to connect to remote servers for development.

## Background

After trying various SSH tools, I finally returned to the good-looking and powerful VS Code interface. 
This article only records for future reference, and some content is not explained in detail. For more tutorials, please refer to the link at the end of the article.

VS Code Basic Configuration: [**VS Code Productivity Guide - Environment Configuration**](https://wiki-power.com/en/VSCode生产力指南-环境配置)

## Extension Configuration

Click to install the extension: [**Remote - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

Click the `Remote` button in the lower left corner to use it.

## Other Configuration

### VS Code cannot monitor file changes in large workspaces

Run this command to view the current limit:

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

Edit the `/etc/sysctl.conf` file:

```shell
sudo vim /etc/sysctl.conf
```

Add the following code to increase this limit to the maximum value:

```shell
fs.inotify.max_user_watches=524288
```

Save and enable the settings:

```shell
sudo sysctl -p
```

### Cannot log in with a custom username

In VS Code settings, find `Remote.SSH: Config File`, fill in the override value as `C:\Users\your_username\.ssh\config`, and create the corresponding configuration file locally.

### Connection failed, but can be connected using other SSH clients

It may be because the version of sshd on the remote server is lower than 7.6.0, which causes the feature of displaying the remote port to be missing. To solve this problem, you need to upgrade the version of sshd:

- For Debian or Ubuntu: `sudo apt-get update && sudo apt-get install openssh-server`
- For Red Hat or CentOS: `sudo yum update openssh-server`

## Reference and Acknowledgement

- [VSCode Remote Experience | Remote Linux Environment Development is Awesome](https://zhuanlan.zhihu.com/p/64849549)
- [VSCode Alarm Handling: VisualStudioCode cannot monitor file changes in this large workspace](http://www.deadnine.com/somehow/2019/0208/1481.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.