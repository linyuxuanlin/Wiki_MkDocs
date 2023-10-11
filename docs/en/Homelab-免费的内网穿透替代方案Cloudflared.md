# Homelab - Free Intranet Penetration Alternative Cloudflared

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416143051.png)

**Cloudflared** is a free intranet penetration solution used for external access to hosts without public IP addresses.

Requirements:

- Although Cloudflared is free, it requires binding to VISA/PayPal.
- The domain NameServer needs to point to Cloudflare.
- Cloudflare CDN needs to be enabled (domestic access speed is slow).

Advantages:

- No need for servers with public IP addresses.
- No need for firewalls or reverse proxies.
- Can use ports 80 and 443 without filing.
- No need to apply for SSL certificates.
- Free.

Disadvantages:

- Slow domestic access speed.
- Relatively dependent on the Cloudflare platform.

## Deployment (Docker Compose)

First, create the `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  cloudflared:
    container_name: ${STACK_NAME}_app
    image: cloudflare/cloudflared:${APP_VERSION}
    network_mode: host
    restart: unless-stopped
    command: tunnel run
    environment:
      - TUNNEL_TOKEN=${APP_TUNNEL_TOKEN}
```

(Optional) It is recommended to create a `.env` file at the same level as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `cloudflared`).

````dotenv title=".env"
STACK_NAME=cloudflared```

# cloudflared
APP_VERSION=latest
APP_TUNNEL_TOKEN=xxx # Replace with your token
````

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

Access the [**Cloudflare Zero Trust**](https://one.dash.cloudflare.com/) panel, select `Access` - `Tunnels` in the left sidebar, and click `Create a tunnel` to create a tunnel. Fill in the tunnel name (used to distinguish different physical machines) and save it. Record the token and fill it in `compose.yaml`.

Then click into the tunnel you created and add the proxy port in the `Public Hostname Page` tab. For example, if I bind a domain name `wiki-power.com` on Cloudflare and the local port of the service I need to proxy is `80` with the `HTTP` protocol, I just need to fill it out like this:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416183438.png)

You can access the local port through <https://dashboard.wiki-power.com>, and it will automatically apply for an SSL certificate for you, allowing you to access it via https on the public network.

## References and Acknowledgements

- [Official Website / Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
- [GitHub repo](https://github.com/cloudflare/cloudflared)
- [Docker Hub](https://hub.docker.com/r/cloudflare/cloudflared)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
