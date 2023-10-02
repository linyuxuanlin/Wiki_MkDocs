# Syncing Cloud Storage Data with Rclone

Rclone is a command-line tool for managing cloud storage files, supporting over 40 cloud storage providers (including S3). Rclone also has a graphical user interface software called RcloneBrowser, which is convenient for general users. This article introduces how to sync Tencent Cloud Object Storage using Rclone.

## Software Installation

- [**Rclone**](https://rclone.org/downloads/): After downloading, extract the `.exe` file and remember the path.
- [**RcloneBrowser**](https://github.com/kapitainsky/RcloneBrowser/releases): GUI tool. After installation, select the path of Rclone.
- ([**WinFsp**](http://www.secfs.net/winfsp/rel/): Dependency library, required if mounting virtual hard disks)

## Configuration Process

Open RcloneBrowser and click `Config...` in the lower left corner, then follow the prompts to enter:

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

Give the remote connection a name (e.g. `test`):

```shell
name> test
```

Select the service provider (I will use Tencent Cloud Object Storage as an example and select `4`):

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

English:

provider> 11
```

Choose authentication type. Since this is our first configuration, select `1`:

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

Enter the password, which is equivalent to SecretKey:

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

Select the read-write type. Generally, the image bed is public read and private write:

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

Whether to edit advanced settings (select `n` for no):

```shell
Edit advanced config? (y/n)
y) Yes
n) No (default)

y/n> n
```

Finally, confirm and enter `y` after checking for errors:

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

Next, double-click on the configured remote connection, select the folder and click `Download` to download to your local machine. In the pop-up window, select the following configurations:

- Select `Copy` mode for Mode (one-way sync from cloud to local), only copying new and changed files, for backup purposes.
- Check `Skip all files that exist` in the Skip files area to avoid redundant downloads and save bandwidth.
- Enter a task name in the Task description area for future reference.

After configuring, switch to the Tasks tab, select the corresponding task, and click `Run` to start the download.

## Configuring on Synology NAS

Note: It is recommended to use CloudSync on Synology instead of modifying the underlying code.

Preparation:

- Enable SSH
- Enable user home directories (`homes`)
- Create a folder for synchronization (e.g. `/volume1/wiki-media`)

Install Rclone:

```shell
curl https://rclone.org/install.sh | sudo bash
```

Configure the service:

```shell
rclone config
```

Follow the steps above.

Sync command:

```shell
# Local to cloud
rclone [function options] <local path> <cloud name:path> [parameters] [parameters] ...

# Cloud to local
rclone [function options] <cloud name:path> <local path> [parameters] [parameters] ...

# Cloud to cloud
rclone [function options] <cloud name:path> <cloud name:path> [parameters] [parameters] ...
```

For example:

```shell
rclone sync COS_backup:/wiki-media-1253965369 /volume1/wiki-media -P
```

Create an automation script (e.g. `rclone-sync.sh`) in the selected path and put the above command in the script.

In Synology `Control Panel` - `Task Scheduler` - `Create` - `Scheduled Task` - `User-defined script`, configure the periodic run time and the script path in the `Schedule` and `Task Settings` tabs.

1. In Synology `Control Panel` - `Task Scheduler` - `Create` - `Scheduled Task` - `User-defined script`, configure the periodic run time and the command to run the script (e.g. `bash /volume1/stash/permanent/rclone-sync.sh`) in the `Schedule` and `Task Settings` tabs.
2. In `Settings`, configure the output path, select the task, and click `Run` to test the run and view the results in the configured output path.

## References and Acknowledgments

- [Rclone Installation, Configuration, and Usage Tutorial, with Detailed Explanation of Common Rclone Commands](https://www.wazhuji.com/jiaocheng/17.html)
- [Low-Cost Full-Featured Private Cloud Setup Based on Object Storage](https://zhuanlan.zhihu.com/p/104628740)
- [Mounting Aliyun OSS/Tencent Cloud COS as Windows Drives Using Rclone and WinFsp](https://www.boxmoe.com/486.html)
- [Mounting Google Personal/Team Drive as Windows Drive Using Rclone on Windows](https://blog.rhilip.info/archives/874/)
- [Using Rclone to Backup Typecho Blog Website Content and MySQL Database to Google Drive/OneDrive and Other Cloud Storage Services on a Daily Basis](https://omo.moe/archives/616/)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.