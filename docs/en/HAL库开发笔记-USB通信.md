# HAL Library Development Notes - USB Communication 🚧

This article is based on the self-developed RobotCtrl development kit, with the MCU core as STM32F407ZET6 and USB_Slave pins as `PA11` and `PA12`. For schematic and detailed introduction, please refer to [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/en/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Simple Steps for Loopback Test

### Configuration in CubeMX

1. Configure as External High Speed Clock (HSE).
2. Configure the clock tree to ensure that the end of the clock tree `48MHz Clocks (MHz)` is 48MHz.
3. On the `USB_OTG_FS` page, configure `Mode` as `Device_Only`, and the default pins are `PA11` and `PA12`.
4. On the `USB_DEVICE` page, configure `Class For FS IP` as `Communication Device Class (Virtual Port Com)`.

### Configuration in Code

To implement the data loopback function, just add a line in the `CDC_Receive_FS` function of the `usbd_cdc_if.c` file:

```c title="usbd_cdc_if.c"
CDC_Transmit_FS(Buf,*Len); // Return the same data
```

### Testing

Open the device manager to see if the device is displayed. If the device is not found or there is a yellow exclamation mark, please download the driver [**STM32 Virtual COM Port Driver**](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html) from the ST official website.

If the driver has been installed but still cannot be recognized properly, try adjusting the `Minimum Heap Size` to `0x600` or higher in CubeMX - `Project Manager` - `Project` - `Linker Settings`.

Open a serial port tool (with any baud rate) and send any character, which will return the same character.

## References and Acknowledgments

- [STM32 Using CubeMX HAL Library to Quickly Generate USBVCP Virtual Serial Port Project](https://blog.csdn.net/yxy244/article/details/102620249)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.