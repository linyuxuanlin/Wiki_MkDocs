---
id: 避免Chrome（Edge）强制转换HTTPS
title: 避免 Chrome（Edge）强制转换 HTTPS
---

有些网站只能用 http 访问，但有时候浏览器会强制转换为 https，导致访问错误。以下步骤将展示如何禁用浏览器的自动转换。

## 操作步骤

在地址栏输入链接并回车：

- Chrome：`chrome://net-internals/#hsts`
- Edge：`edge://net-internals/#hsts`

在 `Delete domain security policies` 栏，将你不需要自动转换的链接填进。比如，我要求 `wiki-power.com` 不被强制转换为 https 访问，则填入 `wiki-power.com` 然后点击 `Delete` 删除即可。

随后在地址栏输入链接并回车：

- Chrome：`chrome://flags/#edge-automatic-https`
- Edge：`edge://flags/#edge-automatic-https`

将 `Automatic HTTPS` 选项的 `Default` 改为 `Disabled`，并重启浏览器。

## 参考与致谢

- [Edge 或谷歌浏览器输入 http 的网址被强制转化为 https，手工修改为 http 都无效](https://blog.csdn.net/Thinker001/article/details/117717690)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
