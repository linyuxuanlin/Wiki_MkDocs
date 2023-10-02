# Semiconductor Test Basics - AC Parameter Test

AC testing ensures that the timing characteristics of the DUT meet its specification requirements.

## Basic AC Parameters

### Setup Time

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094845.png)

Setup time refers to the minimum time that data (in the figure, `DATA IN`) must remain stable and unchanged before the reference signal (in the figure, `WE`) changes (to the middle value of 1.5V) to ensure that it can be correctly read. Before the minimum setup time, the data can change arbitrarily, but if it exceeds the minimum setup time (stays stable too late), it may not be recognized, resulting in errors. The representation in the specification is as follows:

| Parameter | Description              | Min | Max | Unit |
| --------- | ------------------------ | --- | --- | ---- |
| $t_{SD}$  | Data Set-Up to Write End | 11  |     | ns   |

### Hold Time

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094858.png)

Hold time refers to the minimum time that data (in the figure, `DATA IN`) must remain stable and unchanged after the reference signal (in the figure, `WE`) changes (reaches a certain voltage threshold) to ensure that it is error-free (or how long before the clock signal triggers it must maintain a stable level). If the hold time is too short, there is a chance that the data cannot be correctly recognized. The representation in the specification is as follows:

| Parameter | Description              | Min | Max | Unit |
| --------- | ------------------------ | --- | --- | ---- |
| $t_{HD}$  | Data Hold from Write End | 1   |     | ns   |

### Propagation Delay

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094910.png)

Propagation delay refers to the time interval between the transmission of one signal and the transmission of another related signal. Most of the time, it measures the time interval between the input signal (in the figure, `ADDR`) changing and the corresponding output (in the figure, `DATA OUT`) responding (the time required from the input end to the output end). It ensures that the output signal can appear within a certain time after the input signal appears. The representation in the specification is as follows:

| Parameter | Description           | Min | Max | Unit |
| --------- | --------------------- | --- | --- | ---- |
| $t_{AA}$  | Address to Data Valid |     | 15  | ns   |

### Minimum Pulse Widths

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094924.png)

Minimum pulse width usually includes minimum low pulse width and minimum high pulse width, which are used to ensure the minimum operable value of pulse timing. The representation in the specification is as follows:

| Parameter | Description             | Min | Max | Unit |
| --------- | ----------------------- | --- | --- | ---- |
| $t_{WL}$  | Minimum clock low time  | 20  |     | ns   |
| $t_{WH}$  | Minimum clock high time | 25  |     | ns   |

### Maximum Frequency

The maximum operating frequency, in simple terms, refers to the maximum speed at which a device can run. It is represented in the specifications as follows:

| Parameter | Description             | Min | Max  | Unit |
| --------- | ----------------------- | --- | ---- | ---- |
| $f_{MAX}$ | Maximum clock frequency |     | 22.2 | MHz  |

### Output Enable Time

Output Enable Time refers to the time required for a pin to switch from a high-impedance state (disabled) to an active drive level (high or low level), ensuring that the output buffer can change the pin state within the specified time. The time interval from the control signal being sent to the detection of the switch output is calculated during measurement. It is represented in the specifications as follows:

| Parameter | Description          | Min | Max | Unit |
| --------- | -------------------- | --- | --- | ---- |
| $t_{DOE}$ | OE LOW to Data Valid |     | 10  | ns   |

### Output Disable Time

Output Disable Time refers to the time required for a pin to switch from an active drive level (high or low level) to a high-impedance state (disabled), ensuring that the output buffer can change the pin state within the specified time. The time interval from the control signal being sent to the detection of the switch output is calculated during measurement. It is represented in the specifications as follows:

| Parameter  | Description           | Min | Max | Unit |
| ---------- | --------------------- | --- | --- | ---- |
| $t_{HZOE}$ | OE High to Data Valid |     | 8   | ns   |

## Timing Parameters

### Read Cycle Timing

An example of the read cycle timing for a 256 x 4 static RAM is shown below:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220731190300.png)

| Parameter  | Description               | Min | Max | Unit |
| ---------- | ------------------------- | --- | --- | ---- |
| $t_{RC}$   | Read Cycle Time           | 15  |     | ns   |
| $t_{AA}$   | Address to Data Valid     |     | 15  | ns   |
| $t_{ACS}$  | Chip Select to Data Valid |     | 10  | ns   |
| $t_{DOE}$  | OE LOW to Data Valid      |     | 10  | ns   |
| $t_{HZCS}$ | Chip Select to High Z     |     | 8   | ns   |
| $t_{HZOE}$ | OE HIGH to High Z         |     | 8   | ns   |
| $t_{LZCS}$ | Chip Select to Low Z      | 2   |     | ns   |
| $t_{LZOE}$ | OE LOW to Low             | 2   |     | ns   |

1. First, the length of the write cycle is determined by the $t_{RC}$ parameter.
2. Determine which signal controls the read function. In the example in the figure above, the data output of the RAM is controlled by the falling edge of OE.

### Write Cycle Timing

An example of the write cycle of a 256 x 4 static RAM:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220731190328.png)

| Parameter  | Description                   | Min | Max | Unit |
| ---------- | ----------------------------- | --- | --- | ---- |
| $t_{WC}$   | Write Cycle Time              | 15  |     | ns   |
| $t_{HZWE}$ | WE LOW to High Z              |     | 8   | ns   |
| $t_{LZWE}$ | WE HIGH to Low Z              | 2   |     | ns   |
| $t_{PWE}$  | WE Pulse Width                | 11  |     | ns   |
| $t_{SD}$   | Data Set-Up to Write End      | 11  |     | ns   |
| $t_{HD}$   | Data Hold from Write End      | 1   |     | ns   |
| $t_{SA}$   | Address Set-Up to Write Start | 2   |     | ns   |
| $t_{HA}$   | Address Hold from Write End   | 2   |     | ns   |
| $t_{SCS}$  | CS LOW to Write End           | 11  |     | ns   |
| $t_{AW}$   | Address Set-Up to Write End   | 13  |     | ns   |

1. First, the length of the write cycle is determined by the $t_{WC}$ parameter.
2. Determine which signal controls the write function. In the example in the figure above, the data input of the RAM is controlled by the rising edge of WE.

## References and Acknowledgments

- "The Fundamentals Of Digital Semiconductor Testing"

Sorry, there is no Chinese article provided to be translated. Please provide the article for translation.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.