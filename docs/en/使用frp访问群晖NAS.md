# Accessing Synology NAS Using frp

Access your Synology NAS from any network using frp.

## Why Use frp to Access Synology

- No public IP address
- Slow QuickConnect service
- Separate purchase of services like Peanut Shell for traffic

## Server Configuration

Visit the article [**How to Implement External RDP Control (frp) - Server Configuration**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%85%8D%E7%BD%AE). Note that the `vhost_http_port` / `vhost_https_port` parameters in the `frpc.ini` configuration file must be retained.

### Domain Binding

- Add an A record with the server's IP address in your domain registrar's settings.
- Configure domain binding in your cloud server settings.

## Synology NAS Configuration

### Edit the Configuration File

Create a `frpc.ini` file at any location and add the following content:

```ini
[common]
server_addr = Server IP
server_port = Server frp port, default is 7000
token = Key, must match the one configured on the server

[dsm-http]
type = tcp
local_ip = localhost
local_port = Synology DSM HTTP port, default is 5000
custom_domains = Bound domain
remote_port = Custom remote port

[dsm-https]
type = tcp
local_ip = localhost
local_port = Synology DSM HTTPS port, default is 5001
custom_domains = Bound domain
remote_port = Custom remote port

[ssh]
type = tcp
local_ip = localhost
local_port = Default is 22
custom_domains = Bound domain
remote_port = Custom remote port
```

### Using the Docker Method

Install the `stilleshan/frpc` image in Synology's Docker and initialize the container with the following parameters:

- Enable 'Use high privilege to run container'
- Enable 'Auto-restart'
- Add a file under the 'Volume' tab, select your local `frpc.ini` file, and set the Mount path to `/frp/frpc.ini`
- Enable 'Use the same network as Docker Host'

Start the container, and after a moment, you can access Synology DSM using your domain and HTTP port number.

## References and Acknowledgments

- [Synology NAS Docker Installation and Configuration of frpc Intranet Penetration Tutorial](https://www.ioiox.com/archives/26.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.