---
id: VBT_Syntax
title: VBT Syntax
---

## TheHdw and TheExec

There're two global handles in VBT interface, to operate the hardware of the tester:

- **TheHdw (The Hardware)**: Support to access and control the instruments, and include more general function of the hardware, such as alarms.
- **TheExec (The Executive)**: To control the overall test program related functions, such as excute the test, handle the test results, record datalog.

Belows are examples of their usage:

```vb
' Set the pin p0's current range
TheHdw.DCVI.Pins("p0").CurrentRange = 0.002

' Get the path of the current output STDF file
CurrStdfFile = TheExec.Datalog.Setup.STDFOutputFile
```

## Other Data Objects

There are more global handles in VBT interface, such as **PinListData**, **DSPWave**, **RtaDataObj (Run-Time Adjust Data Object)** and so on. We will continue to explore in future articles.
