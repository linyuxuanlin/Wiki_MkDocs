---
id: 电源方案（Buck）-XL2009E1
title: 电源方案（Buck）- XL2009E1
---

XL2009E1 是芯龙的一款最高 36V 输入、3A 输出、固定 180kHz 的 Buck 芯片，被指过流保护功能，当短路的时候，频率会降到 48kHz。

项目仓库：[**Collection_of_Power_Module_Design/DC-DC(Buck)/XL2009E1**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/XL2009E1)

项目在线预览：

<div class="iframe_viewer">
    <iframe 
    scrolling="no"
  src="https://viewer.wiki-power.com/XL2009E1.html"
></iframe>
</div>

## 主要特性

- 拓扑：DC/DC（Buck）
- 器件型号：XL2009E1
- 封装：SOP8L
- 输入电压：8-36 V
- 输出电压：1.25-32V
- 最小输入输出差：0.3V
- 最大占空比：100%
- 工作频率：固定 180kHz
- 最大输出电流： 3A
- 效率（输入 12V，输出5V@2.1A）：89%
- 参考价格：￥ 2.1
- 其他特性
  - 带输出恒流环
  - 内置短路保护
  - 内置限流保护

## 典型应用电路

根据数据手册提供的典型应用电路（输入 8-36V，输出 5V@2.1A）：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407103157.png)

## 引脚定义

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407065806.png)

- FB：反馈输入引脚，由电阻从 $V_{OUT}$ 分压输入反馈，不可直接接地。反馈参考电压为 1.25V。
- OCSET：输出恒流设置引脚。
- VC：内部稳压器旁路电容。一般接 1uF 到 VIN。
- VIN：供电输入引脚。输入电压为 8-36V。需要有大电容去耦。
- SW：Buck 开关输出。

## 特性描述

### 内部功能框图

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407070413.png)

### 输出电压调节

XL2009E1 提供一个 1.25V 的内部参考电压。输出电压通过电阻分压器，从 $V_{OUT}$ 分压出来输入 FB 引脚，在内部进行比较调节。分压电阻建议使用偏差 1% 或更低的、温度系数 100 ppm 或更低的。分压电阻选择较大的阻值有利于提高轻载效率，但如果太大，稳压器将更容易受到来自 FB 输入电流的噪声和电压误差的影响。推荐低侧电阻 $R_1$ 取值为 4.7k，并通过公式计算高侧电阻 $R_2$：

$$
V_{OUT}=1.25*(1+\frac{R_2}{R_1})
$$

### 肖特基二极管选型

二极管的额定击穿电压最好比最大输入电压高 25%。为了最佳可靠性，二极管的额定电流应等于稳压器最大输出电流。在输入电压远大于输出电压的情况下，二极管平均电流会更低，这时候可以使用平均电流额定值较低的二极管，约为 $(1-D) * I_{OUT}$，但峰值电流额定值应高于最大负载电流。

XL2009E1 的数据手册提供了直接选型表（3A）：

| 输入电压 | 型号        |
| -------- | ----------- |
| 20V      | SK32        |
| 30V      | SK33/30WQ03 |
| 40V      | SK34/30WQ04 |
| 50V      | SK35/30WQ05 |
| 60V      | SK36        |

### 参数曲线

输出电压与电流的关系：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407100229.png)

效率与输出电流的关系：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407103033.png)

输出电流与 RCS 电阻的关系（恒流控制）：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407102905.png)

## 参考与致谢

- [XL2009_Datasheet](https://datasheet.lcsc.com/lcsc/1806111754_XLSEMI-XL2009E1_C73335.pdf)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

