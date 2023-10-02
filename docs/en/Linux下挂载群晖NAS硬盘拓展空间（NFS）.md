# Mounting Synology NAS Hard Drive for Space Expansion (NFS) on Linux

If your server has limited storage space, you can try mounting the hard drive on your Synology NAS as an expanded storage space.

## Configuring on Synology NAS

### Enable NFS Service

Open `Settings` - `File Services` - `NFS` on your Synology NAS, check the NFS service and select the latest protocol.

### Configure NFS Permissions for Folders

Under `Settings` - `Shared Folder`, select the shared folder that needs to enable NFS, click `Edit`, switch to the `NFS Permissions` tab, click `Add` to add a new NFS rule.

For `Server or IP Address`, fill in the IP address of the server that needs to access the Synology NAS (for example, if my server and Synology NAS are on the same LAN, I can fill in the internal IP address of my server, 192.168.1.2). Check `Allow connections from non-privileged ports` and `Allow users to access mounted folder`, and keep other settings as default.

## Mounting on Server

First, install NFS service:

```bash
apt update
apt install nfs-common
```

Then, create a mount path on the server, for example:

```bash
sudo mkdir /DATA/nfs/music
```

Finally, execute the mount command:

```bash
mount -t nfs Synology NAS IP address:Shared folder path /NFS client path
```

For example:

```bash
sudo mount -t nfs 192.168.1.3:/volume1/music /DATA/nfs/music
```

If there is no error, use the `df` command to check the mount status.

## Reference and Acknowledgement

- [Mounting Synology NAS as Virtual Disk via NFS Service on Linux (Ubuntu)](https://cloud.tencent.com/developer/article/2104277)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.