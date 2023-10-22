# AD Basic Operations - Basic Knowledge

— Altium Designer Tutorial Series

## Background

After configuring the software environment, it's essential to acquaint ourselves with some fundamental knowledge of Altium Designer and circuit design before starting to design a PCB.

## Library Installation

A library acts as an encapsulation of individual discrete components (e.g., resistors, capacitors), making them readily accessible. It's not always necessary to create schematic libraries or component footprints for every component you use, but **organizing your libraries is a must**. Imagine if every component in your project comes from various sources, each with its own rules; you'll find yourself increasingly restricted as you progress. Having your library not only facilitates migration and improves efficiency but also promotes the organization of knowledge. Your own rules and systems will lead to exponential growth in knowledge over time. While the initial growth curve may be slow, later on, there will be no repetitive work. All you'll need to do is learn new knowledge and incorporate it into your system.

Friendly reminder: Extract all the components you need for your project from your organized schematic libraries or component footprints as much as possible.

### Recommended Libraries

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): My own organized library. It contains complete footprints and only the schematic symbols for the component models required for my projects. Continuously updated.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): A relatively comprehensive library.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): A quite comprehensive library that also includes some microcontroller solution boards.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): A standard integrated library provided by JLCPCB, which includes all components compatible with JLCPCB SMT placement. Using this integrated library ensures better compatibility when ordering PCBs or SMT assembly.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): Curated schematic libraries and component footprints by Bin Ge, covering most components required by the hardware team.

How to install library files: Refer to [**Altium Designer Library Installation**](to_be_replaced[3]).

### Uncommon Components

The libraries provided above already cover over 95% of component models available in the market. If you can't find the component you need, you can try the following methods:

AD Plugins:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): This is incredibly convenient to use.

