# Consideraciones para el uso de Git en AD

## Gestión de proyectos con Git

Altium Designer admite el uso de Git/SVN para el control de versiones. Si estás utilizando Git, simplemente crea un repositorio Git en la ubicación de tu proyecto. Al reiniciar Altium Designer, verás que aparece un estado de versión junto al árbol de archivos:

![Estado de versión](https://media.wiki-power.com/img/20200421100348.png)

Los iconos tienen el siguiente significado:
![Significado de los iconos](https://media.wiki-power.com/img/20200421101221.png)

Puedes realizar operaciones de Git directamente desde el menú `Proyecto (C) - Control de versiones (E)`, e incluso puedes hacer commits directamente en GitHub.

## Archivo .gitignore

Cuando trabajas con Altium Designer, el software genera algunos archivos de caché (como la carpeta 'History'), los cuales no solo ralentizan la velocidad de los commits, sino que también ensucian el registro de commits. En este punto, debes utilizar el archivo `.gitignore` para ignorar estos archivos de caché.

El archivo `.gitignore` adecuado para Altium Designer incluye lo siguiente:

```gitignore
# ============================= Proyectos =============================
*.DesWrk
# Espacio de trabajo de Altium

*.DsnWrk
# Grupo de proyectos de Altium

!*.LibPkg
# Paquete de biblioteca integrada de Altium

*.PrjGrp
# Grupo de proyectos de Altium

!*.PrjMbd
# Proyecto de diseño multiplaca de Altium

!*.PrjPcb
# Proyecto de PCB de Altium

*.PrjScr
# Proyecto de guion de Altium

*.PrjPCBStructure

# ============================= Esquemáticos =============================
*.Dot
# Plantilla de esquemático de Altium

!*.MbsDoc
# Esquemático multitarjeta de Altium

!*.Sch
# Documento de esquemático de Altium

!*.SchDoc
# Documento de esquemático de Altium

*.SchDot
# Plantilla de esquemático de Altium

!*.SchLib
# Biblioteca de esquemáticos de Altium

# ============================= PCB =============================
!*.MbaDoc
# Ensamblaje multitarjeta de Altium

!*.Pcb
# Documento de PCB de Protel

!*.PcbDoc
# Documento de PCB de Altium

!*.PcbLib
# Biblioteca de PCB de Altium

# ============================= Bibliotecas =============================
*.CmpLib
# Biblioteca de componentes de Altium

!*.IntLib
# Biblioteca compilada de Altium

!*.Lib
# Biblioteca de Altium

*.PvLib
# Biblioteca de almohadillas y pasantes de Altium

# ============================= CAMtastic =============================
*.Apr
# Datos de aperturas CAMtastic

*.Apt
# Datos de aperturas CAMtastic

*.Cam
# Documento CAMtastic de Altium

*.Drl
# Datos binarios de taladro NC CAMtastic
```

Espero que esta traducción sea de ayuda. Si tienes alguna pregunta o necesitas más asistencia, no dudes en preguntar.

```markdown
# ============================= Gerber =============================

\*.G[1-30]

# Datos Gerber de capas intermedias 1-30 de CAMtastic

# ============================= Salidas =============================

\*.Drc

# Informe de Verificación de Reglas de Diseño

\*.Drr

# Informe de Taladro NC de Altium

\*.Net

# Archivo de Lista de Red de Altium

\*.Nsx

# Documento de Lista de Red de Simulación

\*.OutJob

# Archivo de Trabajo de Salida de Altium

\*.Rep

# Archivo de Informe

\*.Rpt

# Archivo de Informe

# ============================= Scripts =============================

\*.Bas

# Documento de Script de Altium

\*.SrcDoc

# Documento de Script de Altium

\*.Tcl

# Documento de Script de Altium

# ============================= Simulación =============================

\*.Ckt

# Subcircuito de Simulación

\*.LaxAn

# Archivo Analógico del Analizador Lógico

\*.LaxDig

# Archivo Digital del Analizador Lógico

\*.Mdl

# Modelo de Simulación

\*.Pld

# Archivo PLD de CUPL

\*.Pwl

# Descripción Lineal por Tramos de Simulación

\*.Sdf

# Archivo de Datos de Simulación de Altium

\*.Si

# Archivo de Entrada de Simulación de CUPL

\*.So

# Archivo de Forma de Onda Digital

# ============================= Carpetas =============================

\_\_Previews/

Historial/

Registros del Proyecto para \*/

# ============================= Otros =============================

\*.BomDoc

# Documento de Lista de Materiales (BOM)

\*.DBLib

# Archivo de Biblioteca de Base de Datos de Altium

\*.DBLink

# Archivo de Enlace de Base de Datos de Altium

Colóquelo directamente en la raíz del repositorio de Git. Si hay duplicados, mezcle con el archivo `.gitignore` original.

## Referencias y Agradecimientos

- [.gitignore Configuration for Altium Designer Project File Types](https://blog.csdn.net/u010160335/article/details/80100232)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
