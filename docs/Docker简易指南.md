---
id: Docker简易指南
title: Docker 简易指南
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210116153041.png)

软件开发中最麻烦的就是配环境。运行环境的差异，可能导致意想不到的结果。  
如何通过 Docker 来解决这个问题呢？

## Docker 是什么

Docker 把软件本身和它所需的运行环境打包起来，你用的时候就不需要再去配环境了（环境都在包里），这样就能确保你的环境和开发者的一模一样，杜绝因运行环境而出现的错误。

说起来，虚拟机也是这个原理，但虚拟机的缺点是相对庞大、占用资源也多。简而言之，就是可以，但没必要。Docker 相比虚拟机，不是模拟一个完整的操作系统，而是对进程进行隔离，占用少、启动快、体积小。

Docker 有三要素，分别是 image，container，repository.

- **image（镜像）**：把软件与环境打包在一起，可以看作是一个模板
- **container（容器）**：把 image 实例化，相当于把模板拿来用
- **repository（仓库）**：【待补充】

image 与 container 是一对多的关系，就是同一个模子印多个饼，每个饼可以加不一样的佐料调味。

## Docker 安装配置

各版本系统的下载安装详见 [**Install Docker Engine**](https://docs.docker.com/engine/install/)

- [**CentOS 安装 Docker**](https://wiki-power.com/unlist/CentOS%E5%AE%89%E8%A3%85Docker)

验证是否安装成功：

```shell
docker version
```

### 配置权限

Docker 需要 `sudo` 权限。为了避免每次使用都要获取权限，可以把用户加入 Docker 用户组：

```shell
sudo usermod -aG docker $USER
```

### 启动 Docker

按如下命令启动 Docker：

```shell
sudo systemctl start docker
```

（也可以使用 `sudo service docker start`）

配置开机自启动（可选）：

```shell
sudo systemctl enable docker
```

### 换源

因为 Docker 的官方源地址在国外，所以有时候下载缓慢，我们通过更换国内镜像源来解决：

```shell
sudo vi /etc/default/docker
```

按 `a` 进入编辑模式，在尾部添加一行：

```
DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
```

按 `ESC` 推出编辑后按 `:wq` 保存退出。  
重启 Docker 服务：

```shell
sudo service docker restart
```

## Docker 基本操作

### image 操作

#### 列出本地所有 image

```shell
docker image ls
```

#### 删除 image

```shell
docker image rm [imageName]
```

虽然 image 可以自己造，但我们推荐直接用别人的，既省时省力，又有利于维护环境统一。  
你可以在 [**Docker Hub**](https://hub.docker.com/) 搜索并下载 image 文件，拣下载量较多的用。

### container 操作

#### 列出正在运行的容器

```shell
docker container ls
```

可以加上 `--all` 参数，列出所有（包括已经停止的）容器。

列出容器时，能看到容器对应的 ID，这个 ID 在很多地方会用到。

#### 新建并运行容器

```shell
docker container run [imageName]
```

#### 运行已经存在的容器

```shell
docker container start [containerID]
```

#### 停止容器的运行

```shell
docker container stop [containerID]
```

#### 删除容器

```shell
docker container rm [containerID]
```

#### 查看容器的输出

```shell
docker container logs [containerID]
```

#### 操作容器

```shell
docker container exec -it [containerID] /bin/bash
```

## 实例：Hello World

下面将用官方 hello-world 例子来演示 Docker。

首先，将 image 拉拉取到本地：

```shell
docker image pull library/hello-world
```

拉取后，使用 ls 命令检查是否已经下载：

```shell
docker image ls
```

生成容器并运行：

```shell
docker container run hello-world
```

因为这个 hello-world 只运行一次，所以不用手动去停止。  
对于持续运行的容器，如果需要停止，就用以下命令：

```shell
docker container kill [containID]
```

## 参考与致谢

- [Docker 入门教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

