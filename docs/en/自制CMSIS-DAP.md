# DIY CMSIS-DAP 🚧

CMSIS DAP is an open-source emulator launched by ARM, which supports all Cortex-ARM devices and JTAG/SWD interfaces. In the latest firmware version, it also supports single-wire SWO interfaces, which can directly output corresponding data to the debugging window through the SWO interface in the program, serving a similar purpose as serial debugging. DAP has the following features:

1. Completely open-source, with no license restrictions, so the corresponding price will be very cheap
2. Plug and play, no need for drivers
3. The latest version of DAP integrates a serial port, which can be used as a USB-to-serial module in addition to downloading and debugging, serving two purposes with one device
4. Performance can already meet the needs of general users

(Under construction)

GitHub repository: [**linyuxuanlin/DashDAP**](https://github.com/linyuxuanlin/DashDAP)

## References and Acknowledgments

- [x893/CMSIS-DAP](https://github.com/x893/CMSIS-DAP)
- [ARM official website's introduction to DAP](http://www.keil.com/pack/doc/cmsis/DAP/html/index.html)
- [The sentiment of an electronic otaku: CMSIS DAP emulator](http://www.stmcu.org.cn/module/forum/thread-610968-1-2.html)
- [CMSIS DAP emulator](https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-21405148310.36.78726a3dta5ieC&id=550828063764&scene=taobao_shop)
- [konosubakonoakua/Various_MCU_Debugger_DIY](https://github.com/konosubakonoakua/Various_MCU_Debugger_DIY)

---

`Version 2.0 being edited`

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200613154907.jpg)

Project online preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/DashDAP/raw/master/Hardware/DashDAP.zip"
  ></div>
</div>

## Background

CMSIS-DAP/DAP-Link has the following advantages over J-Link/ST-Link:

- Completely open-source, no legal risks
- Supports virtual serial port
- Driver-free
- DAPLink is CMSIS-DAP, supporting USB drag-and-drop burning/firmware upgrade

## Hardware Part

### MCU

#### Crystal Oscillator

We chose Murata's 8MHz passive crystal oscillator, model CSTCE8M00G53-R0, packaged in 3213, with a capacitance of 15pF. Why did we choose this one? Because it is relatively small in size and integrates the two oscillation capacitors, which can save a lot of trouble in hardware design. As for the naming convention of Murata crystal oscillator models, please refer to the table below:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200612143451.jpg)

### Power Supply

### Functional Module

## Software Part

### Driver

No manual driver installation is required on Win10/MacOS/Linux; Win8 and older systems require manual driver installation.

### Drag-and-Drop Download (MSC)

Simply drag and drop the compiled `.hex` or `.bin` file into DAPLink's virtual U disk to complete the burning. If an error occurs, the error message will be stored in `FAIL.txt`.

### Virtual Serial Port (CDC)

The CDC virtual serial port function has general serial port functions, allowing bidirectional communication and sending interrupt commands to reset the target board.

## References and Acknowledgments

- [Differences between JLink, STLink, DAPLink, and CMSIS DAP](https://blog.csdn.net/zhouml_msn/article/details/105298776)
- [Jixin · DAPLink Simulator](https://www.jixin.pro/bbs/topic/4187)
- [wuxx / nanoDAP](https://github.com/wuxx/nanoDAP)
- [LGG001 / DAPLink-Brochure](https://github.com/LGG001/DAPLink-Brochure)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
