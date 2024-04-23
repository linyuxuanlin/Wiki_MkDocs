# Using VS Code for Remote Development

- Utilize VS Code as an SSH tool to connect to remote servers for development.

## Background

After trying out various SSH tools, I eventually circled back to the aesthetically pleasing and powerful interface of VS Code. This article serves as a documentation for future reference, with some content left briefly explained. For more tutorials, please refer to the links at the end of the article.

Foundational VS Code Configuration: [**VS Code Productivity Guide - Environment Setup**](https://wiki-power.com/VSCode生产力指南-环境配置)

## Configuring Extensions

Click to install the extension: [**Remote - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

Click on the `Remote` button at the bottom left to start using it.

## Additional Configurations

### VS Code Unable to Monitor File Changes in Large Workspaces

Run this command to check the current limit:

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

Edit the `/etc/sysctl.conf` file:

```shell
sudo vim /etc/sysctl.conf
```

Add the following code to increase the limit to the maximum value:

```shell
fs.inotify.max_user_watches=524288
```

Save and enable the settings:

```shell
sudo sysctl -p
```

### Unable to Log in Using a Custom Username

In the VS Code settings, locate `Remote.SSH: Config File`, fill in the override value as `C:\Users\your_username\.ssh\config`, and create the corresponding configuration file locally.

### Connection Failure, While Other SSH Clients Can Connect

It may be due to the remote server having an sshd version lower than 7.6.0, missing the feature to display the remote port which leads to this issue. Resolving this problem requires upgrading the sshd version:

- For Debian or Ubuntu: `sudo apt-get update && sudo apt-get install openssh-server`
- For Red Hat or CentOS: `sudo yum update openssh-server`

It could also be an issue with proxy settings; try switching or disabling proxies.

## References and Acknowledgments

- [VSCode Remote Experience | Remote Linux Environment Development is Awesome](https://zhuanlan.zhihu.com/p/64849549)
- [Handling VSCode Alerts: VisualStudioCode Cannot Watch Changes in this Large Workspace](http://www.deadnine.com/somehow/2019/0208/1481.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.