---
id: ESXi初始化指南
title: ESXi 初始化指南
---

VMware ESXi 是一个可裸机安装的虚拟机管理器。本篇教程基于 ESXi 8，仍在草稿阶段。

可以先跟着这篇教程上手：[**『软路由踩坑指南』 篇二：ESXi 8.0 虚拟机必备知识与保姆级安装过程**](https://post.smzdm.com/p/a8x6o5on/p3/?sort_tab=hot/#comments)

进行至 `5.修改ESXI的默认空间` 这个地方时，改用以下方法，修改 ESXI 的默认空间大小。

### 减小 VMFSL 的占用

在点安装系统后 5 秒内，按 `Shift` + `O`，输入 `cdromBoot runweasel systemMediaSize=min`， 将虚拟内存配置到最小值。具体可参考官方文档 [**ESXi System Storage Overview**](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-474D003B-C6FB-465D-BC1B-5FD30F8E2209.html?hWord=N4IghgNiBcIM4E84BcCmBbAsqgJgSzAGU8AvVEAXyA#esxi-70-system-storage-links-2)。

### Windows 11 虚拟机的安装

Win11 对系统配置比较严苛，安装的时候可能会出现 `这台电脑无法运行Windows 11`。一般问题来自于 TPM 检查，可以通过以下的方法避开：

1. 在虚拟机的初始化页面，启用 `Windows 基于虚拟化的安全性`。
2. 在进入 Windows 虚拟机后的 `现在安装` 页面，按快捷键 `Shift` + `F10` 启动 cmd 窗口（如果调出 cmd 界面，有可能是笔记本的键盘键位问题，可以尝试外接一个键盘）。
3. 输入 regedit，打开注册表。在 `HKEY_LOCAL_MACHINE\SYSTEM\Setup` 路径下，创建两个 32 位的 DWORD 值：
   - `BypassTPMCheck`，数值为 16 进制 `1`。
   - `BypassSecureBootCheck`，数值为 16 进制 `1`。

如果仍然无法安装，可以尝试检查其他的条件。可能是有一些条件达不到要求，比如 1GHz 以上的主频、64GB 以上的磁盘空间、4G 以上的内存。具体可参考 [**System requirements**](https://www.microsoft.com/en-us/windows/windows-11-specifications?r=1)。
