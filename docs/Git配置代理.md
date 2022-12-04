---
id: Git配置代理
title: Git 配置代理
---

## 问题来源

国内 `git clone` 与 `git pull` 速度太慢。

## 解决方法

### 1. 代理软件内设置

1. 在代理软件内勾选 `允许来自局域网的连接`
2. 记下端口号（例如：1080）
3. 开启 `全局模式`

### 2. 给 Git 全局配置 http 代理

```shell
git config --global http.proxy http://127.0.0.1:【端口号】
git config --global https.proxy https://127.0.0.1:【端口号】

# 例如：
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy https://127.0.0.1:10808

# 如果上面的不生效，则用：
git config --global http.proxy 'socks5://127.0.0.1:【端口号】'
git config --global https.proxy 'socks5://127.0.0.1:【端口号】'

# 如果只对 GitHub 进行代理，对国内的仓库不影响（不熟悉配置文件不建议使用）：
git config --global http.https://github.com.proxy https://127.0.0.1:【端口号】
git config --global https.https://github.com.proxy https://127.0.0.1:【端口号】

# 只对 GitLab 进行代理，对国内的仓库不影响（不熟悉配置文件不建议使用）：
git config --global https.https://https://gitlab.com.proxy https://127.0.0.1:1080
```

Ubuntu 下配置：

```shell
git config --global http.https://github.com.proxy socks5://127.0.0.1:10808
```

### 查看配置文件的路径

```
git config –list –show-origin
```

### 恢复

如果不想用代理，可以用以下的方法恢复：

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 参考与致谢

- [**征服 git clone 与 git pull 的龟速提交**](https://c.lanmit.com/czxt/Linux/16965.html)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

