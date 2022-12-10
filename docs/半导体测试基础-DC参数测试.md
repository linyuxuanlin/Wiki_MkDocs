---
id: 半导体测试基础-DC参数测试
title: 半导体测试基础 - DC 参数测试
---

DC 参数测试，测的主要是器件上单个引脚的一些特性。对大多数的 DC 参数来说，实质上是在测半导体的电阻率，而解释电阻率用的是欧姆定律。如需验证 DC 测试流程的可行性，也可以借电阻器来等效 DUT，以排除 DUT 之外的问题。比方说，在芯片规格书里出现的参数 VOL：

| Parameter | Description        | Test Conditions        | Min | Max | Units |
| --------- | ------------------ | ---------------------- | --- | --- | ----- |
| VOL       | Output LOW Voltage | VDD = Min, IOL = 8.0mA |     | 0.4 | V     |

我们可以看出，VOL 最大值为 0.4V，IOL 为 8mA，即当输出逻辑低电平的情况下，必须是在不大于 0.4V 的电压下产生 8mA 的电流，所以我们可以得出，这个器件的最大电阻不超过 50Ω。所以，可以借用不大于 50Ω 的电阻替代 DUT，以验证测试流程。我们的目的是把问题聚焦在 DUT 上，而非 DUT 以外的问题。

## IDD & Gross IDD

IDD 表示的是 CMOS 电路中从漏极（D）到漏极（D）的电流（I），如果是 TTL 电路则称为 ICC（从集电极到集电极的电流）。Gross IDD 指的是流入 VDD 管脚的总电流（在 Wafer Probe 或成品阶段都可测试）。IDD 是看芯片总电流会不会超标，一般要看最低功耗和最大工频下的电流。

测试 Gross IDD 是为了判断能否继续测 DUT。通常这个测试紧接 OS 测试，是 DUT 通电后的第一个测试。如果 Gross IDD 测试不通过（如电流过大），那就不能接着测下去了。

在 Gross IDD 测试阶段时，还不知道预处理是否可以正常进行，所以需要放宽 IDD 规范。待 Gross IDD 测试通过之后进行预处理程序，才可以准确定义出 IDD 规范电流。

Gross IDD 测试需要先通过重置，以将所有输入引脚设低 / 高电平，通常 VIL 设置为 0V、VIH 设置为 VDD，所有输出引脚空载（防止悬空产生漏电流，使 IDD 变大）。测试的示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220728162655.png)

需要注意的事项：

- 需要设置电流钳，防止电流过大损坏测试设备。
- 如果出现负电流，也代表测试不通过。
- 如果测试发生错误，可以先排除是测试设备的问题，不加芯片空着 socket 跑测试，其电流应该是 0，否则意味着 DUT 以外的设备也在消耗电流。

### IDD 测试 - 静态法

静态 IDD 测试，测量的是流入 VDD 引脚的总电流一般需要 DUT 运行在最低功耗的模式下。静态 IDD 与 Gross IDD 测试的区别是，Gross IDD 还没有预处理程序，只是一种粗测，而静态 IDD 测试是已有预处理模式，通过预处理后再进行的测试。

举个例子，下表是一个 IDD 参数样本：

| Parameter  | Description          | Test Conditions                   | Min | Max | Units |
| ---------- | -------------------- | --------------------------------- | --- | --- | ----- |
| IDD Static | Power Supply Current | VDD = 5.25V, inputs = VDD, Iout=0 |     | +22 | µA    |

IDD 静态测试的示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220728162341.png)

测试流程如下：

1. 用测试矢量将 DUT 设置为消耗电流最少、保持在静态的状态。
2. 检测引脚电流值
   - 高于 IDD Spec：Fail
   - 其他区间：Pass

测试时，通常需要在上电与采样之间加延时，让寄生电容充满电，避免造成干扰。

如果需要测试不同逻辑下的静态电流，可以测 IDDQ 参数，增加测试覆盖率（IDDQ 是测某个静止逻辑状态下的电流，比如说开一部分 MOS 管进行某个状态下的测试）。

### IDD 测试 - 动态法

IDD 动态测试的目的，是测试 DUT 在 **动态执行功能** 时（通常为 DUT 最大工频）消耗的电流，确保其不会超过标称值。

举个例子，下表是一个动态 IDD 参数样本：

| Parameter   | Description          | Test Conditions                             | Min | Max | Units |
| ----------- | -------------------- | ------------------------------------------- | --- | --- | ----- |
| IDD Dynamic | Power Supply Current | VDD = 5.25V（commercial）, f=f_max（66MHz） |     | +18 | mA    |

