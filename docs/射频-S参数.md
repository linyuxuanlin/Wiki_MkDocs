---
id: 射频-S参数
title: 射频 - S 参数
---

S 参数（Scattering parameters，S-Parameters，散射参数）用于反映反射信号 / 传输信号在频域范围内的特性（幅度 / 相位），它是一个复数矩阵。我们可以将电路内部视作一个黑盒子（不考虑内部电路元素），通过 S 参数测量它的端口特性。

## S 参数的详细说明

S 参数的名称规范是，第一个数字代表测量的端口，第二个代表参考的端口，比如，S21 代表相对于端口 1 信号激励源，测出来端口 2 的信号。S 参数波的形式可以是功率、电压或电流。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220627100338.png)

如上图所示，S11、S22 代表反射系数（反射 / 输入），S21、S12 代表传输系数（传输 / 输入）。

### S11

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220621000000.gif)

S11 指的是相对于端口 1 的入射信号，端口 1 的反射信号，$S11=\frac{S_{Reflection}}{S_{Incident}}$。

### S21

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220621000001.gif)

S21 指的是相对于端口 1 的入射信号，端口 2 的传输信号，$S21=\frac{S_{Transmission}}{S_{Incident}}$。

### S12

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220621000002.gif)

S12 指的是相对于端口 2 的入射信号，端口 1 的传输信号，$S12=\frac{S_{Transmission}}{S_{Incident}}$。

### S22

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220621000003.gif)

S22 指的是相对于端口 2 的入射信号，端口 2 的反射信号，$S22=\frac{S_{Reflection}}{S_{Incident}}$。

## 参考与致谢

- [S 参数的意义及矢网实操测量方法](http://jietaipu.com/resource/88.html)
- 《S-Parameter Measurements Basics for High Speed Digital》

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

