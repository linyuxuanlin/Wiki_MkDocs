---
id: OrCAD配置与技巧
title: OrCAD 配置与技巧
---

注：本文基于 Cadence OrCAD Capture CIS。

## 基础

绘制原理图使用 OrCAD Capture CIS（开始菜单-》Cadence-》Capture CIS）  
绘制 PCB 使用 Allegro PCB Designer （开始菜单-》Cadence-》PCB Editor）

一般来说，使用一个 `.DSN` 文件即可涵括整个工程，打开会自动生成 `.opj` 等原理图文件。如果使用 git 做版本管理，可以添加以下 gitignore：

```gitignore
# From original gitignore 

#############
## Allegro
#############

# Ignore log file
*.log
*.log,1
*.log,2
*.log,3

*.dml
*.lst

#ignore 记录操作allegro的事件
*.jrl
*.jrl,1

*.tag

#报告文件
*.rpt

#报告文件
*.cfg
*.cfg,1

*.lck

#报表文件
*.txt
*.txt,1
*.txt,2

#XY数据除外
!place_txt.txt

#DXF导入文件
*.cnv

#Gerber param file除外
!art_param.txt

#Folder
#过滤整个文件夹
/signoise.run/ 

#############
## OrCAD
#############
*.dbk
*.opj
*.DRC
*.DSNlck

#ignore netlist
allegro/ 
```

## 一些设置

DRC 设置：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134720.png)

复制元器件时自动重命名位号：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134747.png)

移动字符时贴近栅格：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134758.png)

坑：当使用 CIP 库，显示 `not found in the configured librarie lists` 时，要检查路径内空格的编码。

- **鼠标滚轮缩放**：`Options` - `Preferences…` - `Pan and Zoom` - 左右两个 `Zoom Factor` 设置为 1.1 倍
- **放置元件时刷新原理图**：`Options` - `Preferences…` - `Miscellaneous` - `Place Part` – 勾选 `Refresh part on selection`
- **设置栅格大小**：`Options` - `Preferences…` - `Grid Display` - `Grid Spacing` - 设置为 1/2

## 快捷键

- 拉线：`W`
- 取消：`ESC`
- 拉排线：`F4`
- 放置网络标号：`N`
- 旋转 / 水平镜像 / 垂直镜像元件：`R` / `H` / `V`
- 打开 CIS 面板：`Z`
- 放置电源 / 地：`F` / `G`
- No connect：`X`
- 筛选器：`Ctrl` + `I`
- 多选元素：按住 `Ctrl` 进行选择
- 复制并自动增加标号：按住 `Ctrl` 拖动元器件
- 以鼠标为重心移动原理图：按住 `C`，拖动鼠标
- 放置总线：`E`
- 放置文字：`T`

## 错误与解决

- 无法拖动元器件：一般来说，重启能解决问题。

## 技巧

### off-page 与 port 的区别

off-page 一般用于平坦式原理图，而 port 一般用于层次原理图。

### DRC 检查

1. 在文件树点击选择整个项目
2. 点击工具栏 `Tools` - `Design Rules Check...`
3. 附加勾选 `Run Physical Rules`、`View Output`
4. 点击确定，会生成报告并自动打开

## 参考与致谢

- [【Cadence 快速入门】一文总结版](https://blog.csdn.net/ReCclay/article/details/101225359)
- [OrCAD Capture Tutorial](https://resources.orcad.com/orcad-capture-tutorials)
- [cadence 软件用于高分屏笔记本时候显示字体模糊问题解决](https://blog.csdn.net/qq_34338527/article/details/108846792)
