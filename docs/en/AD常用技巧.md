# Common Techniques for Altium Designer

Here, we've compiled some practical tips and tricks for using Altium Designer.

## Schematic Library Section

### Underlining Pin Names (Active Low)

**Method**: Add a backslash "\" after each letter that needs underlining.  
**Example**: `RESET` with underlining - `R\E\S\E\T`

## PCB Footprint Library Section

(To be updated)

## Schematic Section

### Disabling Add Room Function

**Reason**: Room operations are more useful in multi-channel routing, where you can apply wiring within one channel to other channels. Single-channel designs can skip using Room.
**Method**:

1. Menu bar - Project - Project Options - Class Generation tab.
2. Uncheck "Generate Room."

## PCB Section

### Adding Logos and Labels

**Reason**: Importing images directly results in logos that cannot be freely resized.
**Method**: Use the Font Creator software, download my custom font library as a template from [GitHub](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/%E4%B8%93%E7%94%A8%E5%AD%97%E4%BD%93), and create your personalized font library. After creating the font library, install the .ttf file, and you can use the corresponding characters to insert logos in Altium.

Character-to-logo mapping is as follows:  
![Logo](https://img.wiki-power.com/d/wiki-media/img/20200207200606.png)

### Automatically Placing Components in a Defined Area

**Reason**: When transferring a schematic to the PCB, some components may be placed far from their intended location.
**Method**: Select all components - **TOL** - draw a bounding box.

### Circular Array Layout

**Method**:

1. Select an object - Copy.
2. **EA** - Check "Paste to Current Layer."
3. Click "Paste Array" - Set the number of objects and spacing.

### Quick Via Creation and Layer Change

**Method**: During routing, use the numpad + / - keys to toggle between layers.

### Uniformly Setting Via Network Attributes

**Method**:

1. Right-click on any unattributed via - Find Similar Objects - Set Net to Same.
2. In the properties panel, uniformly assign via network attributes.

### Adding Teardrops

**Reason**: Teardrops enhance signal integrity, reduce signal loss and reflections, and lower the risk of wire-to-via contact point breakage during external force impacts.
**Method**: Use the shortcut key **TE**.

### Windowing Traces

**Reason**: Tinning traces can increase current-carrying capacity.
**Method**: Copy the desired trace, paste it into the corresponding Top/Bottom Solder layer.

### Operations in 3D Preview

**Method**:

- Press the number "3" to enter 3D preview mode.
- Press the number "2" to return to PCB editing.
- Press the number "0" to reset the default view.
- Ctrl + F to flip.
- Ctrl + scroll wheel to zoom.
- Shift + right-click to change the view.

### Maintaining Network Attributes During Copy-Paste

**Reason**: When copying and pasting objects with electrical attributes, network properties may be lost.
**Method**: Copy the object - **EA** - Check "Preserve Network Names" - Paste.

### Outputting Assembly Designator Graphics

(To be updated)

### Creating Slots on the PCB

To create slots on the PCB, draw a closed shape on **Mechanical Layer 1**, select it, and use the shortcut keys `T` - `V` - `B` to generate the slot (preferably switch to 3D view for confirmation).

## References and Acknowledgments

- [Altium Designer 19 Design Compendium: Practical Operations and Troubleshooting Techniques](https://item.jd.com/12756518.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.