测试的示意图：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220728171447.png)

测试流程与静态法相似。

## VOL/IOL & VOH/IOH

VOL 表示低电平（L）输出（O）时的最高电压（V）限制（不会被识别成逻辑 1）。IOL 表示低电平（L）输出（O）时灌电流（I，sink）的驱动能力。它们共同衡量的是引脚 Buffer 在输出低电平时的阻抗，保证在适当输出的电压下能吸收恒定的电流值。

VOH 表示高电平（H）输出（O）时的最低电压（V）限制（不会被识别成逻辑 0）。IOL 表示高电平（H）输出（O）时拉电流（I，source）的驱动能力。它们共同衡量的是 Buffer 在输出高电平时的阻抗，保证在适当输出的电压下能输出恒定的电流值。

举个例子，下表是 256 x 4 Static RAM 的 VOL/IOL & VOH/IOH 参数：

| Parameter | Description         | Test Conditions           | Min | Max | Units |
| --------- | ------------------- | ------------------------- | --- | --- | ----- |
| VOL       | Output LOW Voltage  | VDD = 4.75V, IOL = 8.0mA  |     | 0.4 | V     |
| VOH       | Output HIGH Voltage | VDD = 4.75V, IOH = -5.2mA | 2.4 |     | V     |

对 VOL/IOL & VOH/IOH 的测试，主要是验证当施加拉或灌电流时，VOL/VOH 是否处于正确的电平（在输出一定的电流下能不能达到电平阈值）。测试方法有静态法与动态法。**静态法是对引脚施加电流，再逐一测电压；动态法是在功能测试中提供 VREF，形成动态负载电流再测电压的。**。

### VOL/IOL 测试 - 串行静态法

使用串行静态法测量 VOL/IOL 的测试示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220728150542.png)

测试流程如下：

1. 需要先通过预处理，将待测引脚设置为低电平输出。
2. 向引脚施加恒定的 IOH，等待 1-5 毫秒再测量（在 PMU 设 delay）。
3. 检测引脚电压
   - 高于 VOL（+0.4V）：Fail
   - 其他区间：Pass

需要注意的事项：

- IOL 是一个正电流值，因为它是从 PMU 流向 DUT。
- 因为施加的是恒流，所以需要设置电压钳，如果测出电压比钳位电压还低，有可能是逻辑设成了高电平，触发了对电源保护二极管正偏。
- VDDmin 参数表示能使 DUT 正常进行测试的最小供电电压，再小将无法得出准确的测试结果。

### VOH/IOH 测试 - 串行静态法

使用串行静态法测量 VOH/IOH 的测试示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220728143124.png)

测试流程如下：

1. 需要先通过预处理，将待测引脚设置为高电平输出。
2. 向引脚施加恒定的 IOH，等待 1-5 毫秒再测量（在 PMU 设 delay）。
3. 检测引脚电压
   - 低于 VOH（+2.4V）：Fail
   - 其他区间：Pass

需要注意的事项：

- 因为 IOL 是从 PMU 流向 DUT，所以它是一个负值。
- 因为施加的是恒流，所以需要设置电压钳，如果测出电压比钳位电压还高，有可能是引脚逻辑设成了低电平，触发了对地保护二极管正偏。
- VDDmin 参数表示能使 DUT 正常进行测试的最小供电电压，再小将无法得出准确的测试结果。

## IIL/IIH

IIL 指的是输入引脚（I）逻辑为低电平（L）时，允许的最大拉电流（I，source，从外部经引脚往 DUT 的 VSS 漏），用来看引脚对电源的漏电流会不会超标，也是看隔离的程度，IIH 指的是输入引脚（I）逻辑为高电平（H）时，允许的最大灌电流（I，sink，从 DUT 的 VDD 经引脚往外漏）。举个例子，下表是 256 x 4 Static RAM 的 IIL 和 IIH 参数：

| Parameter | Description        | Test Conditions        | Min | Max | Units |
| --------- | ------------------ | ---------------------- | --- | --- | ----- |
| IIL, IIH  | Input Load Current | Vss ≤ Vin ≤ VDD(5.25V) | -10 | +10 | µA    |

IIL 衡量的是输入引脚到 VDD 的电阻值；IIH 衡量的是输入引脚到 VSS 的电阻值。该测试是为了确保输入阻抗满足设计需求、输入电流不会超标。IIL/IIH 可用串行 / 并行 / 合并法测试，也可用功能测试的方法。串行法对引脚一个一个测试，准确但相对耗时间。

