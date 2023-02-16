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

**如何把时钟源切到机台的 TCXO**：

1. 看原理图
2. 在 powerup vbt 中注释掉 `MW_prescaler_REF 48 * MHz`
3. 在 pinmap 里把 xtal 的值改成 xtali
4. 在 timeset（e.g. tic_func_shmoo）
   1. 确保 i 给时钟，o 确保浮空
   2. 降速率到 333.333E-09，（4/tic_6M）
5. (tic pattern 和功能 pattern boot 时要等十多毫秒)
