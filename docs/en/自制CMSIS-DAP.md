# Homemade CMSIS-DAP 🚧

CMSIS-DAP is an open-source debugger launched by ARM, which supports all Cortex-ARM devices and JTAG/SWD interfaces. In the latest firmware version, it also supports the single-wire SWO interface, which can directly output corresponding data to the debug window through the SWO interface in the program, serving the purpose of serial debugging. DAP has the following features:

1. Completely open-source with no licensing restrictions, so the corresponding price will be very affordable.
2. No driver required, plug and play.
3. The latest version of DAP integrates a serial port, which can not only be used for downloading and debugging but also serve as a USB to serial port module, providing dual functionality.
4. Performance-wise, it can already meet the needs of most users.

(To be continued)

GitHub repository: [**linyuxuanlin/DashDAP**](https://github.com/linyuxuanlin/DashDAP)

## References and Acknowledgements

- [x893/CMSIS-DAP](https://github.com/x893/CMSIS-DAP)
- [Introduction to DAP on ARM's official website](http://www.keil.com/pack/doc/cmsis/DAP/html/index.html)
- [The sentiment of an electronics enthusiast: CMSIS-DAP debugger](http://www.stmcu.org.cn/module/forum/thread-610968-1-2.html)
- [CMSIS-DAP debugger on Taobao](https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-21405148310.36.78726a3dta5ieC&id=550828063764&scene=taobao_shop)
- [konosubakonoakua/Various_MCU_Debugger_DIY](https://github.com/konosubakonoakua/Various_MCU_Debugger_DIY)

---

`Version 2.0 being edited`

![](https://media.wiki-power.com/img/20200613154907.jpg)

Project online preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/DashDAP/raw/master/Hardware/DashDAP.zip"
  ></div>
</div>

## Background

CMSIS-DAP/DAP-Link has the following advantages compared to J-Link/ST-Link:

- Completely open-source with no legal risks.
- Supports virtual serial port.
- Plug and play.
- DAPLink is CMSIS-DAP, supporting drag-and-drop programming/firmware upgrade via USB.

## Hardware Section

### MCU

#### Crystal Oscillator

The chosen crystal oscillator is Murata's 8MHz passive crystal oscillator, model CSTCE8M00G53-R0, packaged in 3213 with a capacitance of 15pF. Why choose this one? Because it has a relatively small size and integrates two oscillation capacitors, which saves a lot of effort in hardware design. As for the naming convention of Murata crystal oscillator models, please refer to the table below:

![](https://media.wiki-power.com/img/20200612143451.jpg)

### Power Supply

### Functional Modules

## Software Section

### Driver

No manual driver installation is required on Win10/MacOS/Linux; manual driver installation is required on Win8 and older systems.

### Drag-and-Drop Programming (MSC)

Simply drag and drop the compiled `.hex` or `.bin` file into the virtual USB drive of DAPLink to complete the programming. If an error occurs, the error message will be stored in `FAIL.txt`.

### Virtual Serial Port (CDC)

The CDC virtual serial port function has general serial port capabilities, allowing bidirectional communication and sending interrupt commands to reset the target board.

## References and Acknowledgements

- [Difference in usage between JLink, STLink, DAPLink, and CMSIS DAP](https://blog.csdn.net/zhouml_msn/article/details/105298776)
- [Jixin · DAPLink Simulator](https://www.jixin.pro/bbs/topic/4187)
- [wuxx / nanoDAP](https://github.com/wuxx/nanoDAP)
- [LGG001 / DAPLink-Brochure](https://github.com/LGG001/DAPLink-Brochure)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
