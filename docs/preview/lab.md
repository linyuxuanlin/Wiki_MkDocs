## 安装 sudo 命令

```
apt-get install sudo
```

## 开启 root 登录

```shell
sudo nano /etc/ssh/sshd_config
```

将 `PermitRootLogin` 这一行取消注释，并将值从 `prohibit-password` 改为 `yes`，保存。

```
sudo systemctl restart ssh # 重启 ssh 服务
```

## 安装 Docker 环境

```shell
apt install curl
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun # 安装 Docker
sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose # 安装 Docker compose
sudo chmod +x /usr/local/bin/docker-compose # 将可执行权限应用于二进制文件
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose # 创建软链
```

## 安装 CasaOS

```shell
curl -fsSL https://get.casaos.io | sudo bash
```

## Docker Apps init

1. 安装 Frp
2. Cloudflared ([**Connect with SSH through Cloudflare Tunnel**](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/use_cases/ssh/))
