# Using PlatformIO with CubeMX

## Background

In the [**previous article**](https://wiki-power.com/PlatformIO—一站式嵌入式开发工具), we observed that PlatformIO offers a more elegant development experience compared to Keil. 
As we all know, in the world of STM32 development, the HAL library, in combination with the powerful tool CubeMX, is more convenient than the standard peripheral library. However, PlatformIO's official support for CubeMX is not entirely seamless, requiring an intermediary Python middleware for code conversion.

In this article, I will introduce a unique method to make PlatformIO work seamlessly with CubeMX for a delightful development experience.

## Project Initialization

TL;DR: I've placed the project folder created using the following steps in [**this repository**](https://github.com/linyuxuanlin/Template_of_PlatformIO_with_CubeMX). You can clone it directly.

### CubeMX Initialization Steps

1. Create a new project.
2. Choose the MCU model.
3. Configure Pinout & Configuration.
   1. Configure RCC (select external/internal clock, as needed).
   2. Configure SYS (change DEBUG option from `No Debug` to `Serial Wire` as necessary).
4. Configure Clock Configuration.
5. Configure Project Manager.
   1. Project Page
      1. Enter the project name (e.g., `Template_of_PlatformIO_with_CubeMX`).
      2. Modify the project path (e.g., `D:/Desktop`).
      3. Change the toolchain/IDE to `Other Toolchains`.
   2. Code Generator Page
      1. Choose the software package option (STM32Cube Firmware Library Package) as `Copy only the necessary library files`.
      2. Check the 'Generate peripheral initialization as a pair of '.c/.h' files per peripheral' in generated files options.

With the configuration completed, let's click on 'Generate Code' in the top right corner to generate the code.

### PlatformIO Initialization Steps

1. Open the PlatformIO main page.
2. Click on 'New Project' to create a new project.
   1. Enter the project name. Note: It must match the name configured in CubeMX (e.g., `Template_of_PlatformIO_with_CubeMX`).
   2. Select the board/MCU model. You can directly choose the MCU model (e.g., STM32F103C8) or the board type (e.g., BluePill F103C8). Note: It must match the configuration in CubeMX.
   3. Choose the code framework as `STM32Cube`.
   4. Uncheck 'Use default location' under the 'Location' path, and set a custom path. Note: It must match the configuration in CubeMX (e.g., `D:/Desktop`).
3. Open the `platformio.ini` file in your project and add the following lines:

   ```ini
   [platformio]
   include_dir=Inc
   src_dir=Src
   ```

   This is because PlatformIO and CubeMX generate framework folders differently. To ensure compatibility, we align with CubeMX.
4. You can delete the 'include' folder in your project. Since Windows file naming is not case-sensitive, the 'src' folder naturally becomes 'Src'.

### Enjoy your development journey!

In the project, `.c` files are located in the `Src` folder, while `.h` files are in the `Inc` folder.  
Any code between `/* USER CODE BEGIN */` and `/* USER CODE END */` will be preserved throughout the subsequent generation process from CubeMX and will not be overwritten.

You can use the following shortcuts in PlatformIO:
- Press `Ctrl + Alt + B` to compile.
- Use `Ctrl + Alt + U` to compile and upload.
- Press `F5` to start debugging.

The next step in your exploration is to learn about the HAL library. To be continued ~

## References and Acknowledgments

- [STM32CubeMX Series Tutorial 03 - Creating and Generating Code Projects](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B03_%E5%88%9B%E5%BB%BA%E5%B9%B6%E7%94%9F%E6%88%90%E4%BB%A3%E7%A0%81%E5%B7%A5%E7%A8%8B.html)
- [STM32CubeMX Series Tutorial 06 - Project Manager Detailed Explanation](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B06_Project%20Manager%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E5%99%A8%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E.html)
- [Using VS Code as an STM32 Development Platform (PlatformIO)](https://www.jianshu.com/p/49cfa03d6164)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.