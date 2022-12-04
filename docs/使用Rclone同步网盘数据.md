---
id: 使用Rclone同步网盘数据
title: 使用 Rclone 同步网盘数据
---

Rclone 是一个用于管理网盘文件的命令行工具，支持 40 余种网盘（包括 S3 类）。Rclone 也有衍生的图形化界面的软件 RcloneBrowser，方便一般用户使用。本文介绍如何通过 Rclone 同步腾讯云对象储存。

## 软件安装

- [**Rclone**](https://rclone.org/downloads/)：下载后将 `.exe` 解压，记下路径。
- [**RcloneBrowser**](https://github.com/kapitainsky/RcloneBrowser/releases)：GUI 工具。安装后选择 Rclone 的路径。
- （[**WinFsp**](http://www.secfs.net/winfsp/rel/)：依赖库，如果挂载虚拟硬盘就需要安装）

## 配置流程

打开 Rclone Browser，点击左下角的 `Config...`，接下来根据提示输入：

输入 `n` 以新建远程连接：

```shell
Name                 Type
====                 ====
rclone config        s3
e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config

e/n/d/r/c/s/q> n
```

给远程连接取个名字（例如 `test`）：

```shell
name> test
```

选择服务商（以下我以腾讯云 COS 为例，选择 `4`）：

```shell
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, and Tencent COS
   \ "s3"
...

Storage> 4
```

```shell
Choose a number from below, or type in your own value
 1 / Amazon Web Services (AWS) S3
   \ "AWS"
 2 / Alibaba Cloud Object Storage System (OSS) formerly Aliyun
   \ "Alibaba"
 3 / Ceph Object Storage
   \ "Ceph"
 4 / Digital Ocean Spaces
   \ "DigitalOcean"
 5 / Dreamhost DreamObjects
   \ "Dreamhost"
 6 / IBM COS S3
   \ "IBMCOS"
 7 / Minio Object Storage
   \ "Minio"
 8 / Netease Object Storage (NOS)
   \ "Netease"
 9 / Scaleway Object Storage
   \ "Scaleway"
10 / StackPath Object Storage
   \ "StackPath"
11 / Tencent Cloud Object Storage (COS)
   \ "TencentCOS"
12 / Wasabi Object Storage
   \ "Wasabi"
13 / Any other S3 compatible provider
   \ "Other"

provider> 11
```

选择认证类型。因为我们是第一次配置，所以选择 `1`：

```shell
Choose a number from below, or type in your own value
 1 / Enter AWS credentials in the next step
   \ "false"
 2 / Get AWS credentials from the environment (env vars or IAM)
   \ "true"

env_auth> 1
```

输入云服务的账号，这里相当于腾讯云 COS 的 SecretId：

```shell
AWS Access Key ID.

access_key_id> ******
```

输入密码，相当于 SecretKey：

```shell
AWS Secret Access Key (password)

secret_access_key> ******
```

选择云服务的地区：

```shell
Endpoint for Tencent COS API.
 1 / Beijing Region.
   \ "cos.ap-beijing.myqcloud.com"
 2 / Nanjing Region.
   \ "cos.ap-nanjing.myqcloud.com"
 3 / Shanghai Region.
   \ "cos.ap-shanghai.myqcloud.com"
 4 / Guangzhou Region.
   \ "cos.ap-guangzhou.myqcloud.com"
...

endpoint> 4
```

选择读写类型，图床一般是公读私写：

```shell
Canned ACL used when creating buckets and storing or copying objects.
 1 / Owner gets Full_CONTROL. No one else has access rights (default).
   \ "default"
 2 / Owner gets FULL_CONTROL. The AllUsers group gets READ access.
   \ "public-read"
   / Owner gets FULL_CONTROL. The AllUsers group gets READ and WRITE access.
...

acl> 2
```

选择储存类型（选择 `1` 默认即可）：

```shell
The storage class to use when storing new objects in Tencent COS.
 1 / Default
   \ ""
 2 / Standard storage class
   \ "STANDARD"
 3 / Archive storage mode.
   \ "ARCHIVE"
 4 / Infrequent access storage mode.
   \ "STANDARD_IA"

storage_class> 1
```

是否编辑高级设置（选择 `n` 否）：

```shell
Edit advanced config? (y/n)
y) Yes
n) No (default)

y/n> n
```

最后确认，检查无误后输入 `y`：

```shell
Remote config
--------------------
[Txcos]
type = s3
provider = TencentCOS
env_auth = false
access_key_id = 我是马赛克
secret_access_key = 我是马赛克
endpoint = cos.ap-guangzhou.myqcloud.com
acl = public-read
--------------------
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y
```

输入 `q` 退出：

```shell
Current remotes:

Name                 Type
====                 ====
Txcos                 s3

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q
```

接下来，双击打开配置好的远程连接，选择文件夹并点击 `Download` 下载到本地，在弹出的窗口选择以下配置：

- Mode 选择 `Copy` 模式（单向从云端到本地同步），只拷贝新增和变化的文件，备份的时候使用。
- 在 Skip files 区域勾选 `Skip all files that exist`，避免重复下载消耗流量。
- 在 Task description 区域输入任务名称，方便下次同步使用。

配置完成后，切换到 Tasks 标签页，选择相应的任务，点击 `Run` 即可开始下载。


## 在群晖 NAS 上配置

注：在群晖上建议使用 CloudSync，不要对底层代码进行修改。

准备工作：

- 开启 ssh
- 启用用户家目录（`homes`）
- 创建用于同步的文件夹（比如我是 `/volume1/wiki-media`）

安装 Rclone:

```shell
curl https://rclone.org/install.sh | sudo bash
```

配置服务：

```shell
rclone config
```

按照上面的步骤就行。

同步的命令：

```shell
# 本地到网盘
rclone [功能选项] <本地路径> <网盘名称:路径> [参数] [参数] ...

# 网盘到本地
rclone [功能选项] <网盘名称:路径> <本地路径> [参数] [参数] ...

# 网盘到网盘
rclone [功能选项] <网盘名称:路径> <网盘名称:路径> [参数] [参数] ...
```

例如我是：

```shell
rclone sync COS_backup:/wiki-media-1253965369 /volume1/wiki-media -P
```

在选定的路径新建一个自动化脚本（如 `rclone-sync.sh`），将上面的命令放进脚本文件内。

在群晖 `控制面板` - `任务计划` - `新增` - `计划的任务` - `用户定义的脚本`，在 `计划` 和 `任务设置` 标签页配置周期运行时间，和脚本的路径

1. `控制面板` - `任务计划` - `新增` - `计划的任务` - `用户定义的脚本`，在 `计划` 和 `任务设置` 标签页配置周期运行时间，和运行脚本的命令（比如 `bash /volume1/stash/permanent/rclone-sync.sh`）
2. 可在 `设置` 内配置输出结果，后选择任务，点击 `运行`，可测试运行，可打开配置的输出路径看运行结果

## 参考与致谢

- [Rclone 安装配置使用教程，附 Rclone 常用命令参数详解](https://www.wazhuji.com/jiaocheng/17.html)
- [基于 [对象存储] 的低成本全功能私有云搭建](https://zhuanlan.zhihu.com/p/104628740)
- [使用 Rclone 和 WinFsp 将阿里云 oss / 腾讯云 cos 挂载为 windows 磁盘](https://www.boxmoe.com/486.html)
- [使用 rclone 在 Windows 下挂载 Google 个人 / 团队云盘](https://blog.rhilip.info/archives/874/)
- [使用 rclone 每天定时备份 typecho 博客网站内容及 mysql 数据库到 Google Drive/Onedrive 等网盘](https://omo.moe/archives/616/)'

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

