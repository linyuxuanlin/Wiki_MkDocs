# OrCAD Configuration and Tips

Note: This article is based on Cadence OrCAD Capture CIS.

## Basics

OrCAD Capture CIS is used for drawing schematics (Start menu -> Cadence -> Capture CIS)  
Allegro PCB Designer is used for drawing PCBs (Start menu -> Cadence -> PCB Editor)

Generally, using a `.DSN` file is sufficient to encompass the entire project, and opening it will automatically generate `.opj` and other schematic files. If using git for version control, the following gitignore can be added:

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

## Some Settings

DRC settings:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134720.png)

Automatically rename reference designators when copying components:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134747.png)

Snap characters to grid when moving them:

Pitfall: When using the CIP library, if "not found in the configured library lists" is displayed, check the encoding of spaces in the path.

- **Mouse wheel zoom**: `Options` - `Preferences...` - `Pan and Zoom` - Set both `Zoom Factor` to 1.1
- **Refresh schematic when placing components**: `Options` - `Preferences...` - `Miscellaneous` - `Place Part` - Check `Refresh part on selection`
- **Set grid size**: `Options` - `Preferences...` - `Grid Display` - `Grid Spacing` - Set to 1/2

## Shortcuts

- Draw wire: `W`
- Cancel: `ESC`
- Draw bus: `F4`
- Place net label: `N`
- Rotate / Horizontal mirror / Vertical mirror component: `R` / `H` / `V`
- Open CIS panel: `Z`
- Place power / ground: `F` / `G`
- No connect: `X`
- Filter: `Ctrl` + `I`
- Select multiple elements: Hold `Ctrl` to select
- Copy and automatically increment reference designator: Hold `Ctrl` and drag component
- Move schematic with mouse as center of gravity: Hold `C` and drag mouse
- Place bus: `E`
- Place text: `T`

## Errors and Solutions

- Unable to drag component: Generally, restarting can solve the problem.

## Tips

### Difference between off-page and port

Off-page is generally used for flat schematics, while port is generally used for hierarchical schematics.

### DRC check

1. Select the entire project by clicking on it in the file tree
2. Click `Tools` - `Design Rules Check...` on the toolbar
3. Check `Run Physical Rules` and `View Output`
4. Click OK, a report will be generated and automatically opened.

## References and Acknowledgments

- [Quick Start Guide to Cadence](https://blog.csdn.net/ReCclay/article/details/101225359)
- [OrCAD Capture Tutorial](https://resources.orcad.com/orcad-capture-tutorials)
- [Solution to Blurry Font Display in Cadence Software on High-Resolution Laptops](https://blog.csdn.net/qq_34338527/article/details/108846792)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.