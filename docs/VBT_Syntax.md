---
id: VBT_Syntax
title: VBT Syntax
---

## TheHdw and TheExec

There are two global handles in VBT interface, to operate the hardware of the tester:

- **TheHdw (The Hardware)**: Support to access and control the instruments, and include more general function of the hardware, such as alarms.
- **TheExec (The Executive)**: To control the overall test program related functions, such as excute the test, handle the test results, record datalog.

Belows are the examples of their usage:

````vb
' Set the current range of pin p0
TheHdw.DCVI.Pins("p0").CurrentRange = 0.002

```vb
' Get the path of the current output STDF file
CurrStdfFile = TheExec.Datalog.Setup.STDFOutputFile
````

## Other Data Objects

More global handles are contained in the VBT interface, such as **PinListData**, **DSPWave**, **RtaDataObj (Run-Time Adjust Data Object)** and so on. We will continue to explore them in the future articles.
