# Implementing HTTPS Access with Synology's Built-in Reverse Proxy

First, you need an external IP or domain name to access Synology, and you have already obtained an SSL certificate. For detailed instructions, you can refer to the article [**Automatically Apply Domain Certificates with acme.sh (Synology Docker)**](https://wiki-power.com/%E5%9F%BA%E4%BA%8Eacme.sh%E8%87%AA%E5%8A%A8%E7%94%B3%E8%AF%B7%E5%9F%9F%E5%90%8D%E8%AF%81%E4%B9%A6%EF%BC%88%E7%BE%A4%E6%99%96Docker%EF%BC%89).

## Configure the Reverse Proxy

Open `Control Panel` - `Login Portal` - `Advanced` - `Reverse Proxy Server`.

For example, we will add a reverse proxy service named `bitwarden`. Fill in the configuration as shown in the following image:

![](https://media.wiki-power.com/img/20210503213004.png)

- `Source`
  - `Protocol`: Select `HTTPS`
  - `Hostname`: Fill in the domain name for external access
  - `Port`: Fill in the port for external access
  - Check `Enable HSTS` (Force HTTPS redirection)
- `Destination`
  - `Protocol`: Select `HTTP`
  - `Hostname`: Fill in `localhost`
  - `Port`: Fill in the port for internal access (for bitwarden, it is the port mapped to container `80`, such as `8003`)

## Configure the Certificate

Open `Control Panel` - `Security` - `Certificate`. Select the certificate being used, click `Settings`, and make sure that the certificate for the domain corresponding to the reverse proxy service `bitwarden` is the current certificate.

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
