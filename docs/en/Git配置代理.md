# Configuring Git Proxy

## Problem

`git clone` and `git pull` are too slow in China.

## Solution

### 1. Configure proxy software

1. Check "Allow connections from local network" in the proxy software.
2. Note the port number (e.g. 1080).
3. Enable "Global Mode".

### 2. Configure Git global http proxy

```shell
git config --global http.proxy http://127.0.0.1:【port number】
git config --global https.proxy https://127.0.0.1:【port number】

# For example:
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy https://127.0.0.1:10808

# If the above does not work, try using the socks5 port:
git config --global http.proxy socks5://127.0.0.1:【port number】
git config --global https.proxy socks5://127.0.0.1:【port number】

# If you only want to proxy GitHub and not affect domestic repositories (not recommended if you are not familiar with configuration files):
git config --global http.https://github.com.proxy https://127.0.0.1:【port number】
git config --global https.https://github.com.proxy https://127.0.0.1:【port number】

# If you only want to proxy GitLab and not affect domestic repositories (not recommended if you are not familiar with configuration files):
git config --global https.https://https://gitlab.com.proxy https://127.0.0.1:1080
```

Configuration on Ubuntu:

```shell
git config --global http.https://github.com.proxy socks5://127.0.0.1:10808
```

### View the path of the configuration file.

```
git config –list –show-origin
```

### Recovery

If you don't want to use a proxy, you can restore it using the following method:

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## References and Acknowledgments

- [**Conquer the Slow Submission of git clone and git pull**](https://c.lanmit.com/czxt/Linux/16965.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.