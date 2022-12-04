---
id: 移除Chrome（Edge）由组织管理
title: 移除 Chrome（Edge） 由组织管理
---

## 步骤

1. `Win` + `R`，输入 `regedit` 打开注册表
2. 找到以下目录并删除它们

Chrome：

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome
HKEY_CURRENT_USER\SOFTWARE\Policies\Google\Chrome
```

Edge：

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge
HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Edge
```

## 参考与致谢 

- [Works! Fix Chrome (or Edge) is Managed by your Organization (in 3 steps!)](https://www.joshualowcock.com/guide/fix-chrome-is-managed-by-your-organization-in-3-steps/)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
