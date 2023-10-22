# Configuring Git Proxy

## Issue

In China, the speed of `git clone` and `git pull` is often too slow.

## Solution

### 1. Configuration within Proxy Software

1. In your proxy software, enable the option for "Allow connections from local network."
2. Take note of the port number (e.g., 1080).
3. Activate "Global Mode."

### 2. Configuring Global Git HTTP Proxy

```shell
git config --global http.proxy http://127.0.0.1:【Port Number】
git config --global https.proxy https://127.0.0.1:【Port Number】

# For example:
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy https://127.0.0.1:10808

# If the above doesn't work, try using the socks5 protocol:
git config --global http.proxy socks5://127.0.0.1:【Port Number】
git config --global https.proxy socks5://127.0.0.1:【Port Number】

# To proxy only GitHub without affecting domestic repositories (not recommended for those unfamiliar with configuration files):
git config --global http.https://github.com.proxy https://127.0.0.1:【Port Number】
git config --global https.https://github.com.proxy https://127.0.0.1:【Port Number】

# To proxy only GitLab without affecting domestic repositories (not recommended for those unfamiliar with configuration files):
git config --global https.https://https://gitlab.com.proxy https://127.0.0.1:1080
```

Configuration on Ubuntu:

```shell
git config --global http.https://github.com.proxy socks5://127.0.0.1:10808
```

### Viewing Configuration File Paths

```shell
git config --list --show-origin
```

### Reverting Changes

If you no longer wish to use the proxy, you can undo the changes using the following method:

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## References and Acknowledgments

- [**Overcoming the Slow Speed of Git Clone and Git Pull**](https://c.lanmit.com/czxt/Linux/16965.html)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.