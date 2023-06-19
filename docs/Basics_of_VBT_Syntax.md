---
id: Basics_of_VBT_Syntax
title: Basics of VBT Syntax
---

## Data Objects

### TheHdw and TheExec

There are two global handles in VBT interface, to operate the hardware of the tester:

- **TheHdw (The Hardware)**: Support to access and control the instruments, and include more general functions of the hardware, such as alarms.
- **TheExec (The Executive)**: To control the overall test program-related functions, such as executing the test, handling the test results, and recording datalog.

Below are examples of their usage:

```vbscript
' Set the current range of pin p0
TheHdw.DCVI.Pins("p0").CurrentRange = 0.002
```

```vbscript
' Get the path of the current output STDF file
CurrStdfFile = TheExec.Datalog.Setup.STDFOutputFile
```

### Other Data Objects

More global handles are included in the VBT interface, such as **PinListData**, **DSPWave**, **RtaDataObj (Run-Time Adjust Data Object)** and so on. We will continue to explore them in future articles.

## Access By-instrument or By-pin

The VBT syntax supports access tester hardware **by-instrument** or **by-pin**, they are equivalent in the result. Below are examples of their usage:

```vbscript
' By-instrument Access, applies a single instrument to different pins
With TheHdw.instrument
    .Pins("Vcc").CurrentLimit = 0.75
    .Pins("Vee").ForceValue = 3.2
End With
```

```vbscript
' By-pin Access, defines a pin list and then using different instruments
With TheHdw.Pins("Vcc,Vdd,Vee")
    .instrument1.Disconnect
    .instrument2.CurrentLimit = 0.75
End With
```

## Structure of the VBT code

A VBT code file must be named as `VBT_xxx`, and the name must be unique.

The **return value** of a VBT function is expected to be 0 by default, or may cause unexpected results.

For the parameters about **timing** and **levels**, you may add them in the Instance Editor or Test Instant sheet, don't need to include in the VBT function. And you can control whether to enable them in the VBT function by following usage:

```vbscript
TheHdw.Digital.ApplyLevelsTiming
```

For the **test limits**, you can use the following code:

```vbscript
TheExec.Flow.TestLimit
```

to compare a result value against low/high limits, and send the test result(`TL_SUCCESS`/`TL_ERROR`) and other information to the datalog.

To see more clearly **the basic structure** of a VBT test function, here is a sample:

```vbscript
Public Function VBTLeakTest(Pins As PinList, ForceVoltage As Double, PrePattern As PatternSet) As Long
    On Error GoTo errHandler

    Dim measure_results As New PinListData

    ' Set up timing and levels for Preconditioning Pattern
    TheHdw.Digital.ApplyLevelsTiming ConnectAllPins:=True, loadLevels:=True, loadTiming:=True, relaymode:=tlPowered

    ' Run Preconditioning Pattern and test for Pass/Fail
    TheHdw.Patterns(PrePattern).test pfAlways, 0

    ' Force V, Measure I
    With TheHdw.DCVI.Pins(Pins)
        .Mode = tlDCVIModeVoltage
            ... ' Addition code
        measure_results = .Meter.Read
    End With

    ' Test using limits in flow and write datalog
    Call TheExec.Flow.TestLimit(resultval:=measure_results, unit:=unitAmp, forceval:=ForceVoltage, forceunit:=unitVolt, ForceResults:=tlForceFlow)

    ' Reset the variable
    measure_results = Nothing

    Exit Function
errHandler:
    If AbortTest Then Exit Function Else Resume Next
End Function
```

## Multi-site

🚧

## PinList Operation

🚧

## Tips in VBA

- Avoid saving code in VBA, because this will create internal hard links in the workbook. Saving in DataTool interface instead.
- If you meet the error "Procedure Too Large", you may against the Excel restriction of 64K limit per vb file. But actually, it is possible that you forgot to switch the version from 32bit to 64bit of the Windows system.
