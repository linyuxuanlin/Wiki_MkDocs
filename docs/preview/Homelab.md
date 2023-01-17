## DEBUG 环境

云服务器

VS Code:

- Remote - SSH
- `"remote.SSH.useLocalServer": false,`

## FRP

## Docker

```bash
docker-compose pull
```

### Code Server

[Docker 方法部署 code-server](https://wiki-power.com/Docker%E6%96%B9%E5%BC%8F%E8%BF%90%E8%A1%8Ccode-server)

### Portainer

```bash
mkdir -p docker/portainer
cd docker/portainer
nano docker-compose.yml
```

```docker
---
version: '3'

services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./portainer-data:/data
    ports:
      - 9000:9000
```

```bash
docker-compose up -d
```

<http://SERVER_IP:9000/>

- [Install Portainer Docker Compose | How-to Guide](https://bobcares.com/blog/install-portainer-docker-compose/)

### acme.sh

- [使用 acme.sh 免费申请泛域名证书和自动续约](https://blog.csdn.net/qwe134133987/article/details/128456550)

---

## CasaOS

https://casaos.io/

```
curl -fsSL https://get.casaos.io | sudo bash
```

## FRP

在 `/root/docker/frp` 下新建 `frps.ini`:

```ini title="frps.ini"
[common]
bind_port = 7000
dashboard_port = 7500
token = 设置 token
dashboard_user = 设置用户名
dashboard_pwd = 设置面板密码
```

