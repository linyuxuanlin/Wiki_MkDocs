# Syncing Cloud Storage Data with Rclone

Rclone is a command-line tool for managing cloud storage files, supporting over 40 different cloud storage providers (including S3). Rclone also has a graphical user interface software called RcloneBrowser, which makes it easier for general users to use. This article explains how to sync Tencent Cloud Object Storage using Rclone.

## Software Installation

- [**Rclone**](https://rclone.org/downloads/): Download and extract the `.exe` file, and take note of the installation path.
- [**RcloneBrowser**](https://github.com/kapitainsky/RcloneBrowser/releases): GUI tool. After installation, select the path of Rclone.
- (Optional) [**WinFsp**](http://www.secfs.net/winfsp/rel/): Dependency library, required for mounting virtual hard drives.

## Configuration Process

Open RcloneBrowser and click on `Config...` at the bottom left corner. Then, follow the prompts to input the following:

Enter `n` to create a new remote connection:

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

Give the remote connection a name (e.g., `test`):

```shell
name> test
```

Choose the cloud storage provider (in this example, I will use Tencent Cloud Object Storage, so select `4`):

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
```

provider> 11
```

Choose the authentication type. Since this is our first configuration, select `1`:

```shell
Choose a number from below, or type in your own value
 1 / Enter AWS credentials in the next step
   \ "false"
 2 / Get AWS credentials from the environment (env vars or IAM)
   \ "true"

env_auth> 1
```

Enter the account for the cloud service, which is equivalent to the SecretId of Tencent Cloud COS:

```shell
AWS Access Key ID.

access_key_id> ******
```

Enter the password, which is equivalent to the SecretKey:

```shell
AWS Secret Access Key (password)

secret_access_key> ******
```

Select the region of the cloud service:

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

Select the read and write type. Generally, the image bed is publicly readable and privately writable:

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

Select the storage type (select `1` by default):

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

Do you want to edit advanced settings? (select `n` for no):

```shell
Edit advanced config? (y/n)
y) Yes
n) No (default)

y/n> n
```

Finally, confirm and enter `y` after checking for accuracy:

```shell
Remote config

[Txcos]
type = s3
provider = TencentCOS
env_auth = false
access_key_id = 我是马赛克
secret_access_key = 我是马赛克
endpoint = cos.ap-guangzhou.myqcloud.com
acl = public-read

y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y
```

Enter `q` to exit:

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

Next, double-click to open the configured remote connection, select a folder, and click `Download` to download it to your local machine. In the pop-up window, select the following configurations:

- Select `Copy` mode (one-way synchronization from cloud to local) in the Mode section, which only copies new and changed files for backup purposes.
- Check the box for `Skip all files that exist` in the Skip files section to avoid redundant downloads and save bandwidth.
- Enter a task name in the Task description section for easy reference in future synchronizations.

After the configuration is complete, switch to the Tasks tab, select the corresponding task, and click `Run` to start the download.

## Configuration on Synology NAS

Note: It is recommended to use CloudSync on Synology NAS and avoid modifying the underlying code.

Preparation:

- Enable SSH
- Enable user home directories (`homes`)
- Create a folder for synchronization (e.g., `/volume1/wiki-media`)

Install Rclone:

```shell
curl https://rclone.org/install.sh | sudo bash
```

Configure the service:

```shell
rclone config
```

Follow the steps mentioned above.

Synchronization commands:

```shell
# Local to cloud
rclone [options] <local path> <remote:path> [flags] [flags] ...

# Cloud to local
rclone [options] <remote:path> <local path> [flags] [flags] ...

# Cloud to cloud
rclone [options] <remote:path> <remote:path> [flags] [flags] ...
```

For example, in my case:

```shell
rclone sync COS_backup:/wiki-media-1253965369 /volume1/wiki-media -P
```

Create an automation script (e.g., `rclone-sync.sh`) in the selected path and place the above command in the script file.

In Synology, go to `Control Panel` - `Task Scheduler` - `Create` - `Scheduled Task` - `User-defined script`, and configure the run time and script path in the `Schedule` and `Task Settings` tabs.

1. Go to `Control Panel` - `Task Scheduler` - `Create` - `Scheduled Task` - `User-defined script`, and configure the run time and the command to run the script (e.g., `bash /volume1/stash/permanent/rclone-sync.sh`).
2. In the `Settings` section, configure the output path, select the task, and click `Run` to test the execution and view the results in the configured output path.

## References and Acknowledgements

- [Rclone installation, configuration and usage tutorial, with detailed explanation of common Rclone command parameters](https://www.wazhuji.com/jiaocheng/17.html)
- [Building a low-cost, fully-featured private cloud based on [object storage]](https://zhuanlan.zhihu.com/p/104628740)
- [Mounting Alibaba Cloud OSS / Tencent Cloud COS as Windows disks using Rclone and WinFsp](https://www.boxmoe.com/486.html)
- [Mounting Google personal / team cloud drives on Windows using Rclone](https://blog.rhilip.info/archives/874/)
- [Using Rclone to schedule daily backups of Typecho blog website content and MySQL database to Google Drive/OneDrive and other cloud storage](https://omo.moe/archives/616/)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.