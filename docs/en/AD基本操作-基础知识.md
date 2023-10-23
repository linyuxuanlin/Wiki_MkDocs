# AD Basic Operations - Fundamentals

— Altium Designer Tutorial Series

## Background

Before we start designing PCBs after configuring the software environment, it is essential to acquaint ourselves with some fundamental knowledge of Altium Designer and circuit design.

## Library File Installation

Libraries serve as encapsulations for individual discrete components (such as resistors, capacitors, etc.), making them readily accessible. It's not always necessary to create schematic or PCB libraries for every component you use, but **organizing your own library is a must**. Imagine if every component in your project comes from different sources (each with its own rules), the further you go, the more constrained you will become. Having your library not only eases migration and enhances efficiency but also promotes systematic knowledge. Following your own rules and systems, your knowledge growth will be exponential over time. Although the initial learning curve might be slow, in the later stages, there will be no repetitive work. What you need to do then is to learn new knowledge and incorporate it into your system.

Friendly advice: Extract all the components your project requires from your organized schematic and PCB libraries as much as possible.

### Recommended Libraries

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): My own organized library. It includes comprehensive packaging libraries and only contains component models required for my projects. Continuously updated.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): A relatively comprehensive library.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): A quite comprehensive library, including some single-board microcontroller solutions.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): JLCPCB's standard integrated library, including all the components that JLCPCB can mount through SMT. Using this integrated library will ensure better compatibility when designing PCBs or assembling SMT components.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): Library and packaging library organized by Bin, covering most components required by our hardware team.

How to install library files: Refer to [**Installing Library Files in Altium Designer**](https://wiki-power.com/AltiumDesigner%E5%AE%89%E8%A3%85%E5%BA%93%E6%96%87%E4%BB%B6)

### Uncommon Components

The provided libraries already cover over 95% of the component models available in the market. If you can't find the component you need, you can try the following methods:

AD Plugins:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): This is incredibly convenient to use.

