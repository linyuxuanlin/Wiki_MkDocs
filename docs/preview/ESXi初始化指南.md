---
id: ESXi初始化指南
title: ESXi 初始化指南
---

### 减小 VMFSL 的占用

在点安装系统后 5 秒内，按 `Shift` + `O`，输入 `cdromBoot runweasel systemMediaSize=min`， 将虚拟内存配置到最小值。具体可参考官方文档 [**ESXi System Storage Overview**](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-474D003B-C6FB-465D-BC1B-5FD30F8E2209.html?hWord=N4IghgNiBcIM4E84BcCmBbAsqgJgSzAGU8AvVEAXyA#esxi-70-system-storage-links-2)。
