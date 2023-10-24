# Using VS Code for Remote Development

— Using VS Code as an SSH tool to connect to a remote server for development.

## Background

After trying various SSH tools, I eventually returned to the visually appealing and powerful VS Code. This article serves as a record for future reference, and some content is not elaborated on in detail. For more tutorials, please refer to the links at the end of this article.

VS Code Basics: [**VS Code Productivity Guide - Environment Configuration**](https://wiki-power.com/VSCodeProductivityGuide-EnvironmentConfiguration)

## Extension Configuration

Click to install the extension: [**Remote - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

Click the `Remote` button in the lower-left corner to use it.

## Other Configurations

### VS Code Cannot Monitor File Changes in a Large Workspace

Run this command to check the current limit:

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

### Unable to Use a Custom Username for Login

In the VS Code settings, find `Remote.SSH: Config File`, and enter the override value as `C:\Users\your_username\.ssh\config`, and create the corresponding configuration file locally.

### Connection Failed, But Can Connect Using Other SSH Clients

This issue may be due to the remote server's sshd version being lower than 7.6.0, causing the absence of the feature to display remote ports. To resolve this issue, you need to upgrade the sshd version:

- For Debian or Ubuntu: `sudo apt-get update && sudo apt-get install openssh-server`
- For Red Hat or CentOS: `sudo yum update openssh-server`

## References and Acknowledgments

- [VSCode Remote Experience | Developing in a Remote Linux Environment](https://zhuanlan.zhihu.com/p/64849549)
- [Handling VSCode Alerts: Visual Studio Code Cannot Monitor Changes in This Large Workspace](http://www.deadnine.com/somehow/2019/0208/1481.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.