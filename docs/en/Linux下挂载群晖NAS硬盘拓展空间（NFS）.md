# Mount Synology NAS Hard Drive for Space Expansion on Linux (NFS)

If your server is running low on storage space, you can consider mounting a hard drive from your Synology NAS to expand your storage capacity.

## Configuration on Synology NAS

### Enabling NFS Service

1. Open your Synology DiskStation's settings.
2. Navigate to `File Services` and select `NFS`.
3. Enable the NFS service, and choose the latest protocol.

### Configuring NFS Permissions for Folders

1. Under `Settings`, go to `Shared Folders`.
2. Select the shared folder you wish to make accessible via NFS and click `Edit`.
3. Go to the `NFS Permissions` tab and click `Add` to create a new NFS rule.
4. For the `Server or IP address` field, enter the IP address of the server that needs access to your Synology (e.g., if your server and Synology are on the same local network, enter your server's local IP, such as 192.168.1.2).
5. Check the boxes for `Allow connections from non-privileged ports` and `Allow users to access mounted subfolders`. Keep other settings at their default values.

## Mounting on the Server

First, install the NFS service:

```bash
apt update
apt install nfs-common
```

Next, create a mount point on your server, for example:

```bash
sudo mkdir /DATA/nfs/music
```

Finally, execute the mount command:

```bash
mount -t nfs NAS_IP_address:/path_to_shared_folder /NFS_client_path
```

For example:

```bash
sudo mount -t nfs 192.168.1.3:/volume1/music /DATA/nfs/music
```

If there are no errors, you can use the `df` command to check the mounting status.

## References and Acknowledgments

- [Mount Synology NAS as a Virtual Disk on Linux (Ubuntu) via NFS](https://cloud.tencent.com/developer/article/2104277)

[to_be_replaced[1]]
[to_be_replaced[2]]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.