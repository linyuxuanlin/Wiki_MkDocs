# Windows Initialization and Software Recommendations (Old)

![Image](https://img.wiki-power.com/d/wiki-media/img/20210117142759.jpg)

> For updated information, please refer to [**Personal Onboarding Workflow (Windows)**](https://wiki-power.com/Personal_Onboarding_Workflow_%28Windows%29/)

You've just set up a Windows system. What are the essential settings and software to install?

## Personal Settings

- Do not use a Microsoft account for initialization.
- Enable diagnostics (required for preview builds).
- Rename the computer.
- Go to Settings - Update & Security - Developer options - and enable Developer Mode.
- Preview mode.
- [**Outstanding Performance**](https://bobi.site/archives/875).
- Install Synology Drive Client.
- Install [**360 Total Security**](https://www.huorong.cn/) (to prevent Windows Defender from mistakenly deleting files).
- Sign in with your Microsoft account.
- Activate Windows using [**HEU_KMS_Activator**](https://github.com/zbezj/HEU_KMS_Activator).
- Update the system and drivers.
- Configure the browser (Edge Canary).
  - Extensions.
  - [**Enable Multi-threaded Download in Chrome (Edge)**](https://wiki-power.com/%E5%BC%80%E5%90%AFChrome%EF%BC%88Edge%EF%BC%89%E5%A4%9A%E7%BA%BF%E7%A8%8B%E4%B8%8B%E8%BD%BD).
- User Account Control settings: Set it to "Never notify."
- Customize the taskbar.
- Configure personalization settings.
- Configure display settings.
- Configure clipboard history and synchronization.
- Configure mouse, touchpad, keyboard, and more.
- Enable hidden settings: [GodMode](https://github.com/linyuxuanlin/File-host/tree/main/software/GodMode.lnk).
- Disable hibernation: `powercfg /hibernate off`.
- [**Solve Chinese Font Display Issues in English Environments**](https://blog.csdn.net/amoscn/article/details/106224359).

## Software Installation

- Work-related software.
- [**VS Code insiders**](https://code.visualstudio.com/docs/?dv=win64&build=insiders)
  - Setting Sync.
- [**Logitech Options**](https://www.logitech.com.cn/zh-cn/product/options): For Logitech mouse (automatically prompts download and installation).
- [**Python**](https://www.microsoft.com/zh-cn/p/python-39/9p7qfqmjrfp7?rtc=1&activetab=pivot:overviewtab).
- [**WeChat (Beta)**](https://dldir1.qq.com/weixin/Windows/Beta/WeChatBeta.exe).
- [**Git**](https://git-scm.com/downloads).
- [winget](https://www.microsoft.com/zh-cn/p/app-installer/9nblggh4nns1?ocid=9nblggh4nns1_ORSEARCH_Bing&rtc=2&activetab=pivot:overviewtab).
  - Powertoys: `WinGet install powertoys`.
- [**Modified QQ**](https://github.com/linyuxuanlin/File-host/blob/main/software/QQ%209.4.2.27666%20Lite-20210118%20by%20flighty-Q.exe).

- [**DiskGenius**](https://www.diskgenius.cn/download.php): Disk Management Tool
  - Reserve 10 GB of Free Space (SSD)
  - NTFS, 4096 Sectors (4k Alignment)
- [**KMS**](https://github.com/linyuxuanlin/File-host/tree/main/software/KMS.exe):

  - Activate Windows (No Longer Functional)
  - Disable Windows Defender

- [**GitHub Desktop**](https://desktop.github.com)

- [**Win10Apps**](https://github.com/linyuxuanlin/File-host/tree/main/software/Win10Apps.exe): A handy application for Windows 10.
- [**Geek Uninstaller**](https://github.com/linyuxuanlin/File-host/tree/main/software/geekuninstaller.exe): Uninstall software with ease.
- [**Bandizip**](https://github.com/linyuxuanlin/File-host/tree/main/software/Bandizip.exe): Ad-free version of Bandizip.
- [**Dism++**](https://www.chuyu.me/zh-Hans/): System utility tool.
- [**JPEGView**](https://github.com/linyuxuanlin/File-host/tree/main/software/JPEGView64.zip): Image viewer and editor.
- [**卡硬工具箱**](http://www.kbtool.cn/down.php): A toolbox for various tasks.
- [**Mem Reduct**](https://github.com/henrypp/memreduct/releases): Memory optimization tool.
- [**OInstall**](https://github.com/linyuxuanlin/File-host/tree/main/software/OInstall.exe): Office tool for installation.
- [**PowerToys**](https://github.com/microsoft/PowerToys/releases/): Windows power utilities.
- [**Snipaste**](https://zh.snipaste.com/download.html): Screenshot and annotation tool.
- [**SpaceSniffer**](https://github.com/linyuxuanlin/File-host/tree/main/software/SpaceSniffer.exe): Disk space analyzer.
- [**Sumatra PDF**](https://www.sumatrapdfreader.org/download-free-pdf-viewer.html): PDF viewer.
- [**PotPlayer**](https://daumpotplayer.com/download/): Multimedia player.
- [**PicGo**](https://github.com/Molunerfinn/PicGo/releases/tag/v2.3.0-beta.4): Image compression tool based on TinyPNG.
- [**Bamboo**](https://christopherwk210.github.io/bamboo/): Image compression software using TinyPNG.
- [**DeskGo**](https://pm.myapp.com/invc/xfspeed/qqpcmgr/data/DeskGo_2_9_1051_127_lite.exe): Desktop organization tool.
- [**Wise Driver Care**](https://github.com/linyuxuanlin/File-host/blob/main/software/Wise%20Driver%20Care.zip): Driver installation and management tool.
- [**NDM**](https://www.neatdownloadmanager.com/index.php/en/): Download manager.
- [**AltDrag**](https://github.com/linyuxuanlin/File-host/tree/main/software/AltDrag.exe): Utility for window dragging, resizing, and transparency adjustments.
- [**Raidrive**](https://github.com/linyuxuanlin/File-host/blob/main/software/raidrive-2020-6-80.exe): Tool for mounting remote hard drives (ad-free version). I use it to mount NAS as a local disk via WebDAV.

## Optional Software

- [**7-Zip**](https://github.com/linyuxuanlin/File-host/tree/main/software/7z.exe): High compression ratio.
- [**WPS Special Edition**](http://wpspro.support.wps.cn/gov/guangdong/chaozhou/installation/WPS%20Office%202019%20%E4%B8%93%E4%B9%A0%E7%89%88%EF%BC%88%E6%BD%AE%E5%B7%9E%E5%B8%82%E5%85%9A%E6%94%BF%E6%9C%BA%E5%85%B3%E5%8D%95%E4%BD%8D%EF%BC%89.exe): Ad-free and lightweight.
  - Alternate link: [https://pan.baidu.com/s/1d_DVwbLScESe1Zh7um6YTA](https://pan.baidu.com/s/1d_DVwbLScESe1Zh7um6YTA)
  - Extraction code: `y1xe`
- [**SoftDownloader**](https://github.com/linyuxuanlin/File-host/tree/main/software/SoftDownloader.zip): A tool to find and install most software with a single click.
- [**万彩办公大师**](https://github.com/linyuxuanlin/File-host/tree/main/software/OfficeBox.zip): A powerful collection of office-related utilities.
- [**IObit Unlocker**](https://github.com/linyuxuanlin/File-host/tree/main/software/IObit_Unlocker.exe): File unlocking tool for resolving file occupation issues.
- [**EmptyFolderNuker**](https://github.com/linyuxuanlin/File-host/tree/main/software/EmptyFolderNuker.exe): A tool for detecting and deleting empty folders.

## References and Acknowledgments

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.