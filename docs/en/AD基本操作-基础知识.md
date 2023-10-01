# AD Basic Operations - Basic Knowledge

- Altium Designer Tutorial Series

## Background

Before starting to design a PCB, it is essential to familiarize oneself with some basic knowledge of Altium Designer and circuit design after configuring the software running environment.

## Library Installation

The library is equivalent to encapsulating the schematic/PCB of each discrete component (such as resistors, capacitors, etc.) to facilitate direct calling. It is not necessary to draw the schematic library/encapsulation library of each component, but **organizing your own library is necessary**. Imagine that every component in your project uses someone else's library (and different libraries have their own rules), then the more you go, the more you will be restricted. Having your own library is not only convenient for migration and efficiency improvement, but also conducive to the systematization of knowledge. Suitable rules and systems for oneself, from the timeline perspective, knowledge will show exponential growth. Although the curve growth is slow at the beginning, there will be no repetitive work in the later stage. At that time, all you need to do is to learn new knowledge and summarize it into the system.

Friendly reminder: try to extract all the components required for your own project from your own organized schematic library/encapsulation library.

### Reference Libraries

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): A library I compiled myself. The packaging library is complete, and the schematic library only contains the component models required for my projects. It is constantly updated.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): A relatively complete library.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): A quite comprehensive library, including some MCU solution boards.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): A standard integrated library provided by JiaLiChuang, including all components that JiaLiChuang can SMT. Using this integrated library will ensure better compatibility when making boards/SMT.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): A schematic library/packaging library compiled by Bin Ge, covering most of the components required by the team's hardware.

How to install library files: refer to [**Altium Designer Install Library Files**](https://wiki-power.com/AltiumDesigner安装库文件)

### Uncommon Components

The libraries provided above already cover more than 95% of the component models on the market. If you really can't find the required components, you can try the following methods:

AD plugins:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): This is really super convenient to use.

Search engine: [**Schematic and Packaging Download · Power's NAV**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Shortcut Keys

For Altium Designer, mastering commonly used shortcuts can greatly improve efficiency. Altium Designer's system shortcuts are composed of letter combinations with underlined letters in the commands under the menu. For example, the shortcut for Place-Line is P-L (press P and then L).

### Schematic

- Display Library panel: PP
- Draw wire: Ctrl + W
- Draw net label: PN
- Copy component and automatically update reference designator: Hold Shift + drag
- Number schematic sheets: TAT
- Automatically number components: TAA
  - Reset All: Reset all component reference designators to "letter + ?" format
  - Update Change List: Change reference designators in the component list
  - Accept Changes (Create ECO): Accept reference designator changes and implement schematic changes
- Generate BOM table: RI
- Update PCB: DU
- Align left (right): AL (AR)

### PCB

- Import schematic changes to PCB: **DI**
- Overlay PCB changes back to schematic: **DU**
- Switch units (inch/mm): **Q**
- Rotate components (any angle): **EMO**
- Place components on bottom layer: **Drag while holding L**
- Auto layout: **Select + TOL**
- Set coordinate origin: **EOS**
- Set grid: **G**
- Auto routing: **UAA**
- Clear routing: **UUA**
- Highlight wiring: **Hold Shift + move cursor over wire**
- Highlight connected wires to a node: **Hold Ctrl + left-click**
- Flip horizontally: **Ctrl + F**
- Measure: **Ctrl + M**
- Switch view (2D/3D): **2/3**
- Rotate in 3D view: **Hold Shift + drag**
- Clear filter: **Shift + C**
- Switch between single/multi-layer display: **Shift + S**
- Cover via with solder mask (optional, can be selected directly when ordering PCB)
  1. Click on a via
  2. Right-click - Find Similar Objects
  3. Select Same for Size attribute and confirm to select all vias
  4. In Solder Mask Expansion under Properties, check both Top and Bottom layers
- Set routing rules
  1. **UAA**
  2. Create a new strategy and edit rules
  3. Generally modify rules in Routing (create new rules)
     - Width: set line thickness
     - Routing Via Style: set via rules
     - Copper Pour: ?

### Schematic Library

To be added...

### Package Library

- Measure distance: **Ctrl + N**
- Switch units (inch/mm): **Q**

## Process and Standards

The basic process for designing a circuit board from scratch is as follows:

1. Initialization
   1. Create a new project
   2. Create schematic and PCB files within the project
2. Draw schematic
   1. Ensure successful compilation upon completion
3. Draw PCB
   1. Import changes from schematic
   2. Hide component designator labels
      1. Open the **Properties** panel on the right
      2. Click the **eye** icon next to **Designator** to hide
   3. Draw board shape
      - Switch between 90°/45° routing (**Shift+Space**)
      - Define board shape with drawn lines (**DSD**)
      - **Set board outline attribute to mechanical layer 1**
      - Fix mounting holes
        - M3 screw holes: inner diameter **3.1** mm, outer diameter **4** mm
   4. Arrange components
      - Refer to [**PCB Component Layout Specification**](https://wiki-power.com/PCB%E5%85%83%E4%BB%B6%E5%B8%83%E5%B1%80%E8%A7%84%E8%8C%83)
   5. Route traces
      - Set routing rules
        - Refer to [**PCB Routing Specification**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
      - **Do not enable auto-routing!**
      - **Enable teardrop function**
   6. Add text labels (pin labels / copyright / misleading text)
      - Place on silkscreen layer (top / bottom)
      - If placing on bottom layer, mirror first
   7. Apply copper pour (**PG**)
      - Refer to [**PCB Routing Specification**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
4. PCB fabrication
   1. Save project
   2. Compress the **.pcb** file (although exporting Gerber is preferred)
   3. Upload to **JLCPCB Order Assistant**
   4. (Optional SMT)

## Other Knowledge

### Component Properties

- **Designator**: Component reference designator, which is a unique identifier for each component used to distinguish different components in the schematic.
  - **R**: Resistor
  - **RN**: Resistor network
  - **C**: Capacitor
  - **J**: Connector/jumper
  - **X**: Crystal oscillator
  - **D**: Diode
  - **Q** or **T**: Transistor
  - **FB**: Ferrite bead
  - **U**: Integrated circuit
  - **TP**: Test point
- **Comment**: Component size parameters, such as resistor value, capacitor value, IC chip model, etc.
- **Description**: Used to describe the function of the component.

### Adding a Logo

Refer to [**Adding a Logo**](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/) for more information.

### Using Git to Manage Projects

Refer to [**Git Usage Notes for Altium Designer**](https://wiki-power.com/AD%E4%BD%BF%E7%94%A8Git%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9) for more information.

## Summary

The above is the basic knowledge of Altium Designer and circuit design. In the next chapter, we will start designing the schematic.

## References and Acknowledgements

- [Altium Designer column by Altium Corporation](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [JLC SMT Solderable List PADS Integrated Library (Official Version)](http://club.szlcsc.com/article/details_2757_1.html)
- [Altium Designer Git Concept](https://blog.csdn.net/weifengdq/article/details/78406438)
- [Using Version Control](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

Sorry, there is no Chinese article provided for translation. Please provide the article to be translated.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.