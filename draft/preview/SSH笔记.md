# SSH

**ssh（Secure Shell）**是一个用于安全连接到远程计算机的命令。它可以通过加密的方式在不安全的网络上进行安全的通信。ssh 命令的基本语法如下：

```sh
ssh [选项] [用户名@]主机 [命令]
ssh -p port_number -i /path/to/private_key  user@hostname
```

## 禁用 SSH 密码登录并改用公私钥登录

假设本地设备 A，通过 ssh 连接到远程服务器 B。

### 1. 生成 SSH 密钥对

如果本地设备 A 还没有公私钥对，可以使用以下命令生成：

```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

这个命令会让你创建一个新密钥对。它会问你是否要把密钥保存在默认位置（通常是 ~/.ssh/id_rsa），你可以按 Enter 键接受默认位置。接着，它会要求你设置一个密码短语（passphrase），你可以设置也可以不设置（建议设置以提高安全性）。密码短语（passphrase）是用来保护你的私钥的一个额外安全措施。命令中的邮箱地址是用来作为密钥对的注释（comment）的，不会影响实际功能

### 2. 将公钥添加到远程服务器

刚生成的公钥（相当于锁）添加到你想连接的远程服务器上的 `~/.ssh/authorized_keys` 文件中。可以使用 ssh-copy-id 命令：

```sh
ssh-copy-id -i ~/.ssh/id_rsa.pub your_username@remote_server_ip
```

### 3. 配置 SSH 服务器禁用密码登录

编辑远程服务器上的 SSH 配置文件 `/etc/ssh/sshd_config`：

```sh
sudo vi /etc/ssh/sshd_config
```

找到并修改以下参数（如果参数不存在，可以手动添加）：

```sh
PasswordAuthentication no
ChallengeResponseAuthentication no
UsePAM no
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
```

### 4. 重启 SSH 服务

保存并关闭配置文件后，重启 SSH 服务以使更改生效：

```sh
sudo systemctl restart sshd
```

### ssh: Bad permissions

ssh 连接时提示：

```
Bad permissions. Try removing permissions for user: UNKNOWN\UNKNOWN (xxxxxx) on file C:/Users/xxx/.ssh/config.
Bad owner or permissions on C:\Users\xxx/.ssh/config
```

这个错误消息表明 SSH 配置文件 (.ssh/config) 的权限设置不正确。需要调整该文件的权限以确保 SSH 能够正确读取它。

```sh
cd C:\Users\Power\.ssh
icacls config /inheritance:r
icacls config /grant:r %username%:F
```
