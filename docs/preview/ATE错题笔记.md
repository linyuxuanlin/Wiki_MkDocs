## Shmoo 相关

- 扫的频率参数需要与 DV 确认，比如要求是扫 tic 还是扫 xtal0_func。

### vbt 方式扫 shmoo 与 char studio 方式的结果不一致

比如 char studio 能扫 pass 的区域 vbt 方法却扫不出，解决方法：

1. 可能是某个频率点导致后续 fail，修改 Shmoo 分辨率，对比粗扫与精扫的结果
2. 扫之前先跑一遍原 pattern
3. 对比 vbt 与 char studio 方式的异同（扫的参数、LevelSheet、TimeSet、RelayMode）。
4. 有些 pattern 可能是要连着上一条一起跑的，这时候需要用 pattern set 的方式扫。
5. 频率 / 电压反着扫，可能会有新的收获

## PCIe

analogsetup

## XO/TCXO

**如何切机台的 TCXO**：

1. （看原理图
2. 在 powerup vbt 中注释掉 `MW_prescaler_REF 48 * MHz`
3. 在 pinmap 里把 xtal 的值改成 xtali
4. 在 timeset（e.g. tic_func_shmoo）
   1. 确保 i 给时钟，o 确保浮空
   2. 降速率到 333.333E-09，（4/tic_6M）
5. (tic pattern 和功能 pattern boot 时要等十多毫秒)
    



