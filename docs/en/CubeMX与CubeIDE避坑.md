# Tips for Using CubeMX and CubeIDE

## Project Names and Paths Should Not Contain Chinese Characters

As mentioned, it's essential that the project name and path are in English. Otherwise, you might encounter peculiar errors.

## Default Debug Port Deactivation

Issue description:

- ST-Link is detected, but the target board is not recognized, showing `No target connected`.
- It works the first time but fails in subsequent attempts.

Reason:

- CubeMX deactivates the debug port.

Immediate Solution:

- Use the **STM32 ST-LINK Utility** tool to restore the factory program.
- Alternatively, follow the method provided in [**this article**](https://www.jianshu.com/p/cea16b641c3d) (via Keil).

Long-term Solution:

- In CubeMX's SYS settings, change the Debug option to Serial Wire (SW).

![Debug Option](https://media.wiki-power.com/img/20200531162352.jpg)

## Garbled Chinese Comments in STM32CubeIDE

If your code is imported from Keil, ensure that the original encoding is GB2312.

Navigate to the menu bar - `Window` - `Preferences` - `General` - `Appearance` - `Colors and Fonts` - `C/C++` - `Editor` - `C/C++ Editor Text Font`. Click on `Edit` on the right, confirm that the font supports Chinese (e.g., Microsoft YaHei), and ensure the script is set to `Chinese GB2312`.

If the issue persists, right-click on the project name in the left file tree, click on the last option, `Properties`, and change the font encoding to `GBK` in the `Resource` panel (if not available, simply type it). Save to resolve the issue.

## Enabling Chinese Language Support in STM32CubeIDE

Visit the link **<http://mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/>** and navigate to the latest data directory (e.g., I chose `mirrors.ustc.edu.cn/eclipse/technology/babel/update-site/`) and copy this link.

In STM32CubeIDE, go to the menu bar, select `Help` - `Install New Software`, click `Add`, and enter `language` for the `Name` field. For the `Location`, paste the link you copied earlier. Then click Add. In the pop-up window, select the Simplified Chinese language pack and install it. Follow the prompts to restart the software.

## References and Acknowledgments

- [Problem and Solution for STM32 Debugger Configuration Abnormalities (Part 1)](https://www.jianshu.com/p/cea16b641c3d)
- [STM32cubeIDE Environment Configuration, Installation, Chinese Localization, and Theme Setup](https://blog.csdn.net/wct3344142/article/details/104142863)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
