---
id: ESXi初始化指南
title: ESXi 初始化指南
---

VMware ESXi 是一个可裸机安装的虚拟机管理器。本篇教程基于 ESXi 8，草稿阶段仍未发布。

可以先跟着这篇教程上手：[**『软路由踩坑指南』 篇二：ESXi 8.0 虚拟机必备知识与保姆级安装过程**](https://post.smzdm.com/p/a8x6o5on/p3/?sort_tab=hot/#comments)

进行至 `5.修改ESXI的默认空间` 这个地方时，改用以下方法，修改 ESXI 的默认空间大小。

### 减小 VMFSL 的占用

在点安装系统后 5 秒内，按 `Shift` + `O`，输入 `cdromBoot runweasel systemMediaSize=min`， 将虚拟内存配置到最小值。具体可参考官方文档 [**ESXi System Storage Overview**](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-474D003B-C6FB-465D-BC1B-5FD30F8E2209.html?hWord=N4IghgNiBcIM4E84BcCmBbAsqgJgSzAGU8AvVEAXyA#esxi-70-system-storage-links-2)。
