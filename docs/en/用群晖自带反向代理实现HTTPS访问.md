# Implementing HTTPS Access with Synology's Built-in Reverse Proxy

First, you need an external IP or domain name to access Synology, and you have already applied for an SSL certificate. For detailed instructions, please refer to the article [**Using acme.sh to Automatically Apply Domain Certificates (Synology Docker)**](https://wiki-power.com/en/%E5%9F%BA%E4%BA%8Eacme.sh%E8%87%AA%E5%8A%A8%E7%94%B3%E8%AF%B7%E5%9F%9F%E5%90%8D%E8%AF%81%E4%B9%A6%EF%BC%88%E7%BE%A4%E6%99%96Docker%EF%BC%89).

## Configuring Reverse Proxy

Open `Control Panel` - `Login Portal` - `Advanced` - `Reverse Proxy Server`.

For example, we add a reverse proxy service named `bitwarden`. Fill in the configuration according to the following figure:

![](https://img.wiki-power.com/d/wiki-media/img/20210503213004.png)

- `Source`
  - `Protocol`: Select `HTTPS`
  - `Hostname`: Fill in the external access domain name
  - `Port`: Fill in the external access port
  - Check `Enable HSTS` (force redirect to HTTPS)
- `Destination`
  - `Protocol`: Select `HTTP`
  - `Hostname`: Fill in `localhost`
  - `Port`: Fill in the port for internal access (for bitwarden, it is the port mapped to port `80` of the container, such as `8003`)

## Configuring Certificates

Open `Control Panel` - `Security` - `Certificate`, select the certificate in use, click `Settings`, and make sure that the certificate for the domain name corresponding to the reverse proxy service `bitwarden` is the current certificate.

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
