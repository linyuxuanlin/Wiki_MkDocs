# Automatically Applying Domain Certificates Using acme.sh (Synology Docker)

This article explains how to use the Docker image acme.sh to achieve automatic domain certificate application and renewal.

[**acme.sh**](https://github.com/acmesh-official/acme.sh) can generate free certificates from letsencrypt, supports Docker deployment, and offers two domain validation methods: HTTP and DNS. These methods include manual, automatic DNS, and DNS alias modes to accommodate various environments and requirements. It can simultaneously apply and merge multiple single-domain and wildcard certificates, automatically renew certificates, and deploy them to projects.

## Preparing DNS API

In this article, we will use Tencent Cloud as an example to apply for the DNS API. For other DNS providers, please refer to the official documentation [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi).

First, open [**DNSPOD**](https://console.dnspod.cn/), click on your profile picture in the upper right corner, and select "Key Management."

Next, create a new key and copy the **ID** and **Token**.

## Deployment on Synology Docker

This tutorial covers Docker's daemon mode, where a container runs continuously to automatically renew certificates upon expiration.

### Creating Configuration Folder

First, create the `/docker/acme.sh` folder and manually create the `account.conf` file:

![acme.sh](https://media.wiki-power.com/img/20210430212420.png)

Next, edit this file and manually add the following lines:

```conf
export DP_Id="ID obtained earlier"
export DP_Key="Token obtained earlier"
AUTO_UPGRADE='1'
```

Then, save and close the file.

### Downloading the Image and Configuring the Container

Open Synology Docker Suite, download the `neilpang/acme.sh` image, double-click to start, and access "Advanced Settings."

On the "Volume" page, configure the mounted folders by clicking "Add Folder" and select the local path to `docker/acme.sh`, and set the mount path to `/acme.sh` (default, do not change):

![Volume Configuration](https://media.wiki-power.com/img/20210430214221.png)

On the "Network" page, check "Use the same network as Docker Host."

Next, switch to the "Environment" page and enter the `daemon` command in the "Command" field:

![Environment Configuration](https://media.wiki-power.com/img/20210430215244.png)

Then create and run the container. Double-click on the running container, switch to the "Terminal" page, click "Start with Command," enter `sh`, and confirm.

To enable automatic updates, enter the following command:

```shell
acme.sh --upgrade --auto-upgrade
```

Then, to apply for a certificate, enter the following command:

```shell
acme.sh --issue --dns dns_dp -d wiki-power.com -d *.wiki-power.com
```

Here, `dns_dp` represents Tencent Cloud DNSPod. If you are using Alibaba Cloud, please use `dns_ali`. For Cloudflare, use `dns_cf`. For other providers, refer to the official documentation [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi). Additionally, `*.wiki-power.com` represents the application for a wildcard domain certificate. If you need to apply for multiple domains simultaneously, you can follow this format:

```shell
acme.sh --issue --dns dns_dp -d aaa.com -d *.aaa.com -d bbb.com -d *.bbb.com -d ccc.com -d *.ccc.com
```

In daemon mode, acme.sh will automatically renew certificates every 60 days.

### Generating Certificates

If everything goes smoothly, you can find the `domain.cer` and `domain.key` files inside the folder named after your domain in `docker/acme.sh`. These are the certificate and key files that you can copy to wherever you need to use them.

## References and Acknowledgments

- [Synology NAS Advanced Services - Deploying acme.sh for Automated Domain Certificate Acquisition](https://www.ioiox.com/archives/88.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
