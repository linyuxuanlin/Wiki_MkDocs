# HAL Library Development Notes - USB Communication 🚧

This article is based on the in-house RobotCtrl development kit, with the microcontroller core being the STM32F407ZET6. The USB_Slave pins are `PA11` and `PA12`. For the schematic and detailed information, please refer to [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/en/RobotCtrl-STM32-Universal-Development-Kit).

## Simple Loopback Test Steps

### Configuration in CubeMX

1. Configure for an external high-speed clock (HSE).
2. Set up the clock tree, ensuring that the "48MHz Clocks (MHz)" at the end of the clock tree is set to 48MHz.
3. On the `USB_OTG_FS` page, configure the `Mode` as `Device_Only`, with the default pins being `PA11` and `PA12`.
4. On the `USB_DEVICE` page, set the `Class For FS IP` to `Communication Device Class (Virtual Port Com)`.

### Configuration in Code

To implement data loopback functionality, you only need to add one line within the `CDC_Receive_FS` function in the `usbd_cdc_if.c` file:

```c title="usbd_cdc_if.c"
CDC_Transmit_FS(Buf, *Len); // Returns the same data
```

### Testing

Open Device Manager to check if the device is displayed. If you cannot find the device or see a yellow exclamation mark, please download the driver from the ST website: [**STM32 Virtual COM Port Driver**](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html).

If you have installed the driver and still cannot recognize the device correctly, try adjusting the `Minimum Heap Size` to `0x600` or higher in CubeMX - `Project Manager` - `Project` - `Linker Settings`.

Open a terminal tool (baud rate can be set arbitrarily), and you will observe that when you send any character, it will return the same character.

## References and Acknowledgments

- [STM32 USBVCP Virtual Serial Port Project Generation Using CubeMX HAL Library](https://blog.csdn.net/yxy244/article/details/102620249)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.