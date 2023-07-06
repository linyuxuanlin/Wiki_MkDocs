---
id: Linux如何配置开机自动运行脚本
title: Linux 如何配置开机自动运行脚本
---

## 适用于使用 SysV init 的系统

注：以下方法适用于使用 SysV init 系统的 Linux 发行版（如 Ubuntu 18.04 及更新版本，或 Debian）。对于使用 Systemd 的发行版（如 Ubuntu 18.04 及更新版本），请使用 `systemctl` 方法来管理启动服务。

假如我们需要开机自动执行的脚本是 `xxx.sh`。首先在 `/etc/init.d` 目录下创建一个用于启动的脚本，例如名为 `autorun.sh`：

```shell
sudo nano /etc/init.d/autorun.sh
```

在其中添加你需要开机自动执行的脚本：

```bash title="autorun.sh"
#!/bin/bash
/path/to/xxx.sh  # 修改为具体路径
```

将 `autorun.sh` 脚本添加到系统的启动服务中:

```shell
sudo update-rc.d autorun.sh defaults
```

将 `autorun.sh` 脚本设置为开机启动:

```shell
sudo update-rc.d autorun.sh enable
```

这样，当重新启动后，`autorun.sh` 脚本将会自动运行。

## 适用于使用 Systemd 的系统

如果你的 Linux 发行版使用 Systemd 作为启动管理器（例如 Ubuntu 18.04 及更高版本），你可以使用 `systemctl` 命令来设置自动启动。

假如我们需要开机自动执行的脚本是 `xxx.sh`。首先创建一个描述你想自启动服务的 Unit 文件，比如 `autorun.service`：

```shell
sudo nano /etc/systemd/system/autorun.service
```

在 Unit 文件中，定义你的服务的配置。以下是一个示例：

```service title="autorun.service"
[Unit]
Description=My Service
After=network.target
[Service]
ExecStart=/path/to/xxx.sh
[Install]
WantedBy=default.target
```

其中的参数分别为：

- `Description`：描述你的服务。
- `After`：指定你的服务在哪些其他服务之后启动。例如，`network.target` 表示在网络服务启动后才启动你的服务。
- `ExecStart`：指定你要执行的脚本或命令的路径。
- `WantedBy`：指定你的服务应该被启动的目标（target）。`default.target` 表示在默认目标启动时启动你的服务。

保存并关闭文件，运行以下命令以重新加载 systemd 配置：

```shell
sudo systemctl daemon-reload
```

使用以下命令使能你的服务：

```shell
sudo systemctl enable autorun.service
```

最后，使用以下命令启动：

```shell
sudo systemctl start autorun.service
```

现在，你的服务已经设置为在系统启动时自动运行。你可以重新启动系统来验证服务是否正常启动。


---

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
