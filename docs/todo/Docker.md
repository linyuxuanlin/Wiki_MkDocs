volume 也是绕过 container 的文件系统，直接将数据写到 host 机器上，只是 volume 是被 docker 管理的，docker 下所有的 volume 都在 host 机器上的指定目录下/var/lib/docker/volumes

docker run -d --cap-add SYS_PTRACE \
 --name=code-server \
 -e PUID=1000 \
 -e PGID=1000 \
 -e PASSWORD=71982547 `#optional` \
 -e HASHED_PASSWORD= `#optional` \
 -e SUDO_PASSWORD=71982547 `#optional` \
 -e SUDO_PASSWORD_HASH= `#optional` \
 -e PROXY_DOMAIN=code-server.my.domain `#optional` \
 -e DEFAULT_WORKSPACE=/config/workspace `#optional` \
 -p 8888:8443 \
 -v /root/config:/config \
 --restart unless-stopped \
 lscr.io/linuxserver/code-server:latest \
 --cert=/config/cert/frp.wiki-power.com_bundle.crt \
 --cert-key=/config/cert/frp.wiki-power.com.key

docker run -d --cap-add SYS_PTRACE \
 --name=code-server \
 -e PUID=1000 \
 -e PGID=1000 \
 -e PASSWORD=71982547 `#optional` \
 -e HASHED_PASSWORD= `#optional` \
 -e SUDO_PASSWORD=71982547 `#optional` \
 -e SUDO_PASSWORD_HASH= `#optional` \
 -e PROXY_DOMAIN=code-server.my.domain `#optional` \
 -e DEFAULT_WORKSPACE=/config/workspace `#optional` \
 -p 8888:8443 \
 -v /root/config:/config \
 -v /root/config/cert/frp.wiki-power.com_bundle.crt:/config/cert/frp.wiki-power.com_bundle.crt \
 -v /root/config/cert/frp.wiki-power.com.key:/config/cert/frp.wiki-power.com.key \
 --restart unless-stopped \
 lscr.io/linuxserver/code-server:latest \
 --cert=/config/cert/frp.wiki-power.com_bundle.crt \
 --cert-key=/config/cert/frp.wiki-power.com.key
