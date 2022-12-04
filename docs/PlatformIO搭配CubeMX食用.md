---
id: PlatformIO搭配CubeMX食用
title: PlatformIO 搭配 CubeMX 食用
---

## 背景

在 [**上一篇文章**](https://wiki-power.com/PlatformIO—一站式嵌入式开发工具) 中，我们可以看到，PlatformIO 用起来比 Keil 优雅多了。  
众所周知，STM32 打开方式中，HAL 库比标准库更方便易用（配合神器 CubeMX），但 PlatformIO 官方对 CubeMX 的兼容不是特别完美（需通过 Python 中间件来进行代码转换）

在这篇文章中，我将介绍一种独特的方法，让 PlatformIO 配合 CubeMX 食用起来更加美味。

## 初始化项目

太长不看：我把以下步骤创建的项目文件夹放在 [**这个仓库**](https://github.com/linyuxuanlin/Template_of_PlatformIO_with_CubeMX)，直接克隆即可。

### CubeMX 的初始化操作

1. 新建项目
2. 选择 MCU 型号
3. 配置 Pinout & Configuration
   1. 配置 RCC（选外部 / 内部时钟，视情况可略）
   2. 配置 SYS（将 DEBUG 选项由 `No Debug` 修改为 `Serial Wire`）
4. 配置 Clock Configuration
5. 配置 Project Manager
   1. Project 页面
      1. 填写项目名称 （Project Name） e.g. `Template_of_PlatformIO_with_CubeMX`
      2. 修改项目路径 （Project Location） e.g. `D:/Desktop`
      3. 将工具链（Toolchain / IDE）修改为 `Other Toolchains`
   2. Code Generator 页面
      1. 将软件包选项（STM32Cube Firmware Library Package）选择为 `Copy only the necessary library files`
      2. 在文件生成选项（Generated files）勾选 `Generate peripheral initialization as a pair of '.c/.h' files per peripheral`

终于配置完成了，我们点击右上角 `Generate Code` 生成代码吧。

### PlatformIO 的初始化操作

1. 打开 PlatformIO 的主页
2. 点击 `New Project` 新建工程
   1. 填写工程的名字。注意：一定要与 CubeMX 中配置的相同！（e.g. `Template_of_PlatformIO_with_CubeMX`）
   2. 选择板子 / MCU 型号。这儿可以直接选择 MCU 的型号（e.g. STM32F103C8），也可以直接选择版型（e.g. BluePill F103C8）。注意：一定要与 CubeMX 中配置的相同！
   3. 代码框架 `Framework` 选择 `STM32Cube`
   4. 将路径 `Location` 下 `Use default location` 取消掉，我们自定义路径。注意：一定要与 CubeMX 中配置的相同！（e.g. `D:/Desktop`）
3. 打开项目中 `platformio.ini` 文件，添加如下几行：

   ```ini
   [platformio]
   include_dir=Inc
   src_dir=Src
   ```

   这里是因为 PlatformIO 与 CubeMX 默认生成的框架文件夹不一样，为了兼容性，我们顺从 CubeMX.

4. 可以将项目中的 `include` 文件夹删了。而因为 Windows 文件命名不区分大小写，所以 `src` 文件夹顺理成章变为 `Src`.

### 尽情享用吧！

项目中， `.c` 存放于 `Src` 文件夹中，`.h` 在 `Inc` 中。  
只要在 `/* USER CODE BEGIN */` 与 `/* USER CODE END */` 之间的代码，后续从 CubeMX 生成的过程中，都将得以保留，不会被覆盖掉。

PlatformIO 可以用快捷键 `Ctrl + Alt + B` 编译，用 `Ctrl + Alt + U` 编译并上传，按 `F5` 开启调试。

接下来的探索，就是 HAL 库的学习了。未完待续 ~

## 参考与致谢

- [STM32CubeMX 系列教程 03\_创建并生成代码工程](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B03_%E5%88%9B%E5%BB%BA%E5%B9%B6%E7%94%9F%E6%88%90%E4%BB%A3%E7%A0%81%E5%B7%A5%E7%A8%8B.html)
- [STM32CubeMX 系列教程 06_Project Manager 工程管理器详细说明](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B06_Project%20Manager%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E5%99%A8%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E.html)
- [用 VS Code 作为 STM32 开发平台（PlatformIO）](https://www.jianshu.com/p/49cfa03d6164)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

