# Winget Install Commands

https://github.com/microsoft/winget-cli/releases

- 列出已安装软件：`winget list`
- 查看软件包详细信息：`winget show <package_name>`
- 搜索软件：`winget search <package_name>`
- 安装软件：`winget install <package_name>`
- 升级软件：`winget upgrade <package_name>`
  - 列出可升级的软件包: `winget upgrade`
  - 升级所有软件包：`winget upgrade --all`
- 卸载软件：`winget uninstall <package_name>`

## 系统工具

```powershell
winget install Anysphere.Cursor                    # 大模型辅助编程工具
winget install Docker.DockerDesktop                # Docker 工具
#winget install Microsoft.WindowsTerminal.Preview  # 一个现代化的终端应用，支持多标签、分屏等功能
winget install Microsoft.PowerToys                 # 一系列实用工具，增强 Windows 用户体验
#winget install Dell.DisplayManager                # 戴尔显示器管理软件，优化显示器设置
winget install Bitwarden.Bitwarden                 # 密码管理工具
winget install XPDNH1FMW7NB40                      # 火绒安全
```

## 文件管理

```powershell
winget install HiBitSoftware.HiBitUninstaller      # 高效的卸载工具，支持彻底清除软件残留
winget install WinMerge.WinMerge                   # 文件和目录比较工具，支持合并差异
winget install Giorgiotani.Peazip                  # 开源的文件压缩解压工具，支持多种格式
winget install Synology.DriveClient                # 群晖 NAS 的桌面客户端，便于文件同步
winget install AntibodySoftware.WizTree            # 高效的磁盘空间分析工具，快速查找大文件和文件夹
```

## 开发工具

```powershell
winget install Git.Git                             # 分布式版本控制系统，广泛用于代码管理
winget install GitHub.GitHubDesktop                # GitHub 的桌面客户端，简化版本控制操作
winget install Microsoft.VisualStudioCode.Insiders # 轻量级的代码编辑器，提供最新的预发布功能
```

## 多媒体工具

```powershell
winget install VideoLAN.VLC                        # 多功能媒体播放器，支持几乎所有音视频格式
winget install sylikc.JPEGView                     # 轻量级的图片查看和编辑工具
winget install SumatraPDF.SumatraPDF               # 轻量级、多功能PDF阅读器
winget install PicGo.PicGo                         # 开源的图片上传工具，支持多种图床
winget install 9P1WXPKB68KX                        # Snipaste：截图和贴图工具，支持高效的截图和标注功能
winget install lyswhut.lx-music-desktop            # 免费 & 开源的音乐查找工具
```

## 网络工具

```powershell
winget install Tencent.WeChat                      # 腾讯微信桌面客户端，支持消息同步和多媒体通讯
winget install Telegram.TelegramDesktop            # 安全的即时通讯工具，支持多平台消息同步
winget install Mobatek.MobaXterm                   # 强大的终端仿真器，内置多种网络工具
winget install RustDesk.RustDesk                   # 开源的远程桌面工具，替代 TeamViewer
```

## 开发辅助工具

```powershell
winget install Redisant.TinyGUI                    # 轻量级的图片压缩工具
winget install AltSnap.AltSnap                     # 窗口管理工具，可使非标准窗口支持 Aero Snap
winget install Logitech.OptionsPlus                # 罗技设备管理工具，优化鼠标键盘性能
winget install Pylogmon.pot                        # 划词翻译软件，可使用 LLM 翻译
winget install Python.Python.3.12                  # Python，需要需求需要下载所需的版本号
```

## 行业工具

```powershell
winget install KiCad.KiCad                         # 开源的电路原理图、PCB 设计工具
```

---

无法使用 winget 的软件：

- HEU KMS Activator
- OInstall
- huorong ?
- clash?
- Win10Apps
- DriverBooster 修改
- WPD
- Dism++
- frp
- Intel® Graphics Command Center (Beta)
- FileZilla
- PDF-XChange 修改

使用 winget 有问题，暂时放到便携式 software 目录下

- Pylogmon.pot

- Python: Python.Python.3.xx

C:\Users\power\AppData\Local\Programs\KiCad\8.0\share\kicad\symbols

可选：

- AppbyTroye.KoodoReader
- Ventoy.Ventoy
- Hugo.Hugo
- WPD.WPD ?
- Rufus.Rufus?
- Balena.Etcher
- JGraph.Draw #draw.io
- Eassos.DiskGenius
- FinalWire.AIDA64.Extreme #(30 天试用)
