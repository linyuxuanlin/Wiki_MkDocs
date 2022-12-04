---
id: AltiumDesigner安装库文件
title: Altium Designer 安装库文件
---

1. 将库文件全部 **拷贝** 至软件对应的 **Shared\Library** 文件夹下；
2. 打开 Altium Designer ，在右侧面板点击 **Components** 页面，点击右上角 **三条杠** 标志，点击 **File-based Library Preferences** 选项，点击 **已安装** 页面，点击 **安装** 按钮，安装对应的库文件；
3. 几种特殊情况：
   - 嘉立创集成库的路径位于 **JLCSMT_LIB\Project Outputs for Miscellaneous Devices LC** 文件夹内；
   - 若第三方库文件非 **集成库（.IntLib）**，而是 **原理图库（SchLib）** 或 **封装库（PcbLib）** 的形式，则需 **同时安装** 以上两个文件。此时需要在安装库文件时弹出的路径选择窗口右侧点击下拉框切换 **All Files\(\*.\*\)** 通配符，否则只能看到 **.Intlib** 格式的文件。



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

