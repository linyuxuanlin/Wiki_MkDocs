**Self-hosting** 指的是在自己的服务器上运行应用程序、服务或网站，而不是使用第三方托管服务。这种做法虽然需要一定的技术能力和成本投入，但是也具有 **提高数据安全性**、**实现完全自主控制** 和 **高度可定制性** 等方面的优势。

|          | 轻量云服务器                                    | HomeLab                                                | NAS                   |
| -------- | ----------------------------------------------- | ------------------------------------------------------ | --------------------- |
| 公网 IP  | 有                                              | 无                                                     | 无                    |
| 储存空间 | 小                                              | 中                                                     | 大                    |
| 性能     | 低                                              | 高                                                     | 低                    |
| 应用     | 反代服务器、NPS/FRP 服务器、uptime 监测、堡垒机 | 对性能有要求的服务、云代码编辑器、浏览器、轻办公类服务 | 大容量存储应用 / 服务 |

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