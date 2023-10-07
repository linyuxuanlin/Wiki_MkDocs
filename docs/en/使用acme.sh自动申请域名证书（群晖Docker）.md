# Using acme.sh to Automatically Apply Domain Certificates (Synology Docker)

This article introduces how to use the Docker image acme.sh to achieve automatic application and renewal of domain certificates.

[**acme.sh**](https://github.com/acmesh-official/acme.sh) can generate free certificates from letsencrypt, supports Docker deployment, and supports two domain verification methods: http and DNS, including manual, automatic DNS, and DNS alias modes to facilitate various environments and needs. It can simultaneously apply and merge multiple single-domain, wildcard domain certificates, and automatically renew certificates and deploy them to projects.

## Prepare DNS API

This article uses Tencent Cloud as an example to apply for DNS API. For other resolution platforms, please refer to the official documentation [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi).

First, open [**DNSPOD**](https://console.dnspod.cn/), click on the avatar in the upper right corner, and select `Key Management`.

Then, create a new key and copy the **ID** and **Token**.

## Deploy on Synology Docker

This tutorial introduces the daemon mode of Docker, which keeps the container running and automatically renews the certificate when it expires.

### Create Configuration Folder

First, we create the `/docker/acme.sh` folder and manually create the `account.conf` file:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210430212420.png)

Then, we edit this file and manually add these lines:

```conf
export DP_Id="ID just applied"
export DP_Key="TOKEN just applied"
AUTO_UPGRADE='1'
```

Then save and close the file.

### Download Image and Configure Container

Open the Synology Docker suite, download the `neilpang/acme.sh` image, double-click to start and enter `Advanced Settings`.

On the `Volume` page, configure the mounted folder, click `Add Folder`, select the local `docker/acme.sh` path, and fill in the mounting path as `/acme.sh` (default and unchangeable):

![](https://f004.backblazeb2.com/file/wiki-media/img/20210430214221.png)

On the `Network` page, check `Use the same network as Docker Host`.

Then switch to the `Environment` page and fill in the `daemon` command in the `Command` box:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210430215244.png)

Then create and run the container. Double-click the running container, switch to the `Terminal` page, click `Start with Command`, enter `sh` and click OK.

Enter the following command to enable automatic updates:

```shell
acme.sh --upgrade --auto-upgrade
```

Then enter the following command to apply for a certificate:

```shell
acme.sh --issue --dns dns_dp -d wiki-power.com -d *.wiki-power.com
```

Here, `dns_dp` represents Tencent Cloud DNSPod. If it is Alibaba Cloud, please fill in `dns_ali`, Cloudflare fill in `dns_cf`, and others please refer to the official manual [**dnsapi**](https://github.com/acmesh-official/acme.sh/wiki/dnsapi). In addition, `*.wiki-power.com` represents a wildcard domain certificate. If you need to apply for multiple domains at the same time, you can follow the following method:

```shell
acme.sh --issue --dns dns_dp -d aaa.com -d *.aaa.com -d bbb.com -d *.bbb.com -d ccc.com -d *.ccc.com
```

In daemon mode, acme.sh will automatically update the certificate every 60 days based on the application record.

### Generating Certificates

If everything goes well, you can find the `domain.cer` and `domain.key` files in the `docker/acme.sh/domain-named folder`. These are the certificate and key files, which can be copied to the required location.

## References and Acknowledgments

- [Advanced Services for Synology NAS - Deploying acme.sh to Automatically Apply Domain Certificates with Docker](https://www.ioiox.com/archives/88.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.