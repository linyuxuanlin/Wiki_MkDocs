---
id: MSI主板开启虚拟化的方法
title: MSI 主板开启虚拟化的方法
---

## 重启进入 BIOS

```cmd
shutdown.exe /r /o
```

重启后，点击 `疑难解答（Troubleshoot）` - `自定义设置（Advanced options）` - `UEFI 固件设置（UEFI Firmware Settings）`，进入主板 BIOS

## 找到相关设置

1. `F7` 进入高级选项
2. 依次点击 `OC` - `CPU 特征（CPU Features）`
3. 找到 `SVM Mode / Intel Virtualization（视 CPU 而定）`

## 修改设置

把 `Disabled（禁用）` 修改为 `Enabled（启用）`

## 保存退出

按 `F10` 保存并退出

## 参考与致谢

- [如何进入 BIOS？](https://zhuanlan.zhihu.com/p/34223088)
- [微星（MSI）电脑、主板开启 VT 的方法](http://mumu.163.com/20181108/25905_784199.html)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