```new
Public Function Power_UP_Miami(VDD1p8 As Double, VDD1p95 As Double, VDD0p8 As Double, VDD0p9 As Double, _
                         VDD1p35 As Double, VDD1p2 As Double, VDD0p95 As Double, VDD33 As Double, AON_ext As Boolean, TurboL1 As Boolean, Optional SlaveMode As Boolean, Optional Datalog_Clean As Boolean) As Long
   
    Dim AVDD1p95 As Double
'''    On Error GoTo errHandler
    Dim WaitTime As Double
    Dim j As Integer
    
    
    WaitTime = 30 * ms

    If TheExec.EnableWord("Enable_VTChar") = True Or TheExec.EnableWord("Enable_TCU") = True Then
        'the following is added to support VTChar.  Basically, if VTChar enable word is set, you need to use the global variables in that file instead
'
'        VDD22 = g_avdd22
'        AVDD1p95 = g_avdd1p95
'        VDD1p28 = g_vdd1p28
'        VDD1p05 = g_vdd1p05
        VDD33 = g_vdd33
        VDD1p95 = g_vdd1p95
        VDD1p8 = g_vdd1p8
        VDD0p8 = g_vdd0p8
        VDD0p9 = g_vdd0p9
        VDD1p35 = g_vdd1p35
        VDD1p2 = g_vdd1p2
        VDD0p95 = g_vdd0p95

    End If
'    TheHdw.Utility("K_all").State = tlUtilBitOff
''    TheHdw.Wait 0.5
    
    Call ConnectBB(BBConnectToClear)
    TheHdw.Wait WaitTime
    
    If InStr(TheExec.CurrentChanmap, "MRQFN") > 0 Or InStr(TheExec.CurrentChanmap, "DRQFN") > 0 Then
        'MW_prescaler_REF 48 * MHz ''TCXO
    End If
    
     TheHdw.Digital.Pins("all_digital").InitState = chInitoff ' must hiz else SSS bootup unstable
     TheHdw.Digital.Pins("all_digital").Disconnect
     
    TheHdw.Wait WaitTime
    TheHdw.Wait 0.1 'must wait else SS bootup unstable
    
    With TheHdw.DCVI.Pins("all_power") 'all_power vdd_1p95,vdd0p9_pmu_aon,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddcx,vddio,vddq_dq,vdd4blow
        .Mode = tlDCVIModeVoltage
        .Voltage = 0
        .CurrentRange.Autorange = True
        .Current = 200 * mA 'ilimit_analog
        .NominalBandwidth = 471
        .Meter.Mode = tlDCVIMeterCurrent
        .Gate = False
        .Disconnect
    End With
    TheHdw.Wait WaitTime
    TheHdw.Wait 0.1 'must wait else SSH bootup unstable
    
    TheHdw.Utility("K1").State = tlUtilBitOff
    TheHdw.Wait WaitTime

    
    TheHdw.Digital.ApplyLevelsTiming False, True, True, tlPowered
    TheHdw.Wait WaitTime

     
    TheHdw.Digital.Pins("gpio_51,gpio_42").InitState = chInitLo  ''''Added for XTAL mode
    TheHdw.Digital.Pins("gpio_47,gpio_20").InitState = chInitHi
    TheHdw.Digital.Pins("gpio_51,gpio_42,gpio_20,gpio_47").Connect
    TheHdw.Wait WaitTime


    TheHdw.Digital.Pins("mode_1").InitState = chInitLo
    TheHdw.Digital.Pins("mode_0").InitState = chInitHi
    TheHdw.Digital.Pins("mode_1,mode_0").Connect
    TheHdw.Wait WaitTime

    TheHdw.Digital.Pins("resin_n").InitState = chInitHi 'chInitLo
    TheHdw.Digital.Pins("posh_ext_pad").InitState = chInitLo 'chInitHi FFL chinitHi bootup unstable
    TheHdw.Digital.Pins("resin_n,posh_ext_pad").Connect
    
    TheHdw.Wait WaitTime
    TheHdw.Wait 0.1 'must wait else SSH bootup unstable
    
    With TheHdw.DCVI.Pins("vdd_1p95,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddcx,vddio,vddq_dq,vdd4blow")
        .Gate = False
        .Mode = tlDCVIModeVoltage
        .CurrentRange.Autorange = True
    End With
    
    With TheHdw.DCVI.Pins("vdd33_pa")
        .Voltage = VDD33
        .Current = 0.5
    End With
    With TheHdw.DCVI.Pins("vdd_3p3")
        .Voltage = 3.3
        .Current = 0.5
    End With
    
    
    With TheHdw.DCVI
        .Pins("vddcx").Voltage = VDD0p8
        .Pins("vddcx").Current = 2
        
        .Pins("vddq_dq").Voltage = 1.2 'VDD1p2
        
        .Pins("vdd_1p95").Voltage = VDD1p95
        .Pins("vdd_1p95").Current = 1
        .Pins("pcie_0p95,uphy_0p95").Voltage = VDD0p95
        
        .Pins("vdd_1p8_rfa,vddio").Voltage = VDD1p8
        .Pins("vdd4blow").Voltage = 1.8
        .Pins("vddq_dq,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vddio,vdd4blow").Current = 1 '0.2
        
    End With
    
    If TurboL1 = True Then
        With TheHdw.DCVI
            .Pins("vddcx").Voltage = VDD0p9
        End With
    End If
  
    If AON_ext = True Then
        
        With TheHdw.DCVI.Pins("vdd0p9_pmu_aon")
            .Voltage = 0.98 ' 0.95v is not enough for SSS
            .Current = 0.3
        End With
    
    End If


    'With TheHdw.DCVI.Pins("vdd_1p95,vdd0p9_pmu_aon,vdd1p8_pmu_io,vdd1p8_pmu_rfa,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddcx,vddio,vddq_dq,vdd4blow")
    With TheHdw.DCVI.Pins("vdd_1p95,vdd0p9_pmu_aon,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddcx,vddio,vdd4blow")   '*******remove Vddq_dq here
        .Meter.Mode = tlDCVIMeterCurrent
        .Connect (tlDCVIConnectDefault)
    End With
    
    
    'Power on

    If SlaveMode = True Then
''
''        TheHdw.DCVI.Pins("VDD_3P3,VDD2P2_RF,VDD_CORE,DVDD_VCO,VDD_1P35").Gate = True
''        TheHdw.Wait WaitTime
''        TheHdw.DCVI.Pins("AVDD_1P95,VDD1P95_PMU_IN").Gate = True
''        TheHdw.Wait WaitTime
'''        TheHdw.DCVI.Pins("VDD1P8_RFA,VDD_IO,VDD1P8_BTPA,VDD1P8_QFPROM_BLOW").Gate = True
''        TheHdw.DCVI.Pins("VDD1P8_RFA,VDD_IO,VDD1P8_BTPA").Gate = True
''        TheHdw.Wait WaitTime
''        If AON_ext = True Then
''            TheHdw.DCVI.Pins("AVDD_1P05_GPHY,AVDD_1P05_PCIE,VDD1P05_PMU_AON").Gate = True
''        Else
''            TheHdw.DCVI.Pins("AVDD_1P05_GPHY,AVDD_1P05_PCIE").Gate = True
''        End If
''        TheHdw.Wait WaitTime
    Else
        
'''        TheHdw.DCVI.Pins("vddio").Gate = True
'''        TheHdw.Wait WaitTime
'''        TheHdw.DCVI.Pins("vdd_1p95").Gate = True
'''        TheHdw.Wait WaitTime
'''        TheHdw.DCVI.Pins("vdd_1p8_rfa").Gate = True
'''        TheHdw.Wait WaitTime
'''        If AON_ext = True Then
'''            TheHdw.DCVI.Pins("pcie_0p95,uphy_0p95,vdd0p9_pmu_aon").Gate = True
'''        Else
'''            TheHdw.DCVI.Pins("pcie_0p95,uphy_0p95").Gate = True
'''        End If
'''        TheHdw.Wait WaitTime

                
        TheHdw.DCVI.Pins("vdd_3p3,vdd33_pa").Gate = True
        TheHdw.Wait WaitTime

        TheHdw.DCVI.Pins("vddcx").Gate = True
        TheHdw.Wait WaitTime

        TheHdw.DCVI.Pins("vdd_1p95").Gate = True
        TheHdw.Wait WaitTime

               
''        TheHdw.DCVI.Pins("vddq_dq").Gate = True
        TheHdw.Wait WaitTime
        

        TheHdw.DCVI.Pins("vddio").Gate = True
        TheHdw.Wait WaitTime

        TheHdw.DCVI.Pins("vdd_1p8_rfa").Gate = True
        TheHdw.Wait WaitTime
        TheHdw.Wait 0.1  ' must wait else SSS bootup unstable
                TheHdw.Wait 0.3 ' added for TT cold temp bootup issue
                
        TheHdw.DCVI.Pins("pcie_0p95,uphy_0p95").Gate = True
        TheHdw.Wait WaitTime

        If AON_ext = True Then
        TheHdw.DCVI.Pins("vdd0p9_pmu_aon").Gate = True
        TheHdw.Wait WaitTime
        End If
    
    End If
      
    TheHdw.Digital.Pins("resin_n").InitState = chInitHi
    TheHdw.Wait 0.1 'WaitTime
    
    
    Dim sPower As String
    Dim pld_power As New PinListData
    Dim pld_power_core As New PinListData
    Dim pld_power_pcie As New PinListData
    
    If AON_ext = True Then
        sPower = "vdd_1p95,vdd0p9_pmu_aon,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddio,vddq_dq" 'pcie_0p95
    Else
        sPower = "vdd_1p95,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddio,vddq_dq"
    End If
    
    pld_power = TheHdw.DCVI.Pins(sPower).Meter.read(tlStrobe, 10)
    pld_power_pcie = TheHdw.DCVI.Pins("pcie_0p95").Meter.read(tlStrobe, 10)
    pld_power_core = TheHdw.DCVI.Pins("vddcx").Meter.read(tlStrobe, 10)
    
    Dim sPat As String
    sPat = ".\Patterns\TIC\TCXO_cold_boot.pat"
    
    If TheExec.Sites.Active.Count > 0 Then
        
        TheHdw.Digital.ApplyLevelsTiming True, True, True, tlPowered
        TheHdw.Patterns(sPat).Load
        TheHdw.Patterns(sPat).test pfAlways, 0
        
    End If

''''''''''''''''''''''''''''''''XOLDO WAR''''''''''''''''''''''''''''''''''''
'''''    TheHdw.Digital.ApplyLevelsTiming False, False, True, , , , , , , , "tlmm_wsi_rfa_reg_test", "Nominal", "Nominal"
'''''    TheHdw.Patterns(".\Patterns\RFA\tlmm_wsi_rfa_reg_test.pat").Load
'''''    TheHdw.Patterns(".\Patterns\RFA\tlmm_wsi_rfa_reg_test.pat").Start
'''''    TheHdw.Digital.Patgen.HaltWait
'''''
'''''     Dim sRead As New SiteLong
'''''    Atest_rfa_msip RFA_Mode
'''''
'''''    Call WSI_Long_WR_PA(&H5000&, &H555AAA, WL_CH0)
'''''
'''''      Call WSI_Long_RD_PA(&H5000&, sRead, WL_CH0)
'''''
'''''    TheExec.Datalog.WriteComment "WSI Read: " & CStr(Hex(sRead(1)))
'''''
''''''''    Call Write_Long(&H5207&, &HC300000, WL_CH0)
''''''''    Call Write_Long(&H5124&, &H300&, WL_CH0)
''''''''    Call Write_Long(&H5137&, &HAE777700, WL_CH0)
''''''''    Call Write_Long(&H5122&, &HC0000000, WL_CH0)
''''''''   Call Write_Long(&H512B&, &H2CF66220, WL_CH0)
''''''''
'''''    Call WL_ScriptWrite("wl_init_boot_up__XO_48M_try")
'''''
'''''    Call WSI_Long_RD_PA(&H5000&, sRead, WL_CH0)
'''''
'''''    TheExec.Datalog.WriteComment "WSI Read: " & CStr(Hex(sRead(1)))
'''''
'''''     'Disable Port
'''''    TheHdw.Protocol.Ports(g_WSIPortName).Enabled = False
'''''    WSI_USE_PA = False
'''''
'''''    ' Apply TIC Timing
'''''
'''''    TheHdw.Digital.ApplyLevelsTiming False, False, True, , , , , , , , "tlmm_wsi_rfa_reg_test", "Nominal", "Nominal"
'''''
'''''    'TIC mode
'''''    TheHdw.Digital.Pins("mode_0").InitState = chInitHi
'''''    TheHdw.Digital.Pins("mode_1").InitState = chInitLo
'''''    TheHdw.Wait 1 * ms
'''''
'''''''''''''''''''''''''''XOLDO WAR''''''''''''''''''''''''''''''''''''

    If Datalog_Clean = False Then
    
        TheExec.Flow.TestLimit resultVal:=pld_power_core, unit:=unitAmp, lowVal:=-0.005, hiVal:=1, ForceResults:=tlForceNone
        TheExec.Flow.TestLimit resultVal:=pld_power, unit:=unitAmp, lowVal:=-0.005, hiVal:=0.05, ForceResults:=tlForceNone
        TheExec.Flow.TestLimit resultVal:=pld_power_pcie, unit:=unitAmp, lowVal:=-0.005, hiVal:=0.8, ForceResults:=tlForceNone
        

        TheExec.Datalog.WriteComment "--------------------------------------------------------------------"
        TheExec.Datalog.WriteComment "---- Power Up ----"
        TheExec.Datalog.WriteComment "VDD1P8_RFA,VDDIO = " & CStr(VDD1p8) & "V"
        TheExec.Datalog.WriteComment "VDD1P95_PMU_IN = " & CStr(VDD1p95) & "V"
        TheExec.Datalog.WriteComment "VDDQ_DQ = " & CStr(VDD1p35) & "V"
        TheExec.Datalog.WriteComment "VDD_3P3,VDD33_PA = " & CStr(VDD33) & "V"
        TheExec.Datalog.WriteComment "VDD_CORE = " & CStr(VDD0p8) & "V"
        TheExec.Datalog.WriteComment "UPHY_0p95,PCIE_0p95 = " & CStr(VDD0p95) & "V"
        TheExec.Datalog.WriteComment "--------------------------------------------------------------------"
        
    Else
    
    End If


    Exit Function

errHandler:
    TheExec.Datalog.WriteComment "Error encountered in " & TheExec.DataManager.InstanceName + vbCrLf + _
                                 "VBT Error # " + Trim(str(err.Number)) + ": " + err.description
    'If AbortTest then Exit Function Else Resume Next
    Resume Next
End Function
```


