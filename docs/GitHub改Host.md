---
id: GitHub改Host
title: GitHub 改 Host
---

## 问题

错误：`curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connection refused `

## 原因

国内 DNS 污染。

## 解决

在本机的 host 文件中添加：

```
199.232.68.133 raw.githubusercontent.com
199.232.68.133 user-images.githubusercontent.com
199.232.68.133 avatars2.githubusercontent.com
199.232.68.133 avatars1.githubusercontent.com
```

Host 路径:

- Windows: `C:\Windows\System32\drivers\etc`
- Linux: `/etc/hosts`

补一点 Linux 下的操作方法：

1. 打开终端
2. 输入命令：`vi /etc/hosts`
3. 按 `A` 切换到编辑模式
4. 在末尾添加上面的几句 Host 指向
5. 按 `Esc` 退出编辑，按 `:wq` 保存并退出

## 拓展

### 查询域名的 IP

使用 [**IPAddress**](https://www.ipaddress.com/)

## 参考与致谢

- [添加 Host 加速访问 github](https://yangshun.win/blogs/2b7abf4f/#%E4%BF%AE%E6%94%B9-host)

> 文章作者：**Power Lin**
> 原文地址：<https://wiki-power.com>
> 版权声明：文章采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议，转载请注明出处。
