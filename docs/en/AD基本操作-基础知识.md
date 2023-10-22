# AD Basic Operations - Basic Knowledge

—— Altium Designer Tutorial Series

## Background

After configuring the software environment, before starting to design a PCB, it is essential to familiarize yourself with some basic knowledge of Altium Designer and circuit design.

## Library File Installation

Libraries serve as encapsulations for individual discrete components (such as resistors, capacitors, etc.), making them readily available for use. Not every component's schematic/library needs to be created from scratch, but **organizing your own library is a must**. Imagine if every component in your project comes from different sources with their unique rules; you would find yourself increasingly constrained as the project progresses. Having your library not only makes migration and efficiency easier but also promotes the systematization of knowledge. Adhering to your own set of rules and systems, you will see knowledge growth following an exponential curve over time. While the initial learning curve may be slow, in the later stages, there will be no repetitive work. At that point, all you need to do is acquire new knowledge and integrate it into your system.

Friendly reminder: Whenever possible, extract all the components needed for your project from your own organized schematic/library.

### Recommended Libraries

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): A library I have organized. It includes comprehensive packaging libraries and schematic libraries containing only the component models required for my projects. It is continuously updated.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): A relatively comprehensive library.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): A fairly comprehensive library, including some microcontroller reference boards.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): JiaLiChuang's standard integrated library, containing all the components compatible with JiaLiChuang's SMT assembly. Using this integrated library ensures good compatibility when manufacturing PCBs or assembling SMT components.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): Schematic and packaging libraries organized by Bin Ge, covering most of the components needed for our team's hardware.

How to install library files: Refer to [**Installing Library Files in Altium Designer**](to_be_replace[3]).

### Uncommon Components

The libraries provided above already cover over 95% of commonly used component models in the market. If you cannot find the component you need, you can try the following methods:

AD Plugins:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): This tool is incredibly convenient to use.

Search Engines: [**Schematic and Package Downloads · Power's NAV**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Keyboard Shortcuts

In the context of Altium Designer, mastering common keyboard shortcuts can significantly enhance efficiency. Altium Designer's system keyboard shortcuts are typically formed from combinations of letters with underscores from the commands under the menu. For example, the shortcut for **Place-Line** is **P-L** (press P, then L).

### Schematic

- Display Library Panel: **PP**
- Draw Wires: **Ctrl + W**
- Create Network Labels: **PN**
- Duplicate Components and Automatically Update Reference Designators: **Hold Shift + Drag**
- Number the Drawing: **TAT**
- Auto-Number Components: **TAA**
  - Reset All: Reset all component reference designators to "Letter + ?" format.
  - Update Change List: Update reference designators for components in the list.
  - Accept Changes (Create ECO): Accept reference designator changes to implement schematic changes.

- Generate BOM Table: **RI**
- Update PCB: **DU**
- Align Left (Right): **AL** (**AR**)

### PCB

- Import Schematic Changes to PCB: **DI**
- Overlay PCB Changes Back to Schematic: **DU**
- Change Units (Inches/Millimeters): **Q**
- Rotate Components (Any Angle): **EMO**
- Place Components on Bottom Layer: **Drag while holding L**
- Auto Layout: **Select + TOL**
- Set Origin Coordinates: **EOS**
- Set Grid: **G**
- Auto Routing: **UAA**
- Clear Routing: **UUA**
- Highlight Connections: **Hold Shift + Hover over a wire**
- Highlight Wires Corresponding to a Node: **Hold Ctrl + Left-click**
- Horizontal Flip: **Ctrl + F**
- Measure: **Ctrl + M**
- Switch View (2D / 3D): **2 / 3**
- Rotate in 3D View: **Hold Shift + Drag**
- Clear Filters: **Shift + C**
- Toggle Single/Multi-Layer Display: **Shift + S**
- Cover Vias with Solder Mask (optional, choose when making the board)
  1. Click on a via.
  2. Right-click - Find Similar Objects.
  3. Select Size attribute as "Same" to select all vias.
  4. In the Solder Mask Expansion attribute, check both Top Layer and Bottom Layer.

- Setting Routing Rules
  1. **UAA**
  2. Create a strategy and edit rules.
  3. Make changes to Routing rules (Create new rules)
     - Width: Set the line width.
     - Routing Via Style: Set via rules.
     - Copper Pour: ?

### Schematic Library

To be added...

### Footprint Library

- Measure Distance: **Ctrl + N**
- Change Units (Inches/Millimeters): **Q**

## Workflow and Standards

The basic process of designing a circuit board from scratch is as follows:

1. **Initialization**
   1. Create a New Project
   2. Create Schematic and PCB Files within the Project
2. **Schematic Design**
   1. Ensure Successful Compilation upon Completion
3. **PCB Design**
   1. Import Changes from Schematic
   2. Hide Component Designator Labels
      1. Open the **Properties** panel on the right
      2. Click the **eye** icon next to **Designator** to deactivate it
   3. Create Board Outline
      - Switch between 90°/45° Routing (**Shift+Space**)
      - Define the board shape with drawn lines (**DSD**)
      - **Set Board Outline Attributes to Mechanical Layer 1**
      - Define Fixed Holes
        - M3 Screw Holes: Inner **3.1** mm, Outer **4** mm
   4. Arrange Components
      - Refer to [**PCB Component Layout Guidelines**](to_be_replaced[3])
   5. Routing
      - Define Routing Rules
        - Refer to [**PCB Routing Guidelines**](to_be_replaced[3])
      - **Do Not Enable Auto Routing!**
      - **Activate Tear-Dropping Function**
   6. Text Markings (Pin Labels / Copyright / Miscellaneous Text)
      - Place them on the Silkscreen Layer (Top / Bottom)
      - When placing on the bottom layer, mirror them first
   7. Copper Pouring (**PG**)
      - Refer to [**PCB Routing Guidelines**](to_be_replaced[3])
4. **Board Fabrication**
   1. Save the Project
   2. Compress the **.pcb** file (Note: Exporting Gerber files might be more appropriate)
   3. Upload it to **JLCPCB Order Assistant**
   4. (Optional: Surface Mount Technology)

## Additional Knowledge

### Component Attributes

- **Designator**: Component reference designator, a unique identifier used to distinguish different components in the schematic.
  - **R**: Resistor
  - **RN**: Network Resistor
  - **C**: Capacitor
  - **J**: Connector/Jumper
  - **X**: Crystal/Oscillator
  - **D**: Diode
  - **Q** or **T**: Transistor
  - **FB**: Ferrite Bead
  - **U**: IC/Chip
  - **TP**: Test Point
- **Comment**: Component size parameters, such as resistance value for resistors, capacitance value for capacitors, IC chip models, etc.
- **Description**: Used to describe the function of a component.

### Adding a Logo

Refer to the article [**Adding a Logo**](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/).

### Managing Projects with Git

For detailed information, please see [**Considerations for Using Git in Altium Designer**](to_be_replaced[3]).

## Conclusion

The above covers the fundamental knowledge of Altium Designer and circuit design.  
In the next chapter, we will commence with schematic design.

## References and Acknowledgments

- [Altium Company's Altium Designer Column](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [Jialichuang SMT Soldering Paste Applicability List PADS Integrated Library (Official Version)](http://club.szlcsc.com/article/details_2757_1.html)
- [Concept of Using Git with Altium Designer](https://blog.csdn.net/weifengdq/article/details/78406438)
- [Utilizing Version Control](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.