```old
Public Function Power_UP_Miami(VDD1p8 As Double, VDD1p95 As Double, VDD0p8 As Double, VDD0p9 As Double, _
                         VDD1p35 As Double, VDD1p2 As Double, VDD0p95 As Double, VDD33 As Double, AON_ext As Boolean, TurboL1 As Boolean, Optional SlaveMode As Boolean, Optional Datalog_Clean As Boolean) As Long
   
    Dim AVDD1p95 As Double
'''    On Error GoTo errHandler
    Dim WaitTime As Double
    Dim j As Integer
    
    
    WaitTime = 3 * ms

    If TheExec.EnableWord("Enable_VTChar") = True Or TheExec.EnableWord("Enable_TCU") = True Then
        'the following is added to support VTChar.  Basically, if VTChar enable word is set, you need to use the global variables in that file instead
'
'        VDD22 = g_avdd22
'        AVDD1p95 = g_avdd1p95
'        VDD1p28 = g_vdd1p28
'        VDD1p05 = g_vdd1p05
        VDD33 = g_vdd33
        VDD1p95 = g_vdd1p95
        VDD1p8 = g_vdd1p8
        VDD0p8 = g_vdd0p8
        VDD0p9 = g_vdd0p9
        VDD1p35 = g_vdd1p35
        VDD1p2 = g_vdd1p2
        VDD0p95 = g_vdd0p95

    End If
'    TheHdw.Utility("K_all").State = tlUtilBitOff
''    TheHdw.Wait 0.5
    
    Call ConnectBB(BBConnectToClear)
    TheHdw.Wait WaitTime
    
    If InStr(TheExec.CurrentChanmap, "MRQFN") > 0 Or InStr(TheExec.CurrentChanmap, "DRQFN") > 0 Then
''        MW_prescaler_REF 48 * MHz
    End If
    
     TheHdw.Digital.Pins("all_digital").InitState = chInitoff ' must hiz else SSS bootup unstable
     TheHdw.Digital.Pins("all_digital").Disconnect
     
    TheHdw.Wait WaitTime
    TheHdw.Wait 0.1 'must wait else SS bootup unstable
    
    With TheHdw.DCVI.Pins("all_power") 'all_power vdd_1p95,vdd0p9_pmu_aon,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddcx,vddio,vddq_dq,vdd4blow
        .Mode = tlDCVIModeVoltage
        .Voltage = 0
        .CurrentRange.Autorange = True
        .Current = 200 * mA 'ilimit_analog
        .NominalBandwidth = 471
        .Meter.Mode = tlDCVIMeterCurrent
        .Gate = False
        .Disconnect
    End With
    TheHdw.Wait WaitTime
    TheHdw.Wait 0.1 'must wait else SSH bootup unstable
    
    TheHdw.Utility("K1").State = tlUtilBitOff
    TheHdw.Wait WaitTime

    
    TheHdw.Digital.ApplyLevelsTiming False, True, True, tlPowered
    TheHdw.Wait WaitTime

     
    TheHdw.Digital.Pins("gpio_51,gpio_42").InitState = chInitLo  ''''Added for XTAL mode
    TheHdw.Digital.Pins("gpio_47,gpio_20").InitState = chInitHi
    TheHdw.Digital.Pins("gpio_51,gpio_42,gpio_20,gpio_47").Connect
    TheHdw.Wait WaitTime


    TheHdw.Digital.Pins("mode_1").InitState = chInitLo
    TheHdw.Digital.Pins("mode_0").InitState = chInitHi
    TheHdw.Digital.Pins("mode_1,mode_0").Connect
    TheHdw.Wait WaitTime

    TheHdw.Digital.Pins("resin_n").InitState = chInitHi 'chInitLo
    TheHdw.Digital.Pins("posh_ext_pad").InitState = chInitLo 'chInitHi FFL chinitHi bootup unstable
    TheHdw.Digital.Pins("resin_n,posh_ext_pad").Connect
    
    TheHdw.Wait WaitTime
    TheHdw.Wait 0.1 'must wait else SSH bootup unstable
    
    With TheHdw.DCVI.Pins("vdd_1p95,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddcx,vddio,vddq_dq,vdd4blow")
        .Gate = False
        .Mode = tlDCVIModeVoltage
        .CurrentRange.Autorange = True
    End With
    
    With TheHdw.DCVI.Pins("vdd_3p3,vdd33_pa")
        .Voltage = VDD33
        .Current = 0.5
    End With
    
    
    With TheHdw.DCVI
        .Pins("vddcx").Voltage = VDD0p8
        .Pins("vddcx").Current = 2
        
        .Pins("vddq_dq").Voltage = 1.2 'VDD1p2
        
        .Pins("vdd_1p95").Voltage = VDD1p95
        .Pins("vdd_1p95").Current = 1
        .Pins("pcie_0p95,uphy_0p95").Voltage = VDD0p95
        
        .Pins("vdd_1p8_rfa,vddio,vdd4blow").Voltage = VDD1p8
        .Pins("vddq_dq,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vddio,vdd4blow").Current = 0.2
        
    End With
    
    If TurboL1 = True Then
        With TheHdw.DCVI
            .Pins("vddcx").Voltage = VDD0p9
        End With
    End If
  
    If AON_ext = True Then
        
        With TheHdw.DCVI.Pins("vdd0p9_pmu_aon")
            .Voltage = 0.98 ' 0.95v is not enough for SSS
            .Current = 0.3
        End With
    
    End If


    'With TheHdw.DCVI.Pins("vdd_1p95,vdd0p9_pmu_aon,vdd1p8_pmu_io,vdd1p8_pmu_rfa,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddcx,vddio,vddq_dq,vdd4blow")
    With TheHdw.DCVI.Pins("vdd_1p95,vdd0p9_pmu_aon,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddcx,vddio,vdd4blow")   '*******remove Vddq_dq here
        .Meter.Mode = tlDCVIMeterCurrent
        .Connect (tlDCVIConnectDefault)
    End With
    
    
    'Power on

    If SlaveMode = True Then
''
''        TheHdw.DCVI.Pins("VDD_3P3,VDD2P2_RF,VDD_CORE,DVDD_VCO,VDD_1P35").Gate = True
''        TheHdw.Wait WaitTime
''        TheHdw.DCVI.Pins("AVDD_1P95,VDD1P95_PMU_IN").Gate = True
''        TheHdw.Wait WaitTime
'''        TheHdw.DCVI.Pins("VDD1P8_RFA,VDD_IO,VDD1P8_BTPA,VDD1P8_QFPROM_BLOW").Gate = True
''        TheHdw.DCVI.Pins("VDD1P8_RFA,VDD_IO,VDD1P8_BTPA").Gate = True
''        TheHdw.Wait WaitTime
''        If AON_ext = True Then
''            TheHdw.DCVI.Pins("AVDD_1P05_GPHY,AVDD_1P05_PCIE,VDD1P05_PMU_AON").Gate = True
''        Else
''            TheHdw.DCVI.Pins("AVDD_1P05_GPHY,AVDD_1P05_PCIE").Gate = True
''        End If
''        TheHdw.Wait WaitTime
    Else
        
'''        TheHdw.DCVI.Pins("vddio").Gate = True
'''        TheHdw.Wait WaitTime
'''        TheHdw.DCVI.Pins("vdd_1p95").Gate = True
'''        TheHdw.Wait WaitTime
'''        TheHdw.DCVI.Pins("vdd_1p8_rfa").Gate = True
'''        TheHdw.Wait WaitTime
'''        If AON_ext = True Then
'''            TheHdw.DCVI.Pins("pcie_0p95,uphy_0p95,vdd0p9_pmu_aon").Gate = True
'''        Else
'''            TheHdw.DCVI.Pins("pcie_0p95,uphy_0p95").Gate = True
'''        End If
'''        TheHdw.Wait WaitTime

                
        TheHdw.DCVI.Pins("vdd_3p3,vdd33_pa").Gate = True
        TheHdw.Wait WaitTime

        TheHdw.DCVI.Pins("vddcx").Gate = True
        TheHdw.Wait WaitTime

        TheHdw.DCVI.Pins("vdd_1p95").Gate = True
        TheHdw.Wait WaitTime

               
''        TheHdw.DCVI.Pins("vddq_dq").Gate = True
        TheHdw.Wait WaitTime
        

        TheHdw.DCVI.Pins("vddio").Gate = True
        TheHdw.Wait WaitTime

        TheHdw.DCVI.Pins("vdd_1p8_rfa").Gate = True
        TheHdw.Wait WaitTime
        TheHdw.Wait 0.1  ' must wait else SSS bootup unstable
                TheHdw.Wait 0.3 ' added for TT cold temp bootup issue
                
        TheHdw.DCVI.Pins("pcie_0p95,uphy_0p95").Gate = True
        TheHdw.Wait WaitTime

        If AON_ext = True Then
        TheHdw.DCVI.Pins("vdd0p9_pmu_aon").Gate = True
        TheHdw.Wait WaitTime
        End If
    
    End If
      
    TheHdw.Digital.Pins("resin_n").InitState = chInitHi
    TheHdw.Wait 0.1 'WaitTime
    
    
    Dim sPower As String
    Dim pld_power As New PinListData
    Dim pld_power_core As New PinListData
    Dim pld_power_pcie As New PinListData
    
    If AON_ext = True Then
        sPower = "vdd_1p95,vdd0p9_pmu_aon,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddio,vddq_dq" 'pcie_0p95
    Else
        sPower = "vdd_1p95,pcie_0p95,uphy_0p95,vdd_1p8_rfa,vdd33_pa,vdd_3p3,vddio,vddq_dq"
    End If
    
    pld_power = TheHdw.DCVI.Pins(sPower).Meter.read(tlStrobe, 10)
    pld_power_pcie = TheHdw.DCVI.Pins("pcie_0p95").Meter.read(tlStrobe, 10)
    pld_power_core = TheHdw.DCVI.Pins("vddcx").Meter.read(tlStrobe, 10)
    
    Dim sPat As String
    sPat = ".\Patterns\TIC\TCXO_cold_boot.pat"
    
    If TheExec.Sites.Active.Count > 0 Then
        
        TheHdw.Digital.ApplyLevelsTiming True, True, True, tlPowered
        TheHdw.Patterns(sPat).Load
        TheHdw.Patterns(sPat).test pfAlways, 0
        
    End If

    If Datalog_Clean = False Then
    
        TheExec.Flow.TestLimit resultVal:=pld_power_core, unit:=unitAmp, lowVal:=-0.005, hiVal:=0.5, ForceResults:=tlForceNone
        TheExec.Flow.TestLimit resultVal:=pld_power, unit:=unitAmp, lowVal:=-0.005, hiVal:=0.05, ForceResults:=tlForceNone
        TheExec.Flow.TestLimit resultVal:=pld_power_pcie, unit:=unitAmp, lowVal:=-0.005, hiVal:=0.1, ForceResults:=tlForceNone
        

        TheExec.datalog.WriteComment "--------------------------------------------------------------------"
        TheExec.datalog.WriteComment "---- Power Up ----"
        TheExec.datalog.WriteComment "VDD1P8_RFA,VDDIO = " & CStr(VDD1p8) & "V"
        TheExec.datalog.WriteComment "VDD1P95_PMU_IN = " & CStr(VDD1p95) & "V"
        TheExec.datalog.WriteComment "VDDQ_DQ = " & CStr(VDD1p35) & "V"
        TheExec.datalog.WriteComment "VDD_3P3,VDD33_PA = " & CStr(VDD33) & "V"
        TheExec.datalog.WriteComment "VDD_CORE = " & CStr(VDD0p8) & "V"
        TheExec.datalog.WriteComment "UPHY_0p95,PCIE_0p95 = " & CStr(VDD0p95) & "V"
        TheExec.datalog.WriteComment "--------------------------------------------------------------------"
        
    Else
    
    End If

    Exit Function

errHandler:
    TheExec.datalog.WriteComment "Error encountered in " & TheExec.DataManager.InstanceName + vbCrLf + _
                                 "VBT Error # " + Trim(str(err.Number)) + ": " + err.description
    'If AbortTest then Exit Function Else Resume Next
    Resume Next
End Function
```