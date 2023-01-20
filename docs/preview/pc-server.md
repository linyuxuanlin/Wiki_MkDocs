https://nginxproxymanager.com/ Nginx Proxy

version: '3'
services:
app:
image: 'jc21/nginx-proxy-manager:latest'
restart: unless-stopped
ports: - '80:80' - '81:81' - '443:443'
volumes: - ./data:/data - ./letsencrypt:/etc/letsencrypt

version: '3'
services:
app:
image: 'jc21/nginx-proxy-manager:latest'
restart: unless-stopped
ports: - '79:80' - '81:81' - '442:443'
volumes: - /root/docker/nginx-proxy-manager/data:/data - /root/docker/nginx-proxy-manager/letsencrypt:/etc/letsencrypt

http://127.0.0.1:81

Email: admin@example.com
Password: changeme

ip addr show docker0
