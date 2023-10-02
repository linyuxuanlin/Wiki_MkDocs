# Building Your Own Homelab

Homelab refers to an experimental (tinkering) environment that can be built at home for experimentation and learning. It usually refers to a series of hardware devices (home servers, small hosts, old computers and phones, Raspberry Pi, etc.) running operating systems and software (Linux, virtual machines, Docker, etc.). Homelab has many uses, such as acting as a software router, remote host, or deploying a series of self-hosted services, such as personal bookshelves, movie libraries, password managers, personal websites, RSS readers, podcast servers, memos, and more. Not only practical, but also can be a hobby, adding fun to life.

## My Homelab Configuration

My own Homelab configuration is a **lightweight cloud server** + **small host** + **NAS**, each with its own configuration and purpose:

|          | Lightweight Cloud Server (Alibaba Cloud 1C2G) | Small Host (N100 CPU) | NAS (Synology DS220+) |
| -------- | ------------------------------------------- | --------------------- | --------------------- |
| Public IP | Yes                                         | No                    | No                    |
| Storage  | Small                                       | Medium                | Large                 |
| Performance | Low                                      | High                  | Low                   |

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304130031463.png)

It is not difficult to see that they are all biased towards a particular area, but as long as they work together, they are a triangle warrior. The **lightweight cloud server** is biased towards network access, the **small host** is biased towards performance processing, and the **NAS** is biased towards storage space.

### Lightweight Cloud Server

The **lightweight cloud server** is actually the surplus material of cloud server manufacturers, with low configuration but affordable prices. For example, the Alibaba Cloud lightweight server I purchased is only ￥96/year (if you have a cheaper package, let me know).

Because it has a public IP (ports 80/443 are also open), the services I deploy on this lightweight cloud host are mainly frp server, reverse proxy server, jump server for accessing other machines, monitoring panel for other hosts, small website services, website uptime monitoring, and other services that need to be accessed directly through the public network.

### Small Host

I chose the zero moment N100 CPU quasi-system for the **small host**, with a self-configured 16G DDR5 memory and 250G SSD hard drive, which cost about ￥1000 in total. The daily power consumption is not high, and it can also be called upon when performance is needed.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304130043744.png)

The types of applications deployed on the small host are mainly web VS Code code editor, private note library, RSS reader, podcast server, movie library, intranet browser, and other services that consume performance.

### NAS

I chose the Synology DS220+ for the **NAS**, which has an X86 architecture that is convenient for running Docker environments. Recently, I also added a 16G memory module to it in an attempt to improve its performance. However, I later found that the bottleneck was still the weak J4025 CPU. The white Synology can be considered as buying software and sending hardware, but it is still worth it for the security of data.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304130053483.png)

What I deploy on the NAS is mainly storage-demanding services such as device data backup, network disk synchronization, photo library, and book library.

## How to Deploy Docker Compose in One Click

With the spirit of tinkering, it is inevitable to brush the system every few days. With so many applications deployed, it is impossible to bring them up one by one. Here is a simple shell script that can deploy all Docker Compose in one click:

```shell title="compose.sh"
echo "starting compose.sh..."

# Traverse the first-level folders in the current directory
for folder in */; do
  [ "$folder" != "Archive/" ] # Ignore the Archive folder
  cd "$folder"  # Enter the folder
  docker-compose up -d # Execute the docker compose up -d command
  cd .. # Return to the parent directory
done

echo "done."
```

My directory structure is like this:

```
├── compose
│   ├── code-server
|   |   ├──compose.yaml
|   |   ├──.env
│   ├── frp
|   |   ├──compose.yaml
│   ├── xxx
|   |   ├──compose.yaml
│   ├── ……
│   └── compose.sh
```

Just execute `sh compose.sh` in the compose directory to start all Docker compose with one click.

## Advantages of Self-Hosting

Compared with third-party hosting, letting others keep your data for you, **Self-Hosting** has full advantages, which are reflected in your complete control over personal data, customization according to your preferences, and the ability to help you obtain more high-quality information sources (personal book library, movie library, RSS service). The premise is that you have a certain amount of time, energy, and financial investment, and have a willingness to tinker.

In the following series of articles, I will introduce some basic configurations and many interesting services. The ATH combination mentioned above is only my personal differentiated configuration. If you only have one machine, it is completely feasible to tinker with it. Most of the content I will introduce is based on Docker and Docker-compose deployment, because this method has extremely high compatibility and can be used out of the box on machines with different configurations. However, it should be mentioned that the machine selection is best X86 architecture, because some containers are not adapted for ARM and need to be compiled and installed by yourself.

## Reference and Acknowledgment

- [What interesting services have you deployed on your NAS?](https://www.v2ex.com/t/901954)
- [One-click to start multiple docker-compose configuration containers](https://juejin.cn/post/7082842557482270734)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.