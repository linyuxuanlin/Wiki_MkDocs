# Basic Operations of Altium Designer - Multi-board System Design 🚧

The reason for using multi-board system design is that a hardware project may contain multiple PCBs and various assembly elements such as casings. If we only design from the perspective of each board, the final product may have fitting errors or interference. When designing hardware projects with multiple elements, it is best to use mechatronics coordination. For hardware engineers, it is possible to achieve this directly in Altium Designer without using software such as SolidWorks.

## Creating a Multi-board Project

First, create a multi-board project type file (`.PrjMbd`), create a logic design file based on the schematic (`.MbsDoc`) and a PCB-based file (`.MbaDoc`) under the project, and then save it. At the file system level, copy multiple individual PCB project folders to the same level directory as `.PrjMbd`, for example:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220106152537.png)

## Inputting Logic Design

Inputting logic design is based on the physical connectors on the PCB. Before this, we need to add parameters to the connectors in the project schematic (open the properties of the connector, add `Parameters`, name it `System`, and the value is `Connector`).

![](https://f004.backblazeb2.com/file/wiki-media/img/20220106163315.png)

### Creating Modules and Linking Projects

Place modules in the logic design file (`.MbsDoc`) and double-click to bring up the properties, then select the corresponding source PCB project.

### Importing Interface Data from Sub-Projects

Right-click with the mouse and select `Design` - `Import from Sub-Project` to automatically import ports with parameters as connectors.

### Adding Logical Connections between Modules

Use the shortcut keys `P` - `W` to draw connection lines.

Click on the connection line to modify the detailed port connections of the two modules in the properties panel.

If a connector needs to connect to multiple boards, you can split a port in the properties.

## Physical Multi-board Assembly

### Importing PCBs from Logic Design Files

Use the shortcut keys `D` - `I` to import the corresponding PCBs from the logic design file.

### Simulating Assembly

Drag the coordinate axis of each PCB to simulate assembly.

## Generating Production Data

🚧

## References and Acknowledgments

- [What is the experience of multi-board design in PCB?](https://www.altium.com.cn/blog/pcb%E4%B8%AD%E8%BF%9B%E8%A1%8C%E5%A4%9A%E6%9D%BF%E8%AE%BE%E8%AE%A1%E4%BC%9A%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84%E4%BD%93%E9%AA%8C%EF%BC%9F)
- [Capturing the Logical System Design](https://www.altium.com/documentation/altium-designer/capturing-the-logical-system-design-ad)
- [Creating the Physical Multi-Board Assembly](https://www.altium.com/documentation/altium-designer/creating-the-physical-multi-board-assembly-ad)
- [Generating Multi-Board Production Data](https://www.altium.com/documentation/altium-designer/generating-multi-board-production-data-ad)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.