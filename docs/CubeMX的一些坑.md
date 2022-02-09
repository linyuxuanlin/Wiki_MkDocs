---
id: CubeMX的一些坑
title: CubeMX 的一些坑
---

## 项目名称路径不能是中文

如题，新建项目的名称与路径，都必须是英文的，不然可能会出现奇奇怪怪的错误。

## 默认关闭调试端口

问题描述：

- 检测到 ST-Link，却检测不到板子，提示 `No target connected`
- 首次能成功下载，第二次及以后就不行了

原因：

- CubeMX 把调试端口给关了

解决方法（本次）：

- 用 **STM32 ST-LINK Utility** 工具，刷出厂程序救回来
- 或者用 [**这篇文章**](https://www.jianshu.com/p/cea16b641c3d) 提供的方法（通过 Keil）

解决方法（长远）：

- 在 CubeMX 的 SYS 设置中，将 Debug 选项更改为 Serial Wire（SW）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200531162352.jpg)

## 参考与致谢

- [STM32 调试器配置异常导致的问题与解决方法（一）](https://www.jianshu.com/p/cea16b641c3d)



> 文章作者：**Power Lin**  
> 原文地址：<https://wiki-power.com>  
> 版权声明：文章采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议，转载请注明出处。