另外，IIL/IIH 测试通常仅能在纯输入引脚上执行。如果遇到双向引脚，则需要加输出负载，将其电平稳定拉高或拉低，避免在保护器件上产生电流，影响测试结果。

### IIL/IIH 测试 - 串行静态法

使用串行法测试输入引脚 IIL 的示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220729100620.png)

测试流程如下：

1. 首先要供 VDDmax（最差情况）的电源给 DUT。
2. 将 DUT 所有输入引脚设高电平（VIH）。
3. 使用 PMU 将单个输入引脚拉低到 VSS。
4. 等待 1~5 微秒，检测电流值。
   - 低于 IIL（-10µA）：Fail（灌进 DUT 的电流超标）
   - 其他区间：Pass

使用串行法测试输入引脚 IIH 的示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220729100739.png)

测试流程如下：

1. 首先要供 VDDmax 的电源给 DUT。
2. 将 DUT 所有输入引脚设低电平（VIL）。
3. 使用 PMU 将单个输入引脚拉高到 VDDmax。
4. 等待 1~5 微秒，检测电流值。
   - 高于 IIH（+10µA）：Fail（流出 DUT 的电流超标）
   - 其他区间：Pass

### IIL/IIH 测试 - 并行静态法

在一些测试系统上，能对漏电流进行并行测量（Parallel Test Method）。并行测漏电流是用多个 PMU 对多个 pin 分别进行测量，所有输入引脚都被强制拉高，并且同时并行测量每个引脚的电流，随后将测试结果与标称值做比较得出结论。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220729103317.png)

1. 首先要供 VDDmax 的电源给 DUT。
2. 使用多个 PMU 对每个输入引脚强制拉高到 VDDmax（测 IIH）。
3. 等待 1~5 微秒，检测电流，对比得出结论。
4. 随后再拉低至 VSS，重复以上步骤测 IIL。

并行法的特点是可以同时测量每个引脚单个电流，快速完成 IIL/IIH 测试；缺点是输入引脚间的泄露更难检测到，因为所有输入都保持在相同的水平。

### IIL/IIH 测试 - 合并静态法

合并测试（Ganged Method）指的是将所有输入引脚合并为一个引脚，用一个 PMU 测漏电流的总和。测试示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220729104449.png)

组合测试方法与以上类似。其电流总限额是单个引脚的标称值，如果测试结果超限，则必须换回串行测试重测，这种测试对 CMOS 器件（高阻抗输入）测试效果比较好。

## IOZL/IOZH

高阻电流 IOZ 指输出引脚（O）高阻态（Z）下的漏电流（I）。其中，IOZL 指引脚低电平（L）状态时的漏电流；IOZH 指高电平（H）状态时的漏电流。用来看引脚关断时漏电流会不会超标。

此参数是确保 **双向或高阻输出引脚能正常关断（输出高阻态）**。IOZL 测的是输出高阻状态时，引脚对 VDD 的阻值；IOZH 测的是引脚对 VSS 的阻值。通常在规格书内是这么表示的：

| Parameter | Description           | Test Conditions                         | Min  | Max  | Units |
| --------- | --------------------- | --------------------------------------- | ---- | ---- | ----- |
| IOZ       | Output Current High-Z | VSS ≤ Vout ≤VDD(5.25V), Output Disabled | -2.0 | +2.0 | µA    |

### IOZL/IOZH 测试 - 串行静态法

串行静态测试 IOZL/IOZH 的示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220807202447.png)

测试流程如下：

1. 首先需要给器件供 VDD 的电源。
2. 将器件引脚预设为高阻状态，使用 PMU 强制将引脚拉高 / 拉低。
3. 测量引脚的电流值
   - 低于 -IOZ（-2µA）：Fail
   - 高于 +IOZ（+2µA）：Fail
   - 其他区间：Pass

串行测试的优点是可以准确测量单个引脚的电流值，缺点是慢。另外，此测试需要设置钳位电流。

### IOZL/IOZH 测试 - 并行静态法

并行静态法即多个 PMU 同时对多个引脚进行，此处不多赘述，其优点是快。

## VI（Input Clamp，输入电压钳）

输入电压钳 VI 指的是当在 TTL 器件（非 CMOS）输入引脚（I）上施加负电流（抽取电流）时，在引脚上测得的电压（V）。此测试的目的是 **验证三极管发射极和地之间钳位二极管的完整性**。它在规格书上是这样表示的：

