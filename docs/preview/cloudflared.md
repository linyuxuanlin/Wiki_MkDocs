条件：

- paypal/visa（免费但要绑定）
- 域名绑定至 Cloudflare
- DNS 记录启用 Cloudflare CDN

优点：

- 不需要公网 IP 的服务器
- 不需要防火墙、反向代理
- 不需要备案就可以使用 80 和 443 端口
- 不需要自行申请 SSL 证书
- 免费

缺点：

- 速度慢
- 依赖 Cloudflare

[免费的 Cloudflared 实现外网访问群晖](https://laosu.ml/2022/04/06/%E5%85%8D%E8%B4%B9%E7%9A%84Cloudflared%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96/#%E8%8E%B7%E5%8F%96%E9%9A%A7%E9%81%93-token)

Cloudflare Zero Trust - Tunnels - Create a tunnel

记录 Tunnel ID (UUID)（格式为：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx）

记录 token `xxx`

在 docker/cloudflared 目录下放 config.yaml 文件:

```yml
tunnel: [Tunnel UUID]
credentials-file: /root/.cloudflared/[Tunnel UUID].json
```

启动 cloudflare/cloudflared

- 启动命令：`tunnel --config /etc/cloudflared/config.yaml --no-autoupdate run --token [token]`
- 网络：host
- docker/cloudflared:/etc/cloudflared

在 cloudflare 面板配置域名