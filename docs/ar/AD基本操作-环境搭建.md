# AD Basic Operations - Environment Setup

- Altium Designer Tutorial Series

## Background

This tutorial series is based on Altium Designer 19 (also compatible with 20), and I will also keep up with future versions.

## Software Download

Refer to the [**Altium Designer 2020 Installation Tutorial**](https://mp.weixin.qq.com/s?__biz=MzIwMjE1MjMyMw==&mid=502718968&idx=1&sn=4c37dc403171ffad01fca95b5a537b2e&chksm=0ee141143996c8021799bb5bf5407b7b56c2d7fa5dc484bda61893efd74a06a1f6be63a7a35e&scene=20&xtrack=1&key=088e5814bbd70a9bf7fb42111d02cbb81bb55981baea77169d867e2871add46f26dccde79326a96e819591677be92412fc05ff2af437922652dfe7ae1b94dc8172f36186ba0b2b460004027131ceae2c&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=62090523&lang=zh_CN&exportkey=AyOYwgP948kprM0EiAGMcyk%3D&pass_ticket=6jBDTE0Qqg%2BrAl1wrTIo2UeJLmUrtbfUKPpgRGdeqhwXUk8QVkc%2Fyekd3BvlvVsB) for software download. No further explanation is needed here.

## Adjust Settings

To do a good job, one must first sharpen one's tools. The first time you open Altium Designer, you can adjust some settings to make the tool more user-friendly. Find the **gear** icon in the upper right corner, **open the settings page**, and continue with the following steps.

### Set to Chinese

1. Click the **System - General** tab in the left column, and check the **Use localized resources** option under **Localization**.
2. Click **Apply** to save the settings and restart Altium Designer.

### PCB Editor

1. Click the **PCB Editor** tab in the left column.
2. Under **PCB Editor**, click the **General** tab, check **Automatically repour copper after modification** under **Copper Pour Rebuild**, check **Disable opening old version reports** and **Disable opening new version reports** under **Document Format Modification Report**, and change **Cursor Type** to **Large 90** under **Other**.
3. Click the **Display** tab, check **Apply Highlight During Interactive Editing** under **Highlight Options**.
4. Click the **Board Insight Color Overrides** tab, select **Solid (Overlay Color)** under **Basic Style**.
5. Click the **DRC Violations Display** tab, select **Solid (Overlay Color)** under **Conflict Overlay Style**.
6. Click **Apply** to save the settings and restart Altium Designer.

### Panels

1. Close the settings page, select **View - Panels** in the main menu bar, and click **Components, Messages** in order.
2. Click the **Paperclip** icon in the upper right corner of the pop-up panel to dock the panel on the right.

### Set Background to Grid

1. Open any PCB file (if there is none, create a new one).
2. Press **Ctrl + G** to open the grid settings window.
3. Under **Display**, set both the **Fine** and **Coarse** tabs to **Dots**.

## Input Method Compatibility

If you cannot use keyboard shortcuts, check if you have switched to English mode (the input method status bar displays **ENG**). If this option is not available, follow these steps:

1. افتح لوحة التحكم وانتقل إلى صفحة اللغة في الساعة واللغة والمنطقة.
2. انقر على زر "إضافة لغة" وأضف اللغة الإنجليزية واختر الإنجليزية (الولايات المتحدة).
3. يمكنك التبديل بين لغات الإدخال في شريط المهام على سطح المكتب.

## الخلاصة

في هذا الفصل ، قمنا بتكوين بيئة Altium Designer الأساسية ، ويمكننا الآن البدء في رسم الدوائر بسعادة :)

## المراجع والشكر

- [Altium Designer Column by Altium Company](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.