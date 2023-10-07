# Avoiding Pitfalls with CubeMX and CubeIDE

## Project Names and Paths Cannot be in Chinese

As the title suggests, the names and paths of newly created projects must be in English, otherwise strange errors may occur.

## Debug Port is Disabled by Default

Problem Description:

- ST-Link is detected, but the board is not detected, prompting "No target connected"
- The first download is successful, but subsequent downloads fail

Reason:

- CubeMX disables the debug port

Solution (for this time):

- Use the **STM32 ST-LINK Utility** tool to flash the factory program and recover
- Or use the method provided in [**this article**](https://www.jianshu.com/p/cea16b641c3d) (via Keil)

Long-term Solution:

- In the SYS settings of CubeMX, change the Debug option to Serial Wire (SW)

![](https://f004.backblazeb2.com/file/wiki-media/img/20200531162352.jpg)

## Chinese Comments in STM32CubeIDE are Garbled

If the code is imported from Keil, make sure the original encoding is GB2312.

Click on the menu bar in order - `Window` - `Preferences` - `General` - `Apperance` - `Colors and Fonts` - `C/C++` - `Editor` - `C/C++ Editor Text Font`, click `Edit` on the right, confirm that the font supports Chinese (such as Microsoft YaHei), and confirm that the script is `Chinese GB2312`.

If the problem still persists, right-click on the project name in the left file tree, click on the last property `Properties`, and change the font encoding in the `Resource` panel to `GBK` (if there is no option, simply enter it), and save to solve the problem.

## STM32CubeIDE Localization

Open the link **<http://mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/>**, select the latest data directory (for example, I can choose `mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/`), and copy this address link.

In STM32CubeIDE, select `Help` - `Install New Software` from the menu bar, click `Add`, fill in `language` in the `Name` field, fill in the link that was just copied in the `Location` field, and then click `Add`. In the pop-up window, select the Simplified Chinese language pack, install it, and restart the software as prompted.

## References and Acknowledgments

- [STM32 Debugger Configuration Issues and Solutions (Part 1)](https://www.jianshu.com/p/cea16b641c3d)
- [STM32cubeIDE Environment Configuration Installation-Chinese Localization-Theme Setting](https://blog.csdn.net/wct3344142/article/details/104142863)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.