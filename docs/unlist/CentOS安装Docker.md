---
id: CentOS安装Docker
title: CentOS 安装 Docker
---

## 卸载可能存在的旧版本

```shell
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

## 用仓库的方法安装

### 设置仓库

```shell
sudo yum install -y yum-utils
```

```shell
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

### 安装 Docker Engine

```shell
sudo yum install docker-ce docker-ce-cli containerd.io
```


## 参考与致谢 

* [Install Docker Engine on CentOS](https://docs.docker.com/engine/install/centos/)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
