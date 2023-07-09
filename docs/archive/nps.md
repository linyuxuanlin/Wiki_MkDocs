A lightweight, high-performance, powerful intranet penetration proxy server, with a powerful web management terminal.

### 服务端 nps

- 下载 [**conf 文件夹**](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/ehang-io/nps/tree/master/conf) 并解压上传。

```yaml title="compose.yaml"
version: "3"
services:
  nps_server:
    image: ffdfgdfg/nps
    restart: always
    network_mode: "host"
    volumes:
      - ${DIR}/conf:/conf
```

### 客户端 npc

```yaml title="compose.yaml"
version: "3"
services:
  web_server:
    image: nginx
    container_name: web_server
    expose:
      - "80"
      - "443"
  nps_client:
    image: geektr/nps
    environment:
      - NPS_SERVER=aika.geektr.co:8024
      - NPS_VKEY=xxxxxxxxxxxxxxxx
    restart: always
```

docker run -d --name npc --net=host ffdfgdfg/npc -server=nginx.wiki-power.com:4000 -vkey=z2begrxvhk35cmni

---
