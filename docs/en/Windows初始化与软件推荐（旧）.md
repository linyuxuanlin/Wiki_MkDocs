# Windows Initialization and Software Recommendations (Old)

![](https://media.wiki-power.com/img/20210117142759.jpg)

> For updated content, please visit [**Personal Onboarding Workflow (Windows)**](https://wiki-power.com/Personal_Onboarding_Workflow_%28Windows%29/)

You've just installed a Windows operating system. What are the essential settings and software that you need?

## Personal Settings

- Do not use a Microsoft account for initialization.
- Enable diagnostics (required for preview versions of the system).
- Rename your computer.
- Go to Settings - Update & Security - Developer options and enable Developer mode.
- Activate Preview mode.
- [**Enhanced Performance**](https://bobi.site/archives/875)
- Install Synology Drive Client.
- Install [**Huorong Security**](https://www.huorong.cn/) (to prevent Windows Defender from deleting files erroneously).
- Log in to your Microsoft account.
- Activate Windows: [**HEU_KMS_Activator**](https://github.com/zbezj/HEU_KMS_Activator)
- Update the system and drivers.
- Configure your browser (Edge Canary).
  - Extensions
  - [**Enable Chrome (Edge) Multi-threaded Download**](https://wiki-power.com/%E5%BC%80%E5%90%AFChrome%EF%BC%88Edge%EF%BC%89%E5%A4%9A%E7%BA%BF%E7%A8%8B%E4%B8%8B%E8%BD%BD)
- User Account Control Settings: Set it to "Never notify."
- Customize the taskbar.
- Configure personalized settings.
- Configure display settings.
- Configure clipboard history and synchronization.
- Configure peripherals like mouse, touchpad, and keyboard.
- Enable GodMode: [GodMode](https://github.com/linyuxuanlin/File-host/tree/main/software/GodMode.lnk)
- Disable hibernation: `powercfg /hibernate off`
- [**Resolve Chinese Font Display Issues in English Environments**](https://blog.csdn.net/amoscn/article/details/106224359)

## Software Installation

- Work-related software
- [**VS Code insiders**](https://code.visualstudio.com/docs/?dv=win64&build=insiders)
  - Setting Sync
- [**Logitech Options**](https://www.logitech.com.cn/zh-cn/product/options): For Logitech mouse users (automatic pop-up for download and installation).
- [**Python**](https://www.microsoft.com/zh-cn/p/python-39/9p7qfqmjrfp7?rtc=1&activetab=pivot:overviewtab)
- [**WeChat (Beta)**](https://dldir1.qq.com/weixin/Windows/Beta/WeChatBeta.exe)
- [**Git**](https://git-scm.com/downloads)
- [winget](https://www.microsoft.com/zh-cn/p/app-installer/9nblggh4nns1?ocid=9nblggh4nns1_ORSEARCH_Bing&rtc=2&activetab=pivot:overviewtab)
  - Powertoys: `WinGet install powertoys`
- [**Modified QQ**](https://github.com/linyuxuanlin/File-host/blob/main/software/QQ%209.4.2.27666%20Lite-20210118%20by%20flighty-Q.exe)

- [**DiskGenius**](https://www.diskgenius.cn/download.php): Disk Utility

  - Reserve 10 GB of Free Space (SSD)
  - NTFS, 4096 Sectors (4k Alignment)

- [**KMS**](https://github.com/linyuxuanlin/File-host/tree/main/software/KMS.exe):

  - Activate Windows (No longer effective)
  - Disable Windows Defender

- [**GitHub Desktop**](https://desktop.github.com)

- [**Win10Apps**](https://github.com/linyuxuanlin/File-host/tree/main/software/Win10Apps.exe)
- [**Geek Uninstaller**](https://github.com/linyuxuanlin/File-host/tree/main/software/geekuninstaller.exe)
- [**Bandizip**](https://github.com/linyuxuanlin/File-host/tree/main/software/Bandizip.exe): Ad-free version
- [**Dism++**](https://www.chuyu.me/zh-Hans/): System utility
- [**JPEGView**](https://github.com/linyuxuanlin/File-host/tree/main/software/JPEGView64.zip)
- [**卡硬工具箱**](http://www.kbtool.cn/down.php)
- [**Mem Reduct**](https://github.com/henrypp/memreduct/releases)
- [**OInstall**](https://github.com/linyuxuanlin/File-host/tree/main/software/OInstall.exe): Office tool
- [**PowerToys**](https://github.com/microsoft/PowerToys/releases/)
- [**Snipaste**](https://zh.snipaste.com/download.html)
- [**SpaceSniffer**](https://github.com/linyuxuanlin/File-host/tree/main/software/SpaceSniffer.exe)
- [**Sumatra PDF**](https://www.sumatrapdfreader.org/download-free-pdf-viewer.html)
- [**PotPlayer**](https://daumpotplayer.com/download/)
- [**PicGo**](https://github.com/Molunerfinn/PicGo/releases/tag/v2.3.0-beta.4)
- [**Bamboo**](https://christopherwk210.github.io/bamboo/): Image compression software based on TinyPNG
- [**DeskGo**](https://pm.myapp.com/invc/xfspeed/qqpcmgr/data/DeskGo_2_9_1051_127_lite.exe): Desktop organization
- [**Wise Driver Care**](https://github.com/linyuxuanlin/File-host/blob/main/software/Wise%20Driver%20Care.zip): Driver installation and management tool
- [**NDM**](https://www.neatdownloadmanager.com/index.php/en/): Downloader
- [**AltDrag**](https://github.com/linyuxuanlin/File-host/tree/main/software/AltDrag.exe): Window dragging/scaling/opacity adjustment utility
- [**Raidrive**](https://github.com/linyuxuanlin/File-host/blob/main/software/raidrive-2020-6-80.exe): Tool for mounting remote drives (ad-free version). I use WebDAV to mount NAS as a local disk.

## Optional Software

- [**7-Zip**](https://github.com/linyuxuanlin/File-host/tree/main/software/7z.exe): Known for its high compression ratio.
- [**WPS Special Edition**](http://wpspro.support.wps.cn/gov/guangdong/chaozhou/installation/WPS%20Office%202019%20%E4%B8%93%E4%B9%A0%E7%89%88%EF%BC%88%E6%BD%AE%E5%B7%9E%E5%B8%82%E5%85%9A%E6%94%BF%E6%9C%BA%E5%85%B3%E5%8D%95%E4%BD%8D%EF%BC%89.exe): Ad-free and clean.
  - Alternate link: [https://pan.baidu.com/s/1d_DVwbLScESe1Zh7um6YTA](https://pan.baidu.com/s/1d_DVwbLScESe1Zh7um6YTA)
  - Extraction code: `y1xe`
- [**SoftDownloader**](https://github.com/linyuxuanlin/File-host/tree/main/software/SoftDownloader.zip): A one-click installer for most software.
- [**Office Master Suite**](https://github.com/linyuxuanlin/File-host/tree/main/software/OfficeBox.zip): A powerful collection of various office-related utilities.
- [**IObit Unlocker**](https://github.com/linyuxuanlin/File-host/tree/main/software/IObit_Unlocker.exe): A tool to unlock file occupation.
- [**EmptyFolderNuker**](https://github.com/linyuxuanlin/File-host/tree/main/software/EmptyFolderNuker.exe): A tool to detect and delete empty folders.

## References and Acknowledgments

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
