---
id: TestInterface与TIC基础
title: Test Interface and TIC Basics
---

In semiconductor testing, **TIC (Test Interface Controller)** is a bus master controller that follows the **Test Interface** protocol in the **AMBA (Advanced Microcontroller Bus Architecture)** specification. AMBA is an on-chip communication standard for embedded microcontrollers, encompassing three types of bus protocols:

- **AHB** (the Advanced High-performance Bus)
- **ASB** (the Advanced System Bus)
- **APB** (the Advanced Peripheral Bus)

Since the philosophy of AMBA is to isolate testing of individual modules in the system, where each module's testing depends only on the bus interface, a testing method is needed to test the input and output of peripherals not connected to the bus.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262214877.png)

This testing method can be achieved through Test Interface. It uses a simple three-wire handshake to control the reading and writing of vectors, and uses **EBI (External Bus Interface)** as the data path to import external vectors into the internal bus.

## Test Interface Pins

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262225257.png)

As shown in the above figure, the Test Interface pins consist of three parts:

- A clock pin **TCLK**
- Three control pins **TREQA**, **TREQB**, and **TACK**
- A 32-bit test bus **TBUS[31:0]**

In the minimum configuration, the Test Interface only requires TREQA and TACK as dedicated pins to control the entry and exit of the test mode. Other pins can be implemented by reusing pins on the device.

TREQA/TREQB (Test Bus Request) is an input signal. During normal system operation, TREQA is used to request entry into test mode, allowing the Vector to be loaded. During the test process, TREQA and TREQB are used together to indicate the type of Vector that will be used in the next cycle.

TACK (Test Bus Acknowledge) is an output signal used to indicate the state of the bus and when a test item is complete. When TACK outputs a low level, it indicates that the current Vector needs more time until TACK becomes high. Only when TACK is high, will TREQA/TREQB read external control signals.

TCLK (Test Clock) is a clock signal input. The test clock of the Test Interface is provided externally. When switching between normal mode and test mode, TCLK is required to have no glitches.

TBUS[31:0] (Test Bus) is a 32-bit bidirectional test interface bus. In input mode, it is used to input Vector Address, Control information, and perform Write operations. In output mode, it can be used to perform Read operations. When it is necessary to change the input/output status of TBUS, the test bus protocol ensures that a cycle is provided for switching.

When the system is running normally, the truth table for the Test Interface controlled by three lines is as follows:

| TREQA | TREQB | TACK | Status                               |
| ----- | ----- | ---- | ------------------------------------ |
| 0     | 0     | 0    | Normal operation, not in test mode    |
| 1     | 0     | 0    | Request to enter test mode            |
| 0     | 1     | 0    | Reserved for external host requests   |
| -     | -     | 1    | Already entered test mode             |

Initially, TREQA is at a low level, indicating that it has not entered test mode. When TREQA is set to a high level, it requests entry into test mode. Then, when TACK outputs a high level, it indicates that TIC allows entry into test mode. At this point, TCLK becomes the internal clock source. Once in test mode, the values on the three lines and their corresponding system states are as follows:

| TREQA | TREQB | TACK | State                             |
| ----- | ----- | ---- | --------------------------------- |
| -     | -     | 0    | Current operation not yet complete |
| 1     | 1     | 1    | Address/Control/TurnAround Vector  |
| 1     | 0     | 1    | Write Test Vector                  |
| 0     | 1     | 1    | Read Test Vector                   |
| 0     | 0     | 1    | Exit test mode                     |

Next, TREQB can be set to a high level to load the Address Vector. Then read and write operations can be performed. When exiting test mode, an Address Vector should be passed first to ensure that all internal transfers have been completed. Then, both TREQA and TREQB should be set to a low level to indicate exit from test mode. Finally, TACK will output a low level, indicating that test mode has been exited.

## Types of Vectors

In the Test Interface, there are five types of vectors:

