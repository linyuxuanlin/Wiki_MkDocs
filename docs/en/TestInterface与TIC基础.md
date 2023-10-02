# Test Interface and TIC Basics

In semiconductor testing, the **Test Interface Controller (TIC)** is a bus master controller that follows the **Test Interface** protocol in the **Advanced Microcontroller Bus Architecture (AMBA)** specification. AMBA is an on-chip communication standard for embedded microcontrollers, encompassing three bus protocols:

- **AHB** (the Advanced High-performance Bus)
- **ASB** (the Advanced System Bus)
- **APB** (the Advanced Peripheral Bus)

Since the philosophy of AMBA is to isolate testing for individual modules in the system, each module's testing relies only on the bus interface. A testing method is needed to test the input and output of peripherals not connected to the bus.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262214877.png)

This testing method can be implemented through the Test Interface. It uses a simple three-way handshake to control Vector read/write and uses the **External Bus Interface (EBI)** as the data path to import external Vectors into the internal bus.

## Test Interface Pins

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262225257.png)

As shown in the above figure, the Test Interface pins consist of three parts:

- A clock pin **TCLK**
- Three control pins **TREQA**, **TREQB**, and **TACK**
- A 32-bit test bus **TBUS[31:0]**

In the minimum configuration, the Test Interface only needs TREQA and TACK as **dedicated pins** to control entry and exit of the testing mode. Other pins can be implemented by reusing pins on the device.

**TREQA/TREQB (Test Bus Request)** is an **input** signal. During normal system operation, TREQA is used to request entry into the testing mode, allowing Vectors to be loaded. During testing, TREQA and TREQB are used together to indicate the type of Vector to be used in the next cycle.

**TACK (Test Bus Acknowledge)** is an **output** signal used to indicate the state of the bus and when a test item is completed. When TACK outputs a low level, it indicates that the current Vector needs more time until TACK becomes high. TREQA/TREQB only reads external control signals when TACK is high.

**TCLK (Test Clock)** is a clock signal input. The testing clock of the Test Interface is provided externally. When switching between normal mode and testing mode, a glitch-free TCLK clock is required.

**TBUS[31:0] (Test Bus)** is a 32-bit bidirectional test interface bus. In the input state, it is used to pass Vector Address, Control information, and perform Write operations. In the output state, it can be used to perform Read operations. When it is necessary to change the TBUS input/output state, the test bus protocol ensures that a cycle is provided for switching.

When the system is operating normally, the truth table for the Test Interface controlled by three lines is as follows:

| TREQA | TREQB | TACK | Status                    |
| ----- | ----- | ---- | ------------------------- |
| 0     | 0     | 0    | Normal operation, not in test mode |
| 1     | 0     | 0    | Request to enter test mode |
| 0     | 1     | 0    | Reserved for external host requests |
| -     | -     | 1    | Entered test mode |

Initially, TREQA is low, indicating that the system has not entered test mode. When TREQA is set to high, a request to enter test mode is made. Then, when TACK outputs high, it indicates that TIC allows entry into test mode. At this point, TCLK becomes the internal clock source. Once in test mode, the values on the three lines and their corresponding system states are as follows:

| TREQA | TREQB | TACK | Status                              |
| ----- | ----- | ---- | ----------------------------------- |
| -     | -     | 0    | Current operation not yet completed |
| 1     | 1     | 1    | Address/Control/TurnAround Vector   |
| 1     | 0     | 1    | Write Test Vector                   |
| 0     | 1     | 1    | Read Test Vector                    |
| 0     | 0     | 1    | Exit test mode                       |

Next, TREQB can be set to high to load the Address Vector. Read and write operations can then be performed. When exiting test mode, an Address Vector should be passed first to ensure that all internal transfers have been completed. Then, both TREQA and TREQB should be set to low to indicate that test mode is being exited. Finally, TACK will output low, indicating that test mode has been exited.

## Types of Vectors

In the Test Interface, there are five types of Vectors:

