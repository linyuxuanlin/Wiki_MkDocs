# 自适应电源管理技术 - CPR

CPR(Core Power Reduction) 通俗地讲，就是找到能让芯片正常运行的最低电压，让芯片尽可能地省电、提高能效、减少发热。如果不采用 CPR，那么所有芯片都只能统一以 SS 电压运行（相对较高），以避免 yeild loss；有了 CPR。就可以根据芯片上 RO 的测量结果，来根据实际情况降低供电电压。初此之外，CPR 结果也能用来划分不同 corner 的芯片；并且因为与制程有密切联系，也能用 CPR 结果来观察 process 情况。

这篇文章将详细讲解半导体 ATE 中 CPR 的应用，相关敏感数据已隐去。

## 一些常用术语

- **RO(Ring oscillator)**: 环形振荡器
- **QUOT (Quotient)**: 1us 内 RO 的实际振荡次数。QUOT MIN/MAX 代表 Sensor 中最慢 / 最快的 RO 的实际振荡次数。
  - **Target QUOT**: 指不同电源 mode 下（比如 NOM/SVS/LSVS）下的目标 QUOT。
- **ERROR**: 偏差值，ERROR = QUOT - Target QUOT。其大小和正负将影响后续的电压推荐，使实际 QUOT 更加接近 Target QUOT。
- **GCNT**: 为计算振荡次数所设的时间周期

## CPR 的组成及原理

一颗芯片上的 CPR，由一个 CPR Controller 和许多个 Sensors 组成。其中，Sensors 分布在芯片上的不同
module 里面，并且是串联而成的，其结果也是以此 shift 回 Controller 的。

![](https://media.wiki-power.com/img/20240114154100.png)

每个 Sensor 中包含许多个 RO。我们需要计算 RO 的实际 QUOT 值，这个值是指在一个 GCNT 周期内的实际振荡次数。此时，CPR Controller 会在已经 enable 的 Sensor 中寻找最慢的 Sensor 中的 RO（下限），通过与 Target QUOT 作比较，得出 ERROR 值，从而来调节 power supply 的高低。

## Global CPR 与 Local CPR

CPR 分 Global 与 Local 两种方式。

一般来说，对 power 相对不敏感的情况，例如 CX、MX，我们一般用 Global CPR，即用统一固定的 Target QUOT（一般是 Design Engineer 提供的），只要使得最慢的 RO 的 QUOT 值对上 Target QUOT，此时的电压就是 CPR 推荐电压。

而对 power 相对敏感的，比如 CPU、APC 之类的，没有统一的 Target QUOT，就要去 search 每个芯片独有的 Target QUOT。Search 的流程是，在做 Char 的时候选定 Vmin 最差的 pattern，并在 Prod 的时候去 search 这些 pattern 的 Vmin 值，当这个值对应到选定最慢的 RO QUOT 值是多少，此时的 QUOT 就作为这颗芯片的 Target QUOT。
