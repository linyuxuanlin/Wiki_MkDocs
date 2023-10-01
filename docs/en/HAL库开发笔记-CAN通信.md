# HAL Library Development Notes - CAN Communication 🚧

This article is based on the self-developed RobotCtrl development kit, with the MCU core being STM32F407ZET6 and the CAN communication using TJA1050 chip. For schematic and detailed introduction, please refer to [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Simple Steps for Loopback Test

### Configuration in CubeMX

1. According to the CAN hardware used, open the `CAN1` or `CAN2` page in the left column, check `Activated`, and configure these parameters on the parameter page:
   1. Set `Prescaler (for Time Quantum)` to `6`, and set `Time Quanta in Bit Segment 1` and `Time Quanta in Bit Segment 2` to `3 Times`. This combination sets the bit rate to 1Mbps (maximum).
   2. Configure `ReSynchronization Jump Width` to `1 Time`, which is the maximum step size that can be adjusted when resynchronizing.
   3. Configure `Operating Mode` to `Loopback` for loopback testing.
2. On the `NVIC Settings` tab, enable `CANx RX0 interrupts`.

### Configuration in Code

Create `can.c` under the project, set the filter, and configure the list mode to filter extended ID `0x2233` and standard ID `0`:

```c title="can.c"/*
 * Function Name: CAN_Filter_Config
 * Description: Configuration of CAN filter
 * Input: None
 * Output: None
 * Call: Internal call
 */
static void CAN_Filter_Config(void) {
	CAN_FilterTypeDef CAN_FilterTypeDef;

/* CAN filter initialization */
CAN_FilterTypeDef.FilterBank = 0; // Filter group 0
CAN_FilterTypeDef.FilterMode = CAN_FILTERMODE_IDLIST; // Work in list mode
CAN_FilterTypeDef.FilterScale = CAN_FILTERSCALE_32BIT; // Filter width is a single 32-bit.
/* Enable the filter, compare and filter according to the content of the flag. If the extended ID is not as follows, it will be discarded. If it is, it will be stored in FIFO0. */

CAN_FilterTypeDef.FilterIdHigh = ((((uint32_t) 0x2233 << 3) | CAN_ID_EXT
        | CAN_RTR_DATA) & 0xFFFF0000) >> 16; // High bit of ID to be filtered
CAN_FilterTypeDef.FilterIdLow = (((uint32_t) 0x2233 << 3) | CAN_ID_EXT
        | CAN_RTR_DATA) & 0xFFFF; // Low bit of ID to be filtered
CAN_FilterTypeDef.FilterMaskIdHigh = 0; // High bit of second ID
CAN_FilterTypeDef.FilterMaskIdLow = 0; // Low bit of second ID
CAN_FilterTypeDef.FilterFIFOAssignment = CAN_FILTER_FIFO0; // Filter is associated with FIFO0
CAN_FilterTypeDef.FilterActivation = ENABLE; // Enable filter
HAL_CAN_ConfigFilter(&hcan1, &CAN_FilterTypeDef);
}
```

### Test

Open the device manager to check if the device is displayed. If the device is not found or there is a yellow exclamation mark, please download the **STM32 Virtual COM Port Driver** from the ST website.

If the driver is installed but still cannot be recognized, try adjusting the `Minimum Heap Size` to `0x600` or higher in CubeMX - `Project Manager` - `Project` - `Linker Settings`.

Open the serial port tool (baud rate is arbitrary) and send any character. The same character will be returned.

## References and Acknowledgments

- [STM32CubeMX and HAL Library Learning - Simple CAN Loopback Test](https://blog.csdn.net/weixin_45209978/article/details/119850600)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.