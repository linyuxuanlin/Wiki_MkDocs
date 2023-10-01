# Installing Library Files in Altium Designer

1. **Copy** all library files to the corresponding **Shared\Library** folder of the software;
2. Open Altium Designer, click on the **Components** page on the right panel, click on the **three-bar** icon in the upper right corner, select **File-based Library Preferences**, click on the **Installed** page, and click on the **Install** button to install the corresponding library files;
3. Several special cases:
   - The path of the Jialichuang integrated library is located in the **JLCSMT_LIB\Project Outputs for Miscellaneous Devices LC** folder;
   - If the third-party library file is not in the form of an **integrated library (.IntLib)**, but in the form of a **schematic library (SchLib)** or a **package library (PcbLib)**, both of the above two files need to be **installed simultaneously**. At this time, click on the dropdown box on the right side of the path selection window that pops up when installing the library files and switch to the **All Files (*.*)** wildcard, otherwise only the **.Intlib** format files can be seen.

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.