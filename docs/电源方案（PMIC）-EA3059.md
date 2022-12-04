---
id: 电源方案（PMIC）-EA3059
title: 电源方案（PMIC）- EA3059
---

EA3059 是一款 4 路 PMIC，适用于由锂电池或直流 5V 供电的应用。它内部集成四个同步降压转换器，可在轻载和重载运行时提供高效率输出。内部补偿架构使应用电路设计简单。此外，独立的使能控制方便控制上电顺序。EA3059 采用 24 脚 QFN 4x4 封装。

项目仓库： [**Collection_of_Power_Module_Design/PMIC/EA3059**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/PMIC/EA3059)

项目在线预览：

<div class="iframe_viewer">
    <iframe 
    scrolling="no"
  src="https://viewer.wiki-power.com/EA3059.html"
></iframe>
</div>

## 主要特性

- 输入电压与控制电路电压：2.7-5.5V
- 输出电压（4 个 Buck 转换器）：0.6V-Vin
- 输出电流：单路连续负载 2A、峰值 4A（4 通道总输出必须小于 10W）
- 固定 1.5MHz 开关频率
- 100% 全占空比输出
- 各通道效率达 95%
- 待机电流：<1uA
- 每路独立使能控制
- 内部补偿
- 逐周期电流限制
- 短路保护
- 自恢复过温（OTP）保护
- 没有输入过压（OVP）保护（相比 EA3059）
- 采用 24 引脚 4mm x 4mm QFN 封装

## 典型应用电路

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420171841.png)

## 内部功能框图

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420171859.png)

## 引脚定义

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420171920.png)

| 引脚名称 | 引脚描述                                                   |
| -------- | ---------------------------------------------------------- |
| VCC      | 内部控制电路的电源输入脚                                   |
| VINx     | 通道 x 的电源输入脚，加 10uF MLCC 电容去耦                 |
| LXx      | 通道 x 内部 MOS 管开关输出，可接低通滤波电路输出更稳定电压 |
| FBx      | 通道 x 的反馈脚，通过分压电路连接电压输出                  |
| ENx      | 使能脚，不能浮空                                           |
| GNDx     | 通道 x 的地                                                |
| AGND     | 模拟地                                                     |
| 底部焊盘 | 散热用，需要接地                                           |
| NC       | 无连接                                                     |

## 特性描述

### PFM/PWM 模式

每一路 Buck 都可以运行在 PFM/PWM 模式下。如果输出电流小于 150mA（典型值），稳压器将自动进入 PFM 模式。PFM 模式下的输出电压和输出纹波高于 PWM 模式下的输出电压和输出纹波。但在轻载的情况下，PFM 比 PWM 效率高。

### 使能开关

EA3059 是一款专为 OTT 应用设计的电源管理 IC，包含四路 2A 同步 Buck，可通过单独的 EN 引脚进行使能开关控制。

如果需要设定每路 Buck 的开启时间，可通过使用如下电路进行编程：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420172125.png)

### 180° 相位偏移架构

为了降低输入纹波电流，EA3059 采用了 180° 相位偏移架构。 Buck1 和 Buck3 相位相同，与 Buck2 和 Buck4 的相位相差 180°。这样子可以减小纹波电流，从而降低 EMI。

### 过流保护

EA3059 内部的四个稳压器都有自己的逐周期限流电路。当电感峰值电流超过电流限制阈值时，输出电压开始下降，直到 FB 引脚电压低于阈值，通常比参考值低 30%。一旦触发阈值，开关频率就会降低到 350KHz（典型值）。

### 热关断

如果芯片温度高于热关断阈值点，EA3059 将自动关断。为避免工作不稳定，热关断的迟滞约为 30°C。

### 输出电压调节

每路稳压器的输出电压都可以通过电阻分压器（R1、R2）进行调节。输出电压由下式计算：

$$
V_{OUTx}=0.6*\frac{R_1}{R_2}+0.6V
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420172602.png)

如果需要输出常用的电压值，则可参考下表配置分压电阻（都需要选用 1% 精度的）：

| 输出电压 | R1    | R2    |
| -------- | ----- | ----- |
| 3.3V     | 510kΩ | 110kΩ |
| 1.8V     | 200kΩ | 100kΩ |
| 1.5V     | 150kΩ | 100kΩ |
| 1.1V     | 68kΩ  | 82kΩ  |

### 输入 / 输出电容选型

输入电容用于抑制输入电压的噪声幅值，为器件提供稳定、干净的直流输入，输出电容可抑制输出电压纹波。输入和输出都可选用 MLCC 电容（低 ESR）

输入 / 输出电容器的建议型号如下：

| NPM            | 容值 | 耐压 | 封装 |
| -------------- | ---- | ---- | ---- |
| C2012X5R1A106M | 10uF | 10V  | 0805 |
| C3216X5R1A106M | 10uF | 10V  | 1206 |
| C2012X5R1A226M | 22uF | 10V  | 0805 |
| C3216X5R1A226M | 22uF | 10V  | 1206 |

### 输出电感选型

输出电感的选择，主要取决于通过电感的纹波电流量 $\Delta I_L$。$\Delta I_L$ 越大，输出电压纹波和损耗也会越大。虽然小电感可节省成本和空间，但较大的电感值可以获得更小的 $\Delta I_L$，带来更小的输出电压纹波和损耗。电感取值的计算公式：

$$
L=\frac{V_{PWR}-V_{OUT}}{\Delta I_L*F_{SW}}*\frac{V_{OUT}}{V_{PWR}}
$$

对于大多数应用场景，EA3059 可选用 1.0~2.2uH 的电感。

### 功耗

EA3059 的总功耗不应超过 10W，计算公式如下：

$$
P_{D(total)}=\Sigma (V_{OUTx}*I_{OUTx})
$$

## Layout 参考

PMIC 的 Layout 需要讲究。可参照以下建议以获得最高性能：

- 建议使用 4 层 PCB 布局，将 LX 平面和输出平面放在顶层，将 VIN 平面放在内层。
- 顶层输入 / 输出贴片电容的接地脚应该打过孔连接到内层地和底层地。
- AGND 应通过过孔直接连接到内部地层。
- 尽量加宽大电流路径走线。
- 将输入电容尽可能靠近 VINx 引脚放置，以减少噪声干扰。
- 使反馈路径（从 VOUTx 到 FBx）远离噪声节点（例如 LXx）。 LXx 是一个高电流噪声节点。使用短而宽的走线完成布局。
- 芯片底部焊盘需要打多个孔到内层和底层地，用以散热。
- 输入电容尽可能靠近 VINx 引脚放置，以减少噪声干扰。

布局参考如下：

顶层：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420175756.png)

中间电源层：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420175833.png)

中间地层：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420175851.png)

底层：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420175906.png)

## 参考与致谢

- [EA3059](http://www.everanalog.com/ProductCN/ProductEA3059DetailInfoCN.aspx)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

