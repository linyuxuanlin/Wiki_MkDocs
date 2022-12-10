---
id: Ubuntu配置笔记
title: Ubuntu 配置笔记
---

## 双系统时间问题

装完双系统，会出现时间问题（Windows 与 Ubuntu 时间不同步），使用下面命令可解决：

```shell
timedatectl set-local-rtc 1 --adjust-system-clock
```

## 安装软件

1. Chrome
2. VS Code
3. [**Qv2ray**](https://qv2ray.net/)
4. Git
   - `sudo apt install git`
   - `git config --global user.name "John Doe"`
   - `git config --global user.email johndoe@example.com`


## 技巧

### 查看隐藏文件

使用快捷键：`Ctrl` + `H`

### 打开终端

使用快捷键：`Ctrl` + `Alt` + `T`

### 命令

注： `<xx>` 表示必须， `(xx)` 表示可选

- cd
  - 切换工作目录
  - `cd <目录路径>`
- pwd
  - 查看当前绝对路径
  - `pwd`
- mkdir
  - 创建目录
  - `mkdir （选项） <目录名称>`
- ls
  - 列出目录下的内容
  - `ls （选项） （目录名称）`
- touch
  - 改变文件 / 目录时间
  - `touch （选项） <文件名称>`
- mv
  - 剪切
  - `mv （选项） （源文件/目录） <目的地文件/目录>`
- cp
  - 复制
  - `cp （选项） （源文件名/目录名） <目的地文件名/目录名>`
- rm
  - 删除
  - `rm （选项） <文件名/目录名>`



## 参考与致谢

- [ROS 安装教程](https://mp.weixin.qq.com/s?__biz=MzU4Mzc1NDA5Mw==&mid=2247486645&idx=1&sn=8ba442af57060b4d608d4c24d4307921&chksm=fda504b7cad28da11a2dd782b60dce466d53ad8e260f161b1e47f24423cc1e9f9aabc486c7f3&mpshare=1&scene=1&srcid=1125YhpxcX5as5se6rsek2IS&sharer_sharetime=1606233866320&sharer_shareid=57baeb2b96d0cff9b17ac2c15b36602b&key=a402d93e91746f46ae3228f3f1014e2c74a235c331168642475573a82dabce23902b3593a2a240439e9e37cd9b2ceaeab2b3b2130d952ee61260b30c6cad24ab3f1907dd57abfae9934d0c9487ddc4364b41261c6fb7277d94de784fa9718f9f60712a15b25f505ab7105346330f16f4b659970a5143e8aa882da96dc76c0100&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=A0ZOktA1B68GOdT4vmLQPxA%3D&pass_ticket=b2tffRx7FG4vxDxfZxW7b9rGQf%2FK8YGbZtslM9VWUgnItoiwUPJYOD8ciwJbwx%2BC&wx_header=0)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

