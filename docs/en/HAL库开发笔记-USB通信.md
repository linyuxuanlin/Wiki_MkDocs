# HAL Library Development Notes - USB Communication 🚧

In this article, based on our in-house RobotCtrl development kit, the microcontroller core is the STM32F407ZET6, and the USB_Slave pins are `PA11` and `PA12`. For schematic diagrams and detailed information, please refer to [**RobotCtrl - STM32 Universal Development Kit**](to_be_replace[3]).

## Simple Steps for Loopback Testing

### Configuration in CubeMX

1. Configure for an external high-speed clock (HSE).
2. Set up the clock tree to ensure the end of the clock tree shows `48MHz Clocks (MHz)` as 48MHz.
3. On the `USB_OTG_FS` page, configure the `Mode` as `Device_Only`, and the default pins are `PA11` and `PA12`.
4. On the `USB_DEVICE` page, set `Class For FS IP` to `Communication Device Class (Virtual Port Com)`.

### Configuration in the Code

To implement data loopback functionality, you only need to add the following line inside the `CDC_Receive_FS` function in the `usbd_cdc_if.c` file:

```c title="usbd_cdc_if.c"
CDC_Transmit_FS(Buf, *Len); // Returns the same data
```

### Testing

Open the Device Manager to check if the device is displayed. If you don't see the device or if there is a yellow exclamation mark, please download the driver from the ST official website [**STM32 Virtual COM Port Driver**](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html).

If you have installed the driver and the device is still not recognized correctly, you can try adjusting the `Minimum Heap Size` in CubeMX - `Project Manager` - `Project` - `Linker Settings` to `0x600` or higher.

Open a terminal tool (any baud rate) and send any character. You will receive the same character in response.

## References and Acknowledgments

- [Quickly Generating USBVCP Virtual Serial Port Projects with STM32 using CubeMX HAL Library](https://blog.csdn.net/yxy244/article/details/102620249)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.