Search Engine: [**Schematic and Packaging Downloads · Power's NAV**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Keyboard Shortcuts

In Altium Designer, mastering common keyboard shortcuts can significantly enhance your efficiency. Altium Designer's system shortcuts are composed of letter combinations with underscores based on commands in the menu. For example, the shortcut for **Place-Line** is **P-L** (press P and then L).

### Schematic

- Show Library Panel: **PP**
- Draw Wires: **Ctrl + W**
- Create Network Labels: **PN**
- Copy Components with Automatic Update of Reference Designators: **Hold Shift + Drag**
- Assign Sheet Numbers: **TAT**
- Automatically Number Components: **TAA**
  - Reset All: Resets all component reference designators to "letter + ?" format.
  - Update Change List: Updates reference designators in the component list.
  - Accept Changes (Create ECO): Indicates acceptance of reference designator changes, implementing changes in the schematic.
- Generate Bill of Materials (BOM): **RI**
- Update PCB: **DU**
- Align Left (Right): **AL** (**AR**)

### PCB

- Import Schematic Changes to PCB: **DI**
- Update Schematic with PCB Changes: **DU**
- Toggle Units (Inch/Millimeter): **Q**
- Rotate Components (Any Angle): **EMO**
- Place Components on the Bottom Layer: **Drag while holding L**
- Auto Arrange: **Select + TOL**
- Set Origin Coordinates: **EOS**
- Set Grid: **G**
- Auto Route: **UAA**
- Clear Routing: **UUA**
- Highlight Nets: **Hold Shift + Hover over Wire**
- Highlight Corresponding Wires to Node: **Hold Ctrl + Left-click**
- Flip Horizontally: **Ctrl + F**
- Measure: **Ctrl + M**
- Switch View (2D / 3D): **2 / 3**
- Rotate in 3D View: **Hold Shift + Drag**
- Clear Filters: **Shift + C**
- Toggle Single/Multi-Layer Display: **Shift + S**
- Cover Via Holes with Solder Mask (Optional, can be selected directly when creating the PCB)
  1. Click on a via hole
  2. Right-click - Find Similar Objects
  3. Select Same in Size attribute to activate the selection of all via holes
  4. In the Solder Mask Expansion attribute, check both top and bottom layers
- Set Routing Rules
  1. **UAA**
  2. Create a new strategy and edit rules
  3. Modify the rules in Routing (Create New Rule)
     - Width: Set the trace width
     - Routing Via Style: Set the via hole rules
     - Copper Pour: ?

### Schematic Library

To be added...

### Component Library

- Measure Distance: **Ctrl + N**
- Toggle Units (Inch/Millimeter): **Q**

## Workflow and Standards

The basic process for designing a circuit board from scratch is as follows:

```markdown
1. Initialization
   1. Create a New Project
   2. Create Schematics and PCB Files within the Project
2. Schematic Design
   1. Ensure a Successful Compilation upon Completion
3. PCB Design
   1. Import Changes from Schematics
   2. Hide Designator Labels
      1. Open the **Properties** panel on the right
      2. Click the **eye** icon next to **Designator** to deactivate it
   3. Define the Board Shape
      - Switch between 90°/45° Routing (**Shift+Space**)
      - Define the board shape using the **DSD** command
      - Set the Board Outline Attributes to Mechanical Layer 1
      - Fix Mounting Holes
        - M3 Holes: Inner **3.1** mm, Outer **4** mm
   4. Component Placement
      - Refer to [**PCB Component Layout Guidelines**](https://wiki-power.com/PCB%E5%85%83%E4%BB%B6%E5%B8%83%E5%B1%80%E8%A7%84%E8%8C%83)
   5. Routing
      - Define Routing Rules
        - Refer to [**PCB Routing Guidelines**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
      - **Do not enable Auto Routing!**
      - Enable Tear-Drop Functionality
   6. Text and Labels (Pin Labels / Copyright / Explanatory Text)
      - Place them on the Silkscreen Layer (Top Layer / Bottom Layer)
      - If placing on the Bottom Layer, remember to mirror them
   7. Copper Pour (**PG**)
      - Refer to [**PCB Routing Guidelines**](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
4. PCB Fabrication
   1. Save the Project
   2. Compress the **.pcb** file (Exporting Gerber files is preferable)
   3. Upload it to **JiaLiChuang Order Assistant**
   4. (Optional SMT)

## Additional Information

### Component Properties

- **Designator**: The component reference designator, a unique identifier used to distinguish components in the schematic
  - **R**: Resistor
  - **RN**: Resistor Network
  - **C**: Capacitor
  - **J**: Connector/Jumper
  - **X**: Crystal/Oscillator
  - **D**: Diode
  - **Q** or **T**: Transistor
  - **FB**: Ferrite Bead
  - **U**: IC/Chip
  - **TP**: Test Point
- **Comment**: Component specifications, such as resistance values for resistors, capacitance values for capacitors, IC part numbers, etc.
- **Description**: Used for providing a functional description of the component

### Adding a Logo

Refer to the article [**Adding a Logo**](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/).

### Managing Projects with Git

For detailed information, see [**Considerations for Using Git with Altium Designer**](https://wiki-power.com/AD%E4%BD%BF%E7%94%A8Git%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9).

## Conclusion

The above represents the fundamental knowledge of Altium Designer and circuit design.  
In the next chapter, we will begin the schematic design.

## References and Acknowledgments
```
This translation maintains the original markdown format while providing a colloquial, professional, and elegant tone.

Sure, here is the translation of the provided text into English:

- [Altium Company Altium Designer Column](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [Jialichuang SMT Solder Paste Applicability List PADS Integrated Library (Official Version)](http://club.szlcsc.com/article/details_2757_1.html)
- [Altium Designer and Git Integration](https://blog.csdn.net/weifengdq/article/details/78406438)
- [Using Version Control](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.