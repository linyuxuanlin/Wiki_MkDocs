# Common Tips for Using Altium Designer

- This article provides some practical tips for organizing and using Altium Designer.

## Schematic Library

### Underlining Pin Names (Active Low)

**Method**: Add a "\" symbol after each letter that needs to be underlined.  
**Example**: `RESET` with underline - `R\E\S\E\T`

## PCB Library

(to be updated)

## Schematic

### Disabling "Add Room" Operation

**Reason**: Room operation is useful in multi-channel wiring, which can apply wiring within one channel directly to other channels. Single channel does not need Room.  
**Method**:

1. Menu bar - Project - Project Options - Class Generation tab
2. Uncheck "Generate Room"

## PCB

### Adding Logo and Markings

**Reason**: If imported images are used, the created logo cannot be freely resized.  
**Method**: Use font software Font Creator, download my font library as a template on [GitHub](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/%E4%B8%93%E7%94%A8%E5%AD%97%E4%BD%93), and customize your own exclusive font library. After the font library is created, install the .ttf file and use the corresponding characters to call out the logo in Altium.

The corresponding logos for characters are shown in the following figure:  
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200207200606.png)

### Automatically Placing Components in a Designated Area

**Reason**: When the schematic is updated to the PCB, some components may move far away.  
**Method**: Select all - **TOL** - box select

### Circular Array Layout

**Method**:

1. Select object - copy
2. **EA** - check "Paste to Current Layer"
3. Click "Paste Array" - set object quantity and spacing

### Quick Via and Layer Change

**Method**: Use the keypad "+" and "-" to switch during routing.

### Uniformly Setting Via Net Properties

**Method**:

1. Right-click any unattributed via - Find Similar Objects - Set Net to Same
2. Uniformly add via net properties in the property panel

### Adding Tear Drops

**Reason**: The function of tear drops is to improve signal integrity, reduce signal loss and reflection, and reduce the risk of wire and via contact point breakage when subjected to external impact.

**Method**: Use the shortcut key **TE**.

### Wire Window

**Reason**: Tinning on wire windows can increase current flow.

**Method**: Copy the required wiring and paste it onto the corresponding Top/Bottom Solder layer.

### Operations in 3D Preview

**Method**:

- Press the number key "3" to enter the 3D preview interface.
- Press the number key "2" to return to PCB editing.
- Press the number key "0" to restore the default perspective.
- Ctrl + F to flip.
- Ctrl + scroll wheel to zoom.
- Shift + right-click to change the perspective.

### Maintaining Network Properties When Copying and Pasting

**Reason**: When copying and pasting objects with electrical properties, network properties are lost.

**Method**: Copy the object - **EA** - check "Maintain Network Name" - paste.

### Output of Soldering Position Diagram

(To be updated)

### How to Create Slots on PCB

Draw a closed shape for the slot on the **Mechanical 1 layer** of the PCB, select it, and use the shortcut keys `T` - `V` - `B` to generate the slot (it is recommended to switch to 3D view for confirmation).

## References and Acknowledgments

- [Altium Designer19 Design Compendium: Practical Operation Skills and Problem Solving Methods](https://item.jd.com/12756518.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.