| Parameter | Description         | Test Conditions        | Min | Max  | Units |
| --------- | ------------------- | ---------------------- | --- | ---- | ----- |
| VI        | Input Clamp Voltage | VCC = Min, Iin = -18mA |     | +1.5 | V     |

### VI 测试 - 串行静态法

串行静态法测 VI，测试示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220729145425.png)

测试流程如下：

1. 首先要确保这是个 TTL 器件的输入引脚，然后供 VCCmin 的电源。
2. 在设置了电压钳后，使用 PMU 抽取 -15mA~-20mA 的电流。
3. 测量引脚上的电压值
   - 低于 VI（-1.5V）：Fail
   - 其他区间：Pass

## IOS（短路输出电流）

短路输出电流表示的是当输出引脚（O）在短路条件（S）下产生的电流（I）。目的是 **衡量当引脚输出高电平，但被短路至零电压时的输出阻抗，确保在最坏的负载条件下，输出电流也不会太大**；也表示了 DUT 引脚可提供容性负载充电的最大瞬时电流，可据此计算上升时间。IOS 在规格书中是这样表示的：

| Parameter | Description                  | Test Conditions                                                                  | Min | Max | Units |
| --------- | ---------------------------- | -------------------------------------------------------------------------------- | --- | --- | ----- |
| IOS       | Output Short Circuit Current | Vout = 0V, VDD = 5.25V, \*Short only 1 output at a time for no longer than 1 sec | -85 | -30 | mA    |

### IOS 测试 - 串行静态法

测试示意图如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220729152549.png)

测试流程如下：

1. 供 VDDmax 的电源，对器件预处理，使得引脚输出高电平。
2. 用 PMU 将引脚拉低至 0V，测量输出电流并与标称值对比，得出结论。

在对 IOS 的测试中，需要有合理的逻辑以避免热切换。需要首先将 PMU 设置为强制零电流的电压测量模式，连接到 DUT 输出，测量并保存 DUT 的 VOH 电压，随后断开连接并设定 PMU 为拉高至刚刚的 VOH 电压，然后重新连接 DUT（此时两端电压都是 VOH），随后再让 PMU 拉低为 0V，测量电流值。测量完成后，PMU 要恢复拉高到 VOH 才能断开连接。这样可以确保继电器在开关切换时，两端的电压是一致的。

导致测试不通过的因素：

- **超过上限值**
  - 输出阻抗太高，导致电流绝对值不足。
  - 夹具本身有电阻。
  - 没有经过正确的预处理。
- **低于下限值**
  - 输出阻抗太低，导致电流绝对值过大。

## Resistive Inputs（上下拉阻性输入）

有些输入引脚可能有主动上拉、下拉结构，需要保证 **输入 Buffer 的上下拉电阻路径正常**。只能串行测试，因为不同引脚内部上下拉结构可能不一样。引脚结构的示意图：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220729130655.png)

## Output Fanout（输出扇出能力）

扇出（Fanout）能力是指输出引脚根据其电压电流参数，驱动多个输入引脚的能力。也就是 **引脚的带驱能力，是衡量一个输出引脚可以带得动多少个输入引脚的指标**。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220729132621.png)

如上图，这个 TTL 输出可以拉高大约 17 个输入引脚，或者拉低 30 个输入引脚。在规格书中，引脚的参数会这样表示出来：

| Parameter | Description             | Test Conditions           | Min  | Max | Units |
| --------- | ----------------------- | ------------------------- | ---- | --- | ----- |
| VOH       | Output HIGH Voltage     | VCC = 4.75V, IOH = -2.6mA | 2.4  |     | V     |
| VOL       | Output LOW Voltage      | VCC = 4.75V, IOH = 24mA   |      | 0.4 | V     |
| IIL       | Input LOW Load Current  | Vin = 0.4V                | -800 |     | µA    |
| IIH       | Input HIGH Load Current | Vin = 2.4V                |      | 150 | µA    |

扇出能力在 TTL 和 CMOS 器件之间差别很大，因为 CMOS 输入阻抗高，所以理论上一个 CMOS 输出可驱动任意多个 CMOS 输入。但 CMOS 输入引脚有寄生电容，连接越多输入，电容越大，在高低电平切换时会存在电容充放电效应，产生延时。

## 参考与致谢

- 《The Fundamentals Of Digital Semiconductor Testing》
- 《DC Test Theory》

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
