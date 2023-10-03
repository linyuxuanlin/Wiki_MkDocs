# Accessing Synology NAS Using frp

Access Synology NAS using frp in any network.

## Why Access Synology Using frp

- No public IP
- Slow QuickConnect service
- Services like Peanut Shell require separate traffic purchase

## Server Configuration

Refer to the article [**How to Implement External Network RDP Remote Control (frp) · Server Configuration**](https://wiki-power.com/en/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%85%8D%E7%BD%AE). Note that the `vhost_http_port` / `vhost_https_port` parameters in the `frpc.ini` configuration file must be retained.

### Bind Domain Name

- Add an A record with the server IP in the domain resolution
- Configure domain name binding on the cloud server

## Synology NAS Configuration

### Edit Configuration File

Create a new `frpc.ini` file in any location and enter the following content:

```ini title="frpc.ini"
[common]
server_addr = Server IP
server_port = Server frp port, default is 7000
token = Key, must be the same as configured on the server

[dsm-http]
type = tcp
local_ip = localhost
local_port = Synology DSM http port, default is 5000
custom_domains = Bound domain name
remote_port = Custom remote port

[dsm-https]
type = tcp
local_ip = localhost
local_port = Synology DSM https port, default is 5001
custom_domains = Bound domain name
remote_port = Custom remote port

[ssh]
type = tcp
local_ip = localhost
local_port = Default is 22
custom_domains = Bound domain name
remote_port = Custom remote port
```

### Using Docker Method

Install the `stilleshan/frpc` image in Synology's Docker and initialize the container using the following parameters:

- Check `Use high privilege to execute container`
- Check `Enable automatic restart`
- Add a file in the `Volume` tab, select the local `frpc.ini` file, and mount it to the path `/frp/frpc.ini`
- Check `Use the same network as Docker Host`

Start the container and wait a moment, then you can access Synology DSM using the domain name + http port number.

## Reference and Acknowledgment

- [Tutorial on Using Docker to Install and Configure frpc Intranet Penetration for Synology NAS](https://www.ioiox.com/archives/26.html)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.