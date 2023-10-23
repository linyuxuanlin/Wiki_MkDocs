# HAL Library Development Notes - CAN Communication 🚧

This article is based on the in-house RobotCtrl development kit, with the microcontroller core being STM32F407ZET6, and TJA1050 chip used for CAN communication. For the schematic and detailed information, please refer to [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Simple Steps for Loopback Testing

### Configuration within CubeMX

1. Depending on the CAN hardware used, on the left sidebar, click on either `CAN1` or `CAN2` page, check `Activated`. In the parameter page, configure these settings:
   1. Set `Prescaler (for Time Quantum)` to `6`, and set both `Time Quanta in Bit Segment 1` and `Time Quanta in Bit Segment 2` to `3 Times`. This combination sets the bitrate to 1Mbps (maximum).
   2. Configure `ReSynchronization Jump Width` as `1 Time`, which is the maximum step adjustable during resynchronization.
   3. Set `Operating Mode` to `Loopback` for loopback testing.
2. On the `NVIC Settings` tab, enable `CANx RX0 interrupts`.

### Configuration within the Code

Create a `can.c` under your project and set the filter. Here, we are configuring it in list mode, filtering the extended ID `0x2233`, and standard ID `0`:

```c title="can.c"/*
 * Function: CAN_Filter_Config
 * Description: Configure CAN filters
 * Input: None
 * Output: None
 * Call: Called internally
 */
static void CAN_Filter_Config(void) {
    CAN_FilterTypeDef CAN_FilterTypeDef;

    /* Initialize CAN filters */
    CAN_FilterTypeDef.FilterBank = 0; // Filter group 0
    CAN_FilterTypeDef.FilterMode = CAN_FILTERMODE_IDLIST; // Operating in list mode
    CAN_FilterTypeDef.FilterScale = CAN_FILTERSCALE_32BIT; // Filter bit width is single 32-bit.
    /* Enable filters, based on the content of the flag, compare and filter out if the extended ID does not match as shown below, it will be discarded, and if it matches, it will be stored in FIFO0. */

    CAN_FilterTypeDef.FilterIdHigh = ((((uint32_t) 0x2233 << 3) | CAN_ID_EXT | CAN_RTR_DATA) & 0xFFFF0000) >> 16; // High part of the ID to be filtered
    CAN_FilterTypeDef.FilterIdLow = (((uint32_t) 0x2233 << 3) | CAN_ID_EXT | CAN_RTR_DATA) & 0xFFFF; // Low part of the ID to be filtered
    CAN_FilterTypeDef.FilterMaskIdHigh = 0; // High part of the second ID
    CAN_FilterTypeDef.FilterMaskIdLow = 0; // Low part of the second ID
    CAN_FilterTypeDef.FilterFIFOAssignment = CAN_FILTER_FIFO0; // Filter is associated with FIFO0
    CAN_FilterTypeDef.FilterActivation = ENABLE; // Enable the filter
    HAL_CAN_ConfigFilter(&hcan1, &CAN_FilterTypeDef);
}
```

### Testing

Open the Device Manager to check if the device is already displayed. If you do not find the device or see a yellow exclamation mark, please visit the official ST website to download the [**STM32 Virtual COM Port Driver**](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html).

If you have installed the driver and the device is still not recognized correctly, you can try adjusting the `Minimum Heap Size` to `0x600` or higher in CubeMX under `Project Manager` - `Project` - `Linker Settings`.

Open a serial communication tool (baud rate can be any), send any character, and it should return the same character.

## References and Acknowledgments

- [STM32CubeMX and HAL Library Learning - Simple CAN Loopback Test](https://blog.csdn.net/weixin_45209978/article/details/119850600)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.