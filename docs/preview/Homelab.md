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

```yml title="docker-compose.yml"
version: "3.7"

services:
  frps:
    restart: always
    container_name: frps
    image: fatedier/frp:latest
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
      - /root/docker/frp/frps.ini:/app/frps.ini:ro
    command: -c /app/frps.ini
    ports:
      - 7000:7000
      - 7500:7500
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
```

version: "3"
services:
frps:
image: fatedier/frp:latest
container_name: frps
volumes: - /root/docker/frp/frps.ini:/etc/frps.ini
network_mode: "host"
command:
frps
restart: always

docker run --restart=always --network host -d -v /root/docker/frp/frps.ini:/etc/frp/frps.ini --name frps snowdreamtech/frps

---

7000
cs http://frps.cs.wiki-power.com/ http://frp.wiki-power.com:7500/ frps
cs http://frp.wiki-power.com:3000/ speed test
:8384 syncing

---

watchtower

```docker run
docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower
```

https://icon.casaos.io/main/all/freshrss.png

```docker-compose.yml
version: "3"
services:
  watchtower:
    image: containrrr/watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

---

---

https://www.docker.com/blog/how-to-use-the-official-nginx-docker-image/

docker run -it --rm -d -p 8080:80 --name nginx-test nginx

docker cp nginx-test:/root/docker/nginx/nginx.conf /etc/nginx/nginx.conf

docker cp nginx-test:/root/docker/nginx/conf.d /etc/nginx/

docker cp nginx-test:/etc/nginx/nginx.conf /root/docker/nginx/  
docker cp nginx-test:/etc/nginx/conf.d /root/docker/nginx/

docker run nginx\
-p 80:80 \
--name nginx \
-v /root/docker/nginx/nginx.conf:/etc/nginx/nginx.conf \
-v /root/docker/nginx/conf.d:/etc/nginx/conf.d \
-v /root/docker/nginx/logs:/var/log/nginx \

---

在服务器管理页面关闭端口访问

## CF 15 年证书

域名迁入 CF，在 SSL/TLS - Orgin Server 开启

---