- **Address Vector**: declares the address
- **Write Test Vector**: vector for writing (0/1)
- **Read Test Vector**: vector for reading (L/H)
- **Control Vector**: vector for control
- **TurnAround Vector**: vector for turning around

The triggering of Address/Control/TurnAround Vectors is determined by the common values of TREQA/TREQB. The following rules can be used to determine the type of Vector:

- If only a single Address/Control/TurnAround Vector appears, it is an Address Vector.
- If a continuous string of Address/Control/TurnAround Vectors appears, all except the last one are Address Vectors and the last one is a Control Vector.
- After one or more Read Vectors, there will always be a TurnAround Vector (one in ASB, two in AHB).

In addition, a Burst Vector is a concatenation of multiple Write/Read Test Vectors of the same type, which can improve testing speed by applying a single Address. This Address can either remain static (using the same Address for all Vectors) or increment (depending on whether an Address incrementer has been enabled in TIC). If no incrementer is present, a static Address will be used by default.

### Address Vector

Before any Read/Write operation, an Address Vector must be passed. It follows these rules:

- TREQA/TREQB must both be set to 1 to indicate that the next cycle is an Address Vector.
- In the next cycle, the Address is loaded onto TBUS[31:0]. The values of TREQA/TREQB will determine the state of the next cycle.

In some high-speed signal systems, multiple Address Vectors may need to be loaded continuously to allow enough time for the Address to be transmitted from the external source to the internal Address bus. In this case, TIC will output a 0 on the TACK of the first Address Vector to force the loading of the second Address Vector Cycle.

### Control Vector

A Control Vector always follows one or a string of Address Vectors and is used to update the Control information inside TIC. It follows these rules:

- Both TREQA/TREQB must be set to 1 to indicate the next Cycle is for Address Vector.
- In the next Cycle, the Address is loaded onto TBUS[31:0]. TREQA/TREQB still remain as 1, and the Control Vector will appear in the next Cycle.
- In the following Cycle, the Control information will be loaded onto TBUS[31:0]. The values on TREQA/TREQB will determine the state of the next Cycle.

If an invalid Control Vector needs to be set, its first bit can be set to 0 to preserve the information but not apply it.

### Write Test Vector

After successfully entering test mode and specifying the Address, read/write operations can be performed. The Address used for Write operation is defined by the previous Address Vector. Write Test Vector can follow any of the following Vectors:

- Single Address Vector.
- Sequence of Address/Control Vectors.
- Another Write Test Vector. Forms a Write Burst.
- TurnAround Vector after a single/multiple Read operations.

When the transfer state needs to be delayed, TACK becomes low. During this waiting period, TREQA/TREQB needs to change to specify the type of the next Vector, but the Write operation on TBUS[31:0] should still continue, and Read operation should not be performed at this time.

### Read Test Vector

Similar to Write Test Vector, the Address used for Read operation depends on the previous Vector and can follow any of the following Vectors:

- Single Address Vector.
- Sequence of Address/Control Vectors.
- Another Read Test Vector. Forms a Read Burst.
- Single/multiple Write operations.

After a single or multiple Read operations, there must always be a TurnAround Vector to prevent bus conflicts on external TBUS signals.

### TurnAround Vector

TurnAround Vector can be used to change the direction of TBUS transmission when switching between Write/Read operations. It is necessary to insert TurnAround Vector when Read operation becomes Write, but this operation will not write a new Address.

---

The above is some basic knowledge about Test Interface and TIC. For the specific operation of TIC on AHB, please refer to the next article [**TIC on AHB**](https://wiki-power.com/AHB%E4%B8%8A%E7%9A%84TIC) (in progress...).

## References and Acknowledgments

- _IHI0011 - ARM advanced microcontroller bus architecture (AMBA) specification.Rev 2.0_

> Original article: <https://wiki-power.com/>  
> This article is protected by the CC BY-NC-SA 4.0 license. Please indicate the source when reprinting.