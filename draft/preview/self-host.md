
轻量云服务器篇

HomeLab 篇

1. 用 ventoy 安装 debian
2. 安装 casaos（带 docker）
3. frp/nps

NAS 篇

---

```
vi /etc/ssh/sshd_config
```

将 PermitRootLogin 设置为 yes

ubuntu/debian 系统安装 Curl 方法：

```shell
apt-get update -y && apt-get install curl -y
```

安装 sudo：

```shell
apt-get install sudo
```

安装 CasaOS：

```shell
curl -fsSL https://get.casaos.io | sudo bash
```

换源：

https://www.24kplus.com/linux/1933.html

## frp:host,高权限

WiFi

sudo apt-get install wireless-tools wpasupplicant
sudo apt-get install aptitude

lspci | grep Wireless

---

cloudflared

https://hub.docker.com/r/cloudflare/cloudflared

```
docker run cloudflare/cloudflared:latest tunnel --no-autoupdate --hello-world
```
---

网卡

https://www.jianshu.com/p/b341ee6ed160

查询WIFI，如下显示了无线网卡的型号

```
$ lspci -nn
...
00:14.3 Network controller [0280]: Intel Corporation Device [8086:54f0]
```

按着网址

---

连WiFi

