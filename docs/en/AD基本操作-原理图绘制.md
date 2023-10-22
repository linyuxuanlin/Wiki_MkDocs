# AD Basic Operations - Schematic Drawing

—— Altium Designer Tutorial Series

## Background

After the warm-up in the previous chapter, we now dive into the schematic drawing phase.

## Drawing the Schematic

### Adjusting the Sheet

Following the basic process mentioned earlier, we have created a new project and added the schematic file to it. At this point, you are presented with a blank sheet. You can begin drawing the schematic directly on it. If the schematic becomes complex, you can also **change the sheet size** to prevent the components from appearing too crowded:

1. **Double-click** anywhere on the sheet.
2. In the Properties panel, locate the **Page Options** section.
3. Click the Sheet Size dropdown and change the sheet's dimensions.

### Placing Components

Next, we start placing components. The installation of libraries was explained in the previous chapter. Open the **Components** panel, click the dropdown displaying the library's name, which you've already installed. Once you've switched libraries, you can search for the required components in the search box (no need to press Enter after typing). After finding the component you need, simply **drag and drop** it onto the schematic using the left mouse button. This successfully places a component.

If you happen to forget which library a component belongs to, you can also use the global search function. Click the **three horizontal bars** to the left of the library name and select **File-based Library Search** from the dropdown to search through all available libraries.

### Component Properties

Placed components have several key attributes:

- **Designator**: The component reference designator, a unique identifier that cannot be duplicated. Typically, R1, R2... for resistors, C1, C2... for capacitors (refer to the knowledge points in the previous chapter).
- **Comment**: Component attributes like resistance value, capacitance value, chip model, etc.
- **Description**: The functional description of the component.
- **Footprint**: Linked to the packaging library, it associates the component with a specific PCB package.
- **Models**: Including Simulation models, Signal Integrity models, and others.

### Basic Operations

- **Left-click**: Select a command.
- **Left-click and hold**: Drag an object.
- **Double left-click**: Set object properties.
- **Right-click**: Cancel or display a command menu.
- **Right-click and hold**: Drag the schematic page.
- **Ctrl + Scroll wheel**: Zoom in/out on the page.
- **Shift + Left-click/box select**: Select multiple components.

For more advanced operations, use the **S** (Select) command to access the command menu:

| Shortcut Key | Detailed Command   | Function                                                                |
| :----------- | :------------------ | :---------------------------------------------------------------------- |
| E            | Lasso S**e**lect    | Lasso select, choose components within a specified range; click the left mouse button to start drawing the lasso and click again to finish. |
| I            | **I**nside Area     | Box select, choose all components within a defined area. |
| O            | **O**utside Area    | Invert selection, choose all components outside a defined area. |
| L            | Touching **L**ine   | Line select, choose components touched by lines. |
| C            | **C**onnection      | Choose components with the same net name. |
| A            | **A**ll             | Select all components. |
| T            | **T**oggle Select   | Invert selection, clicking on previously selected components deselects them, and clicking on previously unselected components selects them. |

- Rotating Components: Select the component, then press the **Space** bar.
- Copy, Cut, Paste: **Ctrl + C**, **Ctrl + X**, **Ctrl + V**.
- Auto-Increment Reference Designators after Copying: Select the component, **hold Shift while dragging** to paste the component with an incremented reference designator. You can set the step size in **TP** (**T**ools-**P**reference-Schematic-General).
- Drawing Wires: **Ctrl + W**.
- Placing Net Labels: **PN**.
- Placing Power/Ground Symbols: Left-click directly from the toolbar to select, right-click to choose different styles.

### Global Component Auto-Numbering

In larger schematic projects with numerous components, issues like duplicate or missing reference designators may arise. In such cases, you can utilize global reference numbering: **TAA**, as a substitute for manual checking.

Select the components you wish to auto-number, click **Update Change List**, then click **Accept Changes (Create ECO)**, and finally, **Execute Changes** to automatically renumber the components.

## Conclusion

The above instructions cover the fundamental operations for creating a schematic, akin to providing a set of cooking utensils. To create more flavorful "dishes," it relies largely on your **imagination** and **continuous practice**.

## References and Acknowledgments

- [Altium Corporation Altium Designer Column](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.