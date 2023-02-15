## Shmoo 相关

- 扫的频率参数需要与 DV 确认，比如要求是扫 tic 还是扫 xtal0_func。

### vbt 方式扫 shmoo 与 char studio 方式的结果不一致

比如 char studio 能扫 pass 的区域 vbt 方法却扫不出，解决方法：

1. 可能是某个频率点导致后续 fail，修改 Shmoo 分辨率，对比粗扫与精扫的结果
2. 扫之前先跑一遍原 pattern
3. 对比 vbt 与 char studio 方式的异同（扫的参数、LevelSheet、TimeSet、RelayMode）。
4. 频率 / 电压反着扫，可能会有新的收获
