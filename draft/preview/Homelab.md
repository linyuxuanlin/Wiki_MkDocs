## DEBUG 环境

云服务器

VS Code:

- Remote - SSH
- `"remote.SSH.useLocalServer": false,`

### Portainer

```shell
mkdir -p docker/portainer
cd docker/portainer
nano compose.yaml
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

```shell
docker-compose up -d
```

<http://SERVER_IP:9000/>

- [Install Portainer Docker Compose | How-to Guide](https://bobcares.com/blog/install-portainer-docker-compose/)

---

cs http://frp.wiki-power.com:3000/ speed test
:8384 syncing

https://icon.casaos.io/main/all/freshrss.png

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

## CF 15 年证书

域名迁入 CF，在 SSL/TLS - Orgin Server 开启

---