- **Address Vector**: Vector that declares an address
- **Write Test Vector**: Vector written (0/1)
- **Read Test Vector**: Vector read (L/H)
- **Control Vector**: Vector that controls
- **TurnAround Vector**: Vector that turns around

The triggering of Address/Control/TurnAround Vectors is determined by the common values of TREQA/TREQB. To determine the type of Vector, the following rules can be followed:

- If only a single Address/Control/TurnAround Vector appears, it is an Address Vector.
- If a continuous string of Address/Control/TurnAround Vectors appears, all but the last one are Address Vectors and the last one is a Control Vector.
- After one or more Read Vectors, there will always be a TurnAround Vector. (In ASB, there is only one, while in AHB, there are two.)

In addition, a **Burst Vector** is a series of multiple Write/Read Test Vectors strung together (note that they are of the same type, not mixed). This reduces testing time as only one Address needs to be applied. This Address can be static (all Vectors use the same Address initially passed in) or incrementing (depending on whether the TIC has an enabled Address incrementer). If there is no incrementer, a static Address will be used by default.

### Address Vector

Before any Read/Write operation, the Address Vector must be passed. It follows the following rules:

- TREQA/TREQB must be set to 1 to indicate that the next cycle is the Address Vector.
- In the next cycle, the Address is loaded onto TBUS[31:0]. At this time, the values on TREQA/TREQB will jointly determine the state of the next cycle.

In some high-speed signal systems, it may be necessary to continuously load multiple Address Vectors (increasing enough time for the Address to be transmitted from the external to the internal Address bus). In this case, TIC will force the second Address Vector Cycle to be loaded when the TACK output of the first Address Vector is 0.

### Control Vector

The Control Vector always follows one or a series of Address Vectors and is used to update the Control information inside TIC. It follows the following rules:

- TREQA/TREQB must be set to 1 to indicate that the next cycle is the Address Vector.
- In the next cycle, the Address is loaded onto TBUS[31:0]. At this time, TREQA/TREQB are still set to 1, and the Control Vector will appear in the next cycle.
- In the next cycle, the Control information will be loaded onto TBUS[31:0]. At this time, the values on TREQA/TREQB will determine the state of the next cycle.

If an invalid Control Vector needs to be set, its first bit can be set to 0 to preserve but not apply the information in the Control Vector.

### Write Test Vector

After successfully entering the test mode and specifying the Address, Read/Write operations can be performed. The Address used for Write operations is defined by the previous Address Vector. Write Test Vectors can follow:

- A single Address Vector.
- A sequence of Address/Control Vectors.
- Another Write Test Vector to form a Write Burst.
- TurnAround Vector after a single/multiple Read operations.

When the transmission state needs to be delayed, TACK will become low. During this waiting time, TREQA/TREQB needs to change to specify the type of the next Vector, but the Write operation performed on TBUS[31:0] should still continue, and no Read operation should be performed at this time.

### Read Test Vector

Similar to Write Test Vector, the Address used for Read operations depends on the previous Vector and can follow:

- A single Address Vector.
- A sequence of Address/Control Vectors.
- Another Read Test Vector to form a Read Burst.
- A single/multiple Write operations.

After a single or multiple Read operations, there must always be a TurnAround Vector to prevent bus conflicts in external TBUS signals.

### TurnAround Vector

The TurnAround Vector can be used to change the direction of TBUS transmission between Write/Read operations. It is necessary to insert a TurnAround Vector when Read operations become Write operations. This operation does not write a new Address.

---

The above is some basic knowledge about Test Interface and TIC. For the specific operation of TIC on AHB, please refer to the next article [**TIC on AHB**](https://wiki-power.com/AHB%E4%B8%8A%E7%9A%84TIC) (in progress...).

## References and Acknowledgments

- _IHI0011 - ARM advanced microcontroller bus architecture (AMBA) specification.Rev 2.0_

Sorry, there is no Chinese article provided to be translated. Please provide the article to be translated.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.