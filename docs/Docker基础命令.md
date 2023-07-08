---
id: Docker基础命令
title: Docker 基础命令
---

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

### Image 操作

#### 列出本地所有 Image

```shell
docker Image ls
```

#### 删除 Image

```shell
docker Image rm [ImageName]
```

虽然 Image 可以自己造，但我们推荐直接用别人的，既省时省力，又有利于维护环境统一。  
你可以在 [**Docker Hub**](https://hub.docker.com/) 搜索并下载 Image 文件，拣下载量较多的用。

### Container 操作

#### 列出正在运行的容器

```shell
docker Container ls
```

可以加上 `--all` 参数，列出所有（包括已经停止的）容器。

列出容器时，能看到容器对应的 ID，这个 ID 在很多地方会用到。

#### 新建并运行容器

```shell
docker Container run [ImageName]
```

#### 运行已经存在的容器

```shell
docker Container start [ContainerID]
```

#### 停止容器的运行

```shell
docker Container stop [ContainerID]
```

#### 删除容器

```shell
docker Container rm [ContainerID]
```

#### 查看容器的输出

```shell
docker Container logs [ContainerID]
```

#### 操作容器

```shell
docker Container exec -it [ContainerID] /bin/bash
```

## 实例：Hello World

下面将用官方 hello-world 例子来演示 Docker。

首先，将 Image 拉拉取到本地：

```shell
docker Image pull library/hello-world
```

拉取后，使用 ls 命令检查是否已经下载：

```shell
docker Image ls
```

生成容器并运行：

```shell
docker Container run hello-world
```

因为这个 hello-world 只运行一次，所以不用手动去停止。  
对于持续运行的容器，如果需要停止，就用以下命令：

```shell
docker Container kill [containID]
```
