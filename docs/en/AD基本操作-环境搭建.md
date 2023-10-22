# AD Basic Operations - Environment Setup

— Altium Designer Tutorial Series

## Background

This tutorial series is based on Altium Designer 19 (also compatible with 20), and I will keep it updated for future versions.

## Software Download

Simply refer to the [**Altium Designer 2020 Installation Tutorial**](https://mp.weixin.qq.com/s?__biz=MzIwMjE1MjMyMw==&mid=502718968&idx=1&sn=4c37dc403171ffad01fca95b5a537b2e&chksm=0ee141143996c8021799bb5bf5407b7b56c2d7fa5dc484bda61893efd74a06a1f6be63a7a35e&scene=20&xtrack=1&key=088e5814bbd70a9bf7fb42111d02cbb81bb55981baea77169d867e2871add46f26dccde79326a96e819591677be92412fc05ff2af437922652dfe7ae1b94dc8172f36186ba0b2b460004027131ceae2c&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=62090523&lang=zh_CN&exportkey=AyOYwgP948kprM0EiAGMcyk%3D&pass_ticket=6jBDTE0Qqg%2BrAl1wrTIo2UeJLmUrtbfUKPpgRGdeqhwXUk8QVkc%2Fyekd3BvlvVsB). I won't go into details here.

## Adjusting Settings

To do a good job, you need good tools. When you first open Altium Designer, you can adjust some settings to make the tool more user-friendly. Find the **gear icon** in the top right corner and **open the settings page**, then follow the steps below.

### Set to Chinese Language

1. On the left panel, click on the **System - General** tab. Under the **Localization** section, check the **Use localized resources** option.
2. Click **Apply** to save the settings and restart Altium Designer.

### PCB Editor

1. Click on the **PCB Editor** tab on the left panel.
2. Under the **PCB Editor** tab, click on the **General** section. Under the **Copper Pour Rebuild** section, check **Rebuild copper after modification**. In the **Document Format Change Report** section, check **Disable open old version reports** and **Disable open new version reports**. In the **Other** section, change the **Cursor Type** to **Large 90**.
3. Click on the **Display** tab. Under the **Highlight Options** section, check **Apply highlight during interactive editing**.
4. Click on the **Board Insight Color Overrides** tab. Under the **Basic Style** section, select **Solid (Override Color)**.
5. Click on the **DRC Violations Display** tab. Under the **Conflict Overlay Style** section, select **Solid (Overlay Color)**.
6. Click **Apply** to save the settings and restart Altium Designer.

### Panels

1. Close the settings page and in the main menu, choose **View - Panels** and select **Components, Messages**.
2. Click the **paperclip icon** in the top right of the pop-up panel to dock the panel on the right side.

### Set Background to Grid

1. Open any PCB file (if you don't have one, create a new one).
2. Press **Ctrl + G** to open the grid settings window.
3. Under the **Display** section, set both **Fine** and **Coarse** options to **Dots**.

## Input Method Compatibility

If you can't use shortcuts, check if you are in English input mode (the input method status bar shows **ENG**). If you don't have this option, follow the steps below:

1. Open the **Control Panel**, then navigate to the **Clock, Language, and Region - Language** section.
2. Click the **Add a language** button, add **English**, and select **English (United States)**.
3. You can switch input methods from the desktop taskbar.

## Summary

In this chapter, we have configured the environment for Altium Designer, and now you can start designing your boards with ease.

## References and Acknowledgments

- [Altium Company's Altium Designer Section](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.