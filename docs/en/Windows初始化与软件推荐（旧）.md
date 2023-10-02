# Windows Initialization and Software Recommendations (Old)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210117142759.jpg)

> For updated information, please refer to [**Personal Onboarding Workflow (Windows)**](https://wiki-power.com/Personal_Onboarding_Workflow_%28Windows%29/)

You just installed a Windows system, what are the necessary settings and software to install?

## Some Personal Settings

- Do not use a Microsoft account for initialization
- Enable diagnostics (required for preview versions)
- Rename the computer name
- Settings - Update & Security - Developer options - Enable developer mode
- Preview mode
- [**Excellent Performance**](https://bobi.site/archives/875)
- Install Synology Drive Client
- Install [**Huorong Security**](https://www.huorong.cn/) (to prevent Windows Defender from deleting files)
- Log in to Microsoft account
- Activate Windows: [**HEU_KMS_Activator**](https://github.com/zbezj/HEU_KMS_Activator)
- Update system and drivers
- Configure browser (Edge Canary)
  - Extensions
  - [**Enable Chrome (Edge) multi-threaded download**](https://wiki-power.com/%E5%BC%80%E5%90%AFChrome%EF%BC%88Edge%EF%BC%89%E5%A4%9A%E7%BA%BF%E7%A8%8B%E4%B8%8B%E8%BD%BD)
- User Account Control Settings: Set to Never Notify
- Customize taskbar
- Configure personalization settings
- Configure display settings
- Configure clipboard history and synchronization
- Configure mouse touchpad keyboard, etc.
- Enable hidden settings: [GodMode](https://github.com/linyuxuanlin/File-host/tree/main/software/GodMode.lnk)
- Disable hibernation: `powercfg /hibernate off`
- [**Solve the problem of Chinese font display in English environment**](https://blog.csdn.net/amoscn/article/details/106224359)

## Software Installation

- Work Software
- [**VS Code insiders**](https://code.visualstudio.com/docs/?dv=win64&build=insiders)
  - Setting Sync
- [**Logitech Options**](https://www.logitech.com.cn/zh-cn/product/options): For Logitech mouse (automatically pops up download and installation)
- [**Python**](https://www.microsoft.com/zh-cn/p/python-39/9p7qfqmjrfp7?rtc=1&activetab=pivot:overviewtab)
- [**WeChat (Beta)**](https://dldir1.qq.com/weixin/Windows/Beta/WeChatBeta.exe)
- [**Git**](https://git-scm.com/downloads)
- [winget](https://www.microsoft.com/zh-cn/p/app-installer/9nblggh4nns1?ocid=9nblggh4nns1_ORSEARCH_Bing&rtc=2&activetab=pivot:overviewtab)
  - Powertoys: `WinGet install powertoys`
- [**Modified QQ**](https://github.com/linyuxuanlin/File-host/blob/main/software/QQ%209.4.2.27666%20Lite-20210118%20by%20flighty-Q.exe)

- [**DiskGenius**](https://www.diskgenius.cn/download.php): Disk tool
  - Reserve 10 GB of free space (SSD)
  - NTFS, 4096 sectors (4k alignment)
- [**KMS**](https://github.com/linyuxuanlin/File-host/tree/main/software/KMS.exe):

  - Activate Windows (no longer effective)
  - Disable Windows Defender

- [**GitHub Desktop**](https://desktop.github.com)

- [**Win10Apps**](https://github.com/linyuxuanlin/File-host/tree/main/software/Win10Apps.exe)
- [**Geek Uninstaller**](https://github.com/linyuxuanlin/File-host/tree/main/software/geekuninstaller.exe)
- [**Bandizip**](https://github.com/linyuxuanlin/File-host/tree/main/software/Bandizip.exe): Ad-free version
- [**Dism++**](https://www.chuyu.me/zh-Hans/): System tool
- [**JPEGView**](https://github.com/linyuxuanlin/File-host/tree/main/software/JPEGView64.zip)
- [**Card Hard Toolbox**](http://www.kbtool.cn/down.php)
- [**Mem Reduct**](https://github.com/henrypp/memreduct/releases)
- [**OInstall**](https://github.com/linyuxuanlin/File-host/tree/main/software/OInstall.exe): Office tool
- [**PowerToys**](https://github.com/microsoft/PowerToys/releases/)
- [**Snipaste**](https://zh.snipaste.com/download.html)
- [**SpaceSniffer**](https://github.com/linyuxuanlin/File-host/tree/main/software/SpaceSniffer.exe)
- [**Sumatra PDF**](https://www.sumatrapdfreader.org/download-free-pdf-viewer.html)
- [**PotPlayer**](https://daumpotplayer.com/download/)
- [**PicGo**](https://github.com/Molunerfinn/PicGo/releases/tag/v2.3.0-beta.4)
- [**Bamboo**](https://christopherwk210.github.io/bamboo/): Image compression software based on TinyPNG
- [**DeskGo**](https://pm.myapp.com/invc/xfspeed/qqpcmgr/data/DeskGo_2_9_1051_127_lite.exe): Desktop organizer
- [**Wise Driver Care**](https://github.com/linyuxuanlin/File-host/blob/main/software/Wise%20Driver%20Care.zip): Driver installation and management tool
- [**NDM**](https://www.neatdownloadmanager.com/index.php/en/): Downloader
- [**AltDrag**](https://github.com/linyuxuanlin/File-host/tree/main/software/AltDrag.exe): Window drag / resize / change transparency small tool
- [**Raidrive**](https://github.com/linyuxuanlin/File-host/blob/main/software/raidrive-2020-6-80.exe): Tool for mounting remote hard drives (ad-free version). I use it to mount my NAS as a local disk via WebDAV.

## Optional software

- [**7-Zip**](https://github.com/linyuxuanlin/File-host/tree/main/software/7z.exe): High compression ratio
- [**WPS Special Edition**](http://wpspro.support.wps.cn/gov/guangdong/chaozhou/installation/WPS%20Office%202019%20%E4%B8%93%E4%B8%9A%E7%89%88%EF%BC%88%E6%BD%AE%E5%B7%9E%E5%B8%82%E5%85%9A%E6%94%BF%E6%9C%BA%E5%85%B3%E5%8D%95%E4%BD%8D%EF%BC%89.exe): Clean and ad-free
  - Alternate link: https://pan.baidu.com/s/1d_DVwbLScESe1Zh7um6YTA
  - Extraction code: `y1xe`
- [**SoftDownloader**](https://github.com/linyuxuanlin/File-host/tree/main/software/SoftDownloader.zip): Can find most software and install with one click
- [**OfficeBox**](https://github.com/linyuxuanlin/File-host/tree/main/software/OfficeBox.zip): Powerful collection of small tools related to office work
- [**IObit Unlocker**](https://github.com/linyuxuanlin/File-host/tree/main/software/IObit_Unlocker.exe): Tool for unlocking files that are in use
- [**EmptyFolderNuker**](https://github.com/linyuxuanlin/File-host/tree/main/software/EmptyFolderNuker.exe): Tool for detecting and deleting empty folders

## References and Acknowledgments

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.