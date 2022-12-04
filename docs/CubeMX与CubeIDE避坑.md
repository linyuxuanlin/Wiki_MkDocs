---
id: CubeMX与CubeIDE避坑
title: CubeMX 与 CubeIDE 避坑
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

## STM32CubeIDE 中文注释乱码

如果代码是从 Keil 导入的，需要先确保原本的编码是 GB2312。

依次点击菜单栏 - `Window` - `Preferences` - `General` - `Apperance` - `Colors and Fonts` - `C/C++` - `Editor` - `C/C++ Editor Text Font`，点击右侧的 `Edit`，确认字体支持中文（如微软雅黑），并确认脚本为 `中文 GB2312`。

如果还是没有解决，那么可以在左侧文件树中，右键项目名称，点击最后的属性 `Properties`，将 `Resource` 面板中的字体编码改为 `GBK`（如果没得选，直接输入即可），保存即可解决。

## STM32CubeIDE 汉化

打开链接 **<http://mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/>** ，点选到最新的数据目录下（比如我可选的是 `mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/`），复制此地址链接。

在 STM32CubeIDE 菜单栏选择 `Help` - `Install New Software`，点击 `Add`，在 `Name` 栏填入 `language`；`Location` 栏填入刚刚复制的链接，然后点击添加，在弹出来的界面选择简体中文语言包，安装后按提示重启软件即可。

## 参考与致谢

- [STM32 调试器配置异常导致的问题与解决方法（一）](https://www.jianshu.com/p/cea16b641c3d)
- [STM32cubeIDE 环境配置安装-汉化-主题设置](https://blog.csdn.net/wct3344142/article/details/104142863)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

