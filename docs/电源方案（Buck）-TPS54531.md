---
id: 电源方案（Buck）-TPS54531
title: 电源方案（Buck）- TPS54531
---

TPS54531 是 TI 的一款具有 Eco-mode 的 3.5V 至 28V 输入、5A、570kHz Buck 转换器。

项目仓库： [**Collection_of_Power_Module_Design/DC-DC(Buck)/TPS54531**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/TPS54531>)

项目在线预览：

<div class="iframe_viewer">
    <iframe 
    scrolling="no"
  src="https://viewer.wiki-power.com/TPS54531.html"
></iframe>
</div>

## 主要特性

- **原理**：DC/DC（Buck）
- **输入电压**：3.5-28 V
- **输出电压**： 最低 0.8 V
- **输出电流**： 5 A
- **工作频率**： 570 kHz
- **效率**：最高 92%
- **价格**：￥ 3.80
- **特性**
  - 轻负载时脉冲跳跃 Eco-mode 功能
  - 可调慢启动可限制涌入电流
  - 可编程欠压闭锁（UVLO）阈值
  - 过压瞬态保护
  - 逐周期电流限制、频率折返和热关断保护

## 引脚定义

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713153815.png)

## 参考设计

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713173605.png)

## 参数调节

（更详细的参数请参考数据手册）

### 输出电压调节

通过调整反馈分压电阻 $R_5$ 和 $R_6$ 来设置输出电压（反馈电压 $V_{REF}=0.8 V$）：

$$
V_{OUT}=V_{REF}\times[\frac{R5}{R6}+1]
$$

$R_5$ 大约取值 10 kΩ，在参考设计中，我们需要输出 4.96 V，所以取 $R_5$ = 10.2 kΩ，$R_6$ = 1.96 kΩ。

### 使能引脚

EN 引脚低于 1.25 V 失能，浮空以使能。这里使用两个电阻进行欠压锁定。

### Eco-mode 节能模式

当电感器的峰值电流低于 160 mA 时，芯片进入节能模式，关闭输出。

### 热关机

当芯片温度超过 165℃ 时，芯片停止运行；当低于 165℃ 时重新启动。

## PCB 布局参考

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713161521.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713162833.png)

## 踩坑总结

- 续流二极管和电感的电流应该大于输出电流。
- 芯片背面需裸铜上锡用于散热。
- 布局应按照 Buck 电流流向。
- 成品板可输出 5 A 电流，但长跑 3 A 以上需要另加散热。功率器件如二极管和电感会发烫。

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