Search Engine: [**Schematic and Footprint Downloads · Power's NAV**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Keyboard Shortcuts

For Altium Designer, mastering commonly used keyboard shortcuts can significantly improve efficiency. Altium Designer's system shortcuts are composed of letter combinations based on the letters with underscores in the menu commands. For example, the shortcut for **Place-Line** is **P-L** (press P followed by L).

### Schematic

- Show Library Panel: **PP**
- Draw Wires: **Ctrl + W**
- Draw Network Labels: **PN**
- Copy Components and Automatically Update Reference Designators: **Hold Shift + Drag**
- Number the Schematic Sheet: **TAT**
- Automatically Number Components: **TAA**
  - Reset All: Reset all component reference designators to "Letter + ?" format.
  - Update Change List: Assign reference designators to components in the list.
  - Accept Changes (Create ECO): Confirm the reference designator changes to implement schematic modifications.
- Generate BOM (Bill of Materials): **RI**
- Update PCB: **DU**
- Left Align (Right): **AL** (**AR**)

### PCB

- Import Schematic Changes into PCB: **DI**
- Overwrite PCB Changes to Schematic: **DU**
- Change Units (Inches/Millimeters): **Q**
- Rotate Components (Any Angle): **EMO**
- Place Components on Bottom Layer: **Drag while holding L**
- Auto Route: **Select + TOL**
- Set the Origin Coordinate: **EOS**
- Set the Grid: **G**
- Auto Route: **UAA**
- Clear Routing: **UUA**
- Highlight Connections: **Hold Shift + Move Cursor to a Wire**
- Highlight Connected Nets: **Hold Ctrl + Left-click**
- Horizontal Flip: **Ctrl + F**
- Measure: **Ctrl + M**
- Switch View (2D/3D): **2 / 3**
- Rotate in 3D View: **Hold Shift + Drag**
- Clear Filters: **Shift + C**
- Toggle Single/Multi-layer Display: **Shift + S**
- Cover Via Holes with Solder Mask (Optional, for PCB manufacturing)
  1. Click on a via hole.
  2. Right-click - Find Similar Objects.
  3. Select Size attribute as Same to activate selecting all via holes.
  4. In the Solder Mask Expansion attribute, check both Top Layer and Bottom Layer.
- Set Routing Rules
  1. **UAA**
  2. Create a new strategy and edit rules.
  3. Modify rules in Routing (Create new rules)
     - Width: Set the line thickness.
     - Routing Via Style: Set via hole rules.
     - Copper Pour: ?

### Schematic Library

To be added...

### Component Library

- Measure Distance: **Ctrl + N**
- Change Units (Inches/Millimeters): **Q**

## Process and Standards

The basic process for designing a circuit board from scratch is as follows:

```markdown
1. Inicialización
   1. Crear un nuevo proyecto
   2. Crear esquemáticos y archivos de PCB dentro del proyecto
2. Diseñar el esquemático
   1. Asegurarse de que compila correctamente una vez terminado
3. Diseñar el PCB
   1. Importar cambios desde el esquemático
   2. Ocultar las designaciones de los componentes
      1. Abrir el panel **Propiedades** en la parte derecha
      2. Hacer clic en el icono del **ojo** junto a **Designator** para desactivarlo
   3. Diseñar la forma de la placa
      - Cambiar el ángulo de las rutas a 90°/45° (presionar **Shift+Espacio**)
      - Definir el contorno de la placa con la forma creada (utilizar **DSD**)
      - Configurar las propiedades del contorno de la placa como "Capa Mecánica 1"
      - Agregar orificios de montaje
        - Orificio M3: Diámetro interior de **3.1** mm, diámetro exterior de **4** mm
   4. Colocar los componentes
      - Consultar el artículo [**Normas de Disposición de Componentes en PCB**](enlace_a_la_norma)
   5. Enrutamiento de pistas
      - Configurar las reglas de enrutamiento
        - Consultar [**Normas de Enrutamiento en PCB**](enlace_a_la_norma)
      - ¡No habilitar el enrutamiento automático!
      - Activar la función de 'teardrops' (lágrimas)
   6. Identificación con texto (marcadores de pines, derechos de autor, texto informativo)
      - Colocar en la capa de serigrafía (superior/inferior)
      - Si se coloca en la capa inferior, se debe espejar primero
   7. Rellenar con cobre (plano de tierra)
      - Consultar [**Normas de Enrutamiento en PCB**](enlace_a_la_norma)
4. Fabricación del PCB
   1. Guardar el proyecto
   2. Comprimir el archivo **.pcb** (si es posible, exportar a formato Gerber)
   3. Subir el archivo al asistente de pedidos de JLCPCB
   4. (Opcional: montaje superficial - SMT)

## Otros Conocimientos

### Atributos de Componentes

- **Designator**: Número de referencia del componente, sirve para identificar de forma única los componentes en el esquemático
  - **R**: Resistencia
  - **RN**: Red de resistencias
  - **C**: Condensador
  - **J**: Conector/Salto
  - **X**: Cristal oscilador
  - **D**: Diodo
  - **Q** o **T**: Transistor
  - **FB**: Ferrita
  - **U**: Microcontrolador
  - **TP**: Punto de prueba
- **Comment**: Parámetros del componente, como el valor de resistencia, la capacitancia o el modelo de un chip IC
- **Description**: Utilizado para describir la función del componente

### Agregar un Logotipo

Consultar el artículo [**Agregar un Logotipo**](enlace_al_artículo).

### Gestión de Proyectos con Git

Más detalles en [**Consideraciones al Usar Git en Altium Designer**](enlace_al_artículo).

## Resumen

Estos son los conceptos fundamentales de Altium Designer y el diseño de circuitos. En el próximo capítulo, comenzaremos con el diseño del esquemático.

## Referencias y Agradecimientos
```


- [Columna sobre Altium Designer de la empresa Altium](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [Lista de componentes SMT para montaje superficial de Jialichuang, integrada en la biblioteca PADS (versión oficial)](http://club.szlcsc.com/article/details_2757_1.html)
- [Conceptos de uso de Git en Altium Designer](https://blog.csdn.net/weifengdq/article/details/78406438)
- [Utilización del control de versiones](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.