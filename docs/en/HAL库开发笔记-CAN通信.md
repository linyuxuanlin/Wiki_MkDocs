# HAL Library Development Notes - CAN Communication 🚧

This article is based on our in-house RobotCtrl development suite, with the STM32F407ZET6 microcontroller core and TJA1050 chip for CAN communication. For the schematic and detailed information, please refer to [**RobotCtrl - STM32 Universal Development Suite**](to_be_replace[3]).

## Simple Loopback Testing Procedure

### CubeMX Configuration

1. Depending on the CAN hardware in use, open the `CAN1` or `CAN2` page on the left sidebar, check the `Activated` box, and configure these parameters in the settings:
   1. Set `Prescaler (for Time Quantum)` to `6`, and set both `Time Quanta in Bit Segment 1` and `Time Quanta in Bit Segment 2` to `3 Times`. This combination sets the bitrate to 1Mbps (maximum).
   2. Configure `ReSynchronization Jump Width` as `1 Time`, which is the maximum step size that can be adjusted during resynchronization.
   3. Set `Operating Mode` to `Loopback` for loopback testing.
2. On the `NVIC Settings` tab, enable `CANx RX0 interrupts`.

### Code Configuration

Create a `can.c` file under your project and configure the filters. Here, we have configured it in list mode, filtering the extended ID `0x2233` and standard ID `0`:

```c title="can.c"
/*
 * Function: CAN_Filter_Config
 * Description: Configure CAN filters
 * Input: None
 * Output: None
 * Call: Internal call
 */
static void CAN_Filter_Config(void) {
	CAN_FilterTypeDef CAN_FilterTypeDef;

	/* Initialize CAN filters */
	CAN_FilterTypeDef.FilterBank = 0;  // Filter group 0
	CAN_FilterTypeDef.FilterMode = CAN_FILTERMODE_IDLIST;  // Operating in list mode
	CAN_FilterTypeDef.FilterScale = CAN_FILTERSCALE_32BIT;  // Filter width is 32 bits.
	/* Enable the filter, compare based on the content of the flags, discard if not as specified, store in FIFO0 if it matches. */

	CAN_FilterTypeDef.FilterIdHigh = ((((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF0000) >> 16;  // High part of the ID to be filtered
	CAN_FilterTypeDef.FilterIdLow = (((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF; // Low part of the ID to be filtered
	CAN_FilterTypeDef.FilterMaskIdHigh = 0;  // High part of the second ID
	CAN_FilterTypeDef.FilterMaskIdLow = 0;  // Low part of the second ID
	CAN_FilterTypeDef.FilterFIFOAssignment = CAN_FILTER_FIFO0;  // Filter associated with FIFO0
	CAN_FilterTypeDef.FilterActivation = ENABLE;  // Enable the filter
	HAL_CAN_ConfigFilter(&hcan1, &CAN_FilterTypeDef);
}
```

### Testing

Open the Device Manager to check if the device is displayed. If you do not find the device or if there is a yellow exclamation mark, please visit the ST website to download the **STM32 Virtual COM Port Driver** from [here](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html).

If you have installed the driver but still cannot recognize the device properly, you can try adjusting the `Minimum Heap Size` to `0x600` or higher in CubeMX under `Project Manager` - `Project` - `Linker Settings`.

Open a serial terminal tool (baud rate can be arbitrary), send any character, and it should return the same character.

## References and Acknowledgments

- [Learning STM32CubeMX and HAL Library - Simple CAN Loopback Test](https://blog.csdn.net/weixin_45209978/article/details/119850600)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.