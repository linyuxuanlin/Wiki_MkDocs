# Consideraciones al usar Git con Altium Designer

## Gestión de proyectos con Git

Altium Designer admite el uso de Git/SVN para el control de versiones. Si se utiliza Git, simplemente se debe crear un repositorio Git en la ruta del proyecto. Al reiniciar Altium Designer, se verá el estado de la versión en el borde del árbol de archivos:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200421100348.png)

El significado de los iconos es el siguiente:
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200421101221.png)

Se pueden realizar operaciones de Git directamente en el menú `Proyecto (C) - Control de versiones (E)`, incluso se puede enviar directamente a GitHub.

## Archivo .gitignore

Al utilizar Altium Designer, el software generará algunos archivos de caché (como la carpeta `History`), que no solo ralentizan la velocidad de envío, sino que también contaminan el registro de envío. En este caso, se debe utilizar `.gitignore` para ignorar estos archivos de caché.

El archivo `.gitignore` para Altium Designer incluye lo siguiente:

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
```

# Datos binarios de perforación NC CAMtastic

# ============================= Gerber =============================
*.G[1-30]
# Datos de capa media 1-30 de CAMtastic Gerber

# ============================= Salidas =============================
*.Drc
# Informe de verificación de reglas de diseño

*.Drr
# Archivo de informe de perforación NC de Altium

*.Net
# Archivo de lista de red de Altium

*.Nsx
# Documento de lista de simulación

*.OutJob
# Archivo de trabajo de salida de Altium

*.Rep
# Archivo de informe

*.Rpt
# Archivo de informe

# ============================= Scripts =============================
*.Bas
# Documento de script de Altium

*.SrcDoc
# Documento de script de Altium

*.Tcl
# Documento de script de Altium

# ============================= Simulación =============================
*.Ckt
# Subcircuito de simulación

*.LaxAn
# Archivo analógico del analizador lógico

*.LaxDig
# Archivo digital del analizador lógico

*.Mdl
# Modelo de simulación

*.Pld
# Archivo PLD de CUPL

*.Pwl
# Descripción lineal por tramos de simulación

*.Sdf
# Archivo de datos de simulación de Altium

*.Si
# Archivo de entrada de simulación de CUPL

*.So
# Archivo de forma de onda digital

# ============================= Carpetas =============================
__Previews/

History/

Registros de proyecto para */

# ============================= Otros =============================
*.BomDoc
# Documento de lista de materiales

*.DBLib
# Archivo de biblioteca de base de datos de Altium

*.DBLink
# Archivo de enlace de base de datos de Altium

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.