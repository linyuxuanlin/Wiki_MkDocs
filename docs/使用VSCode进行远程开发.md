---
id: 使用VSCode进行远程开发
title: 使用 VS Code 进行远程开发
---

—— 将 VS Code 作为 SSH 工具，连接远程服务器进行开发。

## 背景

尝试了各类 SSH 工具，最终还是回到界面好看又强大的 VS Code.  
本篇文章仅记录以供日后参考用，部分内容未详细展开说明。更多教程请参考文末链接。

VS Code 基础配置篇：[**VS Code 生产力指南 - 环境配置**](https://wiki-power.com/VSCode生产力指南-环境配置)

## 配置扩展

点击安装扩展：[**Remote - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

点击左下角 `Remote` 按钮即可使用。

## 其他配置

### VS Code 无法监视大型工作区的文件变化

运行此命令查看当前限制：

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

编辑 `/etc/sysctl.conf` 文件：

```shell
sudo vim /etc/sysctl.conf
```

增加如下代码，将此限制增加到最大值：

```shell
fs.inotify.max_user_watches=524288
```

保存，启用设置：

```shell
sudo sysctl -p
```

## 参考与致谢

- [VSCode Remote 体验 | 远程 Linux 环境开发真香](https://zhuanlan.zhihu.com/p/64849549)
- [VSCode 报警处理：VisualStudioCode 无法监视这个大型工作区的文件变化](http://www.deadnine.com/somehow/2019/0208/1481.html)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

