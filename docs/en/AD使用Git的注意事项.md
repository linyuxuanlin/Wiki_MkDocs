# Considerations for Using Git with AD

## Managing Projects with Git

Altium Designer supports the use of Git/SVN for version control. If you are using Git, you can simply create a Git repository in the project's location. After restarting Altium Designer, you will see the version status displayed next to the file tree:

![Version Status](https://media.wiki-power.com/img/20200421100348.png)

The icons represent the following:

![Icon Meanings](https://media.wiki-power.com/img/20200421101221.png)

You can perform Git operations directly from the `Project (C) - Version Control (E)` menu, and you can even directly submit to GitHub.

## .gitignore File

When using Altium Designer, the software generates certain cache files (such as the `History` folder), which not only slow down the submission process but also clutter the commit history. This is where the `.gitignore` file comes in handy to ignore these cache files.

The `.gitignore` file suitable for Altium Designer includes the following content:

```gitignore
# ============================= Projects =============================
*.DesWrk
# Altium Workspace

*.DsnWrk
# Altium Project Group

!*.LibPkg
# Altium Integrated Library Package

*.PrjGrp
# Altium Project Group

!*.PrjMbd
# Altium Multi-board Design Project

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
```

These guidelines should help you effectively manage your Altium Designer projects using Git.

# ============================= Gerber =============================

\*.G[1-30]

# CAMtastic Mid Layer 1-30 Gerber Data

# ============================= Outputs =============================

\*.Drc

# Design Rule Check Report

\*.Drr

# Altium NC Drill Report File

\*.Net

# Altium Netlist File

\*.Nsx

# Simulation Netlist Document

\*.OutJob

# Altium Output Job File

\*.Rep

# Report File

\*.Rpt

# Report File

# ============================= Scripts =============================

\*.Bas

# Altium Script Document

\*.SrcDoc

# Altium Script Document

\*.Tcl

# Altium Script Document

# ============================= Simulation =============================

\*.Ckt

# Simulation Sub-Circuit

\*.LaxAn

# Logic Analyser Analog File

\*.LaxDig

# Logic Analyser Digital File

\*.Mdl

# Simulation Model

\*.Pld

# CUPL PLD File

\*.Pwl

# Simulation Piecewise Linear Description

\*.Sdf

# Altium Simulation Data File

\*.Si

# CUPL Simulation Input File

\*.So

# Digital Waveform File

# ============================= Folders =============================

\_\_Previews/

History/

Project Logs for \*/

# ============================= Other =============================

\*.BomDoc

# Bom Document

\*.DBLib

# Altium Database Library File

\*.DBLink

# Altium Database Link File

Simply place it in the root directory of your Git repository. In case of duplicates, merge it with the existing `.gitignore` file.

## References and Acknowledgments

- [.gitignore File Configuration: Altium Designer Project File Types](https://blog.csdn.net/u010160335/article/details/80100232)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
