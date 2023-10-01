# AD Basic Operations - Schematic Drawing

- Altium Designer Tutorial Series

## Background

After the warm-up in the previous chapter, we now enter the schematic drawing phase.

## Drawing Schematics

### Adjusting the Sheet

Following the basic process mentioned earlier, we have created a new project and added the schematic file to the project. At this point, a blank sheet appears. We can directly draw the schematic on it. If the schematic becomes complex, we can also **change the sheet size** to avoid overcrowding of components:

1. **Double-click** on any blank area of the sheet,
2. In the Properties panel, find the **Page Options** section,
3. Click on the Sheet Size drop-down box to change the sheet size.

### Placing Components

Next, we start placing components. The installation of libraries was explained in the previous chapter. We open the **Components** panel, click on the drop-down box displaying the name of the library, and switch to the installed library. After switching, we can search for the required component in the search box (type without pressing enter), and then **drag and drop** it into the schematic using the left mouse button. This successfully places a component.

If we forget which library a component belongs to, we can also use the global search function. Click on the **three bars** icon to the left of the library name, select **File-based Librarys Search** from the drop-down box, and search for all available libraries.

### Component Properties

The placed components have several key properties:

- **Designator**: Component reference designator. A unique identifier for the component, cannot have duplicate names. Usually represented by R1, R2... for resistors, C1, C2... for capacitors (refer to the knowledge points in the previous chapter),
- **Comment**: Component size parameters, such as resistance value, capacitance value, chip model, etc.,
- **Description**: Functional description of the component,
- **Footprint**: Links to the packaging library, matching the component with a specific PCB package,
- **Models**: Includes Simulation (simulation model), Signal Integrity (signal integrity), etc.

### Basic Operations

- **Left-click**: Select command
- **Left-click and hold**: Drag object
- **Left-double-click**: Set object properties
- **Right-click**: Cancel or pop-up command menu
- **Right-click and hold**: Drag schematic page
- **Ctrl + scroll wheel**: Zoom page
- **Shift + left-click/box select**: Select multiple components

For more advanced operations, use the command **S** (Select) to bring up the command menu:

| Shortcut | Detailed Command  | Function                                                                 |
| :------- | :---------------- | :----------------------------------------------------------------------- |
| E        | Lasso S**e**lect  | Lasso, select elements within a range; click the left mouse button to start drawing the lasso, click again to finish drawing the range |
| I        | **I**nside Area   | Box select, select all elements within the selected area                 |
| O        | **O**utside Area  | Invert selection, select all elements outside the selected area           |
| L        | Touching **L**ine | Line select, select elements touched by the line                           |
| C        | **C**onnection    | Select elements with the same network name                                 |
| A        | **A**ll           | Select all elements                                                        |
| T        | **T**oggle Select | Invert selection, click on previously selected elements to deselect them, click on previously unselected elements to select them |

- Rotating components: Select the component and press **Space**.
- Copy, cut, and paste: **Ctrl + C**, **Ctrl + X**, **Ctrl + V**.
- Automatically fill in reference designators when copying: Select the component, **hold down Shift and drag** to paste components with incrementing reference designators. The step size can be set in **TP** (**T**ools-**P**reference-Schematic-General).
- Drawing wires: **Ctrl + W**.
- Drawing net labels: **PN**.
- Placing power/ground: Select from the toolbar with **left-click**, and choose different styles with **right-click**.

### Global automatic component numbering

When the schematic project is large and there are many components, there may be duplicate or missing reference designators. In this case, global reference designator management can be used: **TAA**, instead of manual checking.

Check the components that need to be automatically numbered, click **Update Change List**, then click **Accept Changes (Create ECO)**, and **Execute Changes** to complete the automatic numbering of components.

## Summary

The above are only the most basic operations for drawing schematics, like providing a set of kitchen utensils. As for how to make more delicious dishes, it depends more on **imagination** and **continuous practice**.

## References and Acknowledgments

- [Altium Designer column of Altium company](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.