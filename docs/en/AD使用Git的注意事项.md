# Notes on Using Git with Altium Designer

## Managing Projects with Git

Altium Designer supports version control using Git/SVN. To use Git, simply create a Git repository in the project directory. After restarting Altium Designer, you will see the version status appear on the file tree:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200421100348.png)

The icons have the following meanings:
![](https://f004.backblazeb2.com/file/wiki-media/img/20200421101221.png)

You can perform Git operations directly in the `Project (C) - Version Control (E)` menu, and even submit to GitHub directly.

## .gitignore File

When using Altium Designer, the software automatically generates some cache files (such as the `History` folder), which not only slows down the submission speed, but also pollutes the submission record. This is where `.gitignore` comes in, to ignore these cache files.

The `.gitignore` file for Altium Designer includes the following content:

```gitignore
# ============================= Projects =============================
*.DesWrk
# Altium Workspace

*.DsnWrk
# Altium Project Group

!*.LibPkg
# Altium Inegrated Library Package

*.PrjGrp
# Altium Project Group

!*.PrjMbd
# Altium Muti-board Design Project

!*.PrjPcb
# Altium PCB Project

*.PrjScr
# Altium Script Project

*.PrjPCBStructure

# ============================= Schematic =============================
*.Dot
# Altium Schematic Template

!*.MbsDoc
# Altium Multi-board Schematic

!*.Sch
# Altium Schematic Document

!*.SchDoc
# Altium Schematic Document

*.SchDot
# Altium Schematic Template

!*.SchLib
# Altium Schematic Library

# ============================= PCB =============================
!*.MbaDoc
# Altium Multi-board Assembly

!*.Pcb
# Protel PCB Document

!*.PcbDoc
# Altium PCB Document

!*.PcbLib
# Altium PCB Library

# ============================= Libraries =============================
*.CmpLib
# Altium Component Library

!*.IntLib
# Altium Compiled Library

!*.Lib
# Altium Library

*.PvLib
# Altium Pad Via Library

# ============================= CAMtastic =============================
*.Apr
# CAMtastic Aperture Data

*.Apt
# CAMtastic Aperture Data

*.Cam
# Altium CAMtastic Document

*.Drl
# CAMtastic NC Drill Binary Data

# ============================= Gerber =============================
*.G[1-30]
# CAMtastic Mid Layer 1-30 Gerber Data

# ============================= Outputs =============================
*.Drc
# Design Rule Check Report

*.Drr
# Altium NC Drill Report File

*.Net
# Altium Netlist File

*.Nsx
# Simulation Netlist Document

*.OutJob
# Altium Output Job File

*.Rep
# Report File

*.Rpt
# Report File

# ============================= Scripts =============================
*.Bas
# Altium Script Document

*.SrcDoc
# Altium Script Document

*.Tcl
# Altium Script Document

# ============================= Simulation =============================
*.Ckt
# Simulation Sub-Circuit

*.LaxAn
# Logic Analyser Analog File

*.LaxDig
# Logic Analyser Digital File

*.Mdl
# Simulation Model

*.Pld
# CUPL PLD File

*.Pwl
# Simulation Piecewise Linear Description

*.Sdf
# Altium Simulation Data File

*.Si
# CUPL Simulation Input File

*.So
# Digital Waveform File

# ============================= Folders =============================
__Previews/

History/

Project Logs for */

# ============================= Other =============================
*.BomDoc
# Bom Document

*.DBLib
# Altium Database Library File

*.DBLink
# Altium Database Link File
```

Simply place it in the root directory of the Git repository. If there are duplicates, merge it with the original `.gitignore`.

## References and Acknowledgements

- [.gitignore file configuration: Altium Designer project file types](https://blog.csdn.net/u010160335/article/details/80100